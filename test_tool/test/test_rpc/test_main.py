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
sys.path.append('../..')
testpath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(testpath)

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.taskrunner import TaskRunner
from api.apimanager import API
from test_rpc.test_config import test_config


######################################################
# test cases
class test_rpc_1(ParametrizedTestCase):
	def setUp(self):
		logger.open( "test_rpc/" + self._testMethodName+".log",self._testMethodName)
		API.node().stop_all_nodes()
		API.node().start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(5)
		
	def tearDown(self):
		logger.close(self.result())
		
	# can not test
	def test_normal_021_getbestblockhash(self):
		try:
			# self.clear_nodes()
			(process, response) = API.rpc().getbestblockhash()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
		
	# can not test
	def test_normal_023_getblockcount(self):
		try:
			# self.clear_nodes()
			(process, response) = API.rpc().getblockcount()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
class test_rpc_2(ParametrizedTestCase):
	def test_init(self):
		
		API.node().stop_all_nodes()
		API.node().start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True)
		API.node().wait_gen_block()
		API.node().wait_gen_block()
		
		(test_config.m_contractaddr_right, test_config.m_txhash_right) = API.contract().deploy_contract_full(testpath+"/resource/A.neo", "name", "desc", 0)
		API.node().wait_gen_block()

		test_config.m_getstorage_contract_addr = test_config.m_contractaddr_right
		(result, response) = API.rpc().getblockhash(height = 1)
		test_config.m_block_hash_right = response["result"]
		(result, response) = API.contract().sign_transction(Task(testpath+"/resource/cli/siginvoketx.json"), False)
		test_config.m_signed_txhash_right = response["result"]["signed_tx"]
		test_config.m_signed_txhash_wrong = test_config.m_signed_txhash_right + "0f0f0f0f"
		test_config.m_getstorage_contract_addr_wrong = test_config.m_contractaddr_right + "0f0f0f0f"

		
		API.contract().invoke_function(test_config.m_contractaddr_right, "put", "", "1", argvs = [{"type": "bytearray","value": test_config.m_getstorage_contract_key},{"type": "bytearray","value": test_config.m_getstorage_contract_value}], node_index = 0)
		
	def setUp(self):
		logger.open( "test_rpc/"+self._testMethodName+".log",self._testMethodName)
		if self._testMethodName == "test_init":
			return 
		time.sleep(1)
		
	def tearDown(self):
		logger.close(self.result())
			
	def test_base_001_getblock(self):
		try:
			(process, response) = API.rpc().getblock(height = None, blockhash = test_config.m_block_hash_right, verbose = None)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_002_getblock(self):
		try:
			(process, response) = API.rpc().getblock(height = None, blockhash = test_config.m_block_hash_error, verbose = None)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_003_getblock(self):
		try:
			(process, response) = API.rpc().getblock(height = test_config.m_block_height_right, blockhash = None, verbose = None)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_004_getblock(self):
		try:
			(process, response) = API.rpc().getblock(height = 0, blockhash = None, verbose = None)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_abnormal_005_getblock(self):
		try:
			(process, response) = API.rpc().getblock(height = test_config.m_block_height_wrong, blockhash = None, verbose = None)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_006_getblock(self):
		try:
			(process, response) = API.rpc().getblock(height = test_config.m_block_height_overflow, blockhash = None, verbose = None)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_007_getblock(self):
		try:
			(process, response) = API.rpc().getblock(height = test_config.m_block_height_right, blockhash = None, verbose = 0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_008_getblock(self):
		try:
			(process, response) = API.rpc().getblock(height = test_config.m_block_height_right, blockhash = None, verbose = 1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_009_getblock(self):
		try:
			(process, response) = API.rpc().getblock(height = test_config.m_block_height_right, blockhash = None, verbose = -1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_010_getblock(self):
		try:
			(process, response) = API.rpc().getblock(height = test_config.m_block_height_right, blockhash = None, verbose = 2)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_011_getblock(self):
		try:
			(process, response) = API.rpc().getblock(height = test_config.m_block_height_right, blockhash = None, verbose = "abc")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_012_getblock(self):
		try:
			(process, response) = API.rpc().getblock(height = test_config.m_block_height_right, blockhash = None, verbose = None)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_013_getblockhash(self):
		try:
			(process, response) = API.rpc().getblockhash(height = test_config.m_block_height_right)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_014_getblockhash(self):
		try:
			(process, response) = API.rpc().getblockhash(height = 0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_015_getblockhash(self):
		try:
			(process, response) = API.rpc().getblockhash(height = test_config.m_block_height_wrong)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_016_getblockhash(self):
		try:
			(process, response) = API.rpc().getblockhash(height = test_config.m_block_height_overflow)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_017_getblockhash(self):
		try:
			(process, response) = API.rpc().getblockhash(height = "abc")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_018_getblockhash(self):
		try:
			(process, response) = API.rpc().getblockhash(height = -1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_019_getblockhash(self):
		try:
			(process, response) = API.rpc().getblockhash(height = None)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_020_getbestblockhash(self):
		try:
			(process, response) = API.rpc().getbestblockhash()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_base_022_getblockcount(self):
		try:
			(process, response) = API.rpc().getblockcount()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_024_getconnectioncount(self):
		try:
			(process, response) = API.rpc().getconnectioncount()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	# can not test
	def test_normal_025_getconnectioncount(self):
		try:
			API.node().stop_nodes([1, 2, 3, 4, 5, 6])
		
			(process, response) = API.rpc().getconnectioncount()
		
			API.node().start_nodes([1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, False, False)
			time.sleep(10)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
			
	def test_abnormal_026_getgenerateblocktime(self):
		try:
			(process, response) = API.rpc().getgenerateblocktime()
			self.ASSERT(process and (not response["result"]), "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_base_027_getrawtransaction(self):
		try:
			(process, response) = API.rpc().getrawtransaction(test_config.m_txhash_right)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_028_getrawtransaction(self):
		try:
			(process, response) = API.rpc().getrawtransaction(test_config.m_txhash_wrong)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_029_getrawtransaction(self):
		try:
			(process, response) = API.rpc().getrawtransaction("abc")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_030_getrawtransaction(self):
		try:
			(process, response) = API.rpc().getrawtransaction(1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_031_getrawtransaction(self):
		try:
			(process, response) = API.rpc().getrawtransaction(None)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_032_getrawtransaction(self):
		try:
			(process, response) = API.rpc().getrawtransaction(test_config.m_txhash_right, 1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_033_getrawtransaction(self):
		try:
			(process, response) = API.rpc().getrawtransaction(test_config.m_txhash_right, 0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_034_getrawtransaction(self):
		try:
			(process, response) = API.rpc().getrawtransaction(test_config.m_txhash_right, -1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_035_getrawtransaction(self):
		try:
			(process, response) = API.rpc().getrawtransaction(test_config.m_txhash_right, 2)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_036_getrawtransaction(self):
		try:
			(process, response) = API.rpc().getrawtransaction(test_config.m_txhash_right, "abc")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_037_getrawtransaction(self):
		try:
			(process, response) = API.rpc().getrawtransaction(test_config.m_txhash_right, None)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_base_038_sendrawtransaction(self):
		try:
			(process, response) = API.rpc().sendrawtransaction(test_config.m_signed_txhash_right)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_039_sendrawtransaction(self):
		try:
			(process, response) = API.rpc().sendrawtransaction("")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_040_sendrawtransaction(self):
		try:
			(process, response) = API.rpc().sendrawtransaction(None)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_base_041_getstorage(self):
		try:
			(process, response) = API.rpc().getstorage(test_config.m_getstorage_contract_addr, test_config.m_getstorage_contract_key)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_042_getstorage(self):
		try:
			(process, response) = API.rpc().getstorage(test_config.m_getstorage_contract_addr_wrong, test_config.m_getstorage_contract_key)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_043_getstorage(self):
		try:
			(process, response) = API.rpc().getstorage("abc", test_config.m_getstorage_contract_key)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_044_getstorage(self):
		try:
			(process, response) = API.rpc().getstorage(1, test_config.m_getstorage_contract_key)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_045_getstorage(self):
		try:
			(process, response) = API.rpc().getstorage(None, test_config.m_getstorage_contract_key)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_046_getstorage(self):
		try:
			(process, response) = API.rpc().getstorage(test_config.m_getstorage_contract_addr, test_config.m_getstorage_contract_key)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_047_getstorage(self):
		try:
			(process, response) = API.rpc().getstorage(test_config.m_getstorage_contract_addr, "getstorage_key_error")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_048_getstorage(self):
		try:
			(process, response) = API.rpc().getstorage(test_config.m_getstorage_contract_addr, "abc")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_049_getstorage(self):
		try:
			(process, response) = API.rpc().getstorage(test_config.m_getstorage_contract_addr, 123)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_050_getstorage(self):
		try:
			(process, response) = API.rpc().getstorage(test_config.m_getstorage_contract_addr, None)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	

	def test_base_051_getversion(self):
		try:
			(process, response) = API.rpc().getversion()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_058_getcontractstate(self):
		try:
			(process, response) = API.rpc().getcontractstate(test_config.m_contractaddr_right)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_059_getcontractstate(self):
		try:
			(process, response) = API.rpc().getcontractstate(test_config.m_txhash_wrong)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_060_getcontractstate(self):
		try:
			(process, response) = API.rpc().getcontractstate("abc")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_061_getcontractstate(self):
		try:
			(process, response) = API.rpc().getcontractstate(123)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_062_getcontractstate(self):
		try:
			(process, response) = API.rpc().getcontractstate(None, 1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_063_getcontractstate(self):
		try:
			(process, response) = API.rpc().getcontractstate(test_config.m_contractaddr_right, 1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_064_getcontractstate(self):
		try:
			(process, response) = API.rpc().getcontractstate(test_config.m_contractaddr_right, -1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_065_getcontractstate(self):
		try:
			(process, response) = API.rpc().getcontractstate(test_config.m_contractaddr_right, 2)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_066_getcontractstate(self):
		try:
			(process, response) = API.rpc().getcontractstate(test_config.m_contractaddr_right, "abc")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_067_getcontractstate(self):
		try:
			(process, response) = API.rpc().getcontractstate(test_config.m_contractaddr_right, 0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_068_getcontractstate(self):
		try:
			(process, response) = API.rpc().getcontractstate(test_config.m_contractaddr_right, None)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_069_getmempooltxstate(self):
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contractaddr_right, "put", "", "1", argvs = [{"type": "bytearray","value": test_config.m_getstorage_contract_key},{"type": "bytearray","value": test_config.m_getstorage_contract_value}], node_index = 0, sleep = 0)

			(process, response) = API.rpc().getmempooltxstate(response["txhash"])
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_070_getmempooltxstate(self):
		try:
			(process, response) = API.rpc().getmempooltxstate(test_config.m_txhash_right)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_071_getmempooltxstate(self):
		try:
			(process, response) = API.rpc().getmempooltxstate("abc")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_072_getmempooltxstate(self):
		try:
			(process, response) = API.rpc().getmempooltxstate(123)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_073_getmempooltxstate(self):
		try:
			(process, response) = API.rpc().getmempooltxstate(None)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_base_074_getsmartcodeevent(self):
		try:
			(process, response) = API.rpc().getsmartcodeevent(height = test_config.getsmartcodeevent_height)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_075_getsmartcodeevent(self):
		try:
			(process, response) = API.rpc().getsmartcodeevent(height = 99999999)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_076_getsmartcodeevent(self):
		try:
			(process, response) = API.rpc().getsmartcodeevent(height="abc")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_077_getsmartcodeevent(self):
		try:
			(process, response) = API.rpc().getsmartcodeevent(height =None)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_078_getsmartcodeevent(self):
		try:
			(process, response) = API.rpc().getsmartcodeevent(tx_hash = test_config.m_txhash_right)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_079_getsmartcodeevent(self):
		try:
			(process, response) = API.rpc().getsmartcodeevent(tx_hash = test_config.m_txhash_wrong)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_base_080_getblockheightbytxhash(self):
		try:
			(process, response) = API.rpc().getblockheightbytxhash(tx_hash = test_config.m_txhash_right)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_081_getblockheightbytxhash(self):
		try:
			(process, response) = API.rpc().getblockheightbytxhash(tx_hash = test_config.m_txhash_wrong)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_082_getblockheightbytxhash(self):
		try:
			(process, response) = API.rpc().getblockheightbytxhash(tx_hash = "abc")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_083_getblockheightbytxhash(self):
		try:
			(process, response) = API.rpc().getblockheightbytxhash(tx_hash = 123)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_084_getblockheightbytxhash(self):
		try:
			(process, response) = API.rpc().getblockheightbytxhash(tx_hash = None)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_085_getbalance(self):
		try:
			(process, response) = API.rpc().getbalance(test_config.getbalance_address_true)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_086_getbalance(self):
		try:
			(process, response) = API.rpc().getbalance(test_config.getbalance_address_false)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_087_getbalance(self):
		try:
			(process, response) = API.rpc().getbalance("abc")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_088_getbalance(self):
		try:
			(process, response) = API.rpc().getbalance(None)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_base_089_getmerkleproof(self):
		try:
			(process, response) = API.rpc().getmerkleproof(test_config.m_txhash_right)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_090_getmerkleproof(self):
		try:
			(process, response) = API.rpc().getmerkleproof(test_config.m_txhash_wrong)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_091_getmerkleproof(self):
		try:
			(process, response) = API.rpc().getmerkleproof("abc")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_092_getmerkleproof(self):
		try:
			(process, response) = API.rpc().getmerkleproof("123")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_093_getmerkleproof(self):
		try:
			(process, response) = API.rpc().getmerkleproof(None)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_094_getmerkleproof(self):
		try:
			task = Task(testpath+"/resource/rpc/94_getmerkleproof.json")
			task.request()["params"] = [test_config.m_txhash_right]
			(process, response) =  TaskRunner.run_single_task(task)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_095_getmerkleproof(self):
		try:
			task = Task(testpath+"/resource/rpc/95_getmerkleproof.json")
			task.request()["params"] = [test_config.m_txhash_right]
			(process, response) =  TaskRunner.run_single_task(task)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	# can not test
	'''
	def test_abnormal_096_getmerkleproof(self):
		try:
			task = Task(testpath+"/resource/rpc/96_getmerkleproof.json")
			(process, response) =  TaskRunner.run_single_task(task)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	'''
	
	def test_abnormal_097_getmerkleproof(self):
		try:
			task = Task(testpath+"/resource/rpc/97_getmerkleproof.1.json")
			(process, response) =  TaskRunner.run_single_task(task)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

if __name__ == '__main__':
    unittest.main()