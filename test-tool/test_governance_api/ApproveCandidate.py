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
pubKey_3 = "03e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dc" #已经在网络中的节点公钥
pubKey_4 = "123abcd" #乱码
pubKey_5 = "" #留空
####################################################

# test cases
class TestapproveCandidate(ParametrizedTestCase):
    def test_20_approveCandidate(self):
        logger.open("20_approveCandidate.log", "20_approveCandidate")
        (result, response) = invoke_function_candidate("approveCandidate",pubKey_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_21_approveCandidate(self):
        logger.open("21_approveCandidate.log", "21_approveCandidate")
        (result, response) = invoke_function_candidate("approveCandidate",pubKey_2)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_22_approveCandidate(self):
        logger.open("22_approveCandidate.log", "22_approveCandidate")
        (result, response) = invoke_function_candidate("approveCandidate",pubKey_3)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    def test_23_approveCandidate(self):
        logger.open("23_approveCandidate.log", "23_approveCandidate")
        (result, response) = invoke_function_candidate("approveCandidate",pubKey_4)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_24_approveCandidate(self):
        logger.open("24_approveCandidate.log", "24_approveCandidate")
        (result, response) = invoke_function_candidate("approveCandidate",pubKey_5)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()