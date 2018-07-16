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

from utils.commonapi import *
from utils.rpcapi import RPCApi
from utils.init_ong_ont import *
from utils.contractapi import *
from test_governance_api.test_api import nodeCountCheck
logger = LoggerInstance

class Test(ParametrizedTestCase):
	@classmethod
	def setUpClass(cls):
		cls.m_contract_address= deploy_contract_full("tasks/A.neo", "test", "test name")[0]
		time.sleep(5)
		pass
	
	def test_01(self):
		result = False
		logger.open("test_01.log", "test_01")
		(result, response) = invoke_function(self.m_contract_address, "int_to_int", "", argvs = [{"type": "int","value": "0"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		
	def test_02(self):
		result = False
		logger.open("test_02.log", "test_02")
		(result, response) = invoke_function(self.m_contract_address, "int_to_int", "", argvs = [{"type": "int","value": "-1"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		# logger.close(not result or response["result"]["Result"] != '01')
	
	def test_03(self):
		result = False
		logger.open("test_03.log", "test_03")
		(result, response) = invoke_function(self.m_contract_address, "int_to_int", "", argvs = [{"type": "int","value": "65535"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		
	def test_04(self):
		result = False
		logger.open("test_04.log", "test_04")
		(result, response) = invoke_function(self.m_contract_address, "int_to_int", "", argvs = [{"type": "int","value": "65536"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		#logger.close(not result or response["result"]["Result"] != '01')
		
	def test_05(self):
		result = False
		logger.open("test_05.log", "test_05")
		(result, response) = invoke_function(self.m_contract_address, "int_to_int", "", argvs = [{"type": "string","value": "abc"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		# logger.close(not result or response["result"]["Result"] != '01')		
	
	def test_06(self):
		result = False
		logger.open("test_06.log", "test_06")
		(result, response) = invoke_function(self.m_contract_address, "int_to_int", "", argvs = [{"type": "string","value": ""}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		#logger.close(not result or response["result"]["Result"] != '01')	

	def test_07(self):
		result = False
		logger.open("test_07.log", "test_07")
		(result, response) = invoke_function(self.m_contract_address, "int_to_int", "", argvs = [{"type": "bytearray","value": "111122223333"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		#logger.close(not result or response["result"]["Result"] != '01')	

	def test_08(self):
		result = False
		logger.open("test_08.log", "test_08")
		(result, response) = invoke_function(self.m_contract_address, "int_to_int", "", argvs = [{"type": "bool","value": "true"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		#logger.close(not result or response["result"]["Result"] != '01')	

	def test_09(self):
		result = False
		logger.open("test_09.log", "test_09")
		(result, response) = invoke_function(self.m_contract_address, "int_to_int", "", argvs = [{"type": "bool","value": "false"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		#logger.close(not result or response["result"]["Result"] != '01')	
	
	#string to int
	def test_10(self):
		result = False
		logger.open("test_10.log", "test_10")
		(result, response) = invoke_function(self.m_contract_address, "string_to_int", "", argvs = [{"type": "string","value": "qwertyuiop"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')	

	def test_11(self):
		result = False
		logger.open("test_11.log", "test_11")
		(result, response) = invoke_function(self.m_contract_address, "string_to_int", "", argvs = [{"type": "string","value": "~!@@#$$%^&*()_+-={}|:\"<>?;'[] \\,./"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')	

	def test_12(self):
		result = False
		logger.open("test_12.log", "test_12")
		(result, response) = invoke_function(self.m_contract_address, "string_to_int", "", argvs = [{"type": "string","value": "abcd1234_))()*(&^$^%#"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
	
	def test_13(self):
		result = False
		logger.open("test_13.log", "test_13")
		(result, response) = invoke_function(self.m_contract_address, "string_to_int", "", argvs = [{"type": "int","value": "123"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		# logger.close(not result or response["result"]["Result"] != '01')

	def test_14(self):
		result = False
		logger.open("test_14.log", "test_14")
		(result, response) = invoke_function(self.m_contract_address, "string_to_int", "", argvs = [{"type": "bytearray","value": "111122223333"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		#logger.close(not result or response["result"]["Result"] != '01')

	def test_15(self):
		result = False
		logger.open("test_15.log", "test_15")
		(result, response) = invoke_function(self.m_contract_address, "string_to_int", "", argvs = [{"type": "bool","value": "true"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		# logger.close(not result or response["result"]["Result"] != '01')		

	def test_16(self):
		result = False
		logger.open("test_16.log", "test_16")
		(result, response) = invoke_function(self.m_contract_address, "string_to_int", "", argvs = [{"type": "bool","value": "false"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		# logger.close(not result or response["result"]["Result"] != '01')		

	def test_24(self):
		result = False
		logger.open("test_24.log", "test_24")
		(result, response) = invoke_function(self.m_contract_address, "bool_to_int", "", argvs = [{"type": "bool","value": "true"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')				

	def test_25(self):
		result = False
		logger.open("test_25.log", "test_25")
		(result, response) = invoke_function(self.m_contract_address, "bool_to_int", "", argvs = [{"type": "int","value": "0"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')				
	
	def test_26(self):
		result = False
		logger.open("test_26.log", "test_26")
		(result, response) = invoke_function(self.m_contract_address, "bool_to_int", "", argvs = [{"type": "bool","value": "false"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')	
		
	def test_27(self):
		result = False
		logger.open("test_27.log", "test_27")
		(result, response) = invoke_function(self.m_contract_address, "bool_to_int", "", argvs = [{"type": "int","value": "1"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		# logger.close(not result or response["result"]["Result"] != '01')
		
	def test_28(self):
		result = False
		logger.open("test_28.log", "test_28")
		(result, response) = invoke_function(self.m_contract_address, "bool_to_int", "", argvs = [{"type": "string","value": "abc"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		# logger.close(not result or response["result"]["Result"] != '01')
	
	def test_29(self):
		result = False
		logger.open("test_29.log", "test_29")
		(result, response) = invoke_function(self.m_contract_address, "bool_to_int", "", argvs = [{"type": "string","value": ""}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		# logger.close(not result or response["result"]["Result"] != '01')
	
	def test_30(self):
		result = False
		logger.open("test_30.log", "test_30")
		(result, response) = invoke_function(self.m_contract_address, "bool_to_int", "", argvs = [{"type": "bytearray","value": "111122223333"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		# logger.close(not result or response["result"]["Result"] != '01')

	def test_31(self):
		result = False
		logger.open("test_31.log", "test_31")
		(result, response) = invoke_function(self.m_contract_address, "byte_to_int", "", argvs = [{"type": "bytearray","value": "1234567890abcdef"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		
	def test_32(self):
		result = False
		logger.open("test_32.log", "test_32")
		(result, response) = invoke_function(self.m_contract_address, "byte_to_int", "", argvs = [{"type": "bytearray","value": ""}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		# logger.close(not result or response["result"]["Result"] != '01')
	
	def test_33(self):
		result = False
		logger.open("test_33.log", "test_33")
		(result, response) = invoke_function(self.m_contract_address, "byte_to_int", "", argvs = [{"type": "int","value": "123"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		# logger.close(not result or response["result"]["Result"] != '01')
		
	def test_34(self):
		result = False
		logger.open("test_34.log", "test_34")
		(result, response) = invoke_function(self.m_contract_address, "byte_to_int", "", argvs = [{"type": "string","value": "zxcvbnm!@"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		# logger.close(not result or response["result"]["Result"] != '01')

	def test_35(self):
		result = False
		logger.open("test_35.log", "test_35")
		(result, response) = invoke_function(self.m_contract_address, "byte_to_int", "", argvs = [{"type": "bool","value": "true"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		# logger.close(not result or response["result"]["Result"] != '01')
		
	def test_36(self):
		result = False
		logger.open("test_36.log", "test_36")
		(result, response) = invoke_function(self.m_contract_address, "byte_to_int", "", argvs = [{"type": "bool","value": "false"}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		# logger.close(not result or response["result"]["Result"] != '01')
		
	def test_37(self):
		result = False
		logger.open("test_37.log", "test_37")
		(result, response) = invoke_function(self.m_contract_address, "test_37", "", argvs = [{"type": "string","value": ""}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '00')
		
	def test_38(self):
		result = False
		logger.open("test_38.log", "test_38")
		(result, response) = invoke_function(self.m_contract_address, "test_38", "", argvs = [{"type": "string","value": ""}], node_index = 0)
		logger.close(result and response["result"]["Result"] == 'ff')		
	
	def test_39(self):
		result = False
		logger.open("test_39.log", "test_39")
		(result, response) = invoke_function(self.m_contract_address, "test_39", "", argvs = [{"type": "string","value": ""}], node_index = 0)
		logger.close(result and response["result"]["Result"] == 'ffff00')	
	
	def test_46(self):
		result = False
		logger.open("test_46.log", "test_46")
		(result, response) = invoke_function(self.m_contract_address, "test_46", "", argvs = [{"type": "string","value": ""}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '71776572747975696f70')	
	
	def test_47(self):
		result = False
		logger.open("test_47.log", "test_47")
		(result, response) = invoke_function(self.m_contract_address, "test_47", "", argvs = [{"type": "string","value": ""}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '7e214040232424255e262a28295f2b2d3d7b7d7c3a223c3e3f3b275b5d205c2c2e2f')	
	
	def test_48(self):
		result = False
		logger.open("test_48.log", "test_48")
		(result, response) = invoke_function(self.m_contract_address, "test_48", "", argvs = [{"type": "string","value": ""}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '61626364313233345f292928292a28265e245e2523')	
	
	def test_60(self):
		result = False
		logger.open("test_60.log", "test_60")
		(result, response) = invoke_function(self.m_contract_address, "test_60", "", argvs = [{"type": "string","value": ""}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '01')
		
	def test_62(self):
		result = False
		logger.open("test_62.log", "test_62")
		(result, response) = invoke_function(self.m_contract_address, "test_62", "", argvs = [{"type": "string","value": ""}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '00')	
		
	def test_67(self):
		result = False
		logger.open("test_67.log", "test_67")
		(result, response) = invoke_function(self.m_contract_address, "test_67", "", argvs = [{"type": "string","value": ""}], node_index = 0)
		logger.close(result and response["result"]["Result"] == '1234567890abcdef')	
if __name__ == '__main__':
	unittest.main()