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
pubKey_1 = "02b59d88bc4b2f5814b691d32e736bcd7ad018794f0411785092f6954e178198cbcf" #已经进入黑名单的节点公钥
pubKey_2 = "03e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dc" #未进入黑名单的节点公钥
pubKey_3 = "03e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dc" #未申请的节点公钥
pubKey_4 = "1178abcd" #从黑名单中删除的节点公钥
pubKey_5 = "1234abcd" #乱码
pubKey_6 = "" #留空
walletAddress_1 = "AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN" # 自己的钱包地址
walletAddress_2 = "AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN" #其他人的钱包地址
walletAddress_3 = "1178abcd" #乱码
walletAddress_4 = "" #留空
####################################################

# test cases
class TesttransferPenalty(ParametrizedTestCase):
    def test_175_transferPenalty(self):
        logger.open("175_transferPenalty.log", "175_transferPenalty")
        (result, response) = invoke_function_quitNode("transferPenalty",pubKey_1,walletAddress_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_176_transferPenalty(self):
        logger.open("176_transferPenalty.log", "176_transferPenalty")
        (result, response) = invoke_function_quitNode("transferPenalty",pubKey_2,walletAddress_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_177_transferPenalty(self):
        logger.open("177_transferPenalty.log", "177_transferPenalty")
        (result, response) = invoke_function_quitNode("transferPenalty",pubKey_3,walletAddress_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    def test_178_transferPenalty(self):
        logger.open("178_transferPenalty.log", "178_transferPenalty")
        (result, response) = invoke_function_quitNode("transferPenalty",pubKey_4,walletAddress_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_179_transferPenalty(self):
        logger.open("179_transferPenalty.log", "179_transferPenalty")
        (result, response) = invoke_function_quitNode("transferPenalty",pubKey_5,walletAddress_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_180_transferPenalty(self):
        logger.open("180_transferPenalty.log", "180_transferPenalty")
        (result, response) = invoke_function_quitNode("transferPenalty",pubKey_6,walletAddress_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_181_transferPenalty(self):
        logger.open("181_transferPenalty.log", "181_transferPenalty")
        (result, response) = invoke_function_quitNode("transferPenalty",pubKey_1,walletAddress_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_182_transferPenalty(self):
        logger.open("182_transferPenalty.log", "182_transferPenalty")
        (result, response) = invoke_function_quitNode("transferPenalty",pubKey_1,walletAddress_2)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_183_transferPenalty(self):
        logger.open("183_transferPenalty.log", "183_transferPenalty")
        (result, response) = invoke_function_quitNode("transferPenalty",pubKey_1,walletAddress_3)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_184_transferPenalty(self):
        logger.open("184_transferPenalty.log", "184_transferPenalty")
        (result, response) = invoke_function_quitNode("transferPenalty",pubKey_1,walletAddress_4)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()