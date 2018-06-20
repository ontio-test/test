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
class TestMutiContract_34(ParametrizedTestCase):
    def test_main(self):
        logger.open("TestMutiContract_34.log", "TestMutiContract_34")
        result = False
        try:
            (contract_address_A, contract_address_B) = set_premise_a("tasks/contractA.neo", "tasks/contractB.neo")

            # B用户去调用A方法
            (result, response) = invoke_function(contract_address_A, "contractA_Func_A", Common.ontID_B)
            if not result:
                raise Error("invoke_function error")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()

