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
from test_api import *
from test_common import *
logger = LoggerInstance

####################################################
# test cases


class TestMutiContract_2(ParametrizedTestCase):
    def test_main(self):
        logger.open("TestMutiContract_3.log", "TestMutiContract_3")
        result = False
        try:
            # 初始化合约B管理员为A用户,
            contract_address_B = deploy_contract("./tasks/contractB.neo")
            ontID_A = ByteToHex(b"did:ont:TA7TSQ5aJcA8sU5MpqJNyTG1r13AQYLYpR")
            ontID_B = ByteToHex(b"did:ont:TA82XAPQXtVzncQMczcY9SVytjb2VuTQy4") 

            (result, response) = init_admin(contract_address_B, adminOntID_A)
            if not result:
                raise("init_admin error")
            
            # 部署智能合约A
            contract_address_A = deploy_contract("./tasks/contractA.neo")

            

            # A用户去调用A方法
            (result, response) = invoke_function(contract_address_A, "contractA_Func_A", ontID_B)
            if not result:
                raise Error("invoke_function error")
        
        except Exception as e:
            print(e.msg)
            logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()

