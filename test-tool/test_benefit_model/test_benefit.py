# -*- coding:utf-8 -*-
import re
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys
import getopt
import time
import requests
import subprocess

sys.path.append('..')

import utils.base
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase

from utils.commonapi import *
from utils.rpcapi import RPCApi

logger = LoggerInstance

####################################################
# test cases
rpcapi = RPCApi()

priceTest = 100000
maxblockchange = 5

class TestBenefit(ParametrizedTestCase):
	def setUpClass(self):
		pass

	def cost_ong(self, amount):
		address = Config.SERVICES[0]["address"]
		address1 = Config.SERVICES[1]["address"]
		#消耗ong之前的状态
		(result, response) = rpcapi.getblockcount()
		if not result:
			raise Error("get blockcount error")
		startblockcount = int(response["result"])
		(result, response)=rpcapi.getbalance(address)
		if not result:
			raise Error("get balance error")
		ong1=int(response["result"]["ong"])
		
		(result, response)=rpcapi.getbalance(address1)
		if not result:
			raise Error("get balance error")
		ong1_address1=int(response["result"]["ong"])
	
		#消耗ong
		contract_address = deploy_contract("contract.neo", price=amount)
		(result, response) = rpcapi.getbalance(address)
		if not result:
			raise Error("get balance error")
			
		ong2 = int(response["result"]["ong"])
		
		#判断消耗ong是否正确
		print(ong1-ong2==(amount*1000000000))
		print(amount*1000000000)
		print(ong1-ong2)
		if(ong1-ong2==(amount*1000000000)):
			result=True
		else:
			result=False
		if not result:
			raise Error("cost ong error")
		
		#判断是否分润，至少需要等待1个共识时间
		print("等待300秒。。。")
		time.sleep(300)
		(result, response) = rpcapi.getblockcount()
		if not result:
			raise Error("get blockcount error")
		endblockcount = int(response["result"])

		(result, response) = rpcapi.getbalance(address1)
		if not result:
			raise Error("get balance error")
		
		result = int(response["result"]["ong"]) != ong1_address1

	def test_1(self):
		logger.open("TestBenefit1.log", "TestBenefit1")
		result = False
		try:
			result = self.cost_ong(priceTest)
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)

	def test_2(self):
		logger.open("TestBenefit2.log", "TestBenefit2")
		result = False
		try:
			result = self.cost_ong(priceTest)
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
		
	def test_3(self):
		address = Config.SERVICES[0]["address"]
		logger.open("TestBenefit3.log", "TestBenefit3")
		result = False
		try:
			(result1, response)=rpcapi.getbalance(address)
			if not result1:
				raise Error("get balance error")
			ong1=int(response["result"]["ong"])
			ont1=response["result"]["ont"]
		
			contract_address = deploy_contract("contract.neo", price=999999999999999)
			(result1, response) = rpcapi.getbalance(address)
			if not result1:
				raise Error("get balance error")
				
			ong2 = int(response["result"]["ong"])
			ont2 = response["result"]["ont"]
			
			print(ong1-ong2==(priceTest*1000000000))
			print(priceTest*1000000000)
			print(ong1-ong2)
		
			if(ong1-ong2==(priceTest*1000000000)):
				result=True
			else:
				result=False

		except Exception as e:
			print(e.msg)
		logger.close(result)
	
	def test_4(self):
		logger.open("TestBenefit4.log", "TestBenefit4")
		result = False
		try:
			result = self.cost_ong(priceTest)
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
	
	def test_5(self):
		logger.open("TestBenefit5.log", "TestBenefit5")
		result = False
		try:
			result = self.cost_ong(priceTest)
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
		
	def test_6(self):
		logger.open("TestBenefit6.log", "TestBenefit6")
		result = False
		try:
			result = self.cost_ong(priceTest)
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)

	def test_7(self):
		address = Config.SERVICES[2]["address"]
		result = False
		logger.open("TestBenefit7.log", "TestBenefit7")
		try:
			invoke_function_update("updateGlobalParam","2000000000","10000","32","1","50","50","50","50")
			response = withdrawong(2)
			(result1, response)=rpcapi.getbalance(address)
			if not result1:
				raise Error("get balance error")
			ong1=int(response["result"]["ong"])
			ont1=response["result"]["ont"]


			response = transfer_ont(0, 2, 1000)
			print (json.dumps(response))
			time.sleep(5)
			(result2, response)=rpcapi.getbalance(address)
			if not result1:
				raise Error("get balance error")
			ong2=int(response["result"]["ong"])
			ont2=response["result"]["ont"]

			if ong1 == ong2:
				result = False
		
		except Exception as e:
			print(e.msg)
		logger.close(result)
	
####################################################
if __name__ == '__main__':
    unittest.main()
