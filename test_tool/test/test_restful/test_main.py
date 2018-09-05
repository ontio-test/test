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
from test_restful.test_config import test_config


####################################################
#test cases
class test_restful_1(ParametrizedTestCase):

	def setUp(self):
		logger.open( "test_restful/" + self._testMethodName+".log",self._testMethodName)
		if self._testMethodName == "test_init":
			return
		
	def tearDown(self):
		logger.close(self.result())
	'''		
	def test_base_001_getgenerateblocktime(self):
		try:
			API.node().stop_all_nodes()
			API.node().start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True, config="config-dbft-1.json")
			time.sleep(10)
		
			(process, response) = API.restful().getgenerateblocktime()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	'''
		
class test_restful_2(ParametrizedTestCase):
	def setUp(self):
		logger.open("test_restful/" + self._testMethodName+".log",self._testMethodName)
		if self._testMethodName == "test_init":
			return

		API.node().stop_all_nodes()
		API.node().start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(10)
		
	def tearDown(self):
		logger.close(self.result())

	def test_normal_006_getblocktxsbyheight(self,height=0):
		try:
			(process, response) = API.restful().getblocktxsbyheight(height)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
		
	# 无区块
	def test_normal_014_getblockbyheight(self,height=0):
		try:
			(process, response) = API.restful().getblockbyheight(height)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	# 无区块
	def test_normal_023_getblockheight(self):
		try:
			(process, response) = API.restful().getblockheight()	
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	# 无区块
	def test_normal_025_getblockhashbyheight(self,height=0):
		try:
			(process, response) = API.restful().getblockhashbyheight(height)	
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
		
	# 无区块
	def test_abnormal_053_getcontract(self):
		try:
			# (contractaddr_right, txhash_right) = API.contract().deploy_contract_full(testpath+"/resource/A.neo", "name", "desc", 0)
			# time.sleep(10)
			script_hash = "8eeae0cd102461abc82a3fe5df58fa8c31121e0f"
			(process, response) = API.restful().getcontract(script_hash) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
		
