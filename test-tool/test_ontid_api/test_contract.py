# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase

from utils.commonapi import call_contract

logger = LoggerInstance

####################################################
#test cases
class TestContract(ParametrizedTestCase):
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

	def test_neo(self):
		task = self.param
		self.start(task)
		(result, response) = call_contract(task, pre=False)
		self.finish(task, result, response)

####################################################
if __name__ == '__main__':
	filterfile = ""
	opts, args = getopt.getopt(sys.argv[1:], "n:", ["name="])
	for op, value in opts:
		if op in ("-n", "--name"):
			filterfile = value

	suite = unittest.TestSuite()    
	if filterfile == '':
		for task in TaskData('').tasks(True):
			suite.addTest(TestContract("test_neo", param = task)) 	    
	else:
		suite.addTest(TestContract("test_neo", param = Task(filterfile)))
	unittest.TextTestRunner(verbosity=2).run(suite)
