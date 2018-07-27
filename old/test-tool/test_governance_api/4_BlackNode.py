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
nodeNow=7
pubKey_1 = Config.NODES[7]["pubkey"] #已经申请的节点公钥
walletAddress_1= Config.NODES[7]["address"]
ontCount_1="10000"
ontCount_2="30000"
ontID_1=ByteToHex((Config.NODES[7]["ontid"]).encode("utf-8"))
user_1 = "1" #正常的公钥序号
pubKey_2 = "141923c71f012b99280229e5225267ba22e50e61cba9f2d713fe785080c1733f0877" #未申请的节点公钥
pubKey_3 = Config.NODES[nodeNow]["pubkey"] #已经在网络中的节点公钥
pubKey_4 = pubKey_1 #已经在网络中的候选节点公钥
pubKey_5 = "123abcd" #乱码
pubKey_6 = "" #留空
##########################################################

# test cases
class TestblackNode(ParametrizedTestCase):
	def setUp(self):
		#restart all node
		init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
	def test(self):
		pass
	def test_30_blackNode(self):
		logger.open("30_blackNode.log", "30_blackNode")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_1,0)
		time.sleep(15)
		if result:
			(result, response) = invoke_function_node("blackNode",pubKey_1,0)
			if result:
				(result, response) = nodeCountCheck(response,8)
				time.sleep(5)
				(result, response) = invoke_function_commitDpos(0)
				time.sleep(5)
				(result, response) = nodeCountCheck(response,7)
			else:
				nodeCountCheck(response,8)
		logger.close(result)

	def test_31_blackNode(self):
		logger.open("31_blackNode.log", "31_blackNode")
		(result, response) = invoke_function_node("blackNode",pubKey_2,0)

		logger.close(result)
	
	def test_32_blackNode(self):
		logger.open("32_blackNode.log", "32_blackNode")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_2,ontID_1,user_1,0)#成为共识节点
		time.sleep(15)

		(result, response) = invoke_function_candidate("approveCandidate",pubKey_1,0)
		time.sleep(5)
		if result:
			(result, response) = invoke_function_commitDpos(0)
			time.sleep(1)
			(result, response) = nodeCountCheck(response,8)
			time.sleep(15)
			(result, response) = invoke_function_node("blackNode",pubKey_3,0)
			if result:
				(result, response) = nodeCountCheck(response,8)
				time.sleep(5)
				(result, response) = invoke_function_commitDpos(0)
				time.sleep(5)
				(result, response) = nodeCountCheck(response,7)
			else:
				nodeCountCheck(response,8)

		logger.close(result)
	def test_33_blackNode(self):
		logger.open("33_blackNode.log", "33_blackNode")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_1,0)
		time.sleep(15)
		(result, response) = invoke_function_candidate("approveCandidate",pubKey_1,0)
		time.sleep(15)
		if result:
			(result, response) = invoke_function_node("blackNode",pubKey_4,0)
			if result:
				(result, response) = nodeCountCheck(response,8)
				time.sleep(5)
				(result, response) = invoke_function_commitDpos(0)
				time.sleep(5)
				(result, response) = nodeCountCheck(response,7)
			else:
				nodeCountCheck(response,8)

		logger.close(result)
	
	def test_34_blackNode(self):
		logger.open("34_blackNode.log", "34_blackNode")
		(result, response) = invoke_function_node("blackNode",pubKey_5)
		logger.close(result)
	
	def test_35_blackNode(self):
		logger.open("35_blackNode.log", "35_blackNode")
		(result, response) = invoke_function_node("blackNode",pubKey_6)
		logger.close(result)
	
####################################################
if __name__ == '__main__':
	unittest.main()