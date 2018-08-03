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

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.connect import WebSocket
from utils.hexstring import *

from api.apimanager import API

from test_neo_api.test_api import test_api
from test_neo_api.test_config import test_config


####################################################
#test cases
class test_neo_api_1(ParametrizedTestCase):

	def test_init(self):

		time.sleep(2)
		print("stop all")
		API.node().stop_all_nodes()
		print("start all")
		API.node().start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)

		test_config.init()

		for i in range(5):
			test_config.block_with_no_tx = test_api.get_block_with_no_tx(test_config.contract_addr)
			if test_config.block_with_no_tx:
				break
			API.node().wait_gen_block()


	def setUp(self):
		logger.open("test_neo_api/" + self._testMethodName+".log",self._testMethodName)
		
	def tearDown(self):
		logger.close(self.result())
		pass
	
	def test_base_001_blockchainGetHeight(self):
		# log_path = "test_01_blockchainGetHeight.log"
		# task_name = "test_01_blockchainGetHeight"
		try:
			(process, response) = test_api.invoke_func_with_0_param(test_config.CONTRACT_ADDRESS, test_config.GET_HEIGHT_FUNC_NAME)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_base_003_blockchainGetHeader(self):
		# log_path = "test_03_blockchainGetHeader.log"
		# task_name = "test_03_blockchainGetHeader"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_HEADER_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.HEIGHT_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_004_blockchainGetHeader(self):
		# log_path = "test_04_blockchainGetHeader.log"
		# task_name = "test_04_blockchainGetHeader"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_HEADER_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.HEIGHT_INCORRECT_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_005_blockchainGetHeader(self):
		# log_path = "test_05_blockchainGetHeader.log"
		# task_name = "test_05_blockchainGetHeader"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_HEADER_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.HEIGHT_BORDER_BOTTON)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_006_blockchainGetHeader(self):
		# log_path = "test_06_blockchainGetHeader.log"
		# task_name = "test_06_blockchainGetHeader"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_HEADER_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.HEIGHT_BORDER_TOP)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_007_blockchainGetHeader(self):
		# log_path = "test_07_blockchainGetHeader.log"
		# task_name = "test_07_blockchainGetHeader"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_HEADER_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.HEIGHT_INCORRECT_1 )
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_008_blockchainGetHeader(self):
		# log_path = "08_blockchainGet_header.log"
		# task_name = "08_blockchainGet_header"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_HEADER_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.HEIGHT_INCORRECT_3)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_009_blockchainGetHeader(self):
		# log_path = "09_blockchainGet_header.log"
		# task_name = "09_blockchainGet_header"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_HEADER_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.HEIGHT_INCORRECT_4)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	
	def test_base_010_blockchainGetBlock(self):
		# log_path = "10_blockchainGet_block.log"
		# task_name = "10_blockchainGet_block"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_BLOCK_FUNC_NAME, test_config.PARAM_TYPE_BYTEARRAY, test_config.BLOCK_HASH_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_011_blockchainGetHeader(self):
		# log_path = "11_blockchainGet_header.log"
		# task_name = "11_blockchainGet_header"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_BLOCK_FUNC_NAME, test_config.PARAM_TYPE_BYTEARRAY, test_config.BLOCK_HASH_INCORRECT_4)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_012_blockchainGetTransaction(self):
		# log_path = "12_blockchainGetTransaction.log"
		# task_name = "12_blockchainGetTransaction"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_TRANSACTION_FUNC_NAME, test_config.PARAM_TYPE_BYTEARRAY, test_config.TX_HASH_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_013_blockchainGetTransaction(self):
		# log_path = "13_blockchainGetTransaction.log"
		# task_name = "13_blockchainGetTransaction"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_TRANSACTION_FUNC_NAME, test_config.PARAM_TYPE_BYTEARRAY, test_config.TX_HASH_INCORRECT_4)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_015_blockchainGetTransaction(self):
		# log_path = "15_blockchainGetTransaction.log"
		# task_name = "15_blockchainGetTransaction"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_TRANSACTION_FUNC_NAME, test_config.PARAM_TYPE_BYTEARRAY, [test_config.TX_HASH_CORRECT, test_config.TX_HASH_CORRECT])
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_016_blockchainGetContact(self):
		# log_path = "16_blockchainGetContact.log"
		# task_name = "16_blockchainGetContact"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_CONTRACT_FUNC_NAME, test_config.PARAM_TYPE_BYTEARRAY, test_config.SCRIPT_HASH_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_017_blockchainGetContact(self):
		# log_path = "17_blockchainGetContact.log"
		# task_name = "17_blockchainGetContact"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_CONTRACT_FUNC_NAME, test_config.PARAM_TYPE_BYTEARRAY, test_config.SCRIPT_HASH_INCORRECT_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_018_blockchainGetContact(self):
		# log_path = "18_blockchainGetContact.log"
		# task_name = "18_blockchainGetContact"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_CONTRACT_FUNC_NAME, test_config.PARAM_TYPE_BYTEARRAY, test_config.SCRIPT_HASH_INCORRECT_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_020_blockchainGetHash(self):
		# log_path = "20_blockchainGetHash.log"
		# task_name = "20_blockchainGetHash"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_HEADER_HASH_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.HEIGHT_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_base_022_blockchainGetVersion(self):
		# log_path = "22_blockchainGetVersion.log"
		# task_name = "22_blockchainGetVersion"
		#self.test_init()
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_HEADER_VERSION_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.HEIGHT_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_024_blockchainGetPrehash(self):
		# log_path = "24_blockchainGetPrehash.log"
		# task_name = "24_blockchainGetPrehash"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_HEADER_PREHASH_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.HEIGHT_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_026_blockchainGetIndex(self):
		# log_path = "26_blockchainGetIndex.log"
		# task_name = "26_blockchainGetIndex"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_HEADER_INDEX_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.HEIGHT_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_028_blockchainGetMerkle_root(self):
		# log_path = "28_blockchainGet_merkle_root.log"
		# task_name = "28_blockchainGet_merkle_root"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_HEADER_MERKLEROOT_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.HEIGHT_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_030_blockchainGetTimestamp(self):
		# log_path = "30_blockchainGet_timestamp.log"
		# task_name = "30_blockchainGet_timestamp"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_HEADER_TIMESTAMP_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.HEIGHT_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	
	
	def test_base_032_blockchainGetConsensusdata(self):
		# log_path = "32_blockchainGet_consensusdata.log"
		# task_name = "32_blockchainGet_consensusdata"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_HEADER_CONSENSUS_DATA_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.HEIGHT_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_034_blockchainGetNextConsensus(self):
		# log_path = "34_blockchainGet_next_consensus.log"
		# task_name = "34_blockchainGet_next_consensus"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_HEADER_NEXT_CONSENSUS_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.HEIGHT_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_036_blockchainGetTransactionCount(self):
		# log_path = "36_blockchainGetTransaction_count.log"
		# task_name = "36_blockchainGetTransaction_count"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_BLOCK_TRANSACTION_COUNT_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.HEIGHT_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_037_blockchainGetTransactionCount(self):
		# log_path = "37_blockchainGetTransaction_count.log"
		# task_name = "37_blockchainGetTransaction_count"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_BLOCK_TRANSACTION_COUNT_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.block_with_no_tx)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_038_blockchainGetTransactions(self):
		# log_path = "38_blockchainGetTransactions.log"
		# task_name = "38_blockchainGetTransactions"
		try:
			time.sleep(10)
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_BLOCK_TRANSACTIONS_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.HEIGHT_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_039_blockchainGetTransactions(self):
		# log_path = "39_blockchainGetTransactions.log"
		# task_name = "39_blockchainGetTransactions"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_BLOCK_TRANSACTIONS_FUNC_NAME, test_config.PARAM_TYPE_INT, test_config.block_with_no_tx)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_040_blockchainGetTransaction(self):
		# log_path = "40_blockchainGetTransaction.log"
		# task_name = "40_blockchainGetTransaction"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "GetBlockTransaction_40", test_config.PARAM_TYPE_INT, test_config.BLOCK_HEIGHT_WITH_TX, test_config.PARAM_TYPE_INT, "0")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_041_blockchainGetTransaction(self):
		# log_path = "41_blockchainGetTransaction.log"
		# task_name = "41_blockchainGetTransaction"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "GetBlockTransaction_40", test_config.PARAM_TYPE_INT, test_config.BLOCK_HEIGHT_WITHOUT_TX, test_config.PARAM_TYPE_INT, "0")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_042_blockchainGetTransaction(self):
		# log_path = "42_blockchainGetTransaction.log"
		# task_name = "42_blockchainGetTransaction"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "GetBlockTransaction_40", test_config.PARAM_TYPE_INT, test_config.BLOCK_HEIGHT_WITH_TX, test_config.PARAM_TYPE_INT, "-1")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_043_blockchainGetTransaction(self):
		# log_path = "43_blockchainGetTransaction.log"
		# task_name = "43_blockchainGetTransaction"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "GetBlockTransaction_40", test_config.PARAM_TYPE_INT, test_config.BLOCK_HEIGHT_WITH_TX, test_config.PARAM_TYPE_INT, "0")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_044_blockchainGetTransaction(self):
		# log_path = "44_blockchainGetTransaction.log"
		# task_name = "44_blockchainGetTransaction"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "GetBlockTransaction_44", test_config.PARAM_TYPE_INT, test_config.BLOCK_HEIGHT_WITH_TX, test_config.PARAM_TYPE_INT, str(test_config.BLOCK_TX_COUNT - 1))
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_045_blockchainGetTransaction(self):
		# log_path = "45_blockchainGetTransaction.log"
		# task_name = "45_blockchainGetTransaction"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "GetBlockTransaction_45", test_config.PARAM_TYPE_INT, test_config.BLOCK_HEIGHT_WITH_TX, test_config.PARAM_TYPE_INT, str(test_config.BLOCK_TX_COUNT))
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_046_blockchainGetTransactionHash(self):
		# log_path = "46_blockchainGetTransactionHash.log"
		# task_name = "46_blockchainGetTransactionHash"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_CONTRACTION_FUNC_NAME, test_config.PARAM_TYPE_BYTEARRAY, test_config.TX_HASH_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_base_048_blockchainGetTransactionType(self):
		# log_path = "48_blockchainGetTransaction_type.log"
		# task_name = "48_blockchainGetTransaction_type"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_CONTRACTION_TYPE_FUNC_NAME, test_config.PARAM_TYPE_BYTEARRAY, test_config.TX_HASH_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_050_gettransactionAttributes(self):
		# log_path = "50Gettransaction_attributes.log"
		# task_name = "50Gettransaction_attributes"
		try:
			time.sleep(10)
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_TRANSACTIONS_ATTRIBUTE_FUNC_NAME, test_config.PARAM_TYPE_BYTEARRAY, test_config.TX_HASH_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	
	def test_base_052_gettransactionattributeUsage(self):
		# log_path = "52Gettransactionattribute_usage.log"
		# task_name = "52Gettransactionattribute_usage"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, test_config.GET_TRANSACTIONS_ATTRIBUTE_USAGE_FUNC_NAME, test_config.PARAM_TYPE_BYTEARRAY, test_config.TX_HASH_CORRECT,test_config.PARAM_TYPE_INT, test_config.BLOCK_HEIGHT_WITH_TX)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_054_gettransactionattributeData(self):
		# log_path = "54Gettransactionattribute_data.log"
		# task_name = "54Gettransactionattribute_data"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, test_config.GET_TRANSACTIONS_ATTRIBUTE_DATA_FUNC_NAME, test_config.PARAM_TYPE_BYTEARRAY, test_config.TX_HASH_CORRECT,test_config.PARAM_TYPE_INT, "1")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_056_getcontractScript(self):
		# log_path = "56Getcontract_script.log"
		# task_name = "56Getcontract_script"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, test_config.GET_CONTRACT_SCRIPT_FUNC_TIME, test_config.PARAM_TYPE_BYTEARRAY, test_config.SCRIPT_HASH_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_058_getcontractCreate(self):
		# log_path = "58GetcontractCreate.log"
		# task_name = "58GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_059_getcontractCreate(self):
		# log_path = "59GetcontractCreate.log"
		# task_name = "59GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_INCORRECT_1, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_060_getcontractCreate(self):
		# log_path = "60GetcontractCreate.log"
		# task_name = "60GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_INCORRECT_3, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_061_getcontractCreate(self):
		# log_path = "61GetcontractCreate.log"
		# task_name = "61GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_062_getcontractCreate(self):
		# log_path = "62GetcontractCreate.log"
		# task_name = "62GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_2, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_063_getcontractCreate(self):
		# log_path = "63GetcontractCreate.log"
		# task_name = "63GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_3, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_064_getcontractCreate(self):
		# log_path = "64GetcontractCreate.log"
		# task_name = "64GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_4, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_065_getcontractCreate(self):
		# log_path = "65GetcontractCreate.log"
		# task_name = "65GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_5, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_066_getcontractCreate(self):
		# log_path = "66GetcontractCreate.log"
		# task_name = "66GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_067_getcontractCreate(self):
		# log_path = "67GetcontractCreate.log"
		# task_name = "67GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_2, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_068_getcontractCreate(self):
		# log_path = "68GetcontractCreate.log"
		# task_name = "68GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_3, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_069_getcontractCreate(self):
		# log_path = "69GetcontractCreate.log"
		# task_name = "69GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_4, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_070_getcontractCreate(self):
		# log_path = "70GetcontractCreate.log"
		# task_name = "70GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_5, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_071_getcontractCreate(self):
		# log_path = "71GetcontractCreate.log"
		# task_name = "71GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_072_getcontractCreate(self):
		# log_path = "72GetcontractCreate.log"
		# task_name = "72GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_2, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_073_getcontractCreate(self):
		# log_path = "73GetcontractCreate.log"
		# task_name = "73GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_3, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_074_getcontractCreate(self):
		# log_path = "74GetcontractCreate.log"
		# task_name = "74GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_4, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_075_getcontractCreate(self):
		# log_path = "75GetcontractCreate.log"
		# task_name = "75GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_5, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_076_getcontractCreate(self):
		# log_path = "76GetcontractCreate.log"
		# task_name = "76GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_077_getcontractCreate(self):
		# log_path = "77GetcontractCreate.log"
		# task_name = "77GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_2, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_078_getcontractCreate(self):
		# log_path = "78GetcontractCreate.log"
		# task_name = "78GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_3, test_config.DESC_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_079_getcontractCreate(self):
		# log_path = "79GetcontractCreate.log"
		# task_name = "79GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_4, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_080_getcontractCreate(self):
		# log_path = "80GetcontractCreate.log"
		# task_name = "80GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_5, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])


	def test_normal_081_getcontractCreate(self):
		# log_path = "81GetcontractCreate.log"
		# task_name = "81GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_082_getcontractCreate(self):
		# log_path = "82GetcontractCreate.log"
		# task_name = "82GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_2)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_083_getcontractCreate(self):
		# log_path = "83GetcontractCreate.log"
		# task_name = "83GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_3)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_084_getcontractCreate(self):
		# log_path = "84GetcontractCreate.log"
		# task_name = "84GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_4)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_085_getcontractCreate(self):
		# log_path = "85GetcontractCreate.log"
		# task_name = "85GetcontractCreate"
		try:
			(process, response) = test_api.invoke_contract_create(test_config.CONTRACT_ADDRESS, test_config.SCRIPT_HASH_CORRECT, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_5)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_base_086_getcontractDestroy(self):
		# log_path = "86Getcontract_destroy.log"
		# task_name = "86Getcontract_destroy"
		try:
			(process, response) = test_api.invoke_func_with_0_param(test_config.CONTRACT_ADDRESS, test_config.GET_CONTRACT_DESTROY_FUNC_NAME)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_087_getcontractDestroy(self):
		# log_path = "87Getcontract_destroy.log"
		# task_name = "87Getcontract_destroy"
		self.test_init()
		try:
			(process, response) = test_api.invoke_func_with_0_param(test_config.CONTRACT_ADDRESS, test_config.GET_CONTRACT_DESTROY_FUNC_NAME)
			result = str(API.rpc().getblockheightbytxhash(tx_hash=test_config.contract_tx_hash)[1]["result"])
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])



	def test_abnormal_093_storageGet(self):
		# log_path = "93_storageGet.log"
		# task_name = "93_storageGet"
		try:
			(process, response) = test_api.invoke_storage_get(test_config.CONTRACT_ADDRESS)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_094_storageGet(self):
		# log_path = "94_storageGet.log"
		# task_name = "94_storageGet"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Get_94", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])



	def test_abnormal_096_storageGet(self):
		# log_path = "96_storageGet.log"
		# task_name = "96_storageGet"
		try:
			(process, response) = test_api.invoke_storage_get(test_config.CONTRACT_ADDRESS)
			self.ASSERT(not process or response["result"]["Result"] == "", "")
		except Exception as e:
			logger.print(e.args[0])
	


	def test_abnormal_098_storageGet(self):
		# log_path = "98_storageGet.log"
		# task_name = "98_storageGet"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Get_98", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_INCORRECT_1, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])


	
	def test_abnormal_100_storagePut(self):
		# log_path = "100_storagePut.log"
		# task_name = "100_storagePut"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Put_100", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, "")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_101_storagePut(self):
		# log_path = "101_storagePut.log"
		# task_name = "101_storagePut"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Put_101", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_102_storagePut(self):
		# log_path = "102_storagePut.log"
		# task_name = "102_storagePut"
		try:
			self.test_init()
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Put_99", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_103_storagePut(self):
		# log_path = "103_storagePut.log"
		# task_name = "103_storagePut"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Put_99", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT_1, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_104_storagePut(self):
		# log_path = "104_storagePut.log"
		# task_name = "104_storagePut"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Put_99", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT_2, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_105_storagePut(self):
		# log_path = "105_storagePut.log"
		# task_name = "105_storagePut"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Put_99", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT_3, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_106_storagePut(self):
		# log_path = "106_storagePut.log"
		# task_name = "106_storagePut"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Put_99", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_INCORRECT_1, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_107_storagePut(self):
		# log_path = "107_storagePut.log"
		# task_name = "107_storagePut"
		try:
			(process, response) = test_api.invoke_storage_put(test_config.CONTRACT_ADDRESS)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_108_storagePut(self):
		# log_path = "108_storagePut.log"
		# task_name = "108_storagePut"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Put_99", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Put_99", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_109_storagePut(self):
		# log_path = "109_storagePut.log"
		# task_name = "109_storagePut"
		try:
			self.test_init()
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Put_99", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_110_storagePut(self):
		# log_path = "110_storagePut.log"
		# task_name = "110_storagePut"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Put_99", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_111_storagePut(self):
		# log_path = "111_storagePut.log"
		# task_name = "111_storagePut"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Put_99", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT_2)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_112_storagePut(self):
		# log_path = "112_storagePut.log"
		# task_name = "112_storagePut"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Put_99", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT_3)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_113_storagePut(self):
		# log_path = "113_storagePut.log"
		# task_name = "113_storagePut"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Put_99", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_INCORRECT_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_114_storageDelete(self):
		# log_path = "114_storageDelete.log"
		# task_name = "114_storageDelete"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Delete_114", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_115_storageDelete(self):
		# log_path = "115_storageDelete.log"
		# task_name = "115_storageDelete"
		try:
			self.test_init()
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Delete_115", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_116_storageDelete(self):
		# log_path = "116_storageDelete.log"
		# task_name = "116_storageDelete"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Delete_116", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_117_storageDelete(self):
		# log_path = "117_storageDelete.log"
		# task_name = "117_storageDelete"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Delete_114", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_118_storageDelete(self):
		# log_path = "118_storageDelete.log"
		# task_name = "118_storageDelete"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Delete_114", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT_3)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_119_storageDelete(self):
		# log_path = "119_storageDelete.log"
		# task_name = "119_storageDelete"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Delete_114", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_120_storageDelete(self):
		# log_path = "120_storageDelete.log"
		# task_name = "120_storageDelete"
		try:
			self.test_init()
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Delete_120", test_config.PARAM_TYPE_BYTEARRAY, "", test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_base_121_GetTime(self):
		# log_path = "121Get_time.log"
		# task_name = "121Get_time"
		try:
			(process, response) = test_api.invoke_func_with_0_param(test_config.CONTRACT_ADDRESS, "GetTime")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_123_checkWitness(self):
		# log_path = "123_checkWitness.log"
		# task_name = "123_checkWitness"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, "CheckWitness", test_config.PARAM_TYPE_BYTEARRAY, test_config.SCRIPT_HASH_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_124_checkWitness(self):
		# log_path = "124_checkWitness.log"
		# task_name = "124_checkWitness"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, "CheckWitness", test_config.PARAM_TYPE_BYTEARRAY, test_config.SCRIPT_HASH_INCORRECT_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_125_checkWitness(self):
		# log_path = "125_checkWitness.log"
		# task_name = "125_checkWitness"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, "CheckWitness", test_config.PARAM_TYPE_BYTEARRAY, test_config.SCRIPT_HASH_INCORRECT_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_126_checkWitness(self):
		# log_path = "126_checkWitness.log"
		# task_name = "126_checkWitness"
		try:
			self.test_init()
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, "CheckWitness", test_config.PARAM_TYPE_BYTEARRAY, "")
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_127_checkWitness(self):
		# log_path = "127_checkWitness.log"
		# task_name = "127_checkWitness"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, "CheckWitness", test_config.PARAM_TYPE_BYTEARRAY, test_config.PUBLICKEY)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_128_checkWitness(self):
		# log_path = "128_checkWitness.log"
		# task_name = "128_checkWitness"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, "CheckWitness", test_config.PARAM_TYPE_BYTEARRAY, test_config.PUBLICKEY1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_129_checkWitness(self):
		# log_path = "129_checkWitness.log"
		# task_name = "129_checkWitness"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, "CheckWitness", test_config.PARAM_TYPE_BYTEARRAY, "11" + test_config.PUBLICKEY)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_base_130_notify(self):
		# log_path = "130_notify.log"
		# task_name = "130_notify"
		try:
			self.test_init()
			(process, response) = test_api.invoke_func_with_0_param(test_config.CONTRACT_ADDRESS, "Notify_130")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_131_notify(self):
		# log_path = "131_notify.log"
		# task_name = "131_notify"
		try:
			(process, response) = test_api.invoke_func_with_0_param(test_config.CONTRACT_ADDRESS, "Notify_131")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_132_notify(self):
		# log_path = "132_notify.log"
		# task_name = "132_notify"
		try:
			(process, response) = test_api.invoke_func_with_0_param(test_config.CONTRACT_ADDRESS, "Notify_132")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_133_notify(self):
		# log_path = "133_notify.log"
		# task_name = "133_notify"
		try:
			(process, response) = test_api.invoke_func_with_0_param(test_config.CONTRACT_ADDRESS, "Notify_133")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_134_log(self):
		# log_path = "134_log.log"
		# task_name = "134_log"
		try:
			(process, response) = test_api.invoke_func_with_0_param(test_config.CONTRACT_ADDRESS, "Log_134")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_135_log(self):
		# log_path = "135_log.log"
		# task_name = "135_log"
		try:
			self.test_init()
			(process, response) = test_api.invoke_func_with_0_param(test_config.CONTRACT_ADDRESS, "Log_135")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_136_log(self):
		# log_path = "136_log.log"
		# task_name = "136_log"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, "Log_136", "string", test_config.VALUE_CORRECT_2)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_137_log(self):
		# log_path = "137_log.log"
		# task_name = "137_log"
		try:
			(process, response) = test_api.invoke_func_with_0_param(test_config.CONTRACT_ADDRESS, "Log_137")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_138_log(self):
		# log_path = "138_log.log"
		# task_name = "138_log"
		try:
			(process, response) = test_api.invoke_func_with_0_param(test_config.CONTRACT_ADDRESS, "Log_138")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_153_scriptContainer(self):
		# log_path = "153_script_container.log"
		# task_name = "153_script_container"
		try:
			self.test_init()
			(process, response) = test_api.invoke_func_with_0_param(test_config.CONTRACT_ADDRESS, "GetScriptContainer")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_155_ExecutingScriptHash(self):
		# log_path = "155_excuting_script.log"
		# task_name = "155_excuting_script"
		try:
			(process, response) = test_api.invoke_func_with_0_param(test_config.CONTRACT_ADDRESS, "GetExecutingScriptHash")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_157_callingScript(self):
		# log_path = "157_calling_script.log"
		# task_name = "157_calling_script"
		try:
			(process, response) = test_api.invoke_func_with_0_param(test_config.CONTRACT_ADDRESS, "GetCallingScriptHash")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_159_entryScriptHash(self):
		# log_path = "159_entry_scriptHash.log"
		# task_name = "159_entry_scriptHash"
		try:
			(process, response) = test_api.invoke_func_with_0_param(test_config.CONTRACT_ADDRESS, "GetEntryScriptHash")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_163_txType(self):
		# log_path = "163_tx_type.log"
		# task_name = "163_tx_type"
		try:
			self.test_init()
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, "GetTransaction_Type", test_config.PARAM_TYPE_BYTEARRAY, test_config.TX_HASH_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_166_getcontractMigrate(self):
		# log_path = "166getcontractMigrate.log"
		# task_name = "166getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, test_config.CONTRACT_MIGRATE_AVM, test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			self.ASSERT(process, "")
			API.node().wait_gen_block()
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_167_getcontractMigrate(self):
		# log_path = "167getcontractMigrate.log"
		# task_name = "167getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, test_config.CONTRACT_AVM, test_config.NAME_1, test_config.VERSION_2, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_168_getcontractMigrate(self):
		# log_path = "168getcontractMigrate.log"
		# task_name = "168getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, "134e3775b80e6865d36ff34da69d5f5363f8", test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
			API.node().wait_gen_block()
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_169_getcontractMigrate(self):
		# log_path = "169getcontractMigrate.log"
		# task_name = "169getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, "", test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_170_getcontractMigrate(self):
		# log_path = "170getcontractMigrate.log"
		# task_name = "170getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()

			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_171_getcontractMigrate(self):
		# log_path = "171getcontractMigrate.log"
		# task_name = "171getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_2, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_172_getcontractMigrate(self):
		# log_path = "172getcontractMigrate.log"
		# task_name = "172getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_3, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_173_getcontractMigrate(self):
		# log_path = "173getcontractMigrate.log"
		# task_name = "173getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_4, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_174_getcontractMigrate(self):
		# log_path = "174getcontractMigrate.log"
		# task_name = "174getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_5, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_175_getcontractMigrate(self):
		# log_path = "175getcontractMigrate.log"
		# task_name = "175getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_176_getcontractMigrate(self):
		# log_path = "176getcontractMigrate.log"
		# task_name = "176getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_2, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_177_getcontractMigrate(self):
		# log_path = "177getcontractMigrate.log"
		# task_name = "177getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_3, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_178_getcontractMigrate(self):
		# log_path = "178getcontractMigrate.log"
		# task_name = "178getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_4, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_179_getcontractMigrate(self):
		# log_path = "179getcontractMigrate.log"
		# task_name = "179getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_5, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_180_getcontractMigrate(self):
		# log_path = "180getcontractMigrate.log"
		# task_name = "180getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_181_getcontractMigrate(self):
		# log_path = "181getcontractMigrate.log"
		# task_name = "181getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_2, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_182_getcontractMigrate(self):
		# log_path = "182getcontractMigrate.log"
		# task_name = "182getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_3, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_183_getcontractMigrate(self):
		# log_path = "183getcontractMigrate.log"
		# task_name = "183getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_4, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_184_getcontractMigrate(self):
		# log_path = "184getcontractMigrate.log"
		# task_name = "184getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_5, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_185_getcontractMigrate(self):
		# log_path = "185getcontractMigrate.log"
		# task_name = "185getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_186_getcontractMigrate(self):
		# log_path = "186getcontractMigrate.log"
		# task_name = "186getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_2, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_187_getcontractMigrate(self):
		# log_path = "187getcontractMigrate.log"
		# task_name = "187getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_3, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_188_getcontractMigrate(self):
		# log_path = "188getcontractMigrate.log"
		# task_name = "188getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_4, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_189_getcontractMigrate(self):
		# log_path = "189getcontractMigrate.log"
		# task_name = "189getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_5, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_190_getcontractMigrate(self):
		# log_path = "190getcontractMigrate.log"
		# task_name = "190getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_1, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_191_getcontractMigrate(self):
		# log_path = "191getcontractMigrate.log"
		# task_name = "191getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_2, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_192_getcontractMigrate(self):
		# log_path = "192getcontractMigrate.log"
		# task_name = "192getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_3, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_193_getcontractMigrate(self):
		# log_path = "193getcontractMigrate.log"
		# task_name = "193getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_4, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_194_getcontractMigrate(self):
		# log_path = "194getcontractMigrate.log"
		# task_name = "194getcontractMigrate"
		try:
			API.contract().deploy_contract_full(test_config.deploy_neo)
			API.node().wait_gen_block()
			test_config.init()
			(process, response) = test_api.invoke_contract_migrate(test_config.CONTRACT_ADDRESS, ByteToHex(bytes(self._testMethodName, encoding = "utf8")), test_config.NAME_1, test_config.VERSION_1, test_config.AUTHOR_1, test_config.EMAIL_1, test_config.DESC_5, sleep = 0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_195_checkWitness(self):
		# log_path = "195_checkWitness.log"
		# task_name = "195_checkWitness"
		try:
			self.test_init()
			
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, "CheckWitness", test_config.PARAM_TYPE_BYTEARRAY, "1111"+test_config.PUBLICKEY)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])


