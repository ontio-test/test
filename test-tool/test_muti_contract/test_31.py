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


class TestMutiContract_31(ParametrizedTestCase):
    def test_main(self):
        logger.open("TestMutiContract_31.log", "TestMutiContract_31")
        result = False
        try:
            contract_address = set_premise("tasks/test_1.neo")

            # setp 1 绑定用户A，用户B拥有roleA角色
            (result, response) = bind_user_role(contract_address,Common.ontID_Admin, Common.roleA_hex, [Common.ontID_A])
            if not result:
                raise("bind_user_role error")
            
            # setp 1 绑定用户A，用户B拥有roleB角色
            (result, response) = bind_user_role(contract_address,Common.ontID_Admin, Common.roleB_hex, [Common.ontID_B])
            if not result:
                raise("bind_user_role error")
						
			# setp 1 用户A授权用户C拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Common.ontID_A, Common.ontID_C, Common.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 1 用户B授权用户C拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Common.ontID_B, Common.ontID_C, Common.roleB_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
                        
            # setp 1 用户A撤回用户C拥有的roleB角色
            (result, response) = withdraw_user_role(contract_address, Common.ontID_A, Common.ontID_C, Common.roleB_hex)
            if not result:
                raise("bind_user_role error")

            # # setp 2 用户C访问B函数
            # (result, response) = invoke_function(contract_address, "B")
            # if not result:
            #     raise Error("invoke_function error")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()
