# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.rpcapi import RPCApi
from utils.parametrizedtestcase import ParametrizedTestCase

from utils.commonapi import *

from test_api import *
rpcapiTest=RPCApi()
logger = LoggerInstance
nodePath="/home/ubuntu/ontology/node"
contractaddress=deploy_contract("transferong_ont.json")
pay_address="AXbevnGZBypZrcQwQfdYZxXj5zcFTtiMEA"
node_index=5
get_address1="ANdtbPPwfMv79eMev9z7aAZRM6bUuQQ3rf"
get_address2="ASzM79c3kfc1msGuBhaSWivG31rpKpCPU8"
get_address3="AQYJcKBrRvpefyXTMT61d2z83TJj6Mj4UF"
get_address4="AanAa1J2C9uHMmdyqsrqmF1wfkFJykNJjL"
get_address5="AJWZYbpGTeoZuidsfq7XN4G9oMfEmsohHQ"
get_address6="AS6dskFA1CHWiNkk33TtjqESVzSLbNnuKx"
get_address7="APM5LgzLjmp9sqSCxDz7z8PFKEmGHUgNUA"
get_address8="AMrKfXtwdCaxkF8cCGYodz5FXD1GcwbW7M"
get_address9="AR7jzsPWSqJTM7hf41jDbTVUgpurVGBvfk"
get_address10="AQhDgYDY42AwfBdRDu1Wnf224EXKQ5ypGc"
get_address11="ASWGN1aztnnGThLKwXZoTX5Jn752BrGcsd"
####################################################
#test cases
class TestContract(ParametrizedTestCase):
	@classmethod
	def setUpClass(self):
		os.system(nodePath+ "/ontology account import -s wallettest.dat -w "+nodePath+"/wallet.dat")
		deploy_contract
	def test_001(self):
		logger.open("test_001.log", "test_001")
		result=self.all_case(get_address1)
		logger.close(result)
		
	def test_002(self):
		logger.open("test_002.log", "test_002")
		result=self.all_case(get_address2)
		logger.close(result)
		
	def test_003(self):
		logger.open("test_003.log", "test_003")
		result=self.all_case(get_address3)
		logger.close(result)
	
	def test_004(self):
		logger.open("test_004.log", "test_004")
		result=self.all_case(get_address4)
		logger.close(result)
	def test_005(self):
		logger.open("test_005.log", "test_005")
		result=self.all_case(get_address5)
		logger.close(result)
	def test_006(self):
		logger.open("test_006.log", "test_006")
		result=self.all_case(get_address6)
		logger.close(result)
	def test_007(self):
		logger.open("test_007.log", "test_007")
		result=self.all_case(get_address7)
		logger.close(result)
	def test_008(self):
		logger.open("test_008.log", "test_008")
		result=self.all_case(get_address8)
		logger.close(result)
	def test_009(self):
		logger.open("test_009.log", "test_009")
		result=self.all_case(get_address9)
		logger.close(result)
	def test_010(self):
		logger.open("test_010.log", "test_010")
		result=self.all_case(get_address10)
		logger.close(result)
	def test_011(self):
		logger.open("test_011.log", "test_011")
		result=self.all_case(get_address11)
		logger.close(result)		
	def all_case(self,get_address):
		
		result1=self.sample(contractaddress,pay_address,get_address,node_index)
		
		result2=self.sample(contractaddress,get_address,pay_address,node_index,True)
		
		return result1&result2
		
	def sample(self,contract_address,pay_address,get_address,node_index,charge=False):

		#getont/ong
		(result1, response)=rpcapiTest.getbalance(get_address)
		transfervalue1ont=int(response["result"]["ont"])
		transfervalue1ong=int(response["result"]["ong"])
		##case
		if(charge):
			os.system("echo 123456 | "+nodePath+ "/ontology asset transfer --from="+pay_address+" --to=1 --amount=10 --asset=ont -w "+nodePath+"/wallet.dat")
			os.system("echo 123456 | "+nodePath+ "/ontology asset transfer --from="+pay_address+" --to=1 --amount=0.00000001 --asset=ong -w "+nodePath+"/wallet.dat")
			time.sleep(5)
		else:
			(result, response) = forNeo(contract_address,pay_address,get_address, node_index)

		#getont/ong
		(result2, response)=rpcapiTest.getbalance(get_address)
		transfervalue2ont=int(response["result"]["ont"])
		transfervalue2ong=int(response["result"]["ong"])
		changevalue=10
		result1=(transfervalue2ont-transfervalue1ont==changevalue)
		result2=(transfervalue2ong-transfervalue1ong==changevalue)
		print(result1)
		print(result2)
		
		return result1&result2

####################################################
if __name__ == '__main__':
	unittest.main()

