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
from utils.logger import LoggerInstance
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.websocketapi import WebSocketApi
from utils.commonapi import *
from utils.base import WebSocket
from test_api import *
from test_conf import *
from utils.commonapi import call_contract

from utils.rpcapi import RPCApi

rpcApi = RPCApi()

logger = LoggerInstance

####################################################
#test cases
class TestNeoAPI(ParametrizedTestCase):
	
	def setUp(self):
		
		time.sleep(2)
		print("stop all")
		stop_all_nodes()
		print("start all")
		start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(20)
		
		(self.contract_addr, self.contract_tx_hash) = deploy_contract_full("./tasks/neo_1_194.neo")
		(self.contract_addr_1, self.contract_tx_hash_1) = deploy_contract_full("./tasks/neo_1_194.neo", price=1000000000)
		
		#time.sleep(20)
		self.block_height = int(rpcApi.getblockcount()[1]["result"]) - 1
		self.block_hash = script_hash_bl_reserver(rpcApi.getblockhash(self.block_height - 1)[1]["result"])
		self.CONTRACT_ADDRESS = self.contract_addr

		self.PUBLICKEY =Config.NODES[0]["pubkey"]
		self.PUBLICKEY1 =Config.NODES[7]["pubkey"]

		time.sleep(5)

		self.BLOCK_HEIGHT_WITH_TX = str(rpcApi.getblockheightbytxhash(tx_hash=self.contract_tx_hash)[1]["result"])
		self.BLOCK_HEIGHT_WITHOUT_TX = str(rpcApi.getblockheightbytxhash(tx_hash=self.contract_tx_hash)[1]["result"]+1)
		time.sleep(5)
		self.HEIGHT_CORRECT = str(self.block_height)
		self.HEIGHT_BORDER_BOTTON = "0"
		self.HEIGHT_BORDER_TOP = "4294967291"
		self.HEIGHT_INCORRECT_1 = "-1"
		self.HEIGHT_INCORRECT_2 = str(self.block_height + 1000)
		self.HEIGHT_INCORRECT_3 = "abc"
		self.HEIGHT_INCORRECT_4 = ""

		self.BLOCK_HASH_CORRECT = self.block_hash
		self.BLOCK_HASH_INCORRECT_1 = "" # NULL
		self.BLOCK_HASH_INCORRECT_2 = self.block_hash[:-2] # HASH NOT EXISTENT
		self.BLOCK_HASH_INCORRECT_3 = self.block_hash + "1111"
		self.BLOCK_HASH_INCORRECT_4 = "1234"

		self.TX_HASH_CORRECT = script_hash_bl_reserver(self.contract_tx_hash)
		self.TX_HASH_INCORRECT_1 = "" # NULL
		self.TX_HASH_INCORRECT_2 = self.contract_tx_hash[:-2] # TX HASH NOT EXISTENT
		self.TX_HASH_INCORRECT_3 = self.contract_tx_hash + "1111"
		self.TX_HASH_INCORRECT_4 = "1234"

		self.SCRIPT_HASH_CORRECT = script_hash_bl_reserver(self.contract_addr)
		self.SCRIPT_HASH_INCORRECT_1 = "31313131"
		self.SCRIPT_HASH_INCORRECT_2 = ByteToHex(bytes(self.contract_tx_hash_1, encoding = "utf8"))
		self.SCRIPT_HASH_INCORRECT_3 = ""

		self.KEY_CORRECT = "313233"
		self.KEY_CORRECT_1 = "74657374"
		self.KEY_INCORRECT_1 = ""
		self.KEY_CORRECT_2 = Conf.LENGTH_65536
		self.KEY_CORRECT_3 = "2140232524265e2a28295f202b217e60"

		self.VALUE_CORRECT = "313233"
		self.VALUE_CORRECT_1 = "74657374"
		self.VALUE_INCORRECT_1 = ""
		self.VALUE_CORRECT_2 = Conf.LENGTH_65536
		self.VALUE_CORRECT_3 = "2140232524265e2a28295f202b217e60"

		self.NAME_1 = "test"
		self.NAME_2 = "123"
		self.NAME_3 = "!@#%$&^*()_ +!~`"
		self.NAME_4 = Conf.LENGTH_65536
		self.NAME_5 = ""

		self.VERSION_1 = "test"
		self.VERSION_2 = "123"
		self.VERSION_3 = Conf.LENGTH_65536
		self.VERSION_4 = "!@#%$&^*()_ +!~`"
		self.VERSION_5 = ""

		self.AUTHOR_1 = "test"
		self.AUTHOR_2 = "123"
		self.AUTHOR_3 = Conf.LENGTH_65536
		self.AUTHOR_4 = "!@#%$&^*()_ +!~`"
		self.AUTHOR_5 = ""

		self.EMAIL_1 = "test"
		self.EMAIL_2 = "123"
		self.EMAIL_3 = Conf.LENGTH_65536
		self.EMAIL_4 = "!@#%$&^*()_ +!~`"
		self.EMAIL_5 = ""

		self.DESC_1 = "test"
		self.DESC_2 = "123"
		self.DESC_3 = Conf.LENGTH_65536
		self.DESC_4 = "!@#%$&^*()_ +!~`"
		self.DESC_5 = ""


		self.DESC_1 = "test"
	
		self.GET_HEADER_FUNC_NAME = "GetHeader"
		self.GET_HEIGHT_FUNC_NAME = "GetHeight"
		self.GET_BLOCK_FUNC_NAME = "GetBlock"
		self.GET_TRANSACTION_FUNC_NAME = "GetTransaction"
		self.GET_CONTRACT_FUNC_NAME = "GetContract"
		self.GET_HEADER_HASH_FUNC_NAME = "GetHeaderHash"
		self.GET_HEADER_VERSION_FUNC_NAME = "GetHeaderVersion"
		self.GET_HEADER_PREHASH_FUNC_NAME = "GetHeaderPrevHash"
		self.GET_HEADER_INDEX_FUNC_NAME = "GetHeaderIndex"
		self.GET_HEADER_MERKLEROOT_FUNC_NAME = "GetHeaderMerkleRoot"
		self.GET_HEADER_TIMESTAMP_FUNC_NAME = "GetHeaderTimestamp"
		self.GET_HEADER_CONSENSUS_DATA_FUNC_NAME = "GetHeaderConsensusData"
		self.GET_HEADER_NEXT_CONSENSUS_FUNC_NAME = "GetHeaderNextConsensus"
		self.GET_BLOCK_TRANSACTION_COUNT_FUNC_NAME = "GetBlockTransactionCount"
		self.GET_BLOCK_TRANSACTIONS_FUNC_NAME = "GetBlockTransactions"
		self.GET_BLOCK_TRANSACTION_FUNC_NAME = "GetBlockTransaction_40"
		self.GET_CONTRACTION_FUNC_NAME = "GetTransaction_Hash"
		self.GET_CONTRACTION_TYPE_FUNC_NAME = "GetTransaction_Type"
		self.GET_TRANSACTIONS_ATTRIBUTE_FUNC_NAME = "GetTransaction_Attributes"
		self.GET_TRANSACTIONS_ATTRIBUTE_USAGE_FUNC_NAME = "GetTransactionAttribute_Usage"
		self.GET_TRANSACTIONS_ATTRIBUTE_DATA_FUNC_NAME = "GetTransactionAttribute_Data"
		self.GET_CONTRACT_SCRIPT_FUNC_TIME = "GetContract_Script"
		self.GET_CONTRACT_CREATE_FUNC_TIME = "GetContract_Create"
		self.GET_CONTRACT_DESTROY_FUNC_NAME = "GetContract_Destroy"

		self.PARAM_TYPE_INT = "int"
		self.PARAM_TYPE_BYTEARRAY = "bytearray"
	
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
	
	def test_01_blockchain_get_height(self):
		log_path = "01_blockchain_get_height.log"
		task_name = "01_blockchain_get_height"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(self.CONTRACT_ADDRESS, self.GET_HEIGHT_FUNC_NAME)
		self.finish(task_name, log_path, result, "")
	
	def test_03_blockchain_get_header(self):
		log_path = "03_blockchain_get_header.log"
		task_name = "03_blockchain_get_header"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_HEADER_FUNC_NAME, self.PARAM_TYPE_INT, self.HEIGHT_CORRECT)
		self.finish(task_name, log_path, result, "")
	
	def test_04_blockchain_get_header(self):
		log_path = "04_blockchain_get_header.log"
		task_name = "04_blockchain_get_header"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_HEADER_FUNC_NAME, self.PARAM_TYPE_INT, self.HEIGHT_INCORRECT_2)
		self.finish(task_name, log_path, not result, "")

	def test_05_blockchain_get_header(self):
		log_path = "05_blockchain_get_header.log"
		task_name = "05_blockchain_get_header"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_HEADER_FUNC_NAME, self.PARAM_TYPE_INT, self.HEIGHT_BORDER_BOTTON)
		self.finish(task_name, log_path, result, "")

	def test_06_blockchain_get_header(self):
		log_path = "06_blockchain_get_header.log"
		task_name = "06_blockchain_get_header"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_HEADER_FUNC_NAME, self.PARAM_TYPE_INT, self.HEIGHT_BORDER_TOP)
		self.finish(task_name, log_path, not result, "")

	def test_07_blockchain_get_header(self):
		log_path = "07_blockchain_get_header.log"
		task_name = "07_blockchain_get_header"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_HEADER_FUNC_NAME, self.PARAM_TYPE_INT, self.HEIGHT_INCORRECT_1)
		self.finish(task_name, log_path, not result, "")

	def test_08_blockchain_get_header(self):
		log_path = "08_blockchain_get_header.log"
		task_name = "08_blockchain_get_header"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_HEADER_FUNC_NAME, self.PARAM_TYPE_INT, self.HEIGHT_INCORRECT_3)
		self.finish(task_name, log_path, not result, "")

	def test_09_blockchain_get_header(self):
		log_path = "09_blockchain_get_header.log"
		task_name = "09_blockchain_get_header"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_HEADER_FUNC_NAME, self.PARAM_TYPE_INT, self.HEIGHT_INCORRECT_4)
		self.finish(task_name, log_path, not result, "")
	
	
	def test_10_blockchain_get_block(self):
		log_path = "10_blockchain_get_block.log"
		task_name = "10_blockchain_get_block"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_BLOCK_FUNC_NAME, self.PARAM_TYPE_BYTEARRAY, self.BLOCK_HASH_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_11_blockchain_get_header(self):
		log_path = "11_blockchain_get_header.log"
		task_name = "11_blockchain_get_header"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_BLOCK_FUNC_NAME, self.PARAM_TYPE_BYTEARRAY, self.BLOCK_HASH_INCORRECT_4)
		self.finish(task_name, log_path, not result, "")

	def test_12_blockchain_get_transaction(self):
		log_path = "12_blockchain_get_transaction.log"
		task_name = "12_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_TRANSACTION_FUNC_NAME, self.PARAM_TYPE_BYTEARRAY, self.TX_HASH_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_13_blockchain_get_transaction(self):
		log_path = "13_blockchain_get_transaction.log"
		task_name = "13_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_TRANSACTION_FUNC_NAME, self.PARAM_TYPE_BYTEARRAY, self.TX_HASH_INCORRECT_4)
		self.finish(task_name, log_path, not result, "")

	def test_15_blockchain_get_transaction(self):
		log_path = "15_blockchain_get_transaction.log"
		task_name = "15_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_TRANSACTION_FUNC_NAME, self.PARAM_TYPE_BYTEARRAY, [self.TX_HASH_CORRECT, self.TX_HASH_CORRECT])
		self.finish(task_name, log_path, not result, "")

	def test_16_blockchain_get_contact(self):
		log_path = "16_blockchain_get_contact.log"
		task_name = "16_blockchain_get_contact"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_CONTRACT_FUNC_NAME, self.PARAM_TYPE_BYTEARRAY, self.SCRIPT_HASH_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_17_blockchain_get_contact(self):
		log_path = "17_blockchain_get_contact.log"
		task_name = "17_blockchain_get_contact"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_CONTRACT_FUNC_NAME, self.PARAM_TYPE_BYTEARRAY, self.SCRIPT_HASH_INCORRECT_1)
		self.finish(task_name, log_path, not result, "")

	def test_18_blockchain_get_contact(self):
		log_path = "18_blockchain_get_contact.log"
		task_name = "18_blockchain_get_contact"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_CONTRACT_FUNC_NAME, self.PARAM_TYPE_BYTEARRAY, self.SCRIPT_HASH_INCORRECT_2)
		self.finish(task_name, log_path, not result, "")

	def test_20_blockchain_get_hash(self):
		log_path = "20_blockchain_get_hash.log"
		task_name = "20_blockchain_get_hash"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_HEADER_HASH_FUNC_NAME, self.PARAM_TYPE_INT, self.HEIGHT_CORRECT)
		self.finish(task_name, log_path, result, "")
	
	def test_22_blockchain_get_version(self):
		log_path = "22_blockchain_get_version.log"
		task_name = "22_blockchain_get_version"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_HEADER_VERSION_FUNC_NAME, self.PARAM_TYPE_INT, self.HEIGHT_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_24_blockchain_get_prehash(self):
		log_path = "24_blockchain_get_prehash.log"
		task_name = "24_blockchain_get_prehash"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_HEADER_PREHASH_FUNC_NAME, self.PARAM_TYPE_INT, self.HEIGHT_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_26_blockchain_get_index(self):
		log_path = "26_blockchain_get_index.log"
		task_name = "26_blockchain_get_index"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_HEADER_INDEX_FUNC_NAME, self.PARAM_TYPE_INT, self.HEIGHT_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_28_blockchain_get_merkle_root(self):
		log_path = "28_blockchain_get_merkle_root.log"
		task_name = "28_blockchain_get_merkle_root"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_HEADER_MERKLEROOT_FUNC_NAME, self.PARAM_TYPE_INT, self.HEIGHT_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_30_blockchain_get_timestamp(self):
		log_path = "30_blockchain_get_timestamp.log"
		task_name = "30_blockchain_get_timestamp"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_HEADER_TIMESTAMP_FUNC_NAME, self.PARAM_TYPE_INT, self.HEIGHT_CORRECT)
		self.finish(task_name, log_path, result, "")
	
	
	
	def test_32_blockchain_get_consensusdata(self):
		log_path = "32_blockchain_get_consensusdata.log"
		task_name = "32_blockchain_get_consensusdata"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_HEADER_CONSENSUS_DATA_FUNC_NAME, self.PARAM_TYPE_INT, self.HEIGHT_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_34_blockchain_get_next_consensus(self):
		log_path = "34_blockchain_get_next_consensus.log"
		task_name = "34_blockchain_get_next_consensus"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_HEADER_NEXT_CONSENSUS_FUNC_NAME, self.PARAM_TYPE_INT, self.HEIGHT_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_36_blockchain_get_transaction_count(self):
		log_path = "36_blockchain_get_transaction_count.log"
		task_name = "36_blockchain_get_transaction_count"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_BLOCK_TRANSACTION_COUNT_FUNC_NAME, self.PARAM_TYPE_INT, self.HEIGHT_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_37_blockchain_get_transaction_count(self):
		log_path = "37_blockchain_get_transaction_count.log"
		task_name = "37_blockchain_get_transaction_count"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_BLOCK_TRANSACTION_COUNT_FUNC_NAME, self.PARAM_TYPE_INT, "3")
		self.finish(task_name, log_path, not result, "")

	def test_38_blockchain_get_transactions(self):
		log_path = "38_blockchain_get_transactions.log"
		task_name = "38_blockchain_get_transactions"
		self.start(log_path)
		time.sleep(10)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_BLOCK_TRANSACTIONS_FUNC_NAME, self.PARAM_TYPE_INT, self.HEIGHT_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_39_blockchain_get_transactions(self):
		log_path = "39_blockchain_get_transactions.log"
		task_name = "39_blockchain_get_transactions"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_BLOCK_TRANSACTIONS_FUNC_NAME, self.PARAM_TYPE_INT, "2")
		self.finish(task_name, log_path, not result, "")

	def test_40_blockchain_get_transactions(self):
		log_path = "40_blockchain_get_transaction.log"
		task_name = "40_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "GetBlockTransaction_40", self.PARAM_TYPE_INT, "1", self.PARAM_TYPE_INT, "0")
		self.finish(task_name, log_path, not result, "")

	def test_41_blockchain_get_transaction(self):
		log_path = "41_blockchain_get_transaction.log"
		task_name = "41_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "GetBlockTransaction_40", self.PARAM_TYPE_INT, self.BLOCK_HEIGHT_WITHOUT_TX, self.PARAM_TYPE_INT, "0")
		self.finish(task_name, log_path, not result, "")

	def test_42_blockchain_get_transaction(self):
		log_path = "42_blockchain_get_transaction.log"
		task_name = "42_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "GetBlockTransaction_40", self.PARAM_TYPE_INT, self.BLOCK_HEIGHT_WITH_TX, self.PARAM_TYPE_INT, "-1")
		self.finish(task_name, log_path, not result, "")

	def test_43_blockchain_get_transaction(self):
		log_path = "43_blockchain_get_transaction.log"
		task_name = "43_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "GetBlockTransaction_40", self.PARAM_TYPE_INT, self.BLOCK_HEIGHT_WITH_TX, self.PARAM_TYPE_INT, "0")
		self.finish(task_name, log_path, not result, "")

	def test_44_blockchain_get_transaction(self):
		log_path = "44_blockchain_get_transaction.log"
		task_name = "44_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "GetBlockTransaction_44", self.PARAM_TYPE_INT, self.BLOCK_HEIGHT_WITH_TX, self.PARAM_TYPE_INT, "1")
		self.finish(task_name, log_path, not result, "")

	def test_45_blockchain_get_transaction(self):
		log_path = "45_blockchain_get_transaction.log"
		task_name = "45_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "GetBlockTransaction_44", self.PARAM_TYPE_INT, self.BLOCK_HEIGHT_WITH_TX, self.PARAM_TYPE_INT, "2")
		self.finish(task_name, log_path, not result, "")

	def test_46_blockchain_get_transaction_hash(self):
		log_path = "46_blockchain_get_transaction_hash.log"
		task_name = "46_blockchain_get_transaction_hash"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_CONTRACTION_FUNC_NAME, self.PARAM_TYPE_BYTEARRAY, self.TX_HASH_CORRECT)
		self.finish(task_name, log_path, result, "")
	
	def test_48_blockchain_get_transaction_type(self):
		log_path = "48_blockchain_get_transaction_type.log"
		task_name = "48_blockchain_get_transaction_type"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_CONTRACTION_TYPE_FUNC_NAME, self.PARAM_TYPE_BYTEARRAY, self.TX_HASH_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_50_gettransaction_attributes(self):
		log_path = "50_gettransaction_attributes.log"
		task_name = "50_gettransaction_attributes"
		self.start(log_path)
		time.sleep(10)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_TRANSACTIONS_ATTRIBUTE_FUNC_NAME, self.PARAM_TYPE_BYTEARRAY, self.TX_HASH_CORRECT)
		self.finish(task_name, log_path, result, "")
	
	
	def test_52_gettransactionattribute_usage(self):
		log_path = "52_gettransactionattribute_usage.log"
		task_name = "52_gettransactionattribute_usage"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, self.GET_TRANSACTIONS_ATTRIBUTE_USAGE_FUNC_NAME, self.PARAM_TYPE_BYTEARRAY, self.TX_HASH_CORRECT,self.PARAM_TYPE_INT, "1")
		self.finish(task_name, log_path, result, "")

	def test_54_gettransactionattribute_data(self):
		log_path = "54_gettransactionattribute_data.log"
		task_name = "54_gettransactionattribute_data"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, self.GET_TRANSACTIONS_ATTRIBUTE_DATA_FUNC_NAME, self.PARAM_TYPE_BYTEARRAY, self.TX_HASH_CORRECT,self.PARAM_TYPE_INT, "1")
		self.finish(task_name, log_path, result, "")

	def test_56_getcontract_script(self):
		log_path = "56_getcontract_script.log"
		task_name = "56_getcontract_script"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, self.GET_CONTRACT_SCRIPT_FUNC_TIME, self.PARAM_TYPE_BYTEARRAY, self.SCRIPT_HASH_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_58_getcontract_create(self):
		log_path = "58_getcontract_create.log"
		task_name = "58_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_59_getcontract_create(self):
		log_path = "59_getcontract_create.log"
		task_name = "59_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_INCORRECT_1, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_60_getcontract_create(self):
		log_path = "60_getcontract_create.log"
		task_name = "60_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_INCORRECT_3, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_61_getcontract_create(self):
		log_path = "61_getcontract_create.log"
		task_name = "61_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_62_getcontract_create(self):
		log_path = "62_getcontract_create.log"
		task_name = "62_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_2, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_63_getcontract_create(self):
		log_path = "63_getcontract_create.log"
		task_name = "63_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_3, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_64_getcontract_create(self):
		log_path = "64_getcontract_create.log"
		task_name = "64_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_4, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, not result, "")

	def test_65_getcontract_create(self):
		log_path = "65_getcontract_create.log"
		task_name = "65_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_5, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_66_getcontract_create(self):
		log_path = "66_getcontract_create.log"
		task_name = "66_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_67_getcontract_create(self):
		log_path = "67_getcontract_create.log"
		task_name = "67_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_2, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_68_getcontract_create(self):
		log_path = "68_getcontract_create.log"
		task_name = "68_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_3, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, not result, "")

	def test_69_getcontract_create(self):
		log_path = "69_getcontract_create.log"
		task_name = "69_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_4, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_70_getcontract_create(self):
		log_path = "70_getcontract_create.log"
		task_name = "70_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_5, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_71_getcontract_create(self):
		log_path = "71_getcontract_create.log"
		task_name = "71_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_72_getcontract_create(self):
		log_path = "72_getcontract_create.log"
		task_name = "72_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_2, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")
	
	def test_73_getcontract_create(self):
		log_path = "73_getcontract_create.log"
		task_name = "73_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_3, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, not result, "")

	def test_74_getcontract_create(self):
		log_path = "74_getcontract_create.log"
		task_name = "74_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_4, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_75_getcontract_create(self):
		log_path = "75_getcontract_create.log"
		task_name = "75_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_5, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_76_getcontract_create(self):
		log_path = "76_getcontract_create.log"
		task_name = "76_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_77_getcontract_create(self):
		log_path = "77_getcontract_create.log"
		task_name = "77_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_2, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_78_getcontract_create(self):
		log_path = "78_getcontract_create.log"
		task_name = "78_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_3, self.DESC_1)
		self.finish(task_name, log_path, not result, "")

	def test_79_getcontract_create(self):
		log_path = "79_getcontract_create.log"
		task_name = "79_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_4, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_80_getcontract_create(self):
		log_path = "80_getcontract_create.log"
		task_name = "80_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_5, self.DESC_1)
		self.finish(task_name, log_path, result, "")


	def test_81_getcontract_create(self):
		log_path = "81_getcontract_create.log"
		task_name = "81_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_82_getcontract_create(self):
		log_path = "82_getcontract_create.log"
		task_name = "82_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_2)
		self.finish(task_name, log_path, result, "")

	def test_83_getcontract_create(self):
		log_path = "83_getcontract_create.log"
		task_name = "83_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_3)
		self.finish(task_name, log_path, result, "")

	def test_84_getcontract_create(self):
		log_path = "84_getcontract_create.log"
		task_name = "84_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_4)
		self.finish(task_name, log_path, result, "")

	def test_85_getcontract_create(self):
		log_path = "85_getcontract_create.log"
		task_name = "85_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_5)
		self.finish(task_name, log_path, result, "")
	
	def test_86_getcontract_destroy(self):
		log_path = "86_getcontract_destroy.log"
		task_name = "86_getcontract_destroy"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(self.CONTRACT_ADDRESS, self.GET_CONTRACT_DESTROY_FUNC_NAME)
		self.finish(task_name, log_path, result, "")
	
	def test_87_getcontract_destroy(self):
		log_path = "87_getcontract_destroy.log"
		task_name = "87_getcontract_destroy"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(self.CONTRACT_ADDRESS, self.GET_CONTRACT_DESTROY_FUNC_NAME)
		print (str(rpcApi.getblockheightbytxhash(tx_hash=self.contract_tx_hash)[1]["result"]))
		self.finish(task_name, log_path, result, "")

	def test_88_storage_context(self):
		log_path = "88_storage_context.log"
		task_name = "88_storage_context"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, "GetStorageContext", self.PARAM_TYPE_BYTEARRAY, self.SCRIPT_HASH_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_90_current_context(self):
		log_path = "90_current_context.log"
		task_name = "90_current_context"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(self.CONTRACT_ADDRESS, "GetCurrentContext")
		self.finish(task_name, log_path, result, "")

	def test_92_storage_get(self):
		log_path = "92_storage_get.log"
		task_name = "92_storage_get"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Get_92", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_93_storage_get(self):
		log_path = "93_storage_get.log"
		task_name = "93_storage_get"
		self.start(log_path)
		(result, response) = invoke_storage_get(self.CONTRACT_ADDRESS)
		self.finish(task_name, log_path, not result, "")

	def test_94_storage_get(self):
		log_path = "94_storage_get.log"
		task_name = "94_storage_get"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Get_94", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, not result, "")

	def test_95_storage_get(self):
		log_path = "95_storage_get.log"
		task_name = "95_storage_get"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Get_92", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_96_storage_get(self):
		log_path = "96_storage_get.log"
		task_name = "96_storage_get"
		self.start(log_path)
		(result, response) = invoke_storage_get(self.CONTRACT_ADDRESS)
		self.finish(task_name, log_path, result, "")
	
	def test_97_storage_get(self):
		log_path = "97_storage_get.log"
		task_name = "97_storage_get"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Get_92", self.PARAM_TYPE_BYTEARRAY, self.KEY_INCORRECT_1, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_98_storage_get(self):
		log_path = "98_storage_get.log"
		task_name = "98_storage_get"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Get_98", self.PARAM_TYPE_BYTEARRAY, self.KEY_INCORRECT_1, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, not result, "")

	def test_99_storage_put(self):
		log_path = "99_storage_put.log"
		task_name = "99_storage_put"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Put_99", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, result, "")
	
	def test_100_storage_put(self):
		log_path = "100_storage_put.log"
		task_name = "100_storage_put"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Put_100", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, "")
		self.finish(task_name, log_path, not result, "")

	def test_101_storage_put(self):
		log_path = "101_storage_put.log"
		task_name = "101_storage_put"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Put_101", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, not result, "")

	def test_102_storage_put(self):
		log_path = "102_storage_put.log"
		task_name = "102_storage_put"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Put_99", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_103_storage_put(self):
		log_path = "103_storage_put.log"
		task_name = "103_storage_put"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Put_99", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT_1, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_104_storage_put(self):
		log_path = "104_storage_put.log"
		task_name = "104_storage_put"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Put_99", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT_2, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, not result, "")

	def test_105_storage_put(self):
		log_path = "105_storage_put.log"
		task_name = "105_storage_put"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Put_99", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT_3, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_106_storage_put(self):
		log_path = "106_storage_put.log"
		task_name = "106_storage_put"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Put_99", self.PARAM_TYPE_BYTEARRAY, self.KEY_INCORRECT_1, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_107_storage_put(self):
		log_path = "107_storage_put.log"
		task_name = "107_storage_put"
		self.start(log_path)
		(result, response) = invoke_storage_put(self.CONTRACT_ADDRESS)
		self.finish(task_name, log_path, result, "")
	
	def test_108_storage_put(self):
		log_path = "108_storage_put.log"
		task_name = "108_storage_put"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Put_99", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Put_99", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_109_storage_put(self):
		log_path = "109_storage_put.log"
		task_name = "109_storage_put"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Put_99", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT_1)
		self.finish(task_name, log_path, result, "")

	def test_110_storage_put(self):
		log_path = "110_storage_put.log"
		task_name = "110_storage_put"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Put_99", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_111_storage_put(self):
		log_path = "111_storage_put.log"
		task_name = "111_storage_put"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Put_99", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT_2)
		self.finish(task_name, log_path, result, "")

	def test_112_storage_put(self):
		log_path = "112_storage_put.log"
		task_name = "112_storage_put"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Put_99", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT_3)
		self.finish(task_name, log_path, result, "")

	def test_113_storage_put(self):
		log_path = "113_storage_put.log"
		task_name = "113_storage_put"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Put_99", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_INCORRECT_1)
		self.finish(task_name, log_path, result, "")

	def test_114_storage_delete(self):
		log_path = "114_storage_delete.log"
		task_name = "114_storage_delete"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Delete_114", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_115_storage_delete(self):
		log_path = "115_storage_delete.log"
		task_name = "115_storage_delete"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Delete_115", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_116_storage_delete(self):
		log_path = "116_storage_delete.log"
		task_name = "116_storage_delete"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Delete_116", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, not result, "")

	def test_117_storage_delete(self):
		log_path = "117_storage_delete.log"
		task_name = "117_storage_delete"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Delete_114", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_118_storage_delete(self):
		log_path = "118_storage_delete.log"
		task_name = "118_storage_delete"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Delete_114", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT_3)
		self.finish(task_name, log_path, result, "")

	def test_119_storage_delete(self):
		log_path = "119_storage_delete.log"
		task_name = "119_storage_delete"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Delete_114", self.PARAM_TYPE_BYTEARRAY, self.KEY_CORRECT, self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_120_storage_delete(self):
		log_path = "120_storage_delete.log"
		task_name = "120_storage_delete"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(self.CONTRACT_ADDRESS, "Delete_120", self.PARAM_TYPE_BYTEARRAY, "", self.PARAM_TYPE_BYTEARRAY, self.VALUE_CORRECT)
		self.finish(task_name, log_path, result, "")
	
	def test_121_get_time(self):
		log_path = "121_get_time.log"
		task_name = "121_get_time"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(self.CONTRACT_ADDRESS, "GetTime")
		self.finish(task_name, log_path, result, "")

	def test_123_check_witness(self):
		log_path = "123_check_witness.log"
		task_name = "123_check_witness"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, "CheckWitness", self.PARAM_TYPE_BYTEARRAY, self.SCRIPT_HASH_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_124_check_witness(self):
		log_path = "124_check_witness.log"
		task_name = "124_check_witness"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, "CheckWitness", self.PARAM_TYPE_BYTEARRAY, self.SCRIPT_HASH_INCORRECT_2)
		self.finish(task_name, log_path, not result, "")

	def test_125_check_witness(self):
		log_path = "125_check_witness.log"
		task_name = "125_check_witness"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, "CheckWitness", self.PARAM_TYPE_BYTEARRAY, self.SCRIPT_HASH_INCORRECT_1)
		self.finish(task_name, log_path, not result, "")

	def test_126_check_witness(self):
		log_path = "126_check_witness.log"
		task_name = "126_check_witness"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, "CheckWitness", self.PARAM_TYPE_BYTEARRAY, "")
		self.finish(task_name, log_path, not result, "")

	def test_127_check_witness(self):
		log_path = "127_check_witness.log"
		task_name = "127_check_witness"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, "CheckWitness", self.PARAM_TYPE_BYTEARRAY, self.PUBLICKEY)
		self.finish(task_name, log_path, result, "")

	def test_128_check_witness(self):
		log_path = "128_check_witness.log"
		task_name = "128_check_witness"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, "CheckWitness", self.PARAM_TYPE_BYTEARRAY, self.PUBLICKEY1)
		self.finish(task_name, log_path, result, "")

	def test_129_check_witness(self):
		log_path = "129_check_witness.log"
		task_name = "129_check_witness"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, "CheckWitness", self.PARAM_TYPE_BYTEARRAY, "11" + self.PUBLICKEY)
		self.finish(task_name, log_path, not result, "")
	
	def test_130_notify(self):
		log_path = "130_notify.log"
		task_name = "130_notify"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(self.CONTRACT_ADDRESS, "Notify_130")
		self.finish(task_name, log_path, result, "")

	def test_131_notify(self):
		log_path = "131_notify.log"
		task_name = "131_notify"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(self.CONTRACT_ADDRESS, "Notify_131")
		self.finish(task_name, log_path, result, "")

	def test_132_notify(self):
		log_path = "132_notify.log"
		task_name = "132_notify"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(self.CONTRACT_ADDRESS, "Notify_132")
		self.finish(task_name, log_path, result, "")

	def test_133_notify(self):
		log_path = "133_notify.log"
		task_name = "133_notify"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(self.CONTRACT_ADDRESS, "Notify_133")
		self.finish(task_name, log_path, result, "")

	def test_134_log(self):
		log_path = "134_log.log"
		task_name = "134_log"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(self.CONTRACT_ADDRESS, "Log_134")
		self.finish(task_name, log_path, result, "")

	def test_135_log(self):
		log_path = "135_log.log"
		task_name = "135_log"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(self.CONTRACT_ADDRESS, "Log_135")
		self.finish(task_name, log_path, result, "")

	def test_136_log(self):
		log_path = "136_log.log"
		task_name = "136_log"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, "Log_136", "string", self.VALUE_CORRECT_2)
		self.finish(task_name, log_path, result, "")

	def test_137_log(self):
		log_path = "137_log.log"
		task_name = "137_log"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(self.CONTRACT_ADDRESS, "Log_137")
		self.finish(task_name, log_path, result, "")

	def test_138_log(self):
		log_path = "138_log.log"
		task_name = "138_log"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(self.CONTRACT_ADDRESS, "Log_138")
		self.finish(task_name, log_path, result, "")

	def test_153_script_container(self):
		log_path = "153_script_container.log"
		task_name = "153_script_container"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(self.CONTRACT_ADDRESS, "GetScriptContainer")
		self.finish(task_name, log_path, result, "")

	def test_155_script_container(self):
		log_path = "155_excuting_script.log"
		task_name = "155_excuting_script"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(self.CONTRACT_ADDRESS, "GetExecutingScriptHash")
		self.finish(task_name, log_path, result, "")

	def test_157_calling_script(self):
		log_path = "157_calling_script.log"
		task_name = "157_calling_script"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(self.CONTRACT_ADDRESS, "GetCallingScriptHash")
		self.finish(task_name, log_path, result, "")

	def test_159_entry_script_hash(self):
		log_path = "159_entry_script_hash.log"
		task_name = "159_entry_script_hash"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(self.CONTRACT_ADDRESS, "GetEntryScriptHash")
		self.finish(task_name, log_path, result, "")

	def test_163_tx_type(self):
		log_path = "163_tx_type.log"
		task_name = "163_tx_type"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, "GetTransaction_Type", self.PARAM_TYPE_BYTEARRAY, self.TX_HASH_CORRECT)
		self.finish(task_name, log_path, result, "")

	def test_166_getcontract_migrate(self):
		log_path = "166_getcontract_migrate.log"
		task_name = "166_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_167_getcontract_migrate(self):
		log_path = "167_getcontract_migrate.log"
		task_name = "167_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_2, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_168_getcontract_migrate(self):
		log_path = "168_getcontract_migrate.log"
		task_name = "168_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_INCORRECT_2, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, not result, "")

	def test_169_getcontract_migrate(self):
		log_path = "169_getcontract_migrate.log"
		task_name = "169_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, "", self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, not result, "")

	def test_170_getcontract_migrate(self):
		log_path = "170_getcontract_migrate.log"
		task_name = "170_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_171_getcontract_migrate(self):
		log_path = "171_getcontract_migrate.log"
		task_name = "171_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_2, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_172_getcontract_migrate(self):
		log_path = "172_getcontract_migrate.log"
		task_name = "172_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_3, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_173_getcontract_migrate(self):
		log_path = "173_getcontract_migrate.log"
		task_name = "173_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_4, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, not result, "")

	def test_174_getcontract_migrate(self):
		log_path = "174_getcontract_migrate.log"
		task_name = "174_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_5, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_175_getcontract_migrate(self):
		log_path = "175_getcontract_migrate.log"
		task_name = "175_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_176_getcontract_migrate(self):
		log_path = "176_getcontract_migrate.log"
		task_name = "176_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_2, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_177_getcontract_migrate(self):
		log_path = "177_getcontract_migrate.log"
		task_name = "177_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_3, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, not result, "")

	def test_178_getcontract_migrate(self):
		log_path = "178_getcontract_migrate.log"
		task_name = "178_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_4, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_179_getcontract_migrate(self):
		log_path = "179_getcontract_migrate.log"
		task_name = "179_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_5, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_180_getcontract_migrate(self):
		log_path = "180_getcontract_migrate.log"
		task_name = "180_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_181_getcontract_migrate(self):
		log_path = "181_getcontract_migrate.log"
		task_name = "181_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_2, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_182_getcontract_migrate(self):
		log_path = "182_getcontract_migrate.log"
		task_name = "182_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_3, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, not result, "")

	def test_183_getcontract_migrate(self):
		log_path = "183_getcontract_migrate.log"
		task_name = "183_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_4, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_184_getcontract_migrate(self):
		log_path = "184_getcontract_migrate.log"
		task_name = "184_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_5, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_185_getcontract_migrate(self):
		log_path = "185_getcontract_migrate.log"
		task_name = "185_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_186_getcontract_migrate(self):
		log_path = "186_getcontract_migrate.log"
		task_name = "186_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_2, self.DESC_1)
		self.finish(task_name, log_path, result, "")
	
	def test_187_getcontract_migrate(self):
		log_path = "187_getcontract_migrate.log"
		task_name = "187_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_3, self.DESC_1)
		self.finish(task_name, log_path, not result, "")

	def test_188_getcontract_migrate(self):
		log_path = "188_getcontract_migrate.log"
		task_name = "188_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_4, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_189_getcontract_migrate(self):
		log_path = "189_getcontract_migrate.log"
		task_name = "189_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_5, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_190_getcontract_migrate(self):
		log_path = "190_getcontract_migrate.log"
		task_name = "190_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_1)
		self.finish(task_name, log_path, result, "")

	def test_191_getcontract_migrate(self):
		log_path = "191_getcontract_migrate.log"
		task_name = "191_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_2)
		self.finish(task_name, log_path, result, "")

	def test_192_getcontract_migrate(self):
		log_path = "192_getcontract_migrate.log"
		task_name = "192_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_3)
		self.finish(task_name, log_path, result, "")

	def test_193_getcontract_migrate(self):
		log_path = "193_getcontract_migrate.log"
		task_name = "193_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_4)
		self.finish(task_name, log_path, result, "")

	def test_194_getcontract_migrate(self):
		log_path = "194_getcontract_migrate.log"
		task_name = "194_getcontract_migrate"
		self.start(log_path)
		(result, response) = invoke_contract_create(self.CONTRACT_ADDRESS, self.SCRIPT_HASH_CORRECT, self.NAME_1, self.VERSION_1, self.AUTHOR_1, self.EMAIL_1, self.DESC_5)
		self.finish(task_name, log_path, result, "")

	def test_195_check_witness(self):
		log_path = "195_check_witness.log"
		task_name = "195_check_witness"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(self.CONTRACT_ADDRESS, "CheckWitness", self.PARAM_TYPE_BYTEARRAY, "1111"+self.PUBLICKEY)
		self.finish(task_name, log_path, not result, "")
	
####################################################
if __name__ == '__main__':
	suite = unittest.main()
