# -*- coding:utf-8 -*-
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.commonapi import *
from utils.restfulapi import *
from utils.rpcapi import *
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.contractapi import invoke_function

####################################################
#test cases
class Test_01(ParametrizedTestCase):
	def test_01_get_gen_blk_time(self):
		stop_all_nodes()
		start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True, config="config-dbft-1.json")
		time.sleep(10)
		
		logger.open("restful/01_get_gen_blk_time.log", "01_get_gen_blk_time")
		(result, response) = RestfulApi().getgenerateblocktime()
		logger.close(result)

		
class Test_no_block(ParametrizedTestCase):
	def setUp(self):
		stop_all_nodes()
		start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(5)

	def test_06_get_blk_txs_by_height(self,height=0):
		logger.open("restful/06_get_blk_txs_by_height.log", "06_get_blk_txs_by_height")
		(result, response) = RestfulApi().getblocktxsbyheight(height)
		logger.close(result)
		
	# 无区块
	def test_14_get_blk_by_height(self,height=0):
		logger.open("restful/14_get_blk_by_height.log", "14_get_blk_by_height")
		(result, response) = RestfulApi().getblockbyheight(height)
		logger.close(result)

	# 无区块
	def test_23_get_blk_height(self):
		logger.open("restful/23_get_blk_height.log", "23_get_blk_height")
		(result, response) = RestfulApi().getblockheight()	
		logger.close(result)

	# 无区块
	def test_25_get_blk_hash(self,height=0):
		logger.open("restful/25_get_blk_hash.log", "25_get_blk_hash")
		(result, response) = RestfulApi().getblockhashbyheight(height)	
		logger.close(result)
		
	# 无区块
	def test_53_get_contract_state(self):
		(contractaddr_right, txhash_right) = deploy_contract_full("tasks/A.neo", "name", "desc", 0)

		script_hash=contractaddr_right
		logger.open("restful/53_get_contract_state.log", "53_get_contract_state")
		(result, response) = RestfulApi().getcontract(script_hash) 
		logger.close(not result)
		
