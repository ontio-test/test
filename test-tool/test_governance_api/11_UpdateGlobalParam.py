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
from utils.commonapi import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from test_api import *
from test_common import *
#from test_conf import Conf

logger = LoggerInstance



##########################################################
# params
param0_1 = "101010000000" #141
param0_2 = "2147483648" #2147483648
param0_3 = "2147483649" #2147483649
param0_4 = "0" #0
param0_5 = "-1" #-1

param1_1 = "101" #141
param1_2 = "2147483648" #2147483648
param1_3 = "2147483649" #2147483649
param1_4 = "0" #0
param1_5 = "-1" #-1

param2_1 = "28" #共识节点上限数量*4
param2_2 = "29" #大于共识节点上限数量*4的值
param2_3 = "27" #小于共识节点上限数量*4的值
param2_4 = "0" #0
param2_5 = "-1" #-1

param3_1 = "1" #1
param3_2 = "10" #10
param3_3 = "2147483648" #2147483648
param3_4 = "2147483649" #2147483649
param3_5 = "0" #0
param3_6 = "-1" #-1

param4_1 = "50" #50
param4_2 = "0" #0
param4_3 = "100" #141
param4_4 = "0" #0
param4_5 = "99" #140
param4_6 = "-1" #-1

param5_1 = "50" #50
param5_2 = "100" #141
param5_3 = "0" #0
param5_4 = "99" #140
param5_5 = "0" #2
param5_6 = "101" #142

param6_1 = "10" #141
param6_2 = "214713536135" #214713536135
param6_3 = "214713536136" #214713536136
param6_4 = "0" #0
param6_5 = "-1" #-1

param7_1 = "10" #141
param7_2 = "5" #5
param7_3 = "0" #0
param7_4 = "-1" #-1
####################################################

# test cases
class TestupdateGlobalParam(ParametrizedTestCase):
	def test_135_updateGlobalParam(self):
		logger.open("135_updateGlobalParam.log", "135_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)

	def test_136_updateGlobalParam(self):
		logger.open("136_updateGlobalParam.log", "136_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_2,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	
	def test_137_updateGlobalParam(self):
		logger.open("137_updateGlobalParam.log", "137_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_3,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	def test_138_updateGlobalParam(self):
		logger.open("138_updateGlobalParam.log", "138_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_4,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	
	def test_139_updateGlobalParam(self):
		logger.open("139_updateGlobalParam.log", "139_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_5,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	
	def test_140_updateGlobalParam(self):
		logger.open("140_updateGlobalParam.log", "140_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)

	def test_141_updateGlobalParam(self):
		logger.open("141_updateGlobalParam.log", "141_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_2,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)

	def test_142_updateGlobalParam(self):
		logger.open("142_updateGlobalParam.log", "142_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_3,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)

	def test_143_updateGlobalParam(self):
		logger.open("143_updateGlobalParam.log", "143_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_4,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)

	def test_144_updateGlobalParam(self):
		logger.open("144_updateGlobalParam.log", "144_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_5,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	
	def test_145_updateGlobalParam(self):
		logger.open("145_updateGlobalParam.log", "145_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	
	def test_146_updateGlobalParam(self):
		logger.open("146_updateGlobalParam.log", "146_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_2,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	
	def test_147_updateGlobalParam(self):
		logger.open("147_updateGlobalParam.log", "147_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_3,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	
	def test_148_updateGlobalParam(self):
		logger.open("148_updateGlobalParam.log", "148_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_4,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	
	def test_149_updateGlobalParam(self):
		logger.open("149_updateGlobalParam.log", "149_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_5,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	
	def test_150_updateGlobalParam(self):
		logger.open("150_updateGlobalParam.log", "150_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	
	def test_151_updateGlobalParam(self):
		logger.open("151_updateGlobalParam.log", "151_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_2,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	
	def test_152_updateGlobalParam(self):
		logger.open("152_updateGlobalParam.log", "152_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_3,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	
	def test_153_updateGlobalParam(self):
		logger.open("153_updateGlobalParam.log", "153_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_4,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	
	def test_154_updateGlobalParam(self):
		logger.open("154_updateGlobalParam.log", "154_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_5,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	
	def test_155_updateGlobalParam(self):
		logger.open("155_updateGlobalParam.log", "155_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_6,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	
	def test_156_updateGlobalParam(self):
		logger.open("156_updateGlobalParam.log", "156_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	
	def test_157_updateGlobalParam(self):
		logger.open("157_updateGlobalParam.log", "157_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_2,param5_2,param6_1,param7_1)
		logger.close(result)
	
	def test_158_updateGlobalParam(self):
		logger.open("158_updateGlobalParam.log", "158_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_3,param5_3,param6_1,param7_1)
		logger.close(result)
	
	def test_159_updateGlobalParam(self):
		logger.open("159_updateGlobalParam.log", "159_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_4,param5_4,param6_1,param7_1)
		logger.close(result)
	
	def test_160_updateGlobalParam(self):
		logger.open("160_updateGlobalParam.log", "160_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_5,param5_5,param6_1,param7_1)
		logger.close(result)
	
	def test_161_updateGlobalParam(self):
		logger.open("161_updateGlobalParam.log", "161_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_6,param5_6,param6_1,param7_1)
		logger.close(result)
	
	def test_162_updateGlobalParam(self):
		logger.open("162_updateGlobalParam.log", "162_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)
	
	def test_163_updateGlobalParam(self):
		logger.open("163_updateGlobalParam.log", "163_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_2,param7_1)
		logger.close(result)
	def test_164_updateGlobalParam(self):
		logger.open("164_updateGlobalParam.log", "164_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_3,param7_1)
		logger.close(result)

	def test_165_updateGlobalParam(self):
		logger.open("165_updateGlobalParam.log", "165_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_4,param7_1)
		logger.close(result)

	def test_166_updateGlobalParam(self):
		logger.open("166_updateGlobalParam.log", "166_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_5,param7_1)
		logger.close(result)

	def test_167_updateGlobalParam(self): 
		logger.open("167_updateGlobalParam.log", "167_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)
		logger.close(result)

	def test_168_updateGlobalParam(self):
		logger.open("168_updateGlobalParam.log", "168_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_2)
		logger.close(result)

	def test_169_updateGlobalParam(self):
		logger.open("169_updateGlobalParam.log", "169_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_2,param7_3)
		logger.close(result)

	def test_170_updateGlobalParam(self):
		logger.open("170_updateGlobalParam.log", "170_updateGlobalParam")
		(result, response) = invoke_function_update("updateGlobalParam",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_3,param7_4)
		logger.close(result)
	
####################################################
if __name__ == '__main__':
	unittest.main()