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
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from api.apimanager import API

from test_consensus.test_api import test_api
from test_consensus.test_config import test_config

############################################################
############################################################
#正常节点和vbft共识
class test_consensus_1(ParametrizedTestCase):
	def test_init(self):
		test_api.init()

	def setUp(self):
		logger.open("test_consensus/" + self._testMethodName+".log",self._testMethodName)
		if self._testMethodName == "test_init":
			return 
		
	def tearDown(self):
		logger.close(self.result())
	
	def test_base_001_consensus(self):
		storage_key = ByteToHex(b'Test Key 02')
		storage_value = ByteToHex(b'Test Value 02')
		for i in range(10):
			print("test put---------------------", i)
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
			API.node().wait_gen_block()
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
			API.node().wait_gen_block()
		return

		process = False
		try:
			(process, response) = test_api.transfer(test_config.m_contract_addr, Config.NODES[test_config.m_current_node]["address"], Config.NODES[1]["address"], test_config.AMOUNT, test_config.m_current_node)
			self.ASSERT(process, "transfer error...")
	
			(process, response) = API.rpc().getblockheightbytxhash(response["txhash"])
			self.ASSERT(process, "not a valid block...")
		except Exception as e:
			logger.print(e.args[0])
	
	#contract_address, function_str, callerOntID, public_key="1", argvs = [{"type": "string","value": ""}], node_index = None
	def test_normal_002_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 02')
			storage_value = ByteToHex(b'Test Value 02')
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function put error...")
			API.node().wait_gen_block()
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function get error...")
			self.ASSERT(response["result"]["Result"] == storage_value, "invoke_function get error...")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_003_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 03')
			storage_value = ByteToHex(b'Test Value 03')
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
			self.ASSERT(process, "invoke_function put error...")
			API.node().wait_gen_block()
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
			self.ASSERT(response["result"]["Result"] == '', "invoke_function get error...")
		
		except Exception as e:
			logger.print(e.args[0])
		
	def test_normal_004_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 04')
			storage_value = ByteToHex(b'Test Value 04')
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function put error...")
			API.node().wait_gen_block()
			process = API.node().check_node_state([0,1,2,3,4,5,6])
			self.ASSERT(process, "")

		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_005_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 05')
			storage_value = ByteToHex(b'Test Value 05')
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function put error...")
			API.node().wait_gen_block()
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr2, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function get error...[1]")
			self.ASSERT(response["result"]["Result"] != storage_value, "invoke_function get error...[2]")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_base_006_consensus(self):
		try:
			stopnodes = test_config.m_stop_2_nodes
			storage_key = ByteToHex(b'Test Key 06')
			storage_value = ByteToHex(b'Test Value 06')
			
			API.node().stop_nodes(stopnodes)
			
			process = False
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function put error...")
			API.node().wait_gen_block()
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function get error...[1]")
			self.ASSERT(response["result"]["Result"] == storage_value, "invoke_function get error...[2]")

			API.node().start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
			time.sleep(3)
		except Exception as e:
			logger.print(e.args[0])
		
	def test_normal_007_consensus(self):
		try:
			stopnodes = test_config.m_stop_2_nodes
			API.node().stop_nodes(stopnodes)
		
			process = False
			storage_key = ByteToHex(b'Test Key 07')
			storage_value = ByteToHex(b'Test Value 07')

			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
			self.ASSERT(process, "invoke_function put error...")
			API.node().wait_gen_block()
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
			self.ASSERT(response["result"]["Result"] == '', "invoke_function get error...")
			
			API.node().start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
		except Exception as e:
			logger.print(e.args[0])
		
	def test_normal_008_consensus(self):
		try:
			stopnodes = test_config.m_stop_2_nodes
			API.node().stop_nodes(stopnodes)
			process = False
			(process, response) = test_api.transfer(test_config.m_contract_addr, Config.NODES[test_config.m_current_node]["address"], Config.NODES[1]["address"], test_config.AMOUNT, test_config.m_current_node)
			self.ASSERT(process, "transfer error...")
			API.node().wait_gen_block()
			API.node().wait_gen_block()

			(process, response) = API.rpc().getblockheightbytxhash(response["txhash"])
			self.ASSERT(process, "not a valid block...")

			API.node().start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_009_consensus(self):
		try:
			stopnodes = test_config.m_stop_2_nodes
			API.node().stop_nodes(stopnodes)
			process = False
			for i in range(10):
				storage_key = ByteToHex(bytes("Test Key 09-" + str(i), encoding = "utf8"))
				storage_value = ByteToHex(bytes("Test Value 09-" + str(i), encoding = "utf8"))

				logger.print("times: " + str(i))
				(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
				self.ASSERT(process, "invoke_function put error...")

				time.sleep(30)
				(process, response) = API.rpc().getblockheightbytxhash(response["txhash"])
				self.ASSERT(process, "not a valid block...in " + str(i) + " times")
				time.sleep(10)
				
			API.node().start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
		except Exception as e:
			logger.print(e.args[0])


	def test_base_019_consensus(self):
		try:
			(process, response) = test_api.transfer(test_config.m_contract_addr, test_config.ADDRESS_A, test_config.ADDRESS_B, test_config.AMOUNT, node_index=0)
			self.ASSERT(process, "test_base_019_consensus failed")	
		except Exception as e:
			logger.print(e.args[0])
		

	def test_normal_020_consensus(self):
		try:
			m = 1
			pubkey_array = [test_config.PUBLIC_KEY]
			(process, response) = test_api.multi_sig_transfer(test_config.m_contract_addr, test_config.ADDRESS_A, test_config.ADDRESS_B, test_config.AMOUNT, m, pubkey_array, node_index=0)
			self.ASSERT(process, "test_normal_020_consensus failed")	
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_021_consensus(self):
		try:
			m = 1
			pubkey_array = [test_config.PUBLIC_KEY]
			(process, response) = test_api.multi_sig_transfer(test_config.m_contract_addr, test_config.ADDRESS_A, test_config.ADDRESS_B, test_config.AMOUNT, m, pubkey_array, node_index=1)
			self.ASSERT(process, "test_normal_021_consensus failed")	
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_022_consensus(self):
		try:
			m = 1
			pubkey_array = [test_config.PUBLIC_KEY]
			(process, response) = test_api.multi_sig_transfer(test_config.m_contract_addr, test_config.ADDRESS_C, test_config.ADDRESS_B, test_config.AMOUNT, m, pubkey_array, node_index=2)
			self.ASSERT(process, "test_normal_022_consensus failed")	
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_023_consensus(self):
		try:
			m = 1
			pubkey_array = [test_config.PUBLIC_KEY]
			(process, response) = test_api.multi_sig_transfer(test_config.m_contract_addr, test_config.ADDRESS_C, test_config.ADDRESS_B, test_config.AMOUNT, m, pubkey_array, node_index=0)
			self.ASSERT(not process, "test_abnormal_023_consensus failed")	
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_024_consensus(self):
		try:
			# test_api.init()
			m = 4
			pubkey_array = [test_config.PUBLIC_KEY_2, test_config.PUBLIC_KEY_3, test_config.PUBLIC_KEY_4, test_config.PUBLIC_KEY_5]
			(process, response) = test_api.multi_sig_transfer(test_config.m_contract_addr, test_config.ADDRESS_A, test_config.ADDRESS_B, test_config.AMOUNT, m, pubkey_array, node_index=0)
			self.ASSERT(process, "test_normal_024_consensus failed")	
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_025_consensus(self):
		try:
			test_api.init()
			m = 4
			pubkey_array = [test_config.PUBLIC_KEY_3, test_config.PUBLIC_KEY_4, test_config.PUBLIC_KEY_5, test_config.PUBLIC_KEY_6]
			(process, response) = test_api.multi_sig_transfer(test_config.m_contract_addr, test_config.ADDRESS_A, test_config.ADDRESS_B, test_config.AMOUNT, m, pubkey_array, node_index=1)
			self.ASSERT(not process, "test_abnormal_025_consensus failed")	
		except Exception as e:
			logger.print(e.args[0])

	def test_base_030_consensus(self):
		try:
			test_api.init()
			# ensure balance of wallet A is 1000
			balance_of_wallet_A1 = int(API.rpc().getbalance(test_config.ADDRESS_A)[1]["result"]["ont"]) 
			(process, response) = API.native().transfer_ont(test_config.ADDRESS_A, test_config.ADDRESS_B, str(balance_of_wallet_A1-1000), 0)

			balance_of_wallet_A1 = int(API.rpc().getbalance(test_config.ADDRESS_A)[1]["result"]["ont"]) 
			balance_of_wallet_B1 = int(API.rpc().getbalance(test_config.ADDRESS_B)[1]["result"]["ont"]) 
			balance_of_wallet_C1 = int(API.rpc().getbalance(test_config.ADDRESS_C)[1]["result"]["ont"]) 

			(process, response) = API.native().transfer_ont(test_config.ADDRESS_A, test_config.ADDRESS_B, "1000", 0, sleep=0)
			(process, response) = API.native().transfer_ont(test_config.ADDRESS_A, test_config.ADDRESS_C, "1000", 0, sleep=0)
			API.node().wait_gen_block()

			balance_of_wallet_A2 = int(API.rpc().getbalance(test_config.ADDRESS_A)[1]["result"]["ont"]) 
			balance_of_wallet_B2 = int(API.rpc().getbalance(test_config.ADDRESS_B)[1]["result"]["ont"]) 
			balance_of_wallet_C2 = int(API.rpc().getbalance(test_config.ADDRESS_C)[1]["result"]["ont"]) 
			self.ASSERT(balance_of_wallet_A2 == 0, "wallet A balance changed[1]")	
			self.ASSERT((balance_of_wallet_A1 + balance_of_wallet_B1 + balance_of_wallet_C1) == (balance_of_wallet_A2 + balance_of_wallet_B2 + balance_of_wallet_C2), "wallet A balance changed[2]")	
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_031_consensus(self):
		try:
			test_api.init()
			# ensure balance of wallet A is 1000
			balance_of_wallet_A = int(API.rpc().getbalance(test_config.ADDRESS_A)[1]["result"]["ont"]) 
			(process, response) = API.native().transfer_ont(test_config.ADDRESS_A, test_config.ADDRESS_B, str(balance_of_wallet_A-1000), 0)
			API.node().wait_gen_block()

			(process, response) = API.native().approve_ont(test_config.ADDRESS_A, test_config.ADDRESS_B, "1000", 0, sleep=0)
			(process, response) = API.native().approve_ont(test_config.ADDRESS_A, test_config.ADDRESS_C, "1000", 0, sleep=0)
			API.node().wait_gen_block()

			balance_of_wallet_A = int(API.rpc().getbalance(test_config.ADDRESS_A)[1]["result"]["ont"]) 
			self.ASSERT(balance_of_wallet_A == 1000, "wallet A balance changed")

			(process, responseb) = API.native().allowance_ont(test_config.ADDRESS_A, test_config.ADDRESS_B, 0)
			# need to check
			#self.ASSERT(response["result"] == "00" , "allowance to wallet B is not 0")
			(process, responsec) = API.native().allowance_ont(test_config.ADDRESS_A, test_config.ADDRESS_C, 0)
			# need to checkADDRESS_C
			#e803 == 1000 num
			self.ASSERT(responseb["result"]["Result"] == "e803" or responsec["result"]["Result"] == "e803", "allowance to wallet B/C is not 0")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_032_consensus(self):
		try:
			test_api.init()
			# ensure balance of wallet A is 1000
			balance_of_wallet_A = int(API.rpc().getbalance(test_config.ADDRESS_A)[1]["result"]["ont"]) 
			(process, response) = API.native().transfer_ont(test_config.ADDRESS_A, test_config.ADDRESS_B, str(balance_of_wallet_A-1000), 0)
			API.node().wait_gen_block()

			(process, response) = API.native().approve_ont(test_config.ADDRESS_B, test_config.ADDRESS_A, "1000", 1)
			API.node().wait_gen_block()

			(process, response) = API.native().transfer_ont(test_config.ADDRESS_A, test_config.ADDRESS_B, "1000", 0, sleep=0)
			(process, response) = API.native().transfer_ont(test_config.ADDRESS_A, test_config.ADDRESS_C, "1000", 0, sleep=0)
			API.node().wait_gen_block()

			balance_of_wallet_A = int(API.rpc().getbalance(test_config.ADDRESS_A)[1]["result"]["ont"]) 
			self.ASSERT(balance_of_wallet_A == 0, "wallet A balance changed")	

			(process, response) = API.native().allowance_ont(test_config.ADDRESS_B, test_config.ADDRESS_A, 1)
			# need to check
			self.ASSERT(response["result"]["Result"] == "e803" , "allowance to wallet A is not 1000")

		except Exception as e:
			logger.print(e.args[0])

		
############################################################
############################################################
#拜占庭节点, 5, 6节点是拜占庭节点
class test_consensus_2(ParametrizedTestCase):
	def test_init(self):
		pass
	
	def setUp(self):
		logger.open( "test_consensus/" + self._testMethodName+".log",self._testMethodName)
		if self._testMethodName == "test_init":
			return 
		
	def tearDown(self):
		logger.close(self.result())
		
	def init_bft_node(self, bft_index):
		API.node().stop_all_nodes()
		API.node().start_nodes([0,1,2,3,4], Config.DEFAULT_NODE_ARGS, True, True, program = "ontology")
		logger.info("start bft node: " + "ontology-bft_" + str(bft_index))
		API.node().start_nodes([5,6], Config.DEFAULT_NODE_ARGS, True, True, program = "ontology-bft_" + str(bft_index))
		
		for node_index in range(7):			
			API.native().regid_with_publickey(node_index)
		API.native().init_ont_ong()
		
		(test_config.m_contract_addr, test_config.m_contract_txhash) = API.contract().deploy_contract_full(test_config.deploy_neo_1, test_config.name1, test_config.desc, test_config.price)
		(test_config.m_contract_addr2, test_config.m_contract_txhash2) = API.contract().deploy_contract_full(test_config.deploy_neo_2, test_config.name1, test_config.desc, test_config.price)
		
		
	def test_normal_010_consensus(self):
		try:
			process = False
			storage_key = ByteToHex(b'Test Key 10')
			storage_value = ByteToHex(b'Test Value 10')
			for i in range(1, 4):
				self.init_bft_node(i)
				time.sleep(30)
				(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
				self.ASSERT(process, "invoke_function error...")

				(process, response) = API.rpc().getblockheightbytxhash(response["txhash"])
				self.ASSERT(process, "not a valid block...")
				
		except Exception as e:
			logger.print(e.args[0])
	
	#contract_address, function_str, callerOntID, public_key="1", argvs = [{"type": "string","value": ""}], node_index = None
	def test_normal_011_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 11')
			storage_value = ByteToHex(b'Test Value 11')
			for i in range(1, 4):
				self.init_bft_node(i)
				time.sleep(30)
				(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
				self.ASSERT(process, "invoke_function put error...")
				
				(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
				self.ASSERT(process, "invoke_function error...[1]")
				self.ASSERT(response["result"]["Result"] == storage_value, "invoke_function error...[2]")

		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_012_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 12')
			storage_value = ByteToHex(b'Test Value 12')
			for i in range(1, 4):
				self.init_bft_node(i)
				time.sleep(30)
				
				#A节点是Admin节点
				(process, response) = API.contract().init_admin(test_config.m_contract_addr, Config.ontID_A)
				self.ASSERT(process, "init_admin error...")
					
				(process, response) = API.native().bind_role_function(test_config.m_contract_addr, Config.ontID_A, Config.roleA_hex, ["auth_put"])
				self.ASSERT(process, "bind_role_function error...")
				
				(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
				self.ASSERT(process, "invoke_function put error...")
				
				(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
				self.ASSERT(response["result"]["Result"] == '', "invoke_function get error...")

		except Exception as e:
			logger.print(e.args[0])
		
	def test_normal_013_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 13')
			storage_value = ByteToHex(b'Test Value 13')
			for i in range(1, 4):
				self.init_bft_node(i)
				time.sleep(30)
				for j in range(10):
					(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
					self.ASSERT(process, "invoke_function put error...")
					API.node().wait_gen_block()
						
		except Exception as e:
			logger.print(e.args[0])
		
		
############################################################
############################################################
#dbft共识
class test_consensus_3(ParametrizedTestCase):
	def test_init(self):
		for node_index in range(len(Config.NODES)):
			API.node().stop_nodes([node_index])
		API.node().start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True, config="config-dbft.json")
		#start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
		for node_index in range(7):
			API.native().regid_with_publickey(node_index)
		
		API.native().init_ont_ong()
		
		(test_config.m_contract_addr, test_config.m_contract_txhash) = API.contract().deploy_contract_full(test_config.deploy_neo_1, test_config.name1, test_config.desc, test_config.price)
		(test_config.m_contract_addr2, test_config.m_contract_txhash2) = API.contract().deploy_contract_full(test_config.deploy_neo_2, test_config.name1, test_config.desc, test_config.price)
		
		#A节点是Admin节点
		(process, response) = API.contract().init_admin(test_config.m_contract_addr, Config.ontID_A)
		time.sleep(6)
		(process, response) = API.native().bind_role_function(test_config.m_contract_addr, Config.ontID_A, Config.roleA_hex, ["auth_put"])
		
	
	def setUp(self):
		logger.open( "test_consensus/" +  self._testMethodName+".log",self._testMethodName)
		if self._testMethodName == "test_init":
			return 
		test_config.AMOUNT = "1001"
	
	def tearDown(self):
		logger.close(self.result())
	
	def test_normal_014_consensus(self):
		process = False
		try:
			(process, response) = test_api.transfer(test_config.m_contract_addr, Config.NODES[test_config.m_current_node]["address"], Config.NODES[1]["address"], test_config.AMOUNT, test_config.m_current_node)
			self.ASSERT(process, "transfer error...")
			API.node().wait_gen_block()
			(process, response) = API.rpc().getblockheightbytxhash(response["txhash"])
			self.ASSERT(process, "not a valid block...")

		except Exception as e:
			logger.print(e.args[0])
		
	
	def test_normal_015_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 15')
			storage_value = ByteToHex(b'Test Value 15')

			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function put error...")
			
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function get error...")

		except Exception as e:
			logger.print(e.args[0])
		
	def test_abnormal_016_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 16')
			storage_value = ByteToHex(b'Test Value 16')
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
			self.ASSERT(process, "invoke_function put error...")
			
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
			self.ASSERT(response["result"]["Result"] == '', "invoke_function get error...")

		except Exception as e:
			logger.print(e.args[0])
		
	def test_normal_017_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 17')
			storage_value = ByteToHex(b'Test Value 17')
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function put error...")

			process = API.node().check_node_state([0,1,2,3,4,5,6])
			self.ASSERT(process, "check_node_state")

		except Exception as e:
			logger.print(e.args[0])
		
	def test_normal_018_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 18')
			storage_value = ByteToHex(b'Test Value 18')
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function put error...")

			(process, response) = API.contract().invoke_function(test_config.m_contract_addr2, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function get error...[1]")
			self.ASSERT(response["result"]["Result"] != storage_value, "invoke_function get error...[2]")		
		except Exception as e:
			logger.print(e.args[0])


class test_consensus_4(ParametrizedTestCase):
	
	def setUp(self):
		logger.open( "test_consensus/" +  self._testMethodName+".log",self._testMethodName)
		self.m_checknode = 4
		time.sleep(2)
		print("stop all")
		API.node().stop_all_nodes()
		print("start all")
		API.node().start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
		for i in range(0, 7):
			API.native().regid_with_publickey(i)
		API.native().init_ont_ong()
		
	def tearDown(self):
		logger.close(self.result())
	
	def test_base_033_consensus(self):
		process = False
		try:
			test_api.add_candidate_node(7, init_pos = 2000, from_node = 0)
			test_api.getStorageConf("vbftConfig")
			# step 2 wallet A unvote in the second round
			(process, response) = API.native().commit_dpos()
			API.node().wait_gen_block()
			
			test_api.getStorageConf("vbftConfig")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_034_consensus(self):
		process = False
		try:
			vote_node = 13 #投票节点
			peer_node1 = 7 #被投票节点1
			peer_node2 = 8 #被投票节点2
			peer_node3 = 9 #被投票节点3
				
			API.node().start_nodes([vote_node], Config.DEFAULT_NODE_ARGS, True, True)
			API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[vote_node]["address"], "1000000", 0)
			API.native().transfer_ong(Config.NODES[0]["address"], Config.NODES[vote_node]["address"], "1000000000000", 0)

			for i in range(7, 14):
				test_api.add_candidate_node(i, init_pos = 10000, from_node = 0)
			(process, response) = API.native().vote_for_peer(Config.NODES[vote_node]["address"], [Config.NODES[peer_node1]["pubkey"], Config.NODES[peer_node2]["pubkey"], Config.NODES[peer_node3]["pubkey"]], ["15000", "15000", "15000"])
			self.ASSERT(process, "vote_for_peer error")
			
			test_api.getStorageConf("vbftConfig")
			# step 2 wallet A unvote in the second round
			(process, response) = API.native().commit_dpos()
			API.node().wait_gen_block()

			test_api.getStorageConf("vbftConfig")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])


if __name__ == '__main__':
    unittest.main()
