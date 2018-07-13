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
#from test_conf import Conf
from utils.rpcapi import *
logger = LoggerInstance
rpcapiTest=RPCApi()
##########################################################
# params
nodeNow=0
pubKey_1 = Config.NODES[7]["pubkey"] #已经申请的节点公钥
walletAddress_1= Config.NODES[7]["address"]
ontCount_1="10000"
ontID_1=ByteToHex((Config.NODES[7]["ontid"]).encode("utf-8"))
user_1 = "1" #正常的公钥序号
pubKey_2 = "141923c71f012b99280229e5225267ba22e50e61cba9f2d713fe785080c1733f0877" #未申请的节点公钥
pubKey_3 = Config.NODES[nodeNow]["pubkey"] #已经在网络中的节点公钥
pubKey_4 = "123abcd" #乱码
pubKey_5 = "" #留空
####################################################

# test cases
class TestrejectCandidate(ParametrizedTestCase):
	@classmethod
	def setUpClass(cls):
		#restart all node
		init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		# register ONTID
	def test_25_rejectCandidate(self):
		logger.open("25_rejectCandidate.log", "25_rejectCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_1)
		time.sleep(15)
		(result, response) = invoke_function_candidate("rejectCandidate",pubKey_1,0)
		time.sleep(5)

		logger.close(result)

	def test_26_rejectCandidate(self):
		logger.open("26_rejectCandidate.log", "26_rejectCandidate")
		(result, response) = invoke_function_candidate("rejectCandidate",pubKey_2)

		logger.close(result)
	
	def test_27_rejectCandidate(self):
		logger.open("27_rejectCandidate.log", "27_rejectCandidate")
		(result, response) = invoke_function_candidate("rejectCandidate",pubKey_3)

		logger.close(result)
	def test_28_rejectCandidate(self):
		logger.open("28_rejectCandidate.log", "28_rejectCandidate")
		(result, response) = invoke_function_candidate("rejectCandidate",pubKey_4)

		logger.close(result)
	
	def test_29_rejectCandidate(self):
		logger.open("29_rejectCandidate.log", "29_rejectCandidate")
		(result, response) = invoke_function_candidate("rejectCandidate",pubKey_5)

		logger.close(result)
	
####################################################
if __name__ == '__main__':
	unittest.main()