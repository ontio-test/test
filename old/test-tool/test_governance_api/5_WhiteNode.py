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
pubKey_1 = Config.NODES[7]["pubkey"] #已经进入黑名单的节点公钥
walletAddress_1= Config.NODES[7]["address"]
ontCount_1="10000"
ontID_1=ByteToHex((Config.NODES[7]["ontid"]).encode("utf-8"))
user_1 = "1" #正常的公钥序号
pubKey_3 = Config.NODES[nodeNow]["pubkey"] #未进入黑名单的节点公钥
pubKey_2 = "141923c71f012b99280229e5225267ba22e50e61cba9f2d713fe785080c1733f0877" #不在网络中的节点公钥
pubKey_4 = "123abcd" #乱码
pubKey_5 = "" #留空
##########################################################

# test cases
class TestwhiteNode(ParametrizedTestCase):
	@classmethod
	def setUpClass(cls):
		#restart all node
		init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		# register ONTID
		
	def test_36_whiteNode(self):
		logger.open("36_whiteNode.log", "36_whiteNode")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_1,0)
		time.sleep(15)
		if result:
			(result, response) = nodeCountCheck(response,8)
			(result, response) = invoke_function_node("blackNode",pubKey_1,0)
			if result:
				time.sleep(5)
				(result, response) = invoke_function_commitDpos(0)
				time.sleep(5)
				(result, response) = nodeCountCheck(response,7)
				(result, response) = invoke_function_candidate("whiteNode",pubKey_1, 0)
				time.sleep(15)
				(result, response) = nodeCountCheck(response,7)
			else:
				nodeCountCheck(response,7)
		logger.close(result)

	def test_37_whiteNode(self):
		logger.open("37_whiteNode.log", "37_whiteNode")
		(result, response) = invoke_function_candidate("whiteNode",pubKey_2)


		logger.close(result)
	
	def test_38_whiteNode(self):
		logger.open("38_whiteNode.log", "38_whiteNode")
		(result, response) = invoke_function_candidate("whiteNode",pubKey_3)


		logger.close(result)
	
	def test_39_whiteNode(self):
		logger.open("39_whiteNode.log", "39_whiteNode")
		(result, response) = invoke_function_candidate("whiteNode",pubKey_4)


		logger.close(result)
	
	def test_40_whiteNode(self):
		logger.open("40_whiteNode.log", "40_whiteNode")
		(result, response) = invoke_function_candidate("whiteNode",pubKey_5)


		logger.close(result)
	
####################################################
if __name__ == '__main__':
	unittest.main()