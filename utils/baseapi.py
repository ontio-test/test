# -*- coding: utf-8 -*-
from utils.config import Config
from utils.taskthread import TaskThread
from utils.logwriter import LogWriter

from abc import ABCMeta, abstractmethod
import json
import time
import os

class BaseApi:
	def __init__(self):
		self.TYPE = None
		self.CONFIG_PATH = None
		pass

	def load_cfg(self, cfg):
		cfg_file = open(cfg, "rb")
		cfg_json = json.loads(cfg_file.read().decode("utf-8"))
		cfg_file.close()
		return cfg_json

	def multithread_run(self, logwriter, cfg_request, cfg_response):
		result = True
		thread_list = []
		response = None

		for i in range(Config.THREAD):
			t = TaskThread(self.connnet, args=cfg_request)
			thread_list.append(t)
			t.start()

		for t in thread_list:
			t.join()
			result = result and self.judge_result(cfg_response, t.get_result())
			response = t.get_result()
			logwriter.w("[ THREAD %d ]" % thread_list.index(t))
			logwriter.w("[ RESULT   ]" + json.dumps(response, indent = 4))

		return (result, response)

	@abstractmethod
	def judge_result(self, except_respons, real_respones):
		for key in except_respons.keys():
			if real_respones and key in real_respones and real_respones[key] == except_respons[key]:
				continue
			elif real_respones and key.capitalize() in real_respones and real_respones[key.capitalize()] == except_respons[key]:
				continue
			else:
				return False
		return True

	@abstractmethod
	def connnet(self, request):
		pass

	@abstractmethod
	def run(self, api_name):
		logwriter = LogWriter(self.TYPE + "/" + api_name)
		start_time = time.time()
		logwriter.w("[-------------------------------]")
		logwriter.w("[ RUN      ] "+ self.TYPE + "." +api_name)
		cfg_content = self.load_cfg(self.CONFIG_PATH + "/" + api_name + '.json')
		cfg_request = cfg_content["REQUEST"]
		cfg_response = cfg_content["RESPONSE"]
		logwriter.w("[ PARAMS   ]" + json.dumps(cfg_content, indent = 4))

		(result, response) = self.multithread_run(logwriter, cfg_request, cfg_response)
		end_time = time.time()
		time_consumed = (end_time - start_time) * 1000
		
		if result:
			logwriter.w("[ OK       ] " + self.TYPE + "."+api_name+" (%d ms)" % (time_consumed))
		else:
			logwriter.w("[ Failed   ] " + self.TYPE + "."+api_name+" (%d ms)"% (time_consumed))
		logwriter.w("[-------------------------------]")
		logwriter.w("")
		logwriter.close()

	@abstractmethod
	def runAll(self):
		for i in os.listdir(self.CONFIG_PATH):
			file = os.path.join(self.CONFIG_PATH, i)
			if os.path.isfile(file):
				i = i.replace(".json", "")
				self.run(i)
