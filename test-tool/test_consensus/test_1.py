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
		logger.open("TestConsensus1.log", "TestConsensus1")
		try:
			#step 1 send t
			task1 = Task("tasks/demo_step1.json")
			(result, response) = call_contract(task1, pre=False)
			if not result:
				raise Error("send transaction error")

			#step 2 check block
			txhash = response["txhash"]
			task2 = Task(Config.BASEAPI_PATH + "/rpc/getblock.json")
			task2.request()["txhash"] = txhash
			(result, response) = run_single_task(task2)
			if not result:
				raise Error("check block error")

		except Exception as e:
			print(e.msg)
			logger.close(result)

####################################################
if __name__ == '__main__':
	unittest.main()	    