class Test(ParametrizedTestCase):
	@classmethod
	def setUpClass(cls):
		#for node_index in range(len(Config.NODES)):
		#	stop_nodes([node_index])
		#start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True)
		#time.sleep(60)

		(cls.m_contractaddr_right, cls.m_txhash_right) = deploy_contract_full("tasks/A.neo", "name", "desc", 0)
		cls.m_txhash_wrong = "this is a wrong tx hash"
		cls.m_contractaddr_wrong = "this is a wrong address"
		(result, reponse) = RPCApi().getblockhash(height = 1)
		cls.m_block_hash_right = reponse["result"]
		
		cls.m_block_hash_error = "this is a wrong block hash"
		
		cls.m_block_height_right = 1
		
		cls.m_block_height_wrong = 9999
		
		cls.m_block_height_overflow = 99999999
		
		(result, reponse) = sign_transction(Task("tasks/cli/siginvoketx.json"), False)
		cls.m_signed_txhash_right = reponse["result"]["signed_tx"]
		cls.m_signed_txhash_wrong = "0f0f0f0f" + cls.m_signed_txhash_right 
		
		cls.m_getstorage_contract_addr = "03febccf81ac85e3d795bc5cbd4e84e907812aa3"
		cls.m_getstorage_contract_addr_wrong = "5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c"
		cls.m_getstorage_contract_key = ByteToHex(b'key1')
		cls.m_getstorage_contract_value = ByteToHex(b'value1')
		invoke_function(cls.m_contractaddr_right, "put", "", "1", argvs = [{"type": "bytearray","value": cls.m_getstorage_contract_key},{"type": "bytearray","value": cls.m_getstorage_contract_value}], node_index = 0)
		
		cls.getsmartcodeevent_height = 5

		cls.getbalance_address_true = Config.NODES[0]["address"]
		cls.getbalance_address_false = "ccccccccccccccc"
		pass
		
	def setUp(self):
		time.sleep(1)
		pass
		
	def test_02_get_gen_blk_time(self):
		logger.open("restful/02_get_gen_blk_time.log", "02_get_gen_blk_time")
		(result, response) = RestfulApi().getgenerateblocktime()
		logger.close(result)
		
	def test_03_get_conn_count(self):
		logger.open("restful/03_get_conn_count.log", "03_get_conn_count")
		(result, response) = RestfulApi().getconnectioncount()
		logger.close(result)

	# 无节点
	def test_04_get_conn_count(self):
		stop_nodes([1, 2, 3, 4, 5, 6])
		logger.open("restful/04_get_conn_count.log", "04_get_conn_count")
		(result, response) = RestfulApi().getconnectioncount()
		logger.close(result and int(response["result"]) == 0)
		start_nodes([1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(10)
		
	def test_05_get_blk_txs_by_height(self,height=1):
		logger.open("restful/05_get_blk_txs_by_height.log", "05_get_blk_txs_by_height")
		(result, response) = RestfulApi().getblocktxsbyheight(height)
		logger.close(result)
	
	def test_07_get_blk_txs_by_height(self,height=6000):
		logger.open("restful/07_get_blk_txs_by_height.log", "07_get_blk_txs_by_height")
		(result, response) = RestfulApi().getblocktxsbyheight(height)
		logger.close(not result)

	def test_08_get_blk_txs_by_height(self,height=65537):
		logger.open("restful/08_get_blk_txs_by_height.log", "08_get_blk_txs_by_height")
		(result, response) = RestfulApi().getblocktxsbyheight(height)
		logger.close(not result)
		
	def test_09_get_blk_txs_by_height(self,height="abc"):
		logger.open("restful/09_get_blk_txs_by_height.log", "09_get_blk_txs_by_height")
		(result, response) = RestfulApi().getblocktxsbyheight(height)
		logger.close(not result)

	def test_10_get_blk_txs_by_height(self,height=-1):
		logger.open("restful/10_get_blk_txs_by_height.log", "10_get_blk_txs_by_height")
		(result, response) = RestfulApi().getblocktxsbyheight(height)
		logger.close(not result)

	def test_11_get_blk_txs_by_height(self,height=""):
		logger.open("restful/11_get_blk_txs_by_height.log", "11_get_blk_txs_by_height")
		(result, response) = RestfulApi().getblocktxsbyheight(height)
		logger.close(not result)

	def test_12_get_blk_by_height(self,height=1):
		logger.open("restful/12_get_blk_by_height.log", "12_get_blk_by_height")
		(result, response) = RestfulApi().getblockbyheight(height)
		logger.close(result)

	def test_13_get_blk_by_height(self,height=0):
		logger.open("restful/13_get_blk_by_height.log", "13_get_blk_by_height")
		(result, response) = RestfulApi().getblockbyheight(height)
		logger.close(result)
	
	def test_15_get_blk_by_height(self,height=6000):
		logger.open("restful/15_get_blk_by_height.log", "15_get_blk_by_height")
		(result, response) = RestfulApi().getblockbyheight(height)
		logger.close(not result)

	def test_16_get_blk_by_height(self,height=65536):
		logger.open("restful/16_get_blk_by_height.log", "16_get_blk_by_height")
		(result, response) = RestfulApi().getblockbyheight(height)
		logger.close(not result)

	def test_17_get_blk_by_height(self,height="abc"):
		logger.open("restful/17_get_blk_by_height.log", "17_get_blk_by_height")
		(result, response) = RestfulApi().getblockbyheight(height)
		logger.close(not result)

	def test_18_get_blk_by_height(self,height=-1):
		logger.open("restful/18_get_blk_by_height.log", "18_get_blk_by_height")
		(result, response) = RestfulApi().getblockbyheight(height)
		logger.close(not result)

	def test_19_get_blk_by_height(self,height=""):
		logger.open("restful/19_get_blk_by_height.log", "19_get_blk_by_height")
		(result, response) = RestfulApi().getblockbyheight(height)
		logger.close(not result)

	def test_20_get_blk_by_hash(self):	
		logger.open("restful/20_get_blk_by_hash.log", "20_get_blk_by_hash")
		(result, response) = RestfulApi().getblockbyhash(self.m_block_hash_right, 1)	
		logger.close(result)

	def test_21_get_blk_by_hash(self):	
		logger.open("restful/21_get_blk_by_hash.log", "21_get_blk_by_hash")
		(result, response) = RestfulApi().getblockbyhash(self.m_block_hash_error, 1)  
		logger.close(not result)

	def test_22_get_blk_height(self):	
		logger.open("restful/22_get_blk_height.log", "22_get_blk_height")
		(result, response) = RestfulApi().getblockheight()	
		logger.close(result)

	def test_24_get_blk_hash(self,height=1):
		logger.open("restful/24_get_blk_hash.log", "24_get_blk_hash")
		(result, response) = RestfulApi().getblockhashbyheight(height)	
		logger.close(result)

	def test_26_get_blk_hash(self,height=6000):
		logger.open("restful/26_get_blk_hash.log", "26_get_blk_hash")
		(result, response) = RestfulApi().getblockhashbyheight(height)	
		logger.close(result and (response["Result"] == "" or response["Result"] == None))

	def test_27_get_blk_hash(self,height=65536):
		logger.open("restful/27_get_blk_hash.log", "27_get_blk_hash")
		(result, response) = RestfulApi().getblockhashbyheight(height)	
		logger.close(result and (response["Result"] == "" or response["Result"] == None))

	def test_28_get_blk_hash(self,height="abc"):
		logger.open("restful/28_get_blk_hash.log", "28_get_blk_hash")
		(result, response) = RestfulApi().getblockhashbyheight(height)	
		logger.close(not result)

	def test_29_get_blk_hash(self,height=-1):
		logger.open("restful/29_get_blk_hash.log", "29_get_blk_hash")
		(result, response) = RestfulApi().getblockhashbyheight(height) 
		logger.close(not result)

	def test_30_get_blk_hash(self,height=""):
		logger.open("restful/30_get_blk_hash.log", "30_get_blk_hash")
		(result, response) = RestfulApi().getblockhashbyheight(height)   
		logger.close(not result)

	def test_31_get_tx(self):
		logger.open("restful/31_get_tx.log", "31_get_tx")
		(result, response) = RestfulApi().gettransactionbytxhash(self.m_txhash_right) 
		logger.close(result)
		
	def test_32_get_tx(self):
		logger.open("restful/32_get_tx.log", "32_get_tx")
		(result, response) = RestfulApi().gettransactionbytxhash(self.m_txhash_wrong) 
		logger.close(not result)	

	def test_33_post_raw_tx(self):
		rawtxdata=self.m_signed_txhash_right
		action = "sendrawtransaction"
		version = "1.0.0"
		
		logger.open("restful/33_post_raw_tx.log", "33_post_raw_tx")
		(result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
		logger.close(result)

	def test_34_post_raw_tx(self):
		rawtxdata=self.m_signed_txhash_right
		action = "sendrawtransaction_wrong"
		version = "1.0.0"
		
		logger.open("restful/34_post_raw_tx.log", "34_post_raw_tx")
		(result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
		logger.close(result)

	def test_35_post_raw_tx(self):
		rawtxdata=self.m_signed_txhash_right
		action = ""
		version = "1.0.0"
		
		logger.open("restful/35_post_raw_tx.log", "35_post_raw_tx")
		(result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
		logger.close(result)

	def test_36_post_raw_tx(self):
		rawtxdata=self.m_signed_txhash_right
		action = "sendrawtransaction"
		version = "1.0.0"
	
		logger.open("restful/36_post_raw_tx.log", "36_post_raw_tx")
		(result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
		logger.close(result)

	def test_37_post_raw_tx(self):
		rawtxdata=self.m_signed_txhash_right
		action = "sendrawtransaction"
		version = "2.0.8"
		
		logger.open("restful/37_post_raw_tx.log", "37_post_raw_tx")
		(result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
		logger.close(result)   

	def test_38_post_raw_tx(self):
		rawtxdata=self.m_signed_txhash_right
		action = "sendrawtransaction"
		version = ""
		
		logger.open("restful/38_post_raw_tx.log", "38_post_raw_tx")
		(result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
		logger.close(result)

	def test_39_post_raw_tx(self):
		rawtxdata=self.m_signed_txhash_right
		action = "sendrawtransaction"
		version = "1.0.0"
	
		logger.open("restful/39_post_raw_tx.log", "39_post_raw_tx")
		(result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
		logger.close(result)

	def test_40_post_raw_tx(self):
		rawtxdata=self.m_signed_txhash_wrong
		action = "sendrawtransaction"
		version = "1.0.0"
		
		logger.open("restful/40_post_raw_tx.log", "40_post_raw_tx")
		(result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
		logger.close(not result)

	def test_41_post_raw_tx(self):
		rawtxdata=""
		action = "sendrawtransaction"
		version = "1.0.0"
		
		logger.open("restful/41_post_raw_tx.log", "41_post_raw_tx")
		(result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
		logger.close(not result)

	def test_42_get_storage(self):
		script_hash=self.m_getstorage_contract_addr
		key=self.m_getstorage_contract_key
		
		logger.open("restful/42_get_storage.log", "42_get_storage")
		(result, response) = RestfulApi().getstorage(script_hash, key) 
		logger.close(result)

	def test_43_get_storage(self):
		script_hash=self.m_getstorage_contract_addr_wrong
		key=self.m_getstorage_contract_key
		
		logger.open("restful/43_get_storage.log", "43_get_storage")
		(result, response) = RestfulApi().getstorage(script_hash, key) 
		logger.close(result)

	def test_44_get_storage(self):
		script_hash=""
		key=self.m_getstorage_contract_key
	
		logger.open("restful/44_get_storage.log", "44_get_storage")
		(result, response) = RestfulApi().getstorage(script_hash, key) 
		logger.close(not result)

	def test_45_get_storage(self):
		script_hash=self.m_getstorage_contract_addr
		key=self.m_getstorage_contract_key
	
		logger.open("restful/45_get_storage.log", "45_get_storage")
		(result, response) = RestfulApi().getstorage(script_hash, key) 
		logger.close(result)

	def test_46_get_storage(self):
		script_hash=self.m_getstorage_contract_addr
		key=self.m_getstorage_contract_key + "1111"
	
		logger.open("restful/46_get_storage.log", "46_get_storage")
		(result, response) = RestfulApi().getstorage(script_hash, key) 
		logger.close(result)

	def test_47_get_storage(self):
		script_hash=self.m_getstorage_contract_addr
		key=""
	
		logger.open("restful/47_get_storage.log", "47_get_storage")
		(result, response) = RestfulApi().getstorage(script_hash, key) 
		logger.close( result)
		
	def test_48_get_storage(self):
		script_hash=self.m_getstorage_contract_addr
		key=self.m_getstorage_contract_key + "1111"
	
		logger.open("restful/48_get_storage.log", "48_get_storage")
		(result, response) = RestfulApi().getstorage(script_hash, key) 
		logger.close(result)
		
	def test_49_get_balance(self):
		attr=self.getbalance_address_true
	
		logger.open("restful/49_get_balance.log", "49_get_balance")
		(result, response) = RestfulApi().getbalance(attr) 
		logger.close(result)

	def test_50_get_balance(self):
		attr=self.getbalance_address_false
	
		logger.open("restful/50_get_balance.log", "50_get_balance")
		(result, response) = RestfulApi().getbalance(attr) 
		logger.close(not result)

	def test_51_get_balance(self,attr=""):
		logger.open("restful/51_get_balance.log", "51_get_balance")
		(result, response) = RestfulApi().getbalance(attr) 
		logger.close(not result)	

	def test_52_get_contract_state(self):
		script_hash=self.m_contractaddr_right
		
		logger.open("restful/52_get_contract_state.log", "52_get_contract_state")
		(result, response) = RestfulApi().getcontract(script_hash) 
		logger.close(result)
		
	def test_54_get_contract_state(self):
		script_hash=self.m_contractaddr_wrong
	
		logger.open("restful/54_get_contract_state.log", "54_get_contract_state")
		(result, response) = RestfulApi().getcontract(script_hash) 
		logger.close(not result)

	def test_55_get_smtcode_evt_txs(self,height=1):
		logger.open("restful/55_get_smtcode_evt_txs.log", "55_get_smtcode_evt_txs")
		(result, response) = RestfulApi().getsmartcodeeventbyheight(height) 
		logger.close(result)

	def test_56_get_smtcode_evt_txs(self,height=999):
		logger.open("restful/56_get_smtcode_evt_txs.log", "56_get_smtcode_evt_txs")
		(result, response) = RestfulApi().getsmartcodeeventbyheight(height) 
		logger.close(result)

	def test_57_get_smtcode_evt_txs(self,height="abc"):
		logger.open("restful/57_get_smtcode_evt_txs.log", "57_get_smtcode_evt_txs")
		(result, response) = RestfulApi().getsmartcodeeventbyheight(height) 
		logger.close(not result)

	def test_58_get_smtcode_evt_txs(self,height=""):
		logger.open("restful/58_get_smtcode_evt_txs.log", "58_get_smtcode_evt_txs")
		(result, response) = RestfulApi().getsmartcodeeventbyheight(height) 
		logger.close(not result)

	def test_59_get_smtcode_evts(self):
		hash=self.m_txhash_right
		
		logger.open("restful/59_get_smtcode_evts.log", "59_get_smtcode_evts")
		(result, response) = RestfulApi().getsmartcodeeventbyhash(hash) 
		logger.close(result)

	def test_60_get_smtcode_evts(self):
		hash=self.m_txhash_wrong
	
		logger.open("restful/60_get_smtcode_evts.log", "60_get_smtcode_evts")
		(result, response) = RestfulApi().getsmartcodeeventbyhash(hash) 
		logger.close(not result)

	def test_61_get_smtcode_evts(self):
		hash=self.m_txhash_right
	
		logger.open("restful/61_get_smtcode_evts.log", "61_get_smtcode_evts")
		(result, response) = RestfulApi().getsmartcodeeventbyhash(hash) 
		logger.close(result)

	def test_62_get_smtcode_evts(self):
		hash=self.m_txhash_wrong
	
		logger.open("restful/62_get_smtcode_evts.log", "62_get_smtcode_evts")
		(result, response) = RestfulApi().getsmartcodeeventbyhash(hash) 
		logger.close(not result)
	
	def test_63_get_smtcode_evts(self,hash="abc"):
		logger.open("restful/63_get_smtcode_evts.log", "63_get_smtcode_evts")
		(result, response) = RestfulApi().getsmartcodeeventbyhash(hash) 
		logger.close(not result)
		
	def test_64_get_smtcode_evts(self,hash=123):
		logger.open("restful/64_get_smtcode_evts.log", "64_get_smtcode_evts")
		(result, response) = RestfulApi().getsmartcodeeventbyhash(hash) 
		logger.close(not result)
		
	def test_65_get_smtcode_evts(self,hash=""):
		logger.open("restful/65_get_smtcode_evts.log", "65_get_smtcode_evts")
		(result, response) = RestfulApi().getsmartcodeeventbyhash(hash) 
		logger.close(not result)
		
	def test_66_get_blk_hgt_by_txhash(self):
		hash=self.m_txhash_right
	
		logger.open("restful/66_get_blk_hgt_by_txhash.log", "66_get_blk_hgt_by_txhash")
		(result, response) = RestfulApi().getblockheightbytxhash(hash)
		logger.close(result)
		
	def test_67_get_blk_hgt_by_txhash(self):
		hash=self.m_txhash_wrong
	
		logger.open("restful/67_get_blk_hgt_by_txhash.log", "67_get_blk_hgt_by_txhash")
		(result, response) = RestfulApi().getblockheightbytxhash(hash)
		logger.close(not result)
		
	def test_68_get_blk_hgt_by_txhash(self,hash=""):
		logger.open("restful/68_get_blk_hgt_by_txhash.log", "68_get_blk_hgt_by_txhash")
		(result, response) = RestfulApi().getblockheightbytxhash(hash)
		logger.close(not result)
		
	def test_69_get_blk_hgt_by_txhash(self,hash=123):
		logger.open("restful/69_get_blk_hgt_by_txhash.log", "69_get_blk_hgt_by_txhash")
		(result, response) = RestfulApi().getblockheightbytxhash(hash)
		logger.close(not result)

	def test_70_get_merkle_proof(self):
		hash=self.m_txhash_right
	
		logger.open("restful/70_get_merkle_proof.log", "70_get_merkle_proof")
		(result, response) = RestfulApi().getmerkleproofbytxhash(hash) 
		logger.close(result)

	def test_71_get_merkle_proof(self):
		hash=self.m_txhash_wrong
		
		logger.open("restful/71_get_merkle_proof.log", "71_get_merkle_proof")
		(result, response) = RestfulApi().getmerkleproofbytxhash(hash) 
		logger.close(not result)

	def test_72_get_merkle_proof(self,hash=""):
		logger.open("restful/72_get_merkle_proof.log", "72_get_merkle_proof")
		(result, response) = RestfulApi().getmerkleproofbytxhash(hash) 
		logger.close(not result)

	def test_73_get_merkle_proof(self,hash=123):
		logger.open("restful/73_get_merkle_proof.log", "73_get_merkle_proof")
		(result, response) = RestfulApi().getmerkleproofbytxhash(hash) 
		logger.close(not result)
	
	def test_74_get_conn_count1(self):
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
		logger.open("restful/74_get_conn_count1.log", "74_get_conn_count1")
		(result, response) = run_single_task(task)
		logger.close(not result)

	def test_75_no_url(self):
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
		logger.open("restful/75_no_url.log", "75_no_url")
		(result, response) = run_single_task(task)
		logger.close(not result)
		
####################################################
if __name__ == '__main__':
	unittest.main()  