class test_restful_3(ParametrizedTestCase):
	def test_init(self):
		API.node().stop_all_nodes()
		API.node().start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(10)
		while True:
			if API.rpc().getblockcount()[1]["result"] > 0:
				break
			time.sleep(1)

		(test_config.m_contractaddr_right, test_config.m_txhash_right) = API.contract().deploy_contract_full(testpath+"/resource/A.neo", "name", "desc", 0)
		time.sleep(5)
		(result, reponse) = API.rpc().getblockhash(height = 1)
		test_config.m_block_hash_right = reponse["result"]

		(result, reponse) = API.contract().sign_transction(Task(testpath+"/resource/cli/siginvoketx.json"), False)
		test_config.m_signed_txhash_right = reponse["result"]["signed_tx"]
		test_config.m_signed_txhash_wrong = "0f0f0f0f" + test_config.m_signed_txhash_right 

		API.contract().invoke_function(test_config.m_contractaddr_right, "put", "", "1", argvs = [{"type": "bytearray","value": test_config.m_getstorage_contract_key},{"type": "bytearray","value": test_config.m_getstorage_contract_value}], node_index = 0)
		
	def setUp(self):
		logger.open("test_restful/" + self._testMethodName+".log",self._testMethodName)
		if self._testMethodName == "test_init":
			return
		time.sleep(1)
		
	def tearDown(self):
		logger.close(self.result())
	'''	
	def test_normal_002_getgenerateblocktime(self):
		try:
			(process, response) = API.restful().getgenerateblocktime()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	'''	
	def test_base_003_getconnectioncount(self):
		try:
			(process, response) = API.restful().getconnectioncount()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_base_005_getblocktxsbyheight(self,height=1):
		try:
			(process, response) = API.restful().getblocktxsbyheight(height)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_007_getblocktxsbyheight(self,height=6000):
		try:
			(process, response) = API.restful().getblocktxsbyheight(height)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_008_getblocktxsbyheight(self,height=65537):
		try:
			(process, response) = API.restful().getblocktxsbyheight(height)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_abnormal_009_getblocktxsbyheight(self,height="abc"):
		try:
			(process, response) = API.restful().getblocktxsbyheight(height)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_010_getblocktxsbyheight(self,height=-1):
		try:
			(process, response) = API.restful().getblocktxsbyheight(height)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_011_getblocktxsbyheight(self,height=""):
		try:
			(process, response) = API.restful().getblocktxsbyheight(height)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_012_getblockbyheight(self,height=1):
		try:
			(process, response) = API.restful().getblockbyheight(height)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_013_getblockbyheight(self,height=0):
		try:
			(process, response) = API.restful().getblockbyheight(height)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_015_getblockbyheight(self,height=6000):
		try:
			(process, response) = API.restful().getblockbyheight(height)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_016_getblockbyheight(self,height=65536):
		try:
			(process, response) = API.restful().getblockbyheight(height)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_017_getblockbyheight(self,height="abc"):
		try:
			(process, response) = API.restful().getblockbyheight(height)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_018_getblockbyheight(self,height=-1):
		try:
			(process, response) = API.restful().getblockbyheight(height)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_019_getblockbyheight(self,height=""):
		try:
			(process, response) = API.restful().getblockbyheight(height)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_020_getblockbyhash(self):	
		try:
			(process, response) = API.restful().getblockbyhash(test_config.m_block_hash_right, 1)	
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_021_getblockbyhash(self):	
		try:
			(process, response) = API.restful().getblockbyhash(test_config.m_block_hash_error, 1)  
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_022_getblockheight(self):	
		try:
			(process, response) = API.restful().getblockheight()	
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_024_getblockhashbyheight(self,height=1):
		try:
			(process, response) = API.restful().getblockhashbyheight(height)	
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_026_getblockhashbyheight(self,height=6000):
		try:
			(process, response) = API.restful().getblockhashbyheight(height)
			rs = (response["Result"] == "" or response["Result"] == None)
			self.ASSERT(not process and rs, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_027_getblockhashbyheight(self,height=65536):
		try:
			(process, response) = API.restful().getblockhashbyheight(height)
			rs = (response["Result"] == "" or response["Result"] == None)			
			self.ASSERT(not process and rs, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_028_getblockhashbyheight(self,height="abc"):
		try:
			(process, response) = API.restful().getblockhashbyheight(height)	
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_029_getblockhashbyheight(self,height=-1):
		try:
			(process, response) = API.restful().getblockhashbyheight(height) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_030_getblockhashbyheight(self,height=""):
		try:
			(process, response) = API.restful().getblockhashbyheight(height)   
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_031_gettransactionbytxhash(self):
		try:
			(process, response) = API.restful().gettransactionbytxhash(test_config.m_txhash_right) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_abnormal_032_gettransactionbytxhash(self):
		try:
			(process, response) = API.restful().gettransactionbytxhash(test_config.m_txhash_wrong) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])	

	def test_base_033_postrawtx(self):
		
		try:
			(result, reponse) = API.contract().sign_transction(Task(testpath+"/resource/cli/siginvoketx.json"), False)
			rawtxdata=reponse["result"]["signed_tx"]
			action = "sendrawtransaction"
			version = "1.0.0"
			(process, response) = API.restful().postrawtx(rawtxdata,action,version) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_034_postrawtx(self):
		try:
			(result, reponse) = API.contract().sign_transction(Task(testpath+"/resource/cli/siginvoketx.json"), False)
			rawtxdata=reponse["result"]["signed_tx"]
			action = "sendrawtransaction_wrong"
			version = "1.0.0"
		
			(process, response) = API.restful().postrawtx(rawtxdata,action,version) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_035_postrawtx(self):
		try:
			(result, reponse) = API.contract().sign_transction(Task(testpath+"/resource/cli/siginvoketx.json"), False)
			rawtxdata=reponse["result"]["signed_tx"]
			action = ""
			version = "1.0.0"
		
			(process, response) = API.restful().postrawtx(rawtxdata,action,version) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_036_postrawtx(self):
		try:
			(result, reponse) = API.contract().sign_transction(Task(testpath+"/resource/cli/siginvoketx.json"), False)
			rawtxdata=reponse["result"]["signed_tx"]
			action = "sendrawtransaction"
			version = "1.0.0"
	
			(process, response) = API.restful().postrawtx(rawtxdata,action,version) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_037_postrawtx(self):
		try:
			(result, reponse) = API.contract().sign_transction(Task(testpath+"/resource/cli/siginvoketx.json"), False)
			rawtxdata=reponse["result"]["signed_tx"]
			action = "sendrawtransaction"
			version = "2.0.8"
		
			(process, response) = API.restful().postrawtx(rawtxdata,action,version) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_038_postrawtx(self):
		try:
			(result, reponse) = API.contract().sign_transction(Task(testpath+"/resource/cli/siginvoketx.json"), False)
			rawtxdata=reponse["result"]["signed_tx"]
			action = "sendrawtransaction"
			version = ""
		
			(process, response) = API.restful().postrawtx(rawtxdata,action,version) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_039_postrawtx(self):
		try:
			(result, reponse) = API.contract().sign_transction(Task(testpath+"/resource/cli/siginvoketx.json"), False)
			rawtxdata=reponse["result"]["signed_tx"]
			action = "sendrawtransaction"
			version = "1.0.0"
	
			(process, response) = API.restful().postrawtx(rawtxdata,action,version) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_040_postrawtx(self):
		try:
			rawtxdata=test_config.m_signed_txhash_wrong
			action = "sendrawtransaction"
			version = "1.0.0"
		
			(process, response) = API.restful().postrawtx(rawtxdata,action,version) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_041_postrawtx(self):
		try:
			rawtxdata=""
			action = "sendrawtransaction"
			version = "1.0.0"
			
			(process, response) = API.restful().postrawtx(rawtxdata,action,version) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_042_getstorage(self):
		try:
			script_hash=test_config.m_getstorage_contract_addr
			key=test_config.m_getstorage_contract_key
			
			(process, response) = API.restful().getstorage(script_hash, key) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_043_getstorage(self):
		try:
			script_hash=test_config.m_getstorage_contract_addr_wrong
			key=test_config.m_getstorage_contract_key
			
			(process, response) = API.restful().getstorage(script_hash, key)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_044_getstorage(self):
		try:
			script_hash=""
			key=test_config.m_getstorage_contract_key
		
			(process, response) = API.restful().getstorage(script_hash, key) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_045_getstorage(self):
		try:
			script_hash=test_config.m_getstorage_contract_addr
			key=test_config.m_getstorage_contract_key
		
			(process, response) = API.restful().getstorage(script_hash, key) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_046_getstorage(self):
		try:
			script_hash=test_config.m_getstorage_contract_addr
			key=test_config.m_getstorage_contract_key + "1111"
		
			(process, response) = API.restful().getstorage(script_hash, key) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_047_getstorage(self):
		try:
			script_hash=test_config.m_getstorage_contract_addr
			key=""
		
			(process, response) = API.restful().getstorage(script_hash, key) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_normal_048_getstorage(self):
		try:
			script_hash=test_config.m_getstorage_contract_addr
			key=test_config.m_getstorage_contract_key + "1111"
		
			(process, response) = API.restful().getstorage(script_hash, key) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_base_049_getbalance(self):
		try:
			attr=test_config.getbalance_address_true
		
			(process, response) = API.restful().getbalance(attr) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_050_getbalance(self):
		try:
			attr=test_config.getbalance_address_false
		
			(process, response) = API.restful().getbalance(attr) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_051_getbalance(self,attr=""):
		try:
			(process, response) = API.restful().getbalance(attr) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_052_getcontract(self):
		try:
			script_hash=test_config.m_contractaddr_right
			
			(process, response) = API.restful().getcontract(script_hash) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_abnormal_054_getcontract(self):
		try:
			script_hash=test_config.m_contractaddr_wrong
		
			(process, response) = API.restful().getcontract(script_hash) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_055_getsmartcodeeventbyheight(self,height=1):
		try:
			(process, response) = API.restful().getsmartcodeeventbyheight(height) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_056_getsmartcodeeventbyheight(self,height=999):
		try:
			(process, response) = API.restful().getsmartcodeeventbyheight(height) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_057_getsmartcodeeventbyheight(self,height="abc"):
		try:
			(process, response) = API.restful().getsmartcodeeventbyheight(height) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_058_getsmartcodeeventbyheight(self,height=""):
		try:
			(process, response) = API.restful().getsmartcodeeventbyheight(height) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_059_getsmartcodeeventbyhash(self):
		try:
			hash=test_config.m_txhash_right
		
			(process, response) = API.restful().getsmartcodeeventbyhash(hash) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_060_getsmartcodeeventbyhash(self):
		try:
			hash=test_config.m_txhash_wrong
	
			(process, response) = API.restful().getsmartcodeeventbyhash(hash) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_061_getsmartcodeeventbyhash(self):
		try:
			hash=test_config.m_txhash_right
	
			(process, response) = API.restful().getsmartcodeeventbyhash(hash) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_062_getsmartcodeeventbyhash(self):
		try:
			hash=test_config.m_txhash_wrong
	
			(process, response) = API.restful().getsmartcodeeventbyhash(hash) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_063_getsmartcodeeventbyhash(self,hash="abc"):
		try:
			(process, response) = API.restful().getsmartcodeeventbyhash(hash) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_abnormal_064_getsmartcodeeventbyhash(self,hash=123):
		try:
			(process, response) = API.restful().getsmartcodeeventbyhash(hash) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_abnormal_065_getsmartcodeeventbyhash(self,hash=""):
		try:
			(process, response) = API.restful().getsmartcodeeventbyhash(hash) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_base_066_getblockheightbytxhash(self):
		try:
			hash=test_config.m_txhash_right
	
			(process, response) = API.restful().getblockheightbytxhash(hash)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_abnormal_067_getblockheightbytxhash(self):
		try:
			hash=test_config.m_txhash_wrong
	
			(process, response) = API.restful().getblockheightbytxhash(hash)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_abnormal_068_getblockheightbytxhash(self,hash=""):
		try:
			(process, response) = API.restful().getblockheightbytxhash(hash)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_abnormal_069_getblockheightbytxhash(self,hash=123):
		try:
			(process, response) = API.restful().getblockheightbytxhash(hash)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_070_getmerkleproofbytxhash(self):
		try:
			hash=test_config.m_txhash_right
	
			(process, response) = API.restful().getmerkleproofbytxhash(hash) 
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_071_getmerkleproofbytxhash(self):
		try:
			hash=test_config.m_txhash_wrong
		
			(process, response) = API.restful().getmerkleproofbytxhash(hash) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_072_getmerkleproofbytxhash(self,hash=""):
		try:
			(process, response) = API.restful().getmerkleproofbytxhash(hash) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_073_getmerkleproofbytxhash(self,hash=123):
		try:
			(process, response) = API.restful().getmerkleproofbytxhash(hash) 
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_074_getConnCount1(self):
		try:
			request = {
					"TYPE" : "restful",
					"REQUEST": {
					"api": "/api/v1/get_conn_count1"
					},
					"RESPONSE": {
						"Error": 0,
					}
			}
			task = Task(name = "74_get_conn_count1", ijson = request)
			(process, response) = TaskRunner.run_single_task(task)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_075_noUrl(self):
		try:
			request = {
				"TYPE" : "restful",
				"REQUEST": {
				  "api": ""
				},
				"RESPONSE": {
					"Error": 0,
				}
			}
			task = Task(name = "75_no_url", ijson = request)
			(process, response) = TaskRunner.run_single_task(task)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
		
####################################################
if __name__ == '__main__':
	unittest.main()  
