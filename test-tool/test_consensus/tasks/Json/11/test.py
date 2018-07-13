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
class Test(ParametrizedTestCase):
	def test_main(self):
		logger.open("TestConsensus1.log", "TestConsensus1")
		try:
			#step 1
			task1 = Task("tasks/invoke_put.json")
			(result, response) = call_contract(task1)
			if not result:
				raise Error("error")

			#step 2
			if response['result']['Result String'] != "keytest":
				raise Error("key value can not get")	

		except Exception as e:
			print(e.msg)
		logger.close(result)

####################################################
if __name__ == '__main__':
	unittest.main()	    
