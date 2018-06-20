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

from utils.commonapi import *

logger = LoggerInstance

####################################################
# test cases

class TestNode(ParametrizedTestCase):
	def test_main(self):
		logger.open("TestNode.log", "TestNode")
		result = False
		try:
			(result, response) = call_contract(Task("tasks/sample.json"))
			if not result:
				raise Error("call contract error")

			result = pause("please check you next step, then put '1' or '0' in you command window.\n '1' is ok, '0' is not ok")
			result = int(result)
		except Exception as e:
			print(e)
			print(e.msg)
		logger.close(result)

####################################################
if __name__ == '__main__':
    unittest.main()
