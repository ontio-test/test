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
#from utils.commonapi import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from test_api import *
from test_common import *
from utils.rpcapi import *
#from test_conf import Conf

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
class TestapproveCandidate(ParametrizedTestCase):
	@classmethod
	def setUpClass(cls):
		# register ONTID
		init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		
		pass
	def test222(self):
		
		(result1, response)=rpcapiTest.getstorage("0700000000000000000000000000000000000000",ByteToHex(b"governanceView"))
		(result1, response)=invoke_function_commitDpos(3)
		(result1, response)=rpcapiTest.getstorage("0700000000000000000000000000000000000000",ByteToHex(b"governanceView"))
		
	def test_20_approveCandidate(self):
		logger.open("20_approveCandidate.log", "20_approveCandidate")
		#time.sleep(5)
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_1)
		time.sleep(15)
		(result, response) = invoke_function_candidate("approveCandidate",pubKey_1,0)
		time.sleep(5)
		(result1, response)=rpcapiTest.getstorage("0700000000000000000000000000000000000000",ByteToHex(b"governanceView"))
		#(result1, response)=rpcapiTest.getstorage("0700000000000000000000000000000000000000",ByteToHex(b"peerPool")+"01000000")


		logger.close(result)

	def test_21_approveCandidate(self):
		logger.open("21_approveCandidate.log", "21_approveCandidate")
		(result, response) = invoke_function_candidate("approveCandidate",pubKey_2)
		logger.close(result)
	
	def test_22_approveCandidate(self):
		logger.open("22_approveCandidate.log", "22_approveCandidate")
		(result, response) = invoke_function_candidate("approveCandidate",pubKey_3)

		logger.close(result)
	def test_23_approveCandidate(self):
		logger.open("23_approveCandidate.log", "23_approveCandidate")
		(result, response) = invoke_function_candidate("approveCandidate",pubKey_4)

		logger.close(result)
	
	def test_24_approveCandidate(self):
		logger.open("24_approveCandidate.log", "24_approveCandidate")
		(result, response) = invoke_function_candidate("approveCandidate",pubKey_5)

		logger.close(result)
	
####################################################
if __name__ == '__main__':
	unittest.main()