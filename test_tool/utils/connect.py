# -*- coding: utf-8 -*-
import json
import time
import os
import requests
import urllib
import websocket
import threading
import sys
from websocket import create_connection
from abc import ABCMeta, abstractmethod

from utils.config import Config
from utils.taskthread import TaskThread
from utils.taskdata import Task
from utils.logger import LoggerInstance as logger 
from utils.error import TestError


def multithread_run(logger, cfg_request, cfg_response):
	result = True
	thread_list = []
	response = None

	for i in range(Config.THREAD):
		t = TaskThread(self.con, args=cfg_request)
		thread_list.append(t)
		t.start()

	for t in thread_list:
		t.join()
		result = result and self.judge_result(cfg_response, t.get_result())
		response = t.get_result()
		if logger:
			logger.print("[ THREAD %d ]" % thread_list.index(t))
			logger.print("[ RESULT   ]" + json.dumps(response, indent = 4))

	return (result, response)

@abstractmethod
def con(itype, ip, request):
	if request:
		connecttype = itype

		if not connecttype:
			#default use rpc
			connecttype = "RPC"

		if connecttype.upper() == "RPC":
			return con_rpc(ip, request)
		elif connecttype.upper() == "CLI":
			return con_cli(ip, request)
		elif connecttype.upper() == "RESTFUL":
			return con_restful(ip, request)
		elif connecttype.upper() == "WS":
			return con_ws(ip, request)
		elif connecttype.upper() == "ST":
			return con_test_service(ip, request)
	return None

def con_cli(ip, request):
	try:
		url = ""
		if ip:
			url = "http://" + ip + ":20000/jsonrpc"
		else:
			url = Config.CLIRPC_URL

		response = requests.post(url, data=json.dumps(request), headers=Config.RPC_HEADERS, timeout = 10)
		return response.json()
	except Exception as e:
		logger.error("con_cli:"+str(e.args[0]))
		raise TestError(54004)

def con_rpc(ip, request):
	try:
		con_url = ""
		if ip:
			con_url = "http://" + ip + ":20336/jsonrpc"
		else:
			con_url = Config.RPC_URL
		response = requests.post(con_url, data=json.dumps(request), headers=Config.RPC_HEADERS, timeout = 10)
		return response.json()
	except Exception as e:
		logger.error("con_rpc:"+str(e.args[0]))
		raise TestError(54001)

def con_restful(ip, api_request):
	try:
		url = ""
		if ip:
			url = "http://" + ip + ":20334"
		else:
			url = Config.RESTFUL_URL

		api_url = url + api_request["api"]
		api_command = "GET"
		if "command" in api_request:
			api_command = api_request["command"]

		if api_command == "POST":
			api_post_data = None
			if "params" in api_request:
				api_post_data = api_request["params"]
			api_post_data_encode = json.dumps(api_post_data)  
			api_post_data_encode = bytes(api_post_data_encode, 'utf8')
			req = urllib.request.Request(url = api_url, data = api_post_data_encode)
			response = urllib.request.urlopen(req)
			return json.loads(response.read().decode("utf-8"))
		else:
			response = urllib.request.urlopen(api_url)
			return json.loads(response.read().decode("utf-8"))
	except Exception as e:
		logger.error("con_restful:"+str(e.args[0]))
		raise TestError(54002)

def con_ws(ip, request):
	try:
		url = ""
		if ip:
			url = "ws://" + ip + ":20335"
		else:
			url = Config.WS_URL

		ws = create_connection(url)
		ws.send(json.dumps(request))
		response = ws.recv()
		ws.close()
		return json.loads(response)
	except Exception as e:
		logger.error("con_ws:"+str(e.args[0]))
		raise TestError(54003)

def con_test_service(ip, request):
	try:
		con_url = ""
		if ip:
			con_url = "http://" + ip + ":23635/jsonrpc"
		else:
			con_url = "http://127.0.0.1:23635/jsonrpc"

		response = requests.post(con_url, data=json.dumps(request), headers=Config.RPC_HEADERS, timeout = 10)
		return response.json()
	except Exception as e:
		logger.error("con_test_service:"+str(e.args[0]))
		raise TestError(54005)

class WebSocket():
	def __init__(self):
		self.LONG_LIVE_WS = None
		self.terminated = False

	#special test case
	def ws_thread(self, message_cb = None):
		def on_message(ws, message):
			print("message: " + message)
			if message["Error"] == 41001:
				raise TestError("Error")
			if message_cb:
				message_cb(message)

		def on_error(ws):
			self.terminated = True

		def on_close(ws):
			self.terminated = True
			print("### closed ###")

		def on_open(ws):
			print("### open ###")

		self.LONG_LIVE_WS = websocket.WebSocketApp(Config.WS_URL,
							on_message = on_message,
							on_error = on_error,
							on_close = on_close,
							on_open = on_open)
		self.LONG_LIVE_WS.run_forever()

	def ws_heartbeat_thread(self, heartbeat_gap = 5):
		while True:
			time.sleep(heartbeat_gap)
			try:
				if self.terminated:
					raise TestError("Error")
				self.LONG_LIVE_WS.send(json.dumps(Task(Config.BASEAPI_PATH + "/ws/heartbeat.json").data()["REQUEST"]))
			except Exception as e:
				logger.error(str(e.args[0]))
				return False

	def exec(self, heartbeat_gap = 5, message_cb = None):
		t1 = threading.Thread(target=self.ws_thread, args=(message_cb,))
		t1.start()
		if heartbeat_gap > 0:
			t2 = threading.Thread(target=self.ws_heartbeat_thread, args=(heartbeat_gap,))
			t2.start()

		while True:
			try:
				time.sleep(heartbeat_gap+5)
				if self.terminated:
					raise TestError("thread t2 closed")
				command = sys.stdin.readline().strip('\n')
				if ".json" not in command:
					command = command + ".json"
				
				self.LONG_LIVE_WS.send(json.dumps(Task("tasks/ws/" + command).data()["REQUEST"]))
				#ws.send(json.dumps(self.load_cfg(request)))
			except Exception as e:
				print(e)
				return False