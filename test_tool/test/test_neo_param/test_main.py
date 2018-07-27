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

import utils.connect
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger 
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase

from api.apimanager import API
# from utils.api.commonapi import *
# from utils.api.rpcapi import RPCApi
# from utils.api.init_ong_ont import *
# from utils.api.contractapi import *
# from test_governance_api.test_api import nodeCountCheck

from test_neo_param.test_config import test_config

class test_neo_param_1(ParametrizedTestCase):
	def test_init(self):
		test_config.m_contract_address= API.contract().deploy_contract(test_config.deploy_neo, test_config.name, test_config.desc)[0]
		API.node().wait_gen_block()
		time.sleep(5)
		
	def setUp(self):
		logger.open("test_neo_param/" + self._testMethodName+".log",self._testMethodName)
		
	def tearDown(self):
		logger.close(self.result())
	
	def test_base_001_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "int_to_int", "", argvs = [{"type": "int","value": "0"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_abnormal_002_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "int_to_int", "", argvs = [{"type": "int","value": "-1"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
	
	def test_normal_003_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "int_to_int", "", argvs = [{"type": "int","value": "65535"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_abnormal_004_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "int_to_int", "", argvs = [{"type": "int","value": "65536"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
		
	def test_abnormal_005_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "int_to_int", "", argvs = [{"type": "string","value": "abc"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
	
	def test_abnormal_006_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "int_to_int", "", argvs = [{"type": "string","value": ""}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		

	def test_abnormal_007_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "int_to_int", "", argvs = [{"type": "bytearray","value": "111122223333"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		

	def test_abnormal_008_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "int_to_int", "", argvs = [{"type": "bool","value": "true"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		

	def test_abnormal_009_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "int_to_int", "", argvs = [{"type": "bool","value": "false"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
	
	#string to int
	def test_normal_010_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "string_to_int", "", argvs = [{"type": "string","value": "qwertyuiop"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_011_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "string_to_int", "", argvs = [{"type": "string","value": "~!@@#$$%^&*()_+-={}|:\"<>?;'[] \\,./"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_012_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "string_to_int", "", argvs = [{"type": "string","value": "abcd1234_))()*(&^$^%#"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_013_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "string_to_int", "", argvs = [{"type": "int","value": "123"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		

	def test_abnormal_014_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "string_to_int", "", argvs = [{"type": "bytearray","value": "111122223333"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
	

	def test_abnormal_015_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "string_to_int", "", argvs = [{"type": "bool","value": "true"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		

	def test_abnormal_016_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "string_to_int", "", argvs = [{"type": "bool","value": "false"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		

	def test_normal_024_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "bool_to_int", "", argvs = [{"type": "bool","value": "true"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_025_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "bool_to_int", "", argvs = [{"type": "int","value": "0"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_026_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "bool_to_int", "", argvs = [{"type": "bool","value": "false"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_abnormal_027_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "bool_to_int", "", argvs = [{"type": "int","value": "1"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
		
	def test_abnormal_028_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "bool_to_int", "", argvs = [{"type": "string","value": "abc"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
	
	def test_abnormal_029_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "bool_to_int", "", argvs = [{"type": "string","value": ""}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
	
	def test_abnormal_030_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "bool_to_int", "", argvs = [{"type": "bytearray","value": "111122223333"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		

	def test_normal_031_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "byte_to_int", "", argvs = [{"type": "bytearray","value": "1234567890abcdef"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_abnormal_032_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "byte_to_int", "", argvs = [{"type": "bytearray","value": ""}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
	
	def test_abnormal_033_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "byte_to_int", "", argvs = [{"type": "int","value": "123"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
		
	def test_abnormal_034_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "byte_to_int", "", argvs = [{"type": "string","value": "zxcvbnm!@"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		

	def test_abnormal_035_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "byte_to_int", "", argvs = [{"type": "bool","value": "true"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
		
	def test_abnormal_036_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "byte_to_int", "", argvs = [{"type": "bool","value": "false"}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
		
	def test_normal_037_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "test_37", "", argvs = [{"type": "string","value": ""}], node_index = 0)
			rs = response["result"]["Result"] == '00'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_abnormal_038_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "test_38", "", argvs = [{"type": "string","value": ""}], node_index = 0)
			rs = response["result"]["Result"] == 'ff'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_039_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "test_39", "", argvs = [{"type": "string","value": ""}], node_index = 0)
			rs = response["result"]["Result"] == 'ffff00'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_046_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "test_46", "", argvs = [{"type": "string","value": ""}], node_index = 0)
			rs = response["result"]["Result"] == '71776572747975696f70'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_047_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "test_47", "", argvs = [{"type": "string","value": ""}], node_index = 0)
			rs = response["result"]["Result"] == '7e214040232424255e262a28295f2b2d3d7b7d7c3a223c3e3f3b275b5d205c2c2e2f'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_048_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "test_48", "", argvs = [{"type": "string","value": ""}], node_index = 0)
			rs = response["result"]["Result"] == '61626364313233345f292928292a28265e245e2523'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_060_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "test_60", "", argvs = [{"type": "string","value": ""}], node_index = 0)
			rs = response["result"]["Result"] == '01'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_normal_062_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "test_62", "", argvs = [{"type": "string","value": ""}], node_index = 0)
			rs = response["result"]["Result"] == '00'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_normal_067_invokeFunction(self):
		process = False
		try:
			(process, response) = API.contract().invoke_function(test_config.m_contract_address, "test_67", "", argvs = [{"type": "string","value": ""}], node_index = 0)
			rs = response["result"]["Result"] == '1234567890abcdef'
			self.ASSERT(process and rs, "")
		except Exception as e:
			logger.print(e.args[0])
if __name__ == '__main__':
	unittest.main()