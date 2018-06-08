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
class TestConsensus(ParametrizedTestCase):
	def test_main(self):
		result = False
		logger.open("TestConsensus20.log", "TestConsensus20")
		try:
			#step 1 send t
			task1 = Task("tasks/test_20.json")
			(result_1, response_1) = sign_transction(task1)
			(result, response) = call_contract(task1)
			if not result:
				raise Error("send transaction error")

		except Exception as e:
			print(e.msg)
			logger.close(result)

####################################################
if __name__ == '__main__':
	unittest.main()	    
