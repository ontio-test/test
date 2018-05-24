# -*- coding: utf-8 -*-
from websocket import create_connection
import websocket

import requests
import threading
import json
import os
import sys
from utils.config import Config
from utils.baseapi import BaseApi

class WS(BaseApi):
	LONG_LIVE_WS = None
	def __init__(self):
		BaseApi.TYPE = "websocket"
		BaseApi.CONFIG_PATH = "tasks/websocket"
		self.LONG_LIVE_WS = None
		pass

	def connnet(self, request):
		ws = create_connection(Config.WS_URL)
		ws.send(json.dumps(request))
		response = ws.recv()
		ws.close()
		return json.loads(response)		

	#special test case
	def ws_thread(self):
		def on_message(ws, message):
			print("message: " + message)

		def on_error(ws, error):
			print(error)

		def on_close(ws):
			print("### closed ###")

		def on_open(ws):
			print("### open ###")

		WS.LONG_LIVE_WS = websocket.WebSocketApp(Config.WS_URL,
							on_message = on_message,
							on_error = on_error,
							on_close = on_close,
							on_open = on_open)
		WS.LONG_LIVE_WS.run_forever()

	def run_long_connection(self):
		t1 = threading.Thread(target=self.ws_thread)
		t1.start()

		while True:
			try:
				command = sys.stdin.readline().strip('\n')
				if ".json" not in command:
					command = command + ".json"
				WS.LONG_LIVE_WS.send(json.dumps(self.load_cfg(BaseApi.CONFIG_PATH + "/" + command)["REQUEST"]))
				#ws.send(json.dumps(self.load_cfg(request)))
			except Exception as e:
				print(e)

if __name__ == "__main__":
	ws = WS()
	ws.run_block_mode()