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
class TestMutiContract_42(ParametrizedTestCase):
    def test_main(self):
        logger.open("TestMutiContract_42.log", "TestMutiContract_42")
        result = False
        try:
            contract_address = set_premise_b("tasks/test_38.neo")

			# setp 1 用户A授权用户B拥有角色A的权限
            (result, response) = delegate_user_role(contract_address, Common.ontID_A, Common.ontID_B, Common.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")

			# ==================================================================
            # time.sleep(5)

            # 用户B调用智能合约A中的A方法
            (result, response) = invoke_function(contract_address, "allowance", Common.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": script_hash_bl_reserver(base58_to_address(Config.SERVICES[Common.node_C]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": script_hash_bl_reserver(base58_to_address(Config.SERVICES[Common.node_A]["address"]))
																				}])
            if not result:
                raise Error("invoke_function error")
        
        except Exception as e:
            print(e.msg)
            logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()