class test_neo_api_2(ParametrizedTestCase):

	def tearDown(self):
		logger.close(self.result())
		pass
	
	def setUp(self):
		logger.open("test_neo_api/" + self._testMethodName+".log",self._testMethodName)
		time.sleep(2)
		print("stop all")
		API.node().stop_all_nodes()
		print("start all")
		API.node().start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
		
		test_config.init()

		time.sleep(10)

	def test_base_088_storageContext(self):
		# log_path = "88_storage_context.log"
		# task_name = "88_storage_context"
		try:
			(process, response) = test_api.invoke_func_with_1_param(test_config.CONTRACT_ADDRESS, "GetStorageContext", test_config.PARAM_TYPE_BYTEARRAY, test_config.SCRIPT_HASH_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_090_currentContext(self):
		# log_path = "90_current_context.log"
		# task_name = "90_current_context"
		try:
			(process, response) = test_api.invoke_func_with_0_param(test_config.CONTRACT_ADDRESS, "GetCurrentContext")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_092_storageGet(self):
		# log_path = "92_storageGet.log"
		# task_name = "92_storageGet"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Get_92", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
			
	def test_normal_95_storageGet(self):
		# log_path = "95_storageGet.log"
		# task_name = "95_storageGet"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Get_92", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_097_storageGet(self):
		# log_path = "97_storageGet.log"
		# task_name = "97_storageGet"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Get_92", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_INCORRECT_1, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_base_099_storagePut(self):
		# log_path = "99_storagePut.log"
		# task_name = "99_storagePut"
		try:
			(process, response) = test_api.invoke_func_with_2_param(test_config.CONTRACT_ADDRESS, "Put_99", test_config.PARAM_TYPE_BYTEARRAY, test_config.KEY_CORRECT, test_config.PARAM_TYPE_BYTEARRAY, test_config.VALUE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

####################################################
if __name__ == '__main__':
	suite = unittest.main()
