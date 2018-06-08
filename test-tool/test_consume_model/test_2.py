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
		logger.open("TestConsumeModel_2.log", "TestConsumeModel_2")
		try:
			#step 1 准备一个交易
			task1 = Task("tasks/test_2.json")
			(result, response_1) = sign_transction(task1)
			if not result:
				raise Error("sign transction error")
			
			#step 2 调用这个交易
			(result, response_2) = call_signed_contract(response_1["result"]["signed_tx"], pre=False)
			if not result:
				raise Error("send first transaction error")
			
			#step 3 再次调用这个交易
			(result, response_3) = call_signed_contract(response_1["result"]["signed_tx"], pre=False)
			if not result:
				raise Error("send second transaction error")

		except Exception as e:
			print(e.msg)
			logger.close(result)

####################################################
if __name__ == '__main__':
	unittest.main()	    
