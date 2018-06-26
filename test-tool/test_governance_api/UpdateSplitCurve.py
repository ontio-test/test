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
array_1 = ["1","2","3","4","5","6","7","8","9","10","1","2","3","4","5","6","7","8","9","10","1","2","3","4","5","6","7","8","9","10",
            "1","2","3","4","5","6","7","8","9","10","1","2","3","4","5","6","7","8","9","10","1","2","3","4","5","6","7","8","9","10"
            "1","2","3","4","5","6","7","8","9","10","1","2","3","4","5","6","7","8","9","10","1","2","3","4","5","6","7","8","9","10",
            "1","2","3","4","5","6","7","8","9","10","1"] #101个数值组成的符合要求的数组
array_2 = ["1","2","3","4","5","6","7","8","9","10","1","2","3","4","5","6","7","8","9","10","1","2","3","4","5","6","7","8","9","10",
            "1","2","3","4","5","6","7","8","9","10","1","2","3","4","5","6","7","8","9","10","1","2","3","4","5","6","7","8","9","10"
            "1","2","3","4","5","6","7","8","9","10","1","2","3","4","5","6","7","8","9","10","1","2","3","4","5","6","7","8","9","10",
            "1","2","3","4","5","6","7","8","9","10"] #少于101个数值组成的数组
array_3 = ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1",
            "1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1",
            "1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1",
            "1","1","1","1","1","1","1","1","1","1","1"] #101个相同数组成的数组
array_4 = [] #留空
##########################################################

# test cases
class TestupdateSplitCurve(ParametrizedTestCase):
    def test_171_updateSplitCurve(self):
        logger.open("171_updateSplitCurve.log", "171_updateSplitCurve")
        (result, response) = invoke_function_SplitCurve("updateSplitCurve",array_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_172_updateSplitCurve(self):
        logger.open("172_updateSplitCurve.log", "172_updateSplitCurve")
        (result, response) = invoke_function_SplitCurve("updateSplitCurve",array_2)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_173_updateSplitCurve(self):
        logger.open("173_updateSplitCurve.log", "173_updateSplitCurve")
        (result, response) = invoke_function_SplitCurve("updateSplitCurve",array_3)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    def test_174_updateSplitCurve(self):
        logger.open("174_updateSplitCurve.log", "174_updateSplitCurve")
        (result, response) = invoke_function_SplitCurve("updateSplitCurve",array_4)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()