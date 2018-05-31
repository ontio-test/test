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
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.commonapi import *
from utils.parametrizedtestcase import ParametrizedTestCase

####################################################
#test cases
class TestSample1(ParametrizedTestCase):
	def test_main(self):
		logger.open("TestSample1.log")
		try:
			#step 1
			task1 = Task("tasks/sample_step1.json")
			(result, response) = call_contract(task1)
			if not result:
				raise Error("error")

			#step 2
			task2 = Task("tasks/sample_step2.json")
			(result, response) = call_contract(task2)
			if not result:
				raise Error("error")
		except Exception as e:
			print(e.msg)
		logger.close("TestSample1", result)

####################################################
if __name__ == '__main__':
	unittest.main()	    
