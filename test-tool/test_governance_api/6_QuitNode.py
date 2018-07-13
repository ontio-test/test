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

logger = LoggerInstance

##########################################################
# params
nodeNow=7
walletAddress_node=7
pubKey_pre = Config.NODES[7]["pubkey"] #准备用
walletAddress_1= Config.NODES[7]["address"]
ontCount_1="10000"
ontCount_2="30000"
ontID_1=ByteToHex((Config.NODES[7]["ontid"]).encode("utf-8"))
user_1 = "1" #正常的公钥序号


pubKey_1 = Config.NODES[nodeNow]["pubkey"] #已经在网络中的共识节点公钥
pubKey_1_node=nodeNow
pubKey_2 = Config.NODES[7]["pubkey"] #已经在网络中的候选节点公钥
pubKey_2_node=7
pubKey_3 = "141923c71f012b99280229e5225267ba22e50e61cba9f2d713fe785080c1733f0877" #未申请的节点公钥
pubKey_3_node=nodeNow
pubKey_4_node=7
pubKey_5_node=7
pubKey_6_node=nodeNow
pubKey_7_node=nodeNow
pubKey_4 = Config.NODES[pubKey_4_node]["pubkey"] #已经申请的节点公钥
pubKey_5 = Config.NODES[pubKey_5_node]["pubkey"]#已经进入黑名单的节点公钥
pubKey_6 = "123abcd" #乱码
pubKey_7 = "" #留空
walletAddress = Config.NODES[walletAddress_node]["address"] #钱包地址

##########################################################

# test cases
class TestquitNode(ParametrizedTestCase):
	def setUp(self):
		#restart all node
		init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		# register ONTID
	def test_41_quitNode(self):
		logger.open("41_quitNode.log", "41_quitNode")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_2,ontID_1,user_1,0)#准备共识节点
		time.sleep(15)

		(result, response) = invoke_function_candidate("approveCandidate",pubKey_1,0)
		time.sleep(5)
		if result:#正式开始测试
			(result, response) = invoke_function_commitDpos(0)
			time.sleep(10)
			(result, response) = nodeCountCheck(response,8)
			(result, response) = invoke_function_quitNode("quitNode",pubKey_1,walletAddress_1,0,pubKey_1_node)
			if result:
				time.sleep(5)
				(result, response) = invoke_function_commitDpos(0)
				time.sleep(5)
				(result, response) = nodeCountCheck(response,8)
				if result:
					time.sleep(5)
					(result, response) = invoke_function_commitDpos(0)
					time.sleep(5)
					(result, response) = nodeCountCheck(response,7)
			else:
				nodeCountCheck(response,7)
		logger.close(result)

	def test_42_quitNode(self):
		logger.open("42_quitNode.log", "42_quitNode")
		(result, response) = invoke_function_register("registerCandidate",pubKey_pre,walletAddress_1,ontCount_1,ontID_1,user_1,0)#准备候选节点
		time.sleep(15)
		(result, response) = invoke_function_candidate("approveCandidate",pubKey_pre,0)
		time.sleep(15)
		if result:#正式开始测试
			(result, response) = nodeCountCheck(response,8)
			(result, response) = invoke_function_quitNode("quitNode",pubKey_2,walletAddress_1,0,pubKey_2_node)
			if result:
				time.sleep(5)
				(result, response) = invoke_function_commitDpos(0)
				time.sleep(5)
				(result, response) = nodeCountCheck(response,7)
			else:
				nodeCountCheck(response,7)
		logger.close(result)
	
	def test_43_quitNode(self):
		logger.open("43_quitNode.log", "43_quitNode")
		(result, response) = invoke_function_quitNode("quitNode",pubKey_3,walletAddress,node_index=pubKey_3_node)


		logger.close(result)
	def test_44_quitNode(self):
		logger.open("44_quitNode.log", "44_quitNode")
		(result, response) = invoke_function_register("registerCandidate",pubKey_pre,walletAddress_1,ontCount_1,ontID_1,user_1,0)#准备注册节点
		if result:#正式开始测试
			time.sleep(15)
			(result, response) = invoke_function_quitNode("quitNode",pubKey_4,walletAddress,node_index=pubKey_4_node)
		else:
			nodeCountCheck(response,7)
		logger.close(result)
	
	def test_45_quitNode(self):
		logger.open("45_quitNode.log", "45_quitNode")
		(result, response) = invoke_function_register("registerCandidate",pubKey_5,walletAddress_1,ontCount_1,ontID_1,user_1,0)#准备黑名单节点
		time.sleep(15)
		(result, response) = invoke_function_node("blackNode",pubKey_5,0)
		if result:#正式开始测试
			time.sleep(15)
			(result, response) = nodeCountCheck(response,7)
			(result, response) = invoke_function_quitNode("quitNode",pubKey_5,walletAddress,node_index=pubKey_5_node)
		else:
			nodeCountCheck(response,7)
		logger.close(result)
	
	def test_46_quitNode(self):
		logger.open("46_quitNode.log", "46_quitNode")
		(result, response) = invoke_function_quitNode("quitNode",pubKey_6,walletAddress,node_index=pubKey_6_node)
		logger.close(result)

	def test_47_quitNode(self):
		logger.open("47_quitNode.log", "47_quitNode")
		(result, response) = invoke_function_quitNode("quitNode",pubKey_7,walletAddress,node_index=pubKey_7_node)
		logger.close(result)
	
####################################################
if __name__ == '__main__':
	unittest.main()