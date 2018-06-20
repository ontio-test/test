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
class TestMutiContract_56(ParametrizedTestCase):
    def test_main(self):
        logger.open("TestMutiContract_41.log", "TestMutiContract_41")
        result = False
        try:
            address_A = ByteToHex(b"TA7TSQ5aJcA8sU5MpqJNyTG1r13AQYLYpR")
            address_B = ByteToHex(b"TA82XAPQXtVzncQMczcY9SVytjb2VuTQy4")
            address_C = ByteToHex(b"TA6CtF4hZwqAmXdc6opa4B79fRS17YJjX5")
            # (contract_address, adminOntID, roleA_hex, roleB_hex, ontID_A, ontID_B, ontID_C,address_A,address_B,address_C) = set_premise_b("38_contract.neo")

			# # setp 1 用户A授权用户B拥有角色A的权限
            # (result, response) = delegate_user_role(contract_address, ontID_A, ontID_B, roleA_hex, "10000", "1")
            # if not result:
            #     raise("bind_user_role error")

			# ==================================================================
            # time.sleep(5)

            # 用户B调用智能合约A中的A方法
            (result, response) = invoke_function_approve(contract_address, "A",address_A,address_C,10)
            if not result:
                raise Error("invoke_function error")
        
        except Exception as e:
            print(e.msg)
            logger.close(result)
    
    def invoke_function_transfer(self, contract_address, function_str,from_str,to_str,amount):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signeovminvoketx",
                "Params": {
                    "gas_price": 0,
                    "gas_limit": 1000000000,
                    "address": contract_address,
                    "version": 1,
                    "params": [
                        {
                            "type": "string",
                            "value": function_str
                        },
                        {
                            "type": "array",
                            "value": [
                                {
                                    "type": "bytearray",
                                    "value": from_str
                                },
                                {
                                    "type": "bytearray",
                                    "value": to_str
                                },
                                {
                                    "type": "bytearray",
                                    "value": amount
                                }
                            ]
                        }
                    ]
                }
            },
            "RESPONSE":{"error" : 0}
        }
        return call_contract(Task(name="invoke_function", ijson=request))
    
####################################################
if __name__ == '__main__':
    unittest.main()