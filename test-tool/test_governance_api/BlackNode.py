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
pubKey_1 = "02b59d88bc4b2f5814b691d32e736bcd7ad018794f041235092f6954e23198cbcf" #已经申请的节点公钥
pubKey_2 = "03e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dc" #未申请的节点公钥
pubKey_3 = "03e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dc" #已经在网络中的共识节点公钥
pubKey_4 = "03e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dc" #已经在网络中的候选节点公钥
pubKey_5 = "123abcd" #乱码
pubKey_6 = "" #留空
##########################################################

# test cases
class TestblackNode(ParametrizedTestCase):
    def test_30_blackNode(self):
        logger.open("30_blackNode.log", "30_blackNode")
        (result, response) = invoke_function_node("blackNode",pubKey_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_31_blackNode(self):
        logger.open("31_blackNode.log", "31_blackNode")
        (result, response) = invoke_function_node("blackNode",pubKey_2)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_32_blackNode(self):
        logger.open("32_blackNode.log", "32_blackNode")
        (result, response) = invoke_function_node("blackNode",pubKey_3)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    def test_33_blackNode(self):
        logger.open("33_blackNode.log", "33_blackNode")
        (result, response) = invoke_function_node("blackNode",pubKey_4)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_34_blackNode(self):
        logger.open("34_blackNode.log", "34_blackNode")
        (result, response) = invoke_function_node("blackNode",pubKey_5)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_35_blackNode(self):
        logger.open("35_blackNode.log", "35_blackNode")
        (result, response) = invoke_function_node("blackNode",pubKey_6)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()