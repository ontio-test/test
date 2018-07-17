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
from utils.contractapi import *
from test_api import *
from utils.rpcapi import *
from utils.init_ong_ont import *

############################################################
############################################################
#正常节点和vbft共识
class TestConsensus_1_9__19_32(ParametrizedTestCase):
	@classmethod
	def setUpClass(cls):
		for i in range(len(Config.NODES)):
			stop_nodes([i])
		start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(8)
		regIDWithPublicKey(0)
		regIDWithPublicKey(1)
		regIDWithPublicKey(2)
		regIDWithPublicKey(3)
		regIDWithPublicKey(4)
		regIDWithPublicKey(5)
		regIDWithPublicKey(6)
		
		init_ont_ong()
		time.sleep(10)
		
		(cls.m_contract_addr, cls.m_contract_txhash) = deploy_contract_full("tasks/A.neo", "name", "desc", 0)
		(cls.m_contract_addr2, cls.m_contract_txhash2) = deploy_contract_full("tasks/B.neo", "nameB", "descB", 0)
		
		#A节点是Admin节点
		(result, response) = init_admin(cls.m_contract_addr, Config.ontID_A)
		(result, response) = bind_role_function(cls.m_contract_addr, Config.ontID_A, Config.roleA_hex, ["auth_put"])
		
		cls.m_current_node = 0
		cls.m_storage_key = ByteToHex(b'Test Key')
		cls.m_storage_value = ByteToHex(b'Test Value')
		cls.m_stop_2_nodes = [5,6]
	
	def setUp(self):
		(contract_addr, contract_tx_hash) = deploy_contract_full("./tasks/neo.neo")
		self.CONTRACT_ADDRESS = contract_addr
		self.ADDRESS_A = script_hash_bl_reserver(base58_to_address(Config.NODES[0]["address"]))
		self.ADDRESS_B = script_hash_bl_reserver(base58_to_address(Config.NODES[1]["address"]))
		self.ADDRESS_C = script_hash_bl_reserver(base58_to_address(Config.NODES[2]["address"]))
		self.AMOUNT = "1001"
		self.PUBLIC_KEY = Config.NODES[0]["pubkey"]
		self.PUBLIC_KEY_2 = Config.NODES[1]["pubkey"]
		self.PUBLIC_KEY_3 = Config.NODES[2]["pubkey"]
		self.PUBLIC_KEY_4 = Config.NODES[3]["pubkey"]
		self.PUBLIC_KEY_5 = Config.NODES[4]["pubkey"]
	
	def test_01_consensus(self):
		result = False
		logger.open("01_consensus.log", "01_consensus")
		try:
			(result, response) = transfer(self.m_contract_addr, Config.NODES[self.m_current_node]["address"], Config.NODES[1]["address"], self.AMOUNT, self.m_current_node)
			if not result:
				raise Error("transfer error...")
			
			(result, response) = RPCApi().getblockheightbytxhash(response["txhash"])
			if not result:
				raise Error("not a valid block...")
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
	
	#contract_address, function_str, callerOntID, public_key="1", argvs = [{"type": "string","value": ""}], node_index = None
	def test_02_consensus(self):
		result = False
		logger.open("02_consensus.log", "02_consensus")
		storage_key = ByteToHex(b'Test Key 02')
		storage_value = ByteToHex(b'Test Value 02')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
			if not result:
				raise Error("invoke_function put error...")
			
			(result, response) = invoke_function(self.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = self.m_current_node)
			if not result or response["result"]["Result"] == storage_value:
				raise Error("invoke_function get error...")
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)

	def test_03_consensus(self):
		result = False
		logger.open("03_consensus.log", "03_consensus")
		storage_key = ByteToHex(b'Test Key 03')
		storage_value = ByteToHex(b'Test Value 03')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
			if not result:
				raise Error("invoke_function put error...")
			
			(result, response) = invoke_function(self.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
			if response["result"]["Result"] != '':
				result = False
				raise Error("invoke_function get error...")
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
		
	def test_04_consensus(self):
		result = False
		logger.open("04_consensus.log", "04_consensus")
		storage_key = ByteToHex(b'Test Key 04')
		storage_value = ByteToHex(b'Test Value 04')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
			if not result:
				raise Error("invoke_function put error...")
			
			result = check_node_state([0,1,2,3,4,5,6])
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
	
	def test_05_consensus(self):
		result = False
		logger.open("05_consensus.log", "05_consensus")
		storage_key = ByteToHex(b'Test Key 05')
		storage_value = ByteToHex(b'Test Value 05')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
			if not result:
				raise Error("invoke_function put error...")
			
			(result, response) = invoke_function(self.m_contract_addr2, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = self.m_current_node)
			if not result or response["result"]["Result"] == storage_value:
				raise Error("invoke_function get error...")
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
	
	def test_06_consensus(self):
		stopnodes = self.m_stop_2_nodes
		storage_key = ByteToHex(b'Test Key 06')
		storage_value = ByteToHex(b'Test Value 06')
		
		stop_nodes(stopnodes)
		result = False
		logger.open("06_consensus.log", "06_consensus")
		try:
			(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
			if not result:
				raise Error("invoke_function put error...")
			
			(result, response) = invoke_function(self.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = self.m_current_node)
			if not result or response["result"]["Result"] == storage_value:
				raise Error("invoke_function get error...")
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
		start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
		time.sleep(3)
	
	def test_07_consensus(self):
		stopnodes = self.m_stop_2_nodes
		stop_nodes(stopnodes)
	
		result = False
		logger.open("07_consensus.log", "07_consensus")
		storage_key = ByteToHex(b'Test Key 07')
		storage_value = ByteToHex(b'Test Value 07')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
			if not result:
				raise Error("invoke_function put error...")
			
			(result, response) = invoke_function(self.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
			if response["result"]["Result"] != '':
				result = False
				raise Error("invoke_function get error...")
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
		
		start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
		time.sleep(3)
	
	def test_08_consensus(self):
		stopnodes = self.m_stop_2_nodes
		stop_nodes(stopnodes)
		result = False
		logger.open("08_consensus.log", "08_consensus")
		try:
			(result, response) = transfer(self.m_contract_addr, Config.NODES[self.m_current_node]["address"], Config.NODES[1]["address"], self.AMOUNT, self.m_current_node)
			if not result:
				raise Error("transfer error...")
			
			(result, response) = RPCApi().getblockheightbytxhash(response["txhash"])
			if not result:
				raise Error("not a valid block...")
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
		
		start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
		time.sleep(3)
	
	def test_09_consensus(self):
		stopnodes = self.m_stop_2_nodes
		
		logger.open("09_consensus.log", "09_consensus")
		stop_nodes(stopnodes)
		result = False
		logger.open("09_consensus.log", "09_consensus")
		try:
			for i in range(10):
				storage_key = ByteToHex(bytes("Test Key 09-" + str(i), encoding = "utf8"))
				storage_value = ByteToHex(bytes("Test Value 09-" + str(i), encoding = "utf8"))

				logger.print("times: " + str(i))
				(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
				if not result:
					raise Error("invoke_function put error...")
				
				time.sleep(30)
				(result, response) = RPCApi().getblockheightbytxhash(response["txhash"])
				if not result:
					raise Error("not a valid block...in " + str(i) + " times")
				time.sleep(10)
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
		
		start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
		time.sleep(3)
	
	def test_19_consensus(self):
		log_path = "19_consensus.log"
		task_name = "19_consensus"
		self.start(log_path)
		(result, response) = transfer_19(self.CONTRACT_ADDRESS, self.ADDRESS_A, self.ADDRESS_B, self.AMOUNT)
		self.finish(task_name, log_path, result,  "")
		
	def test_20_consensus(self):
		log_path = "20_consensus.log"
		task_name = "20_consensus"
		self.start(log_path)
		(result, response) = transfer_20(self.CONTRACT_ADDRESS, self.ADDRESS_A, self.ADDRESS_B, self.AMOUNT, self.PUBLIC_KEY)
		self.finish(task_name, log_path, result,  "")

	def test_21_consensus(self):
		log_path = "21_consensus.log"
		task_name = "21_consensus"
		self.start(log_path)
		(result, response) = transfer_21(self.CONTRACT_ADDRESS, self.ADDRESS_A, self.ADDRESS_B, self.AMOUNT, self.PUBLIC_KEY)
		self.finish(task_name, log_path, result,  "")

	def test_22_consensus(self):
		log_path = "22_consensus.log"
		task_name = "22_consensus"
		self.start(log_path)
		(result, response) = transfer_22(self.CONTRACT_ADDRESS, self.ADDRESS_C, self.ADDRESS_B, self.AMOUNT, self.PUBLIC_KEY)
		self.finish(task_name, log_path, result,  "")

	def test_23_consensus(self):
		log_path = "23_consensus.log"
		task_name = "23_consensus"
		self.start(log_path)
		(result, response) = transfer_23(self.CONTRACT_ADDRESS, self.ADDRESS_C, self.ADDRESS_B, self.AMOUNT, self.PUBLIC_KEY)
		self.finish(task_name, log_path, result,  "")

	def test_24_consensus(self):
		log_path = "24_consensus.log"
		task_name = "24_consensus"
		self.start(log_path)
		(result, response) = transfer_24(self.CONTRACT_ADDRESS, self.ADDRESS_A, self.ADDRESS_B, self.AMOUNT, self.PUBLIC_KEY, self.PUBLIC_KEY_2, self.PUBLIC_KEY_3, self.PUBLIC_KEY_4)
		self.finish(task_name, log_path, result,  "")

	def test_25_consensus(self):
		log_path = "25_consensus.log"
		task_name = "25_consensus"
		self.start(log_path)
		(result, response) = transfer_25(self.CONTRACT_ADDRESS, self.ADDRESS_A, self.ADDRESS_B, self.AMOUNT, self.PUBLIC_KEY_5, self.PUBLIC_KEY_2, self.PUBLIC_KEY_3, self.PUBLIC_KEY_4)
		self.finish(task_name, log_path, result,  "")

	def test_30_consensus(self):
		log_path = "30_consensus.log"
		task_name = "30_consensus"
		self.start(log_path)
		(result, response) = transfer_19(self.CONTRACT_ADDRESS, self.ADDRESS_A, self.ADDRESS_B, "100000000")
		(result, response) = transfer_19(self.CONTRACT_ADDRESS, self.ADDRESS_A, self.ADDRESS_C, "100000000")
		self.finish(task_name, log_path, result,  "")

	def test_31_consensus(self):
		log_path = "31_consensus.log"
		task_name = "31_consensus"
		self.start(log_path)
		(result, response) = approve_31(self.CONTRACT_ADDRESS, self.ADDRESS_A, self.ADDRESS_B, "100000000")
		(result, response) = approve_31(self.CONTRACT_ADDRESS, self.ADDRESS_A, self.ADDRESS_B, "100000000")
		(result, response) = allowance(self.CONTRACT_ADDRESS, self.ADDRESS_A, self.ADDRESS_B, "100000000")
		(result, response) = allowance(self.CONTRACT_ADDRESS, self.ADDRESS_A, self.ADDRESS_B, "100000000")
		self.finish(task_name, log_path, result,  "")

	def test_32_consensus(self):
		log_path = "32_consensus.log"
		task_name = "32_consensus"
		self.start(log_path)
		(result, response) = approve_32(self.CONTRACT_ADDRESS, self.ADDRESS_C, self.ADDRESS_B, "100000000")
		(result, response) = transfer_19(self.CONTRACT_ADDRESS, self.ADDRESS_A, self.ADDRESS_B, "100000000")
		(result, response) = transfer_19(self.CONTRACT_ADDRESS, self.ADDRESS_A, self.ADDRESS_C, "100000000")
		(result, response) = allowance_32(self.ADDRESS_A, self.ADDRESS_A)
		self.finish(task_name, log_path, result,  "")
		
############################################################
############################################################
#拜占庭节点, 5, 6节点是拜占庭节点
class TestConsensus_10_13(ParametrizedTestCase):
	@classmethod
	def setUpClass(cls):
		pass
		
	def init_bft_node(self, bft_index):
		stop_all_nodes()
		start_nodes([0,1,2,3,4], Config.DEFAULT_NODE_ARGS, True, True, program = "ontology")
		print("start bft node: " + "ontology-bft_" + str(bft_index))
		start_nodes([5,6], Config.DEFAULT_NODE_ARGS, True, True, program = "ontology-bft_" + str(bft_index))
		time.sleep(8)
		
		regIDWithPublicKey(0)
		regIDWithPublicKey(1)
		regIDWithPublicKey(2)
		regIDWithPublicKey(3)
		regIDWithPublicKey(4)
		regIDWithPublicKey(5)
		regIDWithPublicKey(6)
		init_ont_ong()
		time.sleep(15)
		
		(self.m_contract_addr, self.m_contract_txhash) = deploy_contract_full("tasks/A.neo", "name", "desc", 0)
		(self.m_contract_addr2, self.m_contract_txhash2) = deploy_contract_full("tasks/B.neo", "name", "desc", 0)
		
		self.m_current_node = 0
		self.m_storage_key = ByteToHex(b'Test Key')
		self.m_storage_value = ByteToHex(b'Test Value')
		self.m_stop_2_nodes = [5,6]
		
	def test_10_consensus(self):
		result = False
		storage_key = ByteToHex(b'Test Key 10')
		storage_value = ByteToHex(b'Test Value 10')
		logger.open("10_consensus.log", "10_consensus")
		try:
			for i in range(1, 4):
				self.init_bft_node(i)
				time.sleep(30)
				(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
				if not result:
					raise Error("invoke_function error...")
				
				(result, response) = RPCApi().getblockheightbytxhash(response["txhash"])
				if not result:
					raise Error("not a valid block...")
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
	
	#contract_address, function_str, callerOntID, public_key="1", argvs = [{"type": "string","value": ""}], node_index = None
	def test_11_consensus(self):
		result = False
		logger.open("11_consensus.log", "11_consensus")
		storage_key = ByteToHex(b'Test Key 11')
		storage_value = ByteToHex(b'Test Value 11')
		try:
			for i in range(1, 4):
				self.init_bft_node(i)
				time.sleep(30)
				(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
				if not result:
					raise Error("invoke_function put error...")
				
				(result, response) = invoke_function(self.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = self.m_current_node)
				if not result or response["result"]["Result"] != storage_value:
					raise Error("invoke_function get error...")
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)

	def test_12_consensus(self):
		result = False
		logger.open("12_consensus.log", "12_consensus")
		storage_key = ByteToHex(b'Test Key 12')
		storage_value = ByteToHex(b'Test Value 12')
		try:
			for i in range(1, 4):
				self.init_bft_node(i)
				time.sleep(30)
				
				#A节点是Admin节点
				(result, response) = init_admin(self.m_contract_addr, Config.ontID_A)
				if not result:
					raise Error("init_admin error...")
					
				(result, response) = bind_role_function(self.m_contract_addr, Config.ontID_A, Config.roleA_hex, ["auth_put"])
				if not result:
					raise Error("bind_role_function error...")
				
				(result, response) = invoke_function(self.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
				if not result:
					raise Error("invoke_function put error...")
				
				(result, response) = invoke_function(self.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
				if response["result"]["Result"] != '':
					result = False
					raise Error("invoke_function get error...")
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
		
	def test_13_consensus(self):
		result = False
		logger.open("13_consensus.log", "13_consensus")
		storage_key = ByteToHex(b'Test Key 13')
		storage_value = ByteToHex(b'Test Value 13')
		try:
			for i in range(1, 4):
				self.init_bft_node(i)
				time.sleep(30)
				for j in range(10):
					(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
					if not result:
						raise Error("invoke_function put error...")
					time.sleep(10)
					
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
		
		
############################################################
############################################################
#dbft共识
class TestConsensus_14_18(ParametrizedTestCase):
	@classmethod
	def setUpClass(cls):
		for node_index in range(len(Config.NODES)):
			stop_nodes([node_index])
		start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True, config="config-dbft-1.json")
		#start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(8)
		regIDWithPublicKey(0)
		regIDWithPublicKey(1)
		regIDWithPublicKey(2)
		regIDWithPublicKey(3)
		regIDWithPublicKey(4)
		regIDWithPublicKey(5)
		regIDWithPublicKey(6)
		
		init_ont_ong()
		time.sleep(15)
		
		(cls.m_contract_addr, cls.m_contract_txhash) = deploy_contract_full("tasks/A.neo", "name", "desc", 0)
		(cls.m_contract_addr2, cls.m_contract_txhash2) = deploy_contract_full("tasks/B.neo", "name", "desc", 0)
		
		#A节点是Admin节点
		(result, response) = init_admin(cls.m_contract_addr, Config.ontID_A)
		time.sleep(6)
		(result, response) = bind_role_function(cls.m_contract_addr, Config.ontID_A, Config.roleA_hex, ["auth_put"])
		
		cls.m_current_node = 0
		cls.m_storage_key = ByteToHex(b'Test Key')
		cls.m_storage_value = ByteToHex(b'Test Value')
		cls.m_stop_2_nodes = [5,6]
	
	def setUp(self):
		self.AMOUNT = "1001"
	
	def test_14_consensus(self):
		result = False
		logger.open("14_consensus.log", "14_consensus")
		try:
			(result, response) = transfer(self.m_contract_addr, Config.NODES[self.m_current_node]["address"], Config.NODES[1]["address"], self.AMOUNT, self.m_current_node)
			if not result:
				raise Error("transfer error...")
			
			(result, response) = RPCApi().getblockheightbytxhash(response["txhash"])
			if not result:
				raise Error("not a valid block...")
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
	
	def test_15_consensus(self):
		result = False
		logger.open("15_consensus.log", "15_consensus")
		storage_key = ByteToHex(b'Test Key 15')
		storage_value = ByteToHex(b'Test Value 15')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
			if not result:
				raise Error("invoke_function put error...")
			
			(result, response) = invoke_function(self.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = self.m_current_node)
			if not result or response["result"]["Result"] != storage_value:
				raise Error("invoke_function get error...")
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
		
	def test_16_consensus(self):
		result = False
		logger.open("16_consensus.log", "16_consensus")
		storage_key = ByteToHex(b'Test Key 16')
		storage_value = ByteToHex(b'Test Value 16')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
			if not result:
				raise Error("invoke_function put error...")
			
			(result, response) = invoke_function(self.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
			if response["result"]["Result"] != '':
				result = False
				raise Error("invoke_function get error...")
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
		
	def test_17_consensus(self):
		result = False
		logger.open("17_consensus.log", "17_consensus")
		storage_key = ByteToHex(b'Test Key 17')
		storage_value = ByteToHex(b'Test Value 17')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
			if not result:
				raise Error("invoke_function put error...")
			
			result = check_node_state([0,1,2,3,4,5,6])
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
		
	def test_18_consensus(self):
		result = False
		logger.open("18_consensus.log", "18_consensus")
		storage_key = ByteToHex(b'Test Key 18')
		storage_value = ByteToHex(b'Test Value 18')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
			if not result:
				raise Error("invoke_function put error...")
			
			(result, response) = invoke_function(self.m_contract_addr2, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = self.m_current_node)
			if not result or response["result"]["Result"] == storage_value:
				raise Error("invoke_function get error...")
				
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)  


def add_candidate_node(new_node, init_ont = 5000000, init_ong = 1000, init_pos = 10000, from_node = 0):
	#新加入节点, 并申请候选节点
	start_nodes([new_node], clear_chain = True, clear_log = True)
	time.sleep(5)
	regIDWithPublicKey(new_node)
	(result, response) = bind_role_function("0700000000000000000000000000000000000000", ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),["registerCandidate"])
	if not result:
		return (result, response)
		
	(result, response) = bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES[new_node]["ontid"], encoding = "utf8"))])
	if not result:
		return (result, response)
		
	native_transfer_ont(Config.NODES[from_node]["address"], Config.NODES[new_node]["address"], str(init_ont), 0)
	native_transfer_ong(Config.NODES[from_node]["address"], Config.NODES[new_node]["address"], str(init_ong), 0)
	
	time.sleep(10)
	
	(result, response) = invoke_function_register(Config.NODES[new_node]["pubkey"], Config.NODES[new_node]["address"], str(init_pos), ByteToHex(bytes(Config.NODES[new_node]["ontid"], encoding = "utf8")), "1", new_node)
	if not result:
		return (result, response)	
		
	(result, response) = invoke_function_approve(Config.NODES[new_node]["pubkey"])		
	return (result, response)


class TestConsensus_33_34(ParametrizedTestCase):
	
	def setUp(self):
		
		self.m_checknode = 4
		time.sleep(2)
		print("stop all")
		for node_index in range(len(Config.NODES)):
			stop_nodes([node_index])
		print("start all")
		start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(10)
		for i in range(0, 7):
			regIDWithPublicKey(i)
		init_ont_ong()
	
	def test_33_consensus(self):
		result = False
		logger.open("TestConsensus33.log", "TestConsensus33.log")
		try:
			add_candidate_node(7, init_pos = 2000, from_node = 0)
			getStorageConf("vbftConfig")
			# step 2 wallet A unvote in the second round
			(result, response) = invoke_function_consensus(Config.NODES[0]["pubkey"])
			time.sleep(5)
			#if not result:
			#	raise Error("unvote error")

			getStorageConf("vbftConfig")

		except Exception as e:
			print(e.msg)

		logger.close(result)

	def test_34_consensus(self):
		result = False
		logger.open("TestConsensus34.log", "TestConsensus34")
		vote_node = 13 #投票节点
		peer_node1 = 7 #被投票节点1
		peer_node2 = 8 #被投票节点2
		peer_node3 = 9 #被投票节点3
		try:
			
			start_nodes([vote_node], Config.DEFAULT_NODE_ARGS, True, True)
			native_transfer_ont(Config.NODES[0]["address"], Config.NODES[vote_node]["address"], "5000000", 0)
			native_transfer_ong(Config.NODES[0]["address"], Config.NODES[vote_node]["address"], "1000", 0)

			for i in range(7, 14):
				add_candidate_node(i, init_pos = 10000, from_node = 0)

			(result, response) = invoke_function_vote(Config.NODES[vote_node]["address"], [Config.NODES[peer_node1]["pubkey"], Config.NODES[peer_node2]["pubkey"], Config.NODES[peer_node3]["pubkey"]], ["15000", "15000", "15000"])
			if not result:
				raise Error("vote error")
			
			getStorageConf("vbftConfig")
			# step 2 wallet A unvote in the second round
			(result, response) = invoke_function_consensus(Config.NODES[0]["pubkey"])
			time.sleep(5)
			#if not result:
			#	raise Error("unvote error")

			getStorageConf("vbftConfig")

		except Exception as e:
			print(e.msg)

		logger.close(result)


if __name__ == '__main__':
    unittest.main()
