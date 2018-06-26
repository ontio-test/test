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
from test_conf import Conf

logger = LoggerInstance

##########################################################
# params
pubKey_1 = "02b59d88bc4b2f5814b691d32e736bcd7ad018794f041235092f6954e23198cbcf" #未加入节点网络的节点公钥
pubKey_2 = "03e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dc" #已加入节点网络的节点公钥
pubKey_3 = "1234abcd" #乱码
pubKey_4 = "" #留空
walletAddress_1 = "AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN" #节点对应的钱包地址
walletAddress_2 = "AK7wzmkdgjKxbXAJBiaW91YhUokTu9pa5X" #其他已经加入节点网络的节点的钱包地址
walletAddress_3 = "1234abcd" #乱码
walletAddress_4 = "" #留空
ontCount_1 = "100" #钱包里存在的所有ONT值
ontCount_2 = "100" #钱包里存在的所有ONT值
ontCount_3 = "0" #0
ontCount_4 = "" #留空
ontID_1 = "6469643a6f6e743a4162657978714c706d33475a44564a645250363272614d66436d48787344664b444e" #有授权的ontid
ontID_2 = "6469643a6f6e743a414b37777a6d6b64676a4b786258414a4269615739315968556f6b54753970613558" #没有授权的ontid
ontID_3 = "123456abcd" #乱码
ontID_4 = "" #留空
user_1 = "1" #正常的公钥序号
user_2 = "100" #不存在的公钥序号
user_3 = "" #留空
####################################################

# test cases
class TestregisterCandidate(ParametrizedTestCase):
    def test_01_registerCandidate(self):
        logger.open("01_registerCandidate.log", "01_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_02_registerCandidate(self):
        logger.open("02_registerCandidate.log", "02_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_2,walletAddress_1,ontCount_1,ontID_1,user_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_03_registerCandidate(self):
        logger.open("03_registerCandidate.log", "03_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_3,walletAddress_1,ontCount_1,ontID_1,user_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    def test_04_registerCandidate(self):
        logger.open("04_registerCandidate.log", "04_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_4,walletAddress_1,ontCount_1,ontID_1,user_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_05_registerCandidate(self):
        logger.open("05_registerCandidate.log", "05_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_06_registerCandidate(self):
        logger.open("06_registerCandidate.log", "06_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_2,ontCount_1,ontID_1,user_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_07_registerCandidate(self):
        logger.open("07_registerCandidate.log", "07_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_3,ontCount_1,ontID_1,user_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_08_registerCandidate(self):
        logger.open("08_registerCandidate.log", "08_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_4,ontCount_1,ontID_1,user_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_09_registerCandidate(self):
        logger.open("09_registerCandidate.log", "09_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_10_registerCandidate(self):
        logger.open("10_registerCandidate.log", "10_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_2,ontID_1,user_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_11_registerCandidate(self):
        logger.open("11_registerCandidate.log", "11_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_3,ontID_1,user_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_12_registerCandidate(self):
        logger.open("12_registerCandidate.log", "12_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_4,ontID_1,user_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_13_registerCandidate(self):
        logger.open("13_registerCandidate.log", "13_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_14_registerCandidate(self):
        logger.open("14_registerCandidate.log", "14_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_2,user_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_15_registerCandidate(self):
        logger.open("15_registerCandidate.log", "15_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_3,user_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_16_registerCandidate(self):
        logger.open("16_registerCandidate.log", "16_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_4,user_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_17_registerCandidate(self):
        logger.open("17_registerCandidate.log", "17_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_18_registerCandidate(self):
        logger.open("18_registerCandidate.log", "18_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_2)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_19_registerCandidate(self):
        logger.open("19_registerCandidate.log", "19_registerCandidate")
        (result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_3)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()