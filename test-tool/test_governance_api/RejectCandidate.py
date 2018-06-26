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
class TestrejectCandidate(ParametrizedTestCase):
    def test_25_rejectCandidate(self):
        logger.open("25_rejectCandidate.log", "25_rejectCandidate")
        (result, response) = invoke_function_candidate("rejectCandidate",pubKey_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_26_rejectCandidate(self):
        logger.open("26_rejectCandidate.log", "26_rejectCandidate")
        (result, response) = invoke_function_candidate("rejectCandidate",pubKey_2)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_27_rejectCandidate(self):
        logger.open("27_rejectCandidate.log", "27_rejectCandidate")
        (result, response) = invoke_function_candidate("rejectCandidate",pubKey_3)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    def test_28_rejectCandidate(self):
        logger.open("28_rejectCandidate.log", "28_rejectCandidate")
        (result, response) = invoke_function_candidate("rejectCandidate",pubKey_4)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_29_rejectCandidate(self):
        logger.open("29_rejectCandidate.log", "29_rejectCandidate")
        (result, response) = invoke_function_candidate("rejectCandidate",pubKey_5)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()