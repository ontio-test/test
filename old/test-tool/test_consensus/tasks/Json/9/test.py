# -*- coding:utf-8 -*-
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt
import time
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
		for i in range(0,9):
			try:
				#step 1 put
				task1 = Task("tasks/invoke_put.json")
				(result, response) = call_contract(task1)
				if not result:
					raise Error("error")
			
				#step 2 确认区块生成并包含该交易
				txHash = response["result"]["Hash"]
				task2 = Task("../utils/baseapi/rpc/getblock.json")
				task2.data()["REQUEST"]["params"][0] = txHash
				(result, response) = run_single_task(task2)
				if not result:
					raise Error("send transaction error")
			except Exception as e:
				print(e.msg)
			time.sleep(10)
		logger.close(result)

####################################################
if __name__ == '__main__':
	unittest.main()	    
