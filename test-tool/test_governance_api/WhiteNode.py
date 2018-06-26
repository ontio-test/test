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
pubKey_1 = "02b59d88bc4b2f5814b691d32e736bcd7ad018794f041235092f6954e23198cbcf" #已经进入黑名单的节点公钥
pubKey_2 = "03e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dc" #未进入黑名单的节点公钥
pubKey_3 = "03e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dc" #未申请的节点公钥
pubKey_4 = "123abcd" #乱码
pubKey_5 = "" #留空
##########################################################

# test cases
class TestwhiteNode(ParametrizedTestCase):
    def test_36_whiteNode(self):
        logger.open("36_whiteNode.log", "36_whiteNode")
        (result, response) = invoke_function_candidate("whiteNode",pubKey_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_37_whiteNode(self):
        logger.open("37_whiteNode.log", "37_whiteNode")
        (result, response) = invoke_function_candidate("whiteNode",pubKey_2)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_38_whiteNode(self):
        logger.open("38_whiteNode.log", "38_whiteNode")
        (result, response) = invoke_function_candidate("whiteNode",pubKey_3)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_39_whiteNode(self):
        logger.open("39_whiteNode.log", "39_whiteNode")
        (result, response) = invoke_function_candidate("whiteNode",pubKey_4)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_40_whiteNode(self):
        logger.open("40_whiteNode.log", "40_whiteNode")
        (result, response) = invoke_function_candidate("whiteNode",pubKey_5)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()