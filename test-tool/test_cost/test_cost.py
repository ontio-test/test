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
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.contractapi import *
from utils.rpcapi import RPCApi
from utils.commonapi import call_contract

logger = LoggerInstance
rpcapiTest=RPCApi()
address="AXbevnGZBypZrcQwQfdYZxXj5zcFTtiMEA"
cost1="tasks/cost_1.json"
filterfile="tasks/004.json"
####################################################
#test cases
class TestContract(ParametrizedTestCase):
	def start(self, log_path):
		logger.open(log_path)

	def finish(self, task_name, log_path, result, msg):
		if result:
			logger.print("[ OK       ] ")
			logger.append_record(task_name, "pass", log_path)
		else:
			logger.print("[ Failed   ] " + msg)
			logger.append_record(task_name, "fail", log_path)
		logger.close()

	def test_001(self):
		priceTest=20000
		
		log_path = "test_001.log"
		task_name = "test_001"
		
		
		self.start(log_path)
		(result1, response)=rpcapiTest.getbalance(address)
		
		print(result1)
		print(response["result"])
		ong1=int(response["result"]["ong"])
		ont1=response["result"]["ont"]
		
		ontract_address = deploy_contract(cost1,price=priceTest)
		(result1, response)=rpcapiTest.getbalance(address)
		ong2=int(response["result"]["ong"])
		ont2=response["result"]["ont"]
		
		print(ong1-ong2==(priceTest*1000000000))
		print(priceTest*1000000000)
		print(ong1-ong2)
		
		if(ong1-ong2==(priceTest*1000000000)):
			result=True
		else:
			result=False
		#print(ong,ont)
		self.finish(task_name, log_path, result,  "")\

	def test_004(self):
		priceTest=366780
		
		log_path = "test_004.log"
		task_name = "test_004"
		
		
		self.start(log_path)
		(result1, response)=rpcapiTest.getbalance(address)
		
		print(result1)
		print(response["result"])
		ong1=int(response["result"]["ong"])
		ont1=response["result"]["ont"]
		task=Task(filterfile)
		(result, response) = call_contract(task,pre=False)
		
		(result1, response)=rpcapiTest.getbalance(address)
		ong2=int(response["result"]["ong"])
		ont2=response["result"]["ont"]
		
		print(ong1-ong2==(priceTest))
		print(priceTest)
		print(ong1-ong2)
		
		if(ong1-ong2==(priceTest)):
			result=True
		else:
			result=False
		#print(ong,ont)
		self.finish(task_name, log_path, result,  "")

####################################################
if __name__ == '__main__':
	unittest.main()

