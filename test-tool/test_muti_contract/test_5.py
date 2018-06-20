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

class TestMutiContract_5(ParametrizedTestCase):
    def test_main(self):	
        logger.open("TestMutiContract_5.log", "TestMutiContract_5")
        result = False
        try:
            contract_address = set_premise("tasks/test_1.neo", Common.roleA_hex, Common.roleB_hex)

            # setp 1 绑定角色绑定到用户
            (result, response) = bind_user_role(contract_address, Common.ontID_Admin, Common.roleA_hex, [Common.ontID_A])
            if not result:
                raise("bind_user_role error")
			
            (result, response) = bind_user_role(contract_address, Common.ontID_Admin, Common.roleB_hex, [Common.ontID_B])
            if not result:
                raise("bind_user_role error")
			
			# setp 1 用户B授权用户A拥有角色B的权限
            (result, response) = delegate_user_role(contract_address, Common.ontID_B, Common.ontID_A, Common.roleB_hex, "100", "1", node_index = Common.node_B)
            if not result:
                raise("bind_user_role error")
            
            # setp 2 用户A访问B函数
            (result, response) = invoke_function(contract_address, "B", Common.ontID_A, node_index = Common.node_A)
            if not result:
                raise Error("invoke_function error")
        
        except Exception as e:
            print(e.msg)
            logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()
