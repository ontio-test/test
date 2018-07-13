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
from utils.init_ong_ont import *
from utils.parametrizedtestcase import ParametrizedTestCase
from test_api import *
from test_common import *
from utils.rpcapi import *
#from test_conf import Conf
#from utils.contractapi import *
logger = LoggerInstance
rpcapiTest=RPCApi()
##########################################################
# params
nodeNow=5
#systemNode=findSystemNode()
pubKey_1 = Config.NODES[7]["pubkey"]#未加入节点网络的节点公钥
pubKey_2 = Config.NODES[nodeNow]["pubkey"] #已加入节点网络的节点公钥
pubKey_3 = "1234abcd" #乱码
pubKey_4 = "" #留空
walletAddress_1 = Config.NODES[7]["address"] #pubKey_1节点对应的钱包地址,要有钱，超过10000ont
walletAddress_2 = Config.NODES[nodeNow]["address"]#其他已经加入节点网络的节点的钱包地址
walletAddress_3 = "1234abcd" #乱码
walletAddress_4 = "" #留空
ontCount_1 = "10000" #钱包里存在的所有ONT值
ontCount_2 = "100" #钱包里存在的所有ONT值
ontCount_3 = "0" #0
ontCount_4 = "" #留空
ontID_1 = ByteToHex((Config.NODES[7]["ontid"]).encode("utf-8")) #有授权的ontid
ontID_2 = ByteToHex((Config.NODES[nodeNow]["ontid"]).encode("utf-8")) #没有授权的ontid
ontID_3 = "123456abcd" #乱码
ontID_4 = "" #留空
user_1 = "1" #正常的公钥序号
user_2 = "100" #不存在的公钥序号
user_3 = "" #留空
####################################################

# test cases
class TestContract(ParametrizedTestCase):
	@classmethod
	def setUpClass(cls):
		# register ONTID
		pass
	def setUp(self):
		#restart all node
		init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		# register ONTID
		
		
	def test_01_registerCandidate(self):
		logger.open("01_registerCandidate.log", "01_registerCandidate")
		#time.sleep(10)
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_1,errorcode=0)\
		time.sleep(5)
		(result, response) =rpcapiTest.getbalance(address)
		logger.close(result)

	def test_02_registerCandidate(self):
		logger.open("02_registerCandidate.log", "02_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_2,walletAddress_1,ontCount_1,ontID_1,user_1)


		logger.close(result)
	
	def test_03_registerCandidate(self):
		logger.open("03_registerCandidate.log", "03_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_3,walletAddress_1,ontCount_1,ontID_1,user_1)


		logger.close(result)
	def test_04_registerCandidate(self):
		logger.open("04_registerCandidate.log", "04_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_4,walletAddress_1,ontCount_1,ontID_1,user_1)


		logger.close(result)
	
	def test_05_registerCandidate(self):
		logger.open("05_registerCandidate.log", "05_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_1,0)


		logger.close(result)
	
	def test_06_registerCandidate(self):
		logger.open("06_registerCandidate.log", "06_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_2,ontCount_1,ontID_1,user_1)


		logger.close(result)

	def test_07_registerCandidate(self):
		logger.open("07_registerCandidate.log", "07_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_3,ontCount_1,ontID_1,user_1)


		logger.close(result)

	def test_08_registerCandidate(self):
		logger.open("08_registerCandidate.log", "08_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_4,ontCount_1,ontID_1,user_1)


		logger.close(result)

	def test_09_registerCandidate(self):
		logger.open("09_registerCandidate.log", "09_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_1,0)


		logger.close(result)
	
	def test_10_registerCandidate(self):
		logger.open("10_registerCandidate.log", "10_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_2,ontID_1,user_1)


		logger.close(result)
	
	def test_11_registerCandidate(self):
		logger.open("11_registerCandidate.log", "11_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_3,ontID_1,user_1)


		logger.close(result)
	
	def test_12_registerCandidate(self):
		logger.open("12_registerCandidate.log", "12_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_4,ontID_1,user_1)


		logger.close(result)
	
	def test_13_registerCandidate(self):
		logger.open("13_registerCandidate.log", "13_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_1,0)


		logger.close(result)
	
	def test_14_registerCandidate(self):
		logger.open("14_registerCandidate.log", "14_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_2,user_1)


		logger.close(result)
	
	def test_15_registerCandidate(self):
		logger.open("15_registerCandidate.log", "15_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_3,user_1)


		logger.close(result)
	
	def test_16_registerCandidate(self):
		logger.open("16_registerCandidate.log", "16_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_4,user_1)


		logger.close(result)

	def test_17_registerCandidate(self):
		logger.open("17_registerCandidate.log", "17_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_1,0)


		logger.close(result)
	
	def test_18_registerCandidate(self):
		logger.open("18_registerCandidate.log", "18_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_2)


		logger.close(result)

	def test_19_registerCandidate(self):
		logger.open("19_registerCandidate.log", "19_registerCandidate")
		(result, response) = invoke_function_register("registerCandidate",pubKey_1,walletAddress_1,ontCount_1,ontID_1,user_3)


		logger.close(result)
	
####################################################
if __name__ == '__main__':
	unittest.main()