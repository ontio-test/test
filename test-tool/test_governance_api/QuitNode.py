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
pubKey_1 = "02b59d88bc4b2f5814b691d32e736bcd7ad018794f041235092f6954e23198cbcf" #已经在网络中的共识节点公钥
pubKey_2 = "03e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dc" #已经在网络中的候选节点公钥
pubKey_3 = "03e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dc" #未申请的节点公钥
pubKey_4 = "03e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dc" #已经申请的节点公钥
pubKey_5 = "123abcd" #已经进入黑名单的节点公钥
pubKey_6 = "" #乱码
pubKey_7 = "" #留空
walletAddress = "AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN" #钱包地址
##########################################################

# test cases
class TestquitNode(ParametrizedTestCase):
    def test_41_quitNode(self):
        logger.open("41_quitNode.log", "41_quitNode")
        (result, response) = invoke_function_quitNode("quitNode",pubKey_1,walletAddress)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_42_quitNode(self):
        logger.open("42_quitNode.log", "42_quitNode")
        (result, response) = invoke_function_quitNode("quitNode",pubKey_2,walletAddress)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_43_quitNode(self):
        logger.open("43_quitNode.log", "43_quitNode")
        (result, response) = invoke_function_quitNode("quitNode",pubKey_3,walletAddress)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    def test_44_quitNode(self):
        logger.open("44_quitNode.log", "44_quitNode")
        (result, response) = invoke_function_quitNode("quitNode",pubKey_4,walletAddress)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_45_quitNode(self):
        logger.open("45_quitNode.log", "45_quitNode")
        (result, response) = invoke_function_quitNode("quitNode",pubKey_5,walletAddress)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_46_quitNode(self):
        logger.open("46_quitNode.log", "46_quitNode")
        (result, response) = invoke_function_quitNode("quitNode",pubKey_6,walletAddress)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_47_quitNode(self):
        logger.open("47_quitNode.log", "47_quitNode")
        (result, response) = invoke_function_quitNode("quitNode",pubKey_7,walletAddress)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()