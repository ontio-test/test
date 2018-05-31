# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

sys.path.append('..')


import utils.commonapi
import utils.base
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.parametrizedtestcase import ParametrizedTestCase

logger = LoggerInstance

class TestWebAPI(ParametrizedTestCase):
	def start(self, task):
		logger.open(task.log_path())

	def finish(self, task, result, msg):
		if result:
			logger.print("[ OK       ] ")
			logger.append_record(task.name(), "pass", task.log_path())
		else:
			logger.print("[ Failed   ] " + msg)
			logger.append_record(task.name(), "fail", task.log_path())
		logger.close()

	def test_webapi(self):
		task = self.param
		self.start(task)
		(result, response) = utils.commonapi.run_single_task(task)
		self.finish(task, result, "")

####################################################
if __name__ == '__main__':
	filterfile = ""
	opts, args = getopt.getopt(sys.argv[1:], "n:", ["name="])
	for op, value in opts:
		if op in ("-n", "--name"):
			filterfile = value

	suite = unittest.TestSuite()    
	if filterfile == '':
		for task in TaskData('rpc').tasks():
			task.set_type("rpc")
			suite.addTest(TestWebAPI("test_webapi", param = task))
		for task in TaskData('restful').tasks():
			task.set_type("restful")
			suite.addTest(TestWebAPI("test_webapi", param = task))
		for task in TaskData('ws').tasks():
			task.set_type("ws")
			suite.addTest(TestWebAPI("test_webapi", param = task))
	else:
		suite.addTest(TestWebAPI("test_webapi", param = Task(filterfile)))

	unittest.TextTestRunner(verbosity=2).run(suite)