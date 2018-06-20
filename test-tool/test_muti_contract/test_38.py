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
from test_conf import Conf

logger = LoggerInstance

####################################################
# test cases
class TestMutiContract_38(ParametrizedTestCase):
    def test_main(self):
        logger.open("TestMutiContract_38.log", "TestMutiContract_38")
        result = False
        try:
            (contract_address) = set_premise_b("tasks/test_38.neo")

            # 用户A调用智能合约A中的A方法
            (result, response) = invoke_function(contract_address, "transfer", Common.ontID_A, argvs = [ {
																					"type": "bytearray",
																					"value": script_hash_bl_reserver(base58_to_address(Config.SERVICES[Common.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": script_hash_bl_reserver(base58_to_address(Config.SERVICES[Common.node_B]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])
            if not result:
                raise Error("invoke_function error")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()

