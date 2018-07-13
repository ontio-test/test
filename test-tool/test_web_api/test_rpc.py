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
from utils.rpcapi import RPCApi
from utils.commonapi import *
from utils.contractapi import invoke_function

####################################################
logger = LoggerInstance
rpcApi = RPCApi()
####################################################



######################################################
# test cases
class Test_no_block(ParametrizedTestCase):
	def setUp(self):
		stop_all_nodes()
		start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(5)
		
	# can not test
	def test_21_getbestblockhash(self):
		self.clear_nodes()
		logger.open("rpc/21_getbestblockhash.log", "21_getbestblockhash")
		(result, response) = rpcApi.getbestblockhash()
		logger.close(result)
		
	# can not test
	def test_23_getblockcount(self):
		self.clear_nodes()
		logger.open("rpc/23_getblockcount.log", "23_getblockcount")
		(result, response) = rpcApi.getblockcount()
		logger.close(result and int(response["result"]) == 1)
	
class TestRpc(ParametrizedTestCase):
	@classmethod
	def setUpClass(cls):
		stop_all_nodes()
		start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(60)
		
		(cls.m_contractaddr_right, cls.m_txhash_right) = deploy_contract_full("tasks/A.neo", "name", "desc", 0)
		cls.m_txhash_wrong = "is a wrong tx hash"
		
		(result, reponse) = rpcApi.getblockhash(height = 1)
		cls.m_block_hash_right = reponse["result"]
		
		cls.m_block_hash_error = "this is a wrong block hash"
		
		cls.m_block_height_right = 1
		
		cls.m_block_height_wrong = 9999
		
		cls.m_block_height_overflow = 99999999
		
		(result, reponse) = sign_transction(Task("tasks/cli/siginvoketx.json"), False)
		cls.m_signed_txhash_right = reponse["result"]["signed_tx"]
		cls.m_signed_txhash_wrong = cls.m_signed_txhash_right + "0f0f0f0f"
		
		
		cls.m_getstorage_contract_addr = cls.m_contractaddr_right
		cls.m_getstorage_contract_addr_wrong = cls.m_contractaddr_right + "0f0f0f0f"
		cls.m_getstorage_contract_key = ByteToHex(b'key1')
		cls.m_getstorage_contract_value = ByteToHex(b'value1')
		invoke_function(cls.m_contractaddr_right, "put", "", "1", argvs = [{"type": "bytearray","value": cls.m_getstorage_contract_key},{"type": "bytearray","value": cls.m_getstorage_contract_value}], node_index = 0)
		
		cls.getsmartcodeevent_height = 5

		cls.getbalance_address_true = Config.NODES[0]["address"]
		cls.getbalance_address_false = "ccccccccccccccc"
		
	def setUp(self):
		time.sleep(1)
			
	def test_01_getblock(self):
		logger.open("rpc/01_getblock.log", "01_getblock")
		(result, response) = rpcApi.getblock(height = None, blockhash = self.m_block_hash_right, verbose = None)
		logger.close(result)

	def test_02_getblock(self):
		logger.open("rpc/02_getblock.log", "02_getblock")
		(result, response) = rpcApi.getblock(height = None, blockhash = self.m_block_hash_error, verbose = None)
		logger.close(not result)
	
	def test_03_getblock(self):
		logger.open("rpc/03_getblock.log", "03_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = None)
		logger.close(result)
	
	def test_04_getblock(self):
		logger.open("rpc/04_getblock.log", "04_getblock")
		(result, response) = rpcApi.getblock(height = 0, blockhash = None, verbose = None)
		logger.close(result)
		
	def test_05_getblock(self):
		logger.open("rpc/05_getblock.log", "05_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_wrong, blockhash = None, verbose = None)
		logger.close(not result)

	def test_06_getblock(self):
		logger.open("rpc/06_getblock.log", "06_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_overflow, blockhash = None, verbose = None)
		logger.close(not result)

	def test_07_getblock(self):
		logger.open("rpc/07_getblock.log", "07_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = 0)
		logger.close(result)

	def test_08_getblock(self):
		logger.open("rpc/08_getblock.log", "08_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = 1)
		logger.close(result)

	def test_09_getblock(self):
		logger.open("rpc/09_getblock.log", "09_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = -1)
		logger.close(result)
	
	def test_10_getblock(self):
		logger.open("rpc/10_getblock.log", "10_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = 2)
		logger.close(result)
	
	def test_11_getblock(self):
		logger.open("rpc/11_getblock.log", "11_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = "abc")
		logger.close(not result)
	
	def test_12_getblock(self):
		logger.open("rpc/12_getblock.log", "12_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = None)
		logger.close(result)

	def test_13_getblockhash(self):
		logger.open("rpc/13_getblockhash.log", "13_getblockhash")
		(result, response) = rpcApi.getblockhash(height = self.m_block_height_right)
		logger.close(result)
	
	def test_14_getblockhash(self):
		logger.open("rpc/14_getblockhash.log", "14_getblockhash")
		(result, response) = rpcApi.getblockhash(height = 0)
		logger.close(result)
	
	def test_15_getblockhash(self):
		logger.open("rpc/15_getblockhash.log", "15_getblockhash")
		(result, response) = rpcApi.getblockhash(height = self.m_block_height_wrong)
		logger.close(not result)

	def test_16_getblockhash(self):
		logger.open("rpc/16_getblockhash.log", "16_getblockhash")
		(result, response) = rpcApi.getblockhash(height = self.m_block_height_overflow)
		logger.close(not result)

	def test_17_getblockhash(self):
		logger.open("rpc/17_getblockhash.log", "17_getblockhash")
		(result, response) = rpcApi.getblockhash(height = "abc")
		logger.close(not result)

	def test_18_getblockhash(self):
		logger.open("rpc/18_getblockhash.log", "18_getblockhash")
		(result, response) = rpcApi.getblockhash(height = -1)
		logger.close(not result)
	
	def test_19_getblockhash(self):
		logger.open("rpc/19_getblockhash.log", "19_getblockhash")
		(result, response) = rpcApi.getblockhash(height = None)
		logger.close(not result)

	def test_20_getbestblockhash(self):
		logger.open("rpc/20_getbestblockhash.log", "20_getbestblockhash")
		(result, response) = rpcApi.getbestblockhash()
		logger.close(result)
	
	def test_22_getblockcount(self):
		logger.open("rpc/22_getblockcount.log", "22_getblockcount")
		(result, response) = rpcApi.getblockcount()
		logger.close(result)

	def test_24_getconnectioncount(self):
		logger.open("rpc/24_getconnectioncount.log", "24_getconnectioncount")
		(result, response) = rpcApi.getconnectioncount()
		logger.close(result and int(response["result"]) == 6)

	# can not test
	def test_25_getconnectioncount(self):
		stop_nodes([1, 2, 3, 4, 5, 6])
		
		logger.open("rpc/25_getconnectioncount.log", "25_getconnectioncount")
		(result, response) = rpcApi.getconnectioncount()
		logger.close(result and int(response["result"]) == 0)
		
		start_nodes([1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, False, False)
		time.sleep(10)
	
	def test_26_getgenerateblocktime(self):
		logger.open("rpc/26_getgenerateblocktime.log", "26_getgenerateblocktime")
		(result, response) = rpcApi.getgenerateblocktime()
		logger.close(result)
	'''
	# can not test
	def test_26_getconnectioncount_1(self):
		logger.open("rpc/27_getconnectioncount.log", "27_getconnectioncount")
		(result, response) = rpcApi.getgenerateblocktime()
		logger.close(not result)
	'''
	
	def test_27_getrawtransaction(self):
		logger.open("rpc/27_getrawtransaction.log", "27_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(self.m_txhash_right)
		logger.close(result)
	
	def test_28_getrawtransaction(self):
		logger.open("rpc/28_getrawtransaction.log", "28_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(self.m_txhash_wrong)
		logger.close(not result)

	def test_29_getrawtransaction(self):
		logger.open("rpc/29_getrawtransaction.log", "29_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction("abc")
		logger.close(not result)

	def test_30_getrawtransaction(self):
		logger.open("rpc/30_getrawtransaction.log", "30_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(1)
		logger.close(not result)
	
	def test_31_getrawtransaction(self):
		logger.open("rpc/31_getrawtransaction.log", "31_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(None)
		logger.close(not result)
	
	def test_32_getrawtransaction(self):
		logger.open("rpc/32_getrawtransaction.log", "32_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(self.m_txhash_right, 1)
		logger.close(result)
	
	def test_33_getrawtransaction(self):
		logger.open("rpc/33_getrawtransaction.log", "33_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(self.m_txhash_right, 0)
		logger.close(result)

	def test_34_getrawtransaction(self):
		logger.open("rpc/34_getrawtransaction.log", "34_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(self.m_txhash_right, -1)
		logger.close(result)

	def test_35_getrawtransaction(self):
		logger.open("rpc/35_getrawtransaction.log", "35_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(self.m_txhash_right, 2)
		logger.close(result)

	def test_36_getrawtransaction(self):
		logger.open("rpc/36_getrawtransaction.log", "36_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(self.m_txhash_right, "abc")
		logger.close(not result)

	def test_37_getrawtransaction(self):
		logger.open("rpc/37_getrawtransaction.log", "37_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(self.m_txhash_right, None)
		logger.close(result)
	
	def test_38_sendrawtransaction(self):
		logger.open("rpc/38_sendrawtransaction.log", "38_sendrawtransaction")
		(result, response) = rpcApi.sendrawtransaction(self.m_signed_txhash_right)
		logger.close(result)
	
	def test_39_sendrawtransaction(self):
		logger.open("rpc/39_sendrawtransaction.log", "39_sendrawtransaction")
		(result, response) = rpcApi.sendrawtransaction("")
		logger.close(not result)
	
	def test_40_sendrawtransaction(self):
		logger.open("rpc/40_sendrawtransaction.log", "40_sendrawtransaction")
		(result, response) = rpcApi.sendrawtransaction(None)
		logger.close(not result)
	
	def test_41_getstorage(self):
		logger.open("rpc/41_getstorage.log", "41_getstorage")
		(result, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, self.m_getstorage_contract_key)
		logger.close(result and response["result"] == self.m_getstorage_contract_value)

	def test_42_getstorage(self):
		logger.open("rpc/42_getstorage.log", "42_getstorage")
		(result, response) = rpcApi.getstorage(self.m_getstorage_contract_addr_wrong, self.m_getstorage_contract_key)
		logger.close(not result)

	def test_43_getstorage(self):
		logger.open("rpc/43_getstorage.log", "43_getstorage")
		(result, response) = rpcApi.getstorage("abc", self.m_getstorage_contract_key)
		logger.close(not result)

	def test_44_getstorage(self):
		logger.open("rpc/44_getstorage.log", "44_getstorage")
		(result, response) = rpcApi.getstorage(1, self.m_getstorage_contract_key)
		logger.close(not result)

	def test_45_getstorage(self):
		logger.open("rpc/45_getstorage.log", "45_getstorage")
		(result, response) = rpcApi.getstorage(None, self.m_getstorage_contract_key)
		logger.close(not result)

	def test_46_getstorage(self):
		logger.open("rpc/46_getstorage.log", "46_getstorage")
		(result, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, self.m_getstorage_contract_key)
		logger.close(result)

	def test_47_getstorage(self):
		logger.open("rpc/47_getstorage.log", "47_getstorage")
		(result, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, "getstorage_key_error")
		logger.close(not result)

	def test_48_getstorage(self):
		logger.open("rpc/48_getstorage.log", "48_getstorage")
		(result, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, "abc")
		logger.close(not result)

	def test_49_getstorage(self):
		logger.open("rpc/49_getstorage.log", "49_getstorage")
		(result, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, 123)
		logger.close(not result)
	
	def test_50_getstorage(self):
		logger.open("rpc/50_getstorage.log", "50_getstorage")
		(result, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, None)
		logger.close(not result)
	

	def test_51_getversion(self):
		logger.open("rpc/51_getversion.log", "51_getversion")
		(result, response) = rpcApi.getversion()
		logger.close(result)

	# can not test
	'''
	def test_52_getversion(self):
		self.clear_nodes();
		logger.open("rpc/52_getversion.log", "52_getversion")
		(result, response) = rpcApi.getversion()
		logger.close(not result)
	
	def test_53_getblocksysfee(self):
		logger.open("rpc/52_getversion.log", "52_getversion")
		(result, response) = rpcApi.getblocksysfee(getblocksysfee_index_true)
		logger.close(result)

	# can not test
	def test_54_getblocksysfee(self):
		logger.open("rpc/54_getblocksysfee.log", "54_getblocksysfee")
		(result, response) = rpcApi.getblocksysfee(getblocksysfee_index_true)
		logger.close(result)

	def test_55_getblocksysfee(self):
		logger.open("rpc/55_getblocksysfee.log", "55_getblocksysfee")
		(result, response) = rpcApi.getblocksysfee(getblocksysfee_index_false)
		logger.close(not result)

	def test_56_getblocksysfee(self):
		logger.open("rpc/56_getblocksysfee.log", "56_getblocksysfee")
		(result, response) = rpcApi.getblocksysfee("abc")
		logger.close(not result)

	def test_57_getblocksysfee(self):
		logger.open("rpc/57_getblocksysfee.log", "57_getblocksysfee")
		(result, response) = rpcApi.getblocksysfee(None)
		logger.close(not result)
	'''
	def test_58_getcontractstate(self):
		logger.open("rpc/58_getcontractstate.log", "58_getcontractstate")
		(result, response) = rpcApi.getcontractstate(self.m_contractaddr_right)
		logger.close(result)

	def test_59_getcontractstate(self):
		logger.open("rpc/59_getcontractstate.log", "59_getcontractstate")
		(result, response) = rpcApi.getcontractstate(self.m_txhash_wrong)
		logger.close(not result)

	def test_60_getcontractstate(self):
		logger.open("rpc/60_getcontractstate.log", "60_getcontractstate")
		(result, response) = rpcApi.getcontractstate("abc")
		logger.close(not result)

	def test_61_getcontractstate(self):
		logger.open("rpc/61_getcontractstate", "61_getcontractstate")
		(result, response) = rpcApi.getcontractstate(123)
		logger.close(not result)

	def test_62_getcontractstate(self):
		logger.open("rpc/62_getcontractstate.log", "62_getcontractstate")
		(result, response) = rpcApi.getcontractstate(None, 1)
		logger.close(not result)

	def test_63_getcontractstate(self):
		logger.open("rpc/63_getcontractstate.log", "63_getcontractstate")
		(result, response) = rpcApi.getcontractstate(self.m_contractaddr_right, 1)
		logger.close(result)

	def test_64_getcontractstate(self):
		logger.open("rpc/64_getcontractstate.log", "64_getcontractstate")
		(result, response) = rpcApi.getcontractstate(self.m_contractaddr_right, -1)
		logger.close(result)

	def test_65_getcontractstate(self):
		logger.open("rpc/65_getcontractstate.log", "65_getcontractstate")
		(result, response) = rpcApi.getcontractstate(self.m_contractaddr_right, 2)
		logger.close(result)

	def test_66_getcontractstate(self):
		logger.open("rpc/66_getcontractstate.log", "66_getcontractstate")
		(result, response) = rpcApi.getcontractstate(self.m_contractaddr_right, "abc")
		logger.close(not result)

	def test_67_getcontractstate(self):
		logger.open("rpc/67_getcontractstate.log", "67_getcontractstate")
		(result, response) = rpcApi.getcontractstate(self.m_contractaddr_right, 0)
		logger.close(result)

	def test_68_getcontractstate(self):
		logger.open("rpc/68_getcontractstate.log", "68_getcontractstate")
		(result, response) = rpcApi.getcontractstate(self.m_contractaddr_right, None)
		logger.close(result)

	def test_69_getmempooltxstate(self):
		logger.open("rpc/69_getmempooltxstate.log", "69_getmempooltxstate")
		(result, response) = invoke_function(self.m_contractaddr_right, "put", "", "1", argvs = [{"type": "bytearray","value": self.m_getstorage_contract_key},{"type": "bytearray","value": self.m_getstorage_contract_value}], node_index = 0, sleep = 0)

		(result, response) = rpcApi.getmempooltxstate(response["txhash"])
		logger.close(result)

	def test_70_getmempooltxstate(self):
		logger.open("rpc/70_getmempooltxstate.log", "70_getmempooltxstate")
		(result, response) = rpcApi.getmempooltxstate(self.m_txhash_right)
		logger.close(not result)

	def test_71_getmempooltxstate(self):
		logger.open("rpc/71_getmempooltxstate.log", "71_getmempooltxstate")
		(result, response) = rpcApi.getmempooltxstate("abc")
		logger.close(not result)

	def test_72_getmempooltxstate(self):
		logger.open("rpc/72_getmempooltxstate.log", "72_getmempooltxstate")
		(result, response) = rpcApi.getmempooltxstate(123)
		logger.close(not result)

	def test_73_getmempooltxstate(self):
		logger.open("rpc/73_getmempooltxstate.log", "73_getmempooltxstate")
		(result, response) = rpcApi.getmempooltxstate(None)
		logger.close(not result)
	
	def test_74_getsmartcodeevent(self):
		logger.open("rpc/74_getsmartcodeevent.log", "74_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent(height = self.getsmartcodeevent_height)
		logger.close(result)

	def test_75_getsmartcodeevent(self):
		logger.open("rpc/75_getsmartcodeevent.log", "75_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent(height = 99999999)
		logger.close(not result)

	def test_76_getsmartcodeevent(self):
		logger.open("rpc/76_getsmartcodeevent.log", "76_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent(height="abc")
		logger.close(not result)

	def test_77_getsmartcodeevent(self):
		logger.open("rpc/77_getsmartcodeevent.log", "77_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent(height =None)
		logger.close(not result)
	
	def test_78_getsmartcodeevent(self):
		logger.open("rpc/78_getsmartcodeevent.log", "78_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent(tx_hash = self.m_txhash_right)
		logger.close(result)

	def test_79_getsmartcodeevent(self):
		logger.open("rpc/79_getsmartcodeevent.log", "79_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent(tx_hash = self.m_txhash_wrong)
		logger.close(not result)
	
	def test_80_getblockheightbytxhash(self):
		logger.open("rpc/80_getblockheightbytxhash.log", "80_getblockheightbytxhash")
		(result, response) = rpcApi.getblockheightbytxhash(tx_hash = self.m_txhash_right)
		logger.close(result)

	def test_81_getblockheightbytxhash(self):
		logger.open("rpc/81_getblockheightbytxhash.log", "81_getblockheightbytxhash")
		(result, response) = rpcApi.getblockheightbytxhash(tx_hash = self.m_txhash_wrong)
		logger.close(not result)

	def test_82_getblockheightbytxhash(self):
		logger.open("rpc/82_getblockheightbytxhash.log", "82_getblockheightbytxhash")
		(result, response) = rpcApi.getblockheightbytxhash(tx_hash = "abc")
		logger.close(not result)

	def test_83_getblockheightbytxhash(self):
		logger.open("rpc/83_getblockheightbytxhash.log", "83_getblockheightbytxhash")
		(result, response) = rpcApi.getblockheightbytxhash(tx_hash = 123)
		logger.close(not result)
	
	def test_84_getblockheightbytxhash(self):
		logger.open("rpc/84_getblockheightbytxhash.log", "84_getblockheightbytxhash")
		(result, response) = rpcApi.getblockheightbytxhash(tx_hash = None)
		logger.close(not result)

	def test_85_getbalance(self):
		logger.open("rpc/85_getbalance.log", "85_getbalance")
		(result, response) = rpcApi.getbalance(self.getbalance_address_true)
		logger.close(result)
	
	def test_86_getbalance(self):
		logger.open("rpc/86_getbalance.log", "86_getbalance")
		(result, response) = rpcApi.getbalance(self.getbalance_address_false)
		logger.close(not result)
	
	def test_87_getbalance(self):
		logger.open("rpc/85_getbalance.log", "85_getbalance")
		(result, response) = rpcApi.getbalance("abc")
		logger.close(not result)

	def test_88_getbalance(self):
		logger.open("rpc/85_getbalance.log", "85_getbalance")
		(result, response) = rpcApi.getbalance(None)
		logger.close(not result)
	
	def test_89_getmerkleproof(self):
		logger.open("rpc/89_getmerkleproof.log", "89_getmerkleproof")
		(result, response) = rpcApi.getmerkleproof(self.m_txhash_right)
		logger.close(result)

	def test_90_getmerkleproof(self):
		logger.open("rpc/90_getmerkleproof.log", "90_getmerkleproof")
		(result, response) = rpcApi.getmerkleproof(self.m_txhash_wrong)
		logger.close(not result)

	def test_91_getmerkleproof(self):
		logger.open("rpc/91_getmerkleproof.log", "91_getmerkleproof")
		(result, response) = rpcApi.getmerkleproof("abc")
		logger.close(not result)

	def test_92_getmerkleproof(self):
		logger.open("rpc/92_getmerkleproof.log", "92_getmerkleproof")
		(result, response) = rpcApi.getmerkleproof("123")
		logger.close(not result)
	
	def test_93_getmerkleproof(self):
		logger.open("rpc/93_getmerkleproof.log", "93_getmerkleproof")
		(result, response) = rpcApi.getmerkleproof(None)
		logger.close(not result)

	def test_94_getmerkleproof(self):
		logger.open("rpc/94_getmerkleproof.log", "94_getmerkleproof")
		task = Task("tasks/rpc/94_getmerkleproof.json")
		task.request()["params"] = [self.m_txhash_right]
		(result, response) =  run_single_task(task)
		logger.close(result)

	def test_95_getmerkleproof(self):
		logger.open("rpc/95_getmerkleproof.log", "95_getmerkleproof")
		task = Task("tasks/rpc/95_getmerkleproof.json")
		task.request()["params"] = [self.m_txhash_right]
		(result, response) =  run_single_task(task)
		logger.close(result)

	# can not test
	def test_96_getmerkleproof(self):
		logger.open("rpc/96_getmerkleproof.log", "96_getmerkleproof")
		task = Task("tasks/rpc/96_getmerkleproof.json")
		(result, response) =  run_single_task(task)
		logger.close(not result)
	
	def test_97_getmerkleproof(self):
		logger.open("rpc/97_getmerkleproof.log", "97_getmerkleproof")
		task = Task("tasks/rpc/97_getmerkleproof.1.json")
		(result, response) =  run_single_task(task)
		logger.close(not result)	

if __name__ == '__main__':
    unittest.main()