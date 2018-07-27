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
param0_1 = "8" #目前节点数量的值
param0_2 = "7" #小于目前节点数量的值
param0_3 = "9" #大于目前节点数量的值
param0_4 = "2147943694" #2147943694
param0_5 = "2147943695" #2147943695
param0_6 = "-1" #-1
param1_1 = "2" #目前节点数量的值/3
param1_2 = "1" #小于目前节点数量/3的值
param1_3 = "3" #大于目前节点数量/3的值
param1_4 = "0" #0
param1_5 = "-1" #-1
param2_1 = "7" #7
param2_2 = "6" #小于目前共识节点数量的值
param2_3 = "9" #大于目前共识节点数量的值
param2_4 = "7" #等于目前共识节点数量
param3_1 = "112" #目前共识节点数量*16的值
param3_2 = "111" #小于目前共识节点数量*16的值
param3_3 = "113" #大于目前共识节点数量*16的值
param3_4 = "2147943694" #2147943694
param3_5 = "2147943695" #2147943695
param3_6 = "-1" #-1
param4_1 = "5033" #100
param4_2 = "2147943694" #2147943694
param4_3 = "2147943695" #2147943695
param4_4 = "0" #0
param4_5 = "-1" #-1
param5_1 = "5000" #100
param5_2 = "2147943694" #2147943694
param5_3 = "2147943695" #2147943695
param5_4 = "0" #0
param5_5 = "-1" #-1
param6_1 = "100" #100
param6_2 = "2147943694" #2147943694
param6_3 = "2147943695" #2147943695
param6_4 = "0" #0
param6_5 = "-1" #-1
param7_1 = "100" #100
param7_2 = "2147943694" #2147943694
param7_2 = "2147943694" #2147943694
param7_3 = "2147943695" #2147943695
param7_4 = "0" #0
param7_5 = "-1" #-1
####################################################

# test cases
class TestupdateConfig(ParametrizedTestCase):
    def test_94_updateConfig(self):
        logger.open("94_updateConfig.log", "94_updateConfig")

        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)
		

        logger.close(result)

    def test_95_updateConfig(self):
        logger.open("95_updateConfig.log", "95_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_2,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_96_updateConfig(self):
        logger.open("96_updateConfig.log", "96_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_3,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    def test_97_updateConfig(self):
        logger.open("97_updateConfig.log", "97_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_4,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_98_updateConfig(self):
        logger.open("98_updateConfig.log", "98_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_5,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_99_updateConfig(self):
        logger.open("99_updateConfig.log", "99_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_6,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)

    def test_100_updateConfig(self):
        logger.open("100_updateConfig.log", "100_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)

    def test_101_updateConfig(self):
        logger.open("101_updateConfig.log", "101_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_2,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)

    def test_102_updateConfig(self):
        logger.open("102_updateConfig.log", "102_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_3,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)

    def test_103_updateConfig(self):
        logger.open("103_updateConfig.log", "103_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_4,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_104_updateConfig(self):
        logger.open("104_updateConfig.log", "104_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_5,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_105_updateConfig(self):
        logger.open("105_updateConfig.log", "105_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_106_updateConfig(self):
        logger.open("106_updateConfig.log", "106_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_2,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_107_updateConfig(self):
        logger.open("107_updateConfig.log", "107_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_3,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_108_updateConfig(self):
        logger.open("108_updateConfig.log", "108_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_4,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_109_updateConfig(self):
        logger.open("109_updateConfig.log", "109_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_110_updateConfig(self):
        logger.open("110_updateConfig.log", "110_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_2,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_111_updateConfig(self):
        logger.open("111_updateConfig.log", "111_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_3,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_112_updateConfig(self):
        logger.open("112_updateConfig.log", "112_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_4,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_113_updateConfig(self):
        logger.open("113_updateConfig.log", "113_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_5,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_114_updateConfig(self):
        logger.open("114_updateConfig.log", "114_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_6,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_115_updateConfig(self):
        logger.open("115_updateConfig.log", "115_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_116_updateConfig(self):
        logger.open("116_updateConfig.log", "116_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_2,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_117_updateConfig(self):
        logger.open("117_updateConfig.log", "117_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_3,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_118_updateConfig(self):
        logger.open("118_updateConfig.log", "118_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_4,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_119_updateConfig(self):
        logger.open("119_updateConfig.log", "119_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_5,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_120_updateConfig(self):
        logger.open("120_updateConfig.log", "120_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)
    
    def test_121_updateConfig(self):
        logger.open("121_updateConfig.log", "121_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_2,param6_1,param7_1)


        logger.close(result)
    
    def test_122_updateConfig(self):
        logger.open("122_updateConfig.log", "122_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_3,param6_1,param7_1)


        logger.close(result)
    def test_123_updateConfig(self):
        logger.open("123_updateConfig.log", "123_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_4,param6_1,param7_1)


        logger.close(result)

    def test_124_updateConfig(self):
        logger.open("124_updateConfig.log", "124_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_5,param6_1,param7_1)


        logger.close(result)

    def test_125_updateConfig(self):
        logger.open("125_updateConfig.log", "125_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)

    def test_126_updateConfig(self):
        logger.open("126_updateConfig.log", "126_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_2,param7_1)


        logger.close(result)

    def test_127_updateConfig(self):
        logger.open("127_updateConfig.log", "127_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_3,param7_1)


        logger.close(result)

    def test_128_updateConfig(self):
        logger.open("128_updateConfig.log", "128_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_4,param7_1)


        logger.close(result)

    def test_129_updateConfig(self):
        logger.open("129_updateConfig.log", "129_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_5,param7_1)


        logger.close(result)

    def test_130_updateConfig(self):
        logger.open("130_updateConfig.log", "130_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_1)


        logger.close(result)

    def test_131_updateConfig(self):
        logger.open("131_updateConfig.log", "131_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_2)


        logger.close(result)

    def test_132_updateConfig(self):
        logger.open("132_updateConfig.log", "132_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_3)


        logger.close(result)
    
    def test_133_updateConfig(self):
        logger.open("133_updateConfig.log", "133_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_4)


        logger.close(result)

    def test_134_updateConfig(self):
        logger.open("134_updateConfig.log", "134_updateConfig")
        (result, response) = invoke_function_update("updateConfig",param0_1,param1_1,param2_1,param3_1,param4_1,param5_1,param6_1,param7_5)


        logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()