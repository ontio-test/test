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
sys.path.append('../..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from api.apimanager import API
from test_cost.test_config import test_config

#test cases
class test_cost(ParametrizedTestCase):
	def setUp(self):
		logger.open("test_cost/" + self._testMethodName+".log",self._testMethodName)
		
	def tearDown(self):
		logger.close(self.result())

	def test_base_001(self):
		priceTest=20000
		try:
			(process1, response)= API.rpc().getbalance(test_config.address)
			print(process1)
			print(response["result"])
			ong1=int(response["result"]["ong"])
			ont1=response["result"]["ont"]
			
			ontract_address = API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[0]["address"], "1", gas_price=priceTest)
			(process1, response)= API.rpc().getbalance(test_config.address)
			ong2=int(response["result"]["ong"])
			ont2=response["result"]["ont"]
			
			print(ong1-ong2==(priceTest*20000))
			print(priceTest*20000)
			print(ong1-ong2)
			
			#print(ong,ont)
			#self.finish(task_name, log_path, result,  "")\
			self.ASSERT((ong1-ong2)==(priceTest*20000), "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_normal_004(self):
		priceTest=681280
		try:
			(process1, response)= API.rpc().getbalance(test_config.address)
			
			print(process1)
			print(response["result"])
			ong1=int(response["result"]["ong"])
			ont1=response["result"]["ont"]
			task=Task(name = "cost 681280 ong", ijson = test_config.task004)
			(process, response) = API.contract().call_contract(task,pre=False)
			
			(process1, response)= API.rpc().getbalance(test_config.address)
			ong2=int(response["result"]["ong"])
			ont2=response["result"]["ont"]
			
			print(ong1-ong2==(priceTest))
			print(priceTest)
			print(ong1-ong2)
			
			self.ASSERT((ong1-ong2)==(priceTest), "")
		except Exception as e:
			logger.print(e.args[0])

####################################################
if __name__ == '__main__':
	unittest.main()

