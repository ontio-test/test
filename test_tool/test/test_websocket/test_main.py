# -*- coding:utf-8 -*-
###2,27,48,106需要重启节点所以还没测
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
testpath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(testpath)

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.parametrizedtestcase import ParametrizedTestCase
#from api.commonapi import *
from utils.connect import WebSocket
from api.apimanager import API
from utils.taskrunner import TaskRunner

#from ws_api_conf import Conf
from test_config import test_config
from test_websocket.test_api import *



class test_websocket_1(ParametrizedTestCase):

	def test_init(self):
		time.sleep(2)
		# print("stop all")
		# API.node().stop_all_nodes()
		# print("start all")
		# API.node().start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(1)
		print("waiting for 60s......")

		(test_config.contract_addr, test_config.contract_tx_hash) = API.contract().deploy_contract_full(testpath+"/resource/test.neo")
		test_config.CONTRACT_ADDRESS_CORRECT = test_config.contract_addr
		test_config.CONTRACT_ADDRESS_INCORRECT_2 = test_config.contract_addr + "11"
		test_config.TX_HASH_CORRECT = test_config.contract_tx_hash
		test_config.TX_HASH_INCORRECT_2 = test_config.contract_tx_hash[:-2]
		test_config.TX_HASH_INCORRECT_3 = test_config.contract_tx_hash + "1111"

		test_config.block_height = int(API.rpc().getblockcount()[1]["result"]) - 1
		test_config.block_hash = API.rpc().getblockhash(test_config.block_height - 1)[1]["result"]
		test_config.signed_data = get_signed_data()

		test_config.HEIGHT_CORRECT = test_config.block_height - 1
		test_config.HEIGHT_INCORRECT_2 = test_config.block_height + 1000
		test_config.BLOCK_HASH_CORRECT = test_config.block_hash
		test_config.BLOCK_HASH_INCORRECT_2 = test_config.block_hash[:-2] # HASH NOT EXISTENT
		test_config.BLOCK_HASH_INCORRECT_3 = test_config.block_hash + "1111"

		test_config.RAW_TRANSACTION_DATA_CORRECT = test_config.signed_data
		test_config.RAW_TRANSACTION_DATA_INCORRECT_2 = "11111111" + test_config.signed_data + "1111111111" 

	def setUp(self):
		logger.open("test_websocket/" + self._testMethodName+".log",self._testMethodName)
		if self._testMethodName == "test_init":
			return 
		
	def tearDown(self):
		logger.close(self.result())
	
	def test_base_001_heartbeat(self):
		try:
			(process, response) = API.ws().heartbeat()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	# def test_abnormal_002_heartbeat(self):
		# try:
			# API.node().stop_node(0)
			# (process, response) = API.ws().heartbeat()
			# API.node().start_node(0, Config.DEFAULT_NODE_args[0])
			# time.sleep(5)
			# self.ASSERT(not process, "")
		# except Exception as e:
			# logger.print(e.args[0])
	
	def test_abnormal_003_heartbeat(self):
		try:
			API.ws = WebSocket()
			process=API.ws.exec(heartbeat_gap=320)
			# (result, response) = API.ws().heartbeat()
			self.ASSERT(process, "")
		except Exception as e:
			process=False
	
	def test_base_004_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_CORRECT])
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_005_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_INCORRECT_2])
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_006_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_INCORRECT_3])
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_007_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_CORRECT], sevent=True)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_008_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_CORRECT], sevent=False)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_009_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_CORRECT], sevent=None)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_010_subscribe(self):
		try:
			(process, response) = API.ws().subscribe(None, sevent=True)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_011_subscribe(self):
		try:
			(process, response) = API.ws().subscribe(None, sevent=0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_012_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_CORRECT], sjsonblock=True)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_013_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_CORRECT], sjsonblock=False)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_014_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_CORRECT], sjsonblock=None)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_015_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_CORRECT], sjsonblock=0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_016_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_CORRECT], srawblock=True)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_017_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_CORRECT], srawblock=False)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_018_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_CORRECT], srawblock=None)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_019_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_CORRECT], srawblock=0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_020_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_CORRECT], sblocktxhashs=True)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_021_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_CORRECT], sblocktxhashs=False)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_022_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_CORRECT], sblocktxhashs=None)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_023_subscribe(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().subscribe([test_config.CONTRACT_ADDRESS_CORRECT], sblocktxhashs=0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_024_getgenerateblocktime(self):
		try:
			(process, response) = API.ws().getgenerateblocktime()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_025_getgenerateblocktime(self):
		try:
			(process, response) = API.ws().getgenerateblocktime({"height":"1"})
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_026_getconnectioncount(self):
		try:
			(process, response) = API.ws().getconnectioncount()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	# def test_abnormal_027_getconnectioncount(self):
		# try:
			# API.node().stop_node(0)
			# (process, response) = API.ws().getconnectioncount()
			# API.node().start_node(0, Config.DEFAULT_NODE_args)
			# time.sleep(5)
			# self.ASSERT(not process, "")
		# except Exception as e:
			# logger.print(e.args[0])

	def test_normal_028_getconnectioncount(self):
		try:
			(process, response) = API.ws().getconnectioncount({"height":"1"})
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_029_getblocktxsbyheight(self):
		try:
			(process, response) = API.ws().getblocktxsbyheight(test_config.HEIGHT_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_031_getblocktxsbyheight(self):
		try:
			(process, response) = API.ws().getblocktxsbyheight(test_config.HEIGHT_BORDER)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_032_getblocktxsbyheight(self):
		try:
			(process, response) = API.ws().getblocktxsbyheight(test_config.HEIGHT_INCORRECT_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_033_getblocktxsbyheight(self):
		try:
			(process, response) = API.ws().getblocktxsbyheight(test_config.HEIGHT_INCORRECT_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_034_getblocktxsbyheight(self):
		try:
			(process, response) = API.ws().getblocktxsbyheight(test_config.HEIGHT_INCORRECT_3)
			self.ASSERT(not process, "")		
		except Exception as e:
			logger.print(e.args[0])

	def test_base_035_getblockbyheight(self):
		try:
			(process, response) = API.ws().getblockbyheight(test_config.HEIGHT_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_037_getblockbyheight(self):
		try:
			(process, response) = API.ws().getblockbyheight(test_config.HEIGHT_BORDER)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_038_getblockbyheight(self):
		try:
			(process, response) = API.ws().getblockbyheight(test_config.HEIGHT_INCORRECT_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_039_getblockbyheight(self):
		try:
			(process, response) = API.ws().getblockbyheight(test_config.HEIGHT_INCORRECT_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_040_getblockbyheight(self):
		try:
			(process, response) = API.ws().getblockbyheight(test_config.HEIGHT_INCORRECT_3)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_041_getblockbyhash(self):
		try:
			(process, response) = API.ws().getblockbyhash(test_config.BLOCK_HASH_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_043_getblockbyhash(self):
		try:
			(process, response) = API.ws().getblockbyhash(test_config.BLOCK_HASH_INCORRECT_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_044_getblockbyhash(self):
		try:
			(process, response) = API.ws().getblockbyhash(test_config.BLOCK_HASH_INCORRECT_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_045_getblockbyhash(self):
		try:
			(process, response) = API.ws().getblockbyhash(test_config.BLOCK_HASH_INCORRECT_3)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_046_getblockbyhash(self):
		try:
			(process, response) = API.ws().getblockbyhash(test_config.BLOCK_HASH_INCORRECT_4)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_047_getblockheight(self):
		try:
			(process, response) = API.ws().getblockheight()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	# def test_normal_048_getblockheight(self):
		# try:
			# API.node().stop_nodes([0, 1, 2, 3, 4, 5, 6])
			# start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_args)
			# time.sleep(10)
			# (process, response) = API.ws().getblockheight()
			# self.ASSERT(process, "")
		# except Exception as e:
			# logger.print(e.args[0])
	
	def test_base_049_getblockhashbyheight(self):
		try:
			(process, response) = API.ws().getblockhashbyheight(test_config.HEIGHT_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_051_getblockhashbyheight(self):
		try:
			(process, response) = API.ws().getblockhashbyheight(test_config.HEIGHT_BORDER)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_052_getblockhashbyheight(self):
		try:
			(process, response) = API.ws().getblockhashbyheight(test_config.HEIGHT_INCORRECT_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_053_getblockhashbyheight(self):
		try:
			(process, response) = API.ws().getblockhashbyheight(test_config.HEIGHT_INCORRECT_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_054_getblockhashbyheight(self):
		try:
			(process, response) = API.ws().getblockhashbyheight(test_config.HEIGHT_INCORRECT_3)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_055_gettransaction(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().gettransaction(test_config.TX_HASH_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_056_gettransaction(self):
		try:
			(process, response) = API.ws().gettransaction(test_config.TX_HASH_INCORRECT_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_057_gettransaction(self):
		try:
			(process, response) = API.ws().gettransaction(test_config.TX_HASH_INCORRECT_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_058_gettransaction(self):
		try:
			(process, response) = API.ws().gettransaction(test_config.TX_HASH_INCORRECT_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_059_gettransaction(self):
		try:
			(process, response) = API.ws().gettransaction(test_config.TX_HASH_INCORRECT_3)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_060_gettransaction(self):
		try:
			(process, response) = API.ws().gettransaction(test_config.TX_HASH_INCORRECT_4)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_061_sendrawtransaction(self):
		try:
			(process, response) = API.ws().sendrawtransaction(test_config.RAW_TRANSACTION_DATA_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_063_sendrawtransaction(self):
		try:
			(process, response) = API.ws().sendrawtransaction(test_config.RAW_TRANSACTION_DATA_INCORRECT_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_064_sendrawtransaction(self):
		try:
			(process, response) = API.ws().sendrawtransaction(test_config.RAW_TRANSACTION_DATA_INCORRECT_3)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_065_sendrawtransaction(self):
		try:
			(process, response) = API.ws().sendrawtransaction(test_config.RAW_TRANSACTION_DATA_INCORRECT_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_066_get_version(self):
		try:
			task = Task(Config.BASEAPI_PATH + "/ws/getversion.json")
			task.set_type("ws")
			param = None
			if param and isinstance(param, dict):
				taskrequest = task.request()
				for key in param:
					taskrequest[key] = param[key]
				task.set_request(taskrequest)
			(process, response) = TaskRunner.run_single_task(task)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_068_get_version(self):
		try:
			task = Task(Config.BASEAPI_PATH + "/ws/getversion.json")
			task.set_type("ws")
			param = {"height":""}
			if param and isinstance(param, dict):
				taskrequest = task.request()
				for key in param:
					taskrequest[key] = param[key]
				task.set_request(taskrequest)
			(process, response) = TaskRunner.run_single_task(task)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_069_get_version(self):
		try:
			task = Task(Config.BASEAPI_PATH + "/ws/getversion.json")
			task.set_type("ws")
			param = {"height":"abc"}
			if param and isinstance(param, dict):
				taskrequest = task.request()
				for key in param:
					taskrequest[key] = param[key]
				task.set_request(taskrequest)
			(process, response) = TaskRunner.run_single_task(task)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_070_getbalancebyaddr(self):
		try:
			(process, response) = API.ws().getbalancebyaddr(test_config.ACCOUNT_ADDRESS_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_071_getbalancebyaddr(self):
		try:
			(process, response) = API.ws().getbalancebyaddr(test_config.ACCOUNT_ADDRESS_INCORRECT_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_072_getbalancebyaddr(self):
		try:
			(process, response) = API.ws().getbalancebyaddr(test_config.ACCOUNT_ADDRESS_INCORRECT_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_073_getbalancebyaddr(self):
		try:
			(process, response) = API.ws().getbalancebyaddr(test_config.ACCOUNT_ADDRESS_INCORRECT_3)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_074_getcontract(self):
		try:
			(process, response) = API.ws().getcontract(test_config.ACCOUNT_ADDRESS_INCORRECT_4)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_075_getcontract(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().getcontract(test_config.CONTRACT_ADDRESS_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_077_getcontract(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().getcontract(test_config.CONTRACT_ADDRESS_INCORRECT_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_078_getcontract(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().getcontract(test_config.CONTRACT_ADDRESS_INCORRECT_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_079_getcontract(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().getcontract(test_config.CONTRACT_ADDRESS_INCORRECT_3)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_080_getcontract(self):
		try:
			time.sleep(5)
			(process, response) = API.ws().getcontract(test_config.CONTRACT_ADDRESS_INCORRECT_4)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_081_getsmartcodeeventbyheight(self):
		try:
			(process, response) = API.ws().getsmartcodeeventbyheight(test_config.HEIGHT_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_082_getsmartcodeeventbyheight(self):
		try:
			(process, response) = API.ws().getsmartcodeeventbyheight(test_config.HEIGHT_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_083_getsmartcodeeventbyheight(self):
		try:
			(process, response) = API.ws().getsmartcodeeventbyheight(test_config.HEIGHT_BORDER)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_084_getsmartcodeeventbyheight(self):
		try:
			(process, response) = API.ws().getsmartcodeeventbyheight(test_config.HEIGHT_INCORRECT_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_085_getsmartcodeeventbyheight(self):
		try:
			(process, response) = API.ws().getsmartcodeeventbyheight(test_config.HEIGHT_INCORRECT_2)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_086_getsmartcodeeventbyheight(self):
		try:
			(process, response) = API.ws().getsmartcodeeventbyheight(test_config.HEIGHT_INCORRECT_3)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_087_getsmartcodeeventbyhash(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().getsmartcodeeventbyhash(test_config.TX_HASH_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_088_getsmartcodeeventbyhash(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().getsmartcodeeventbyhash(test_config.TX_HASH_INCORRECT_5)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_089_getsmartcodeeventbyhash(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().getsmartcodeeventbyhash(test_config.TX_HASH_INCORRECT_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_090_getsmartcodeeventbyhash(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().getsmartcodeeventbyhash(test_config.TX_HASH_INCORRECT_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_091_getsmartcodeeventbyhash(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().getsmartcodeeventbyhash(test_config.TX_HASH_INCORRECT_3)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_092_getsmartcodeeventbyhash(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().getsmartcodeeventbyhash(test_config.TX_HASH_INCORRECT_4)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_093_getblockheightbytxhash(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().getblockheightbytxhash(test_config.TX_HASH_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_094_getblockheightbytxhash(self):
		try:
			(process, response) = API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[1]["address"], "100000000", 0, pre=False, twice=False)
			tx_hash_failed = response["result"]
			API.node().wait_gen_block()
			(process, response) = API.ws().getblockheightbytxhash(tx_hash_failed)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_095_getblockheightbytxhash(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().getblockheightbytxhash(test_config.TX_HASH_INCORRECT_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_096_getblockheightbytxhash(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().getblockheightbytxhash(test_config.TX_HASH_INCORRECT_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_097_getblockheightbytxhash(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().getblockheightbytxhash(test_config.TX_HASH_INCORRECT_3)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_098_getblockheightbytxhash(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().getblockheightbytxhash(test_config.TX_HASH_INCORRECT_4)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_099_getmerkleproof(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().getmerkleproof(test_config.TX_HASH_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_100_getmerkleproof(self):
		try:
			(process, response) = API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[1]["address"], "100000000", 0, pre=False, twice=False)
			tx_hash_failed = response["result"]
			API.node().wait_gen_block()
			(process, response) = API.ws().getmerkleproof(tx_hash_failed)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_101_getmerkleproof(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().getmerkleproof(test_config.TX_HASH_INCORRECT_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_102_getmerkleproof(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().getmerkleproof(test_config.TX_HASH_INCORRECT_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_103_getmerkleproof(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().getmerkleproof(test_config.TX_HASH_INCORRECT_3)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_104_getmerkleproof(self):
		try:
			time.sleep(10)
			(process, response) = API.ws().getmerkleproof(test_config.TX_HASH_INCORRECT_4)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_105_getsessioncount(self):
		try:
			(process, response) = API.ws().getsessioncount()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	# def test_abnormal_106_getsessioncount(self):
		# try:
			# API.node().stop_node(0)
			# (process, response) = API.ws().getsessioncount()
			# API.node().start_node(0, Config.DEFAULT_NODE_args)
			# time.sleep(5)
			# self.ASSERT(not process, "")
		# except Exception as e:
			# logger.print(e.args[0])
	
	'''
	def test_107_getstorage(self):
		log_path = "107_getstorage.log"
		task_name = "107_getstorage"
		logger.open(".log","")
		(result, response) = API.ws().getstorage(CONTRACT_ADDRESS_CORRECT, KEY_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_108_getstorage(self):
		log_path = "108_getstorage.log"
		task_name = "108_getstorage"
		logger.open(".log","")
		(result, response) = API.ws().getstorage(CONTRACT_ADDRESS_INCORRECT_2, KEY_CORRECT)
		logger.close(result)

	def test_109_getstorage(self):
		log_path = "109_getstorage.log"
		task_name = "109_getstorage"
		logger.open(".log","")
		(result, response) = API.ws().getstorage(CONTRACT_ADDRESS_INCORRECT_3, KEY_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_110_getstorage(self):
		log_path = "110_getstorage.log"
		task_name = "110_getstorage"
		logger.open(".log","")
		(result, response) = API.ws().getstorage(CONTRACT_ADDRESS_INCORRECT_4, KEY_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_111_getstorage(self):
		log_path = "111_getstorage.log"
		task_name = "111_getstorage"
		logger.open(".log","")
		(result, response) = API.ws().getstorage(CONTRACT_ADDRESS_INCORRECT_1, KEY_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_112_getstorage(self):
		log_path = "112_getstorage.log"
		task_name = "112_getstorage"
		logger.open(".log","")
		(result, response) = API.ws().getstorage(CONTRACT_ADDRESS_CORRECT, KEY_CORRECT)
		logger.close(result)

	def test_113_getstorage(self):
		log_path = "113_getstorage.log"
		task_name = "113_getstorage"
		logger.open(".log","")
		(result, response) = API.ws().getstorage(CONTRACT_ADDRESS_CORRECT, KEY_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_114_getstorage(self):
		log_path = "114_getstorage.log"
		task_name = "114_getstorage"
		logger.open(".log","")
		(result, response) = API.ws().getstorage(CONTRACT_ADDRESS_CORRECT, KEY_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_115_getstorage(self):
		log_path = "115_getstorage.log"
		task_name = "115_getstorage"
		logger.open(".log","")
		(result, response) = API.ws().getstorage(CONTRACT_ADDRESS_CORRECT, KEY_INCORRECT_4)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_116_getstorage(self):
		log_path = "116_getstorage.log"
		task_name = "116_getstorage"
		logger.open(".log","")
		(result, response) = API.ws().getstorage(CONTRACT_ADDRESS_CORRECT, KEY_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")
	'''
####################################################
if __name__ == '__main__':
	suite = unittest.main()