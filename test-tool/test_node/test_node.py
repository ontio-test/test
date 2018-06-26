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

class TestNode(ParametrizedTestCase):
	def test_1(self):
		logger.open("TestNode.log", "TestNode")
		result = False
		try:
			node_i = 7
			task = Task("tasks/transfer.json")
			nodeaddress = Config.SERVICES[node_i]["address"]
			task.data()["NODE_INDEX"] = node_i
			task.data()["REQUEST"]["Params"]["params"][1]["value"][0]["value"] = script_hash_bl_reserver(base58_to_address(nodeaddress))
			task.data()["REQUEST"]["Params"]["params"][1]["value"][1]["value"] = script_hash_bl_reserver(base58_to_address(nodeaddress))
			task.data()["REQUEST"]["Params"]["params"][1]["value"][2]["value"] = "1000"  
			(result, response) = call_contract(task, twice = True)
			if not result:
				raise Error("call contract error")

			result = pause("please check you next step, then put '1' or '0' in you command window.\n '1' is ok, '0' is not ok")
			result = int(result)
		except Exception as e:
			print(e)
			print(e.msg)
		logger.close(result)
		
	def test_7(self):
		logger.open("TestNode7.log", "TestNode7")
		result = False
		rpcapi.getblockcount(node_index = 0)
		rpcapi.getblockcount(node_index = 2)
		logger.close(result)
		
	def test_8(self):
		logger.open("TestNode7.log", "TestNode7")
		result = False
		rpcapi.getblockcount(node_index = 0)
		rpcapi.getblockcount(node_index = 7)
		logger.close(result)

	def test_11(self):
		logger.open("TestNode8.log", "TestNode8")
		result = False
		print("normal node.................")
		rpcapi.getblockcount(node_index = 0)
		print("\n\n\n")
		print("abnormal node...............")
		rpcapi.getblockcount(node_index = 1)
		logger.close(result)

	def test_15(self):
		logger.open("TestNode15.log", "TestNode15")
		result = False
		print("normal node.................")
		rpcapi.getblockcount(node_index = 0)
		rpcapi.getblockcount(node_index = 3)
		print("\n\n\n")
		print("abnormal node..............")
		rpcapi.getblockcount(node_index = 1)
		rpcapi.getblockcount(node_index = 2)
		logger.close(result)

	def test_16(self):
		logger.open("TestNode16.log", "TestNode16")
		result = False
		print("normal node.................")
		rpcapi.getblockcount(node_index=0)
		print("\n\n\n")
		print("abnormal node..............")
		rpcapi.getblockcount( node_index= 7)
		rpcapi.getblockcount( node_index= 8)
		rpcapi.getblockcount( node_index= 9)
		rpcapi.getblockcount( node_index= 10)
		logger.close(result)		

####################################################
if __name__ == '__main__':
    unittest.main()
