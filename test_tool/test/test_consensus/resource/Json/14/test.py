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
			txHash = ""
			task1 = Task("../utils/baseapi/rpc/getblock.json")
			(result, response) = run_single_task(task1)
			print(response["result"]["Hash"])
			#step 2
			txHash = response["result"]["Hash"]
			task2 = Task("../utils/baseapi/rpc/getblock.json")
			task2.data()["REQUEST"]["params"][0] = txHash
			(result, response) = run_single_task(task2)
			if not result:
			  raise Error("send transaction error")
		except Exception as e:
			print(e.msg)
		logger.close(result)

####################################################
if __name__ == '__main__':
	unittest.main()	 