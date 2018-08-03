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
sys.path.append('../..')

import utils.connect
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from api.apimanager import API

from test_governance_api.test_api import *
from test_governance_api.test_config import test_config


# test cases
class test_governance_api_1(ParametrizedTestCase):	
	def setUp(self):
		logger.open( "test_governance_api/" +self._testMethodName + ".log",self._testMethodName)
		if self._testMethodName == "test_init":
			return 
		init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		# register ONTID

	def tearDown(self):
		logger.close(self.result())
		
	def test_base_001_registerCandidate(self):
		try:
			time.sleep(10)
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_1,test_config.registerCandidate_walletAddress_1,test_config.registerCandidate_ontCount_1,test_config.registerCandidate_ontID_1,test_config.registerCandidate_user_1,errorcode=0)
			if process:
				API.node().wait_gen_block()
				API.rpc().getbalance(test_config.registerCandidate_walletAddress_1)
				(process, response) = nodeCountCheck(response,8)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_002_registerCandidate(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_2,test_config.registerCandidate_walletAddress_1,test_config.registerCandidate_ontCount_1,test_config.registerCandidate_ontID_1,test_config.registerCandidate_user_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_003_registerCandidate(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_3,test_config.registerCandidate_walletAddress_1,test_config.registerCandidate_ontCount_1,test_config.registerCandidate_ontID_1,test_config.registerCandidate_user_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
			
	def test_abnormal_004_registerCandidate(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_4,test_config.registerCandidate_walletAddress_1,test_config.registerCandidate_ontCount_1,test_config.registerCandidate_ontID_1,test_config.registerCandidate_user_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_005_registerCandidate(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_1,test_config.registerCandidate_walletAddress_1,test_config.registerCandidate_ontCount_1,test_config.registerCandidate_ontID_1,test_config.registerCandidate_user_1,0)
			if process:
				API.node().wait_gen_block()
				API.rpc().getbalance(test_config.registerCandidate_walletAddress_1)
			(process, response) = nodeCountCheck("",8)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_006_registerCandidate(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_1,test_config.registerCandidate_walletAddress_2,test_config.registerCandidate_ontCount_1,test_config.registerCandidate_ontID_1,test_config.registerCandidate_user_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_007_registerCandidate(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_1,test_config.registerCandidate_walletAddress_3,test_config.registerCandidate_ontCount_1,test_config.registerCandidate_ontID_1,test_config.registerCandidate_user_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_008_registerCandidate(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_1,test_config.registerCandidate_walletAddress_4,test_config.registerCandidate_ontCount_1,test_config.registerCandidate_ontID_1,test_config.registerCandidate_user_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_009_registerCandidate(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_1,test_config.registerCandidate_walletAddress_1,test_config.registerCandidate_ontCount_1,test_config.registerCandidate_ontID_1,test_config.registerCandidate_user_1,0)
			if process:
				API.node().wait_gen_block()
				API.rpc().getbalance(test_config.registerCandidate_walletAddress_1)
				(process, response) = nodeCountCheck(response,8)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_010_registerCandidate(self):
		try:
			API.native().update_global_param("2000000000","10000","32","10","50","50","50","50")
			API.node().wait_gen_block()
			time.sleep(15)
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_1,test_config.registerCandidate_walletAddress_1,test_config.registerCandidate_ontCount_2,test_config.registerCandidate_ontID_1,test_config.registerCandidate_user_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_011_registerCandidate(self):
		try:
			API.native().update_global_param("2000000000","10000","32","10","50","50","50","50")
			API.node().wait_gen_block()
			time.sleep(15)
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_1,test_config.registerCandidate_walletAddress_1,test_config.registerCandidate_ontCount_3,test_config.registerCandidate_ontID_1,test_config.registerCandidate_user_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_012_registerCandidate(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_1,test_config.registerCandidate_walletAddress_1,test_config.registerCandidate_ontCount_4,test_config.registerCandidate_ontID_1,test_config.registerCandidate_user_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_013_registerCandidate(self):
		try:
			time.sleep(10)
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_1,test_config.registerCandidate_walletAddress_1,test_config.registerCandidate_ontCount_1,test_config.registerCandidate_ontID_1,test_config.registerCandidate_user_1,0)
			if process:
				API.node().wait_gen_block()
				API.rpc().getbalance(test_config.registerCandidate_walletAddress_1)
				(process, response) = nodeCountCheck(response,8)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_014_registerCandidate(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_1,test_config.registerCandidate_walletAddress_1,test_config.registerCandidate_ontCount_1,test_config.registerCandidate_ontID_2,test_config.registerCandidate_user_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_015_registerCandidate(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_1,test_config.registerCandidate_walletAddress_1,test_config.registerCandidate_ontCount_1,test_config.registerCandidate_ontID_3,test_config.registerCandidate_user_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_016_registerCandidate(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_1,test_config.registerCandidate_walletAddress_1,test_config.registerCandidate_ontCount_1,test_config.registerCandidate_ontID_4,test_config.registerCandidate_user_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_017_registerCandidate(self):
		try:
			time.sleep(10)
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_1,test_config.registerCandidate_walletAddress_1,test_config.registerCandidate_ontCount_1,test_config.registerCandidate_ontID_1,test_config.registerCandidate_user_1,0)
			if process:
				API.node().wait_gen_block()
				API.rpc().getbalance(test_config.registerCandidate_walletAddress_1)
				(process, response) = nodeCountCheck(response,8)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_018_registerCandidate(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_1,test_config.registerCandidate_walletAddress_1,test_config.registerCandidate_ontCount_1,test_config.registerCandidate_ontID_1,test_config.registerCandidate_user_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_019_registerCandidate(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.registerCandidate_pubKey_1,test_config.registerCandidate_walletAddress_1,test_config.registerCandidate_ontCount_1,test_config.registerCandidate_ontID_1,test_config.registerCandidate_user_3)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
			
			
			
class test_governance_api_2(ParametrizedTestCase):		
	def setUp(self):
		if self._testMethodName == "test_init":
			return
		logger.open( "test_governance_api/" +self._testMethodName + ".log",self._testMethodName)
		init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		
	def tearDown(self):
		if self._testMethodName == "test_init":
			return
		logger.close(self.result())	
			
	def test_base_020_approveCandidate(self):
		try:
			time.sleep(5)
			(process, response) = invoke_function_register("registerCandidate",test_config.approveCandidate_pubKey_1,test_config.approveCandidate_walletAddress_1,test_config.approveCandidate_ontCount_1,test_config.approveCandidate_ontID_1,test_config.approveCandidate_user_1,errorcode=0)
			if process:
				API.node().wait_gen_block()
				(process, response) = nodeCountCheck(response,8)
				(process, response) = invoke_function_candidate("approveCandidate",test_config.approveCandidate_pubKey_1,0)
				API.node().wait_gen_block()
				#time.sleep(5)
			(process1, response)= API.rpc().getstorage("0700000000000000000000000000000000000000",ByteToHex(b"governanceView"))
			#(process1, response)=API.rpc().getstorage("0700000000000000000000000000000000000000",ByteToHex(b"peerPool")+"01000000")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_021_approveCandidate(self):
		try:
			(process, response) = invoke_function_candidate("approveCandidate",test_config.approveCandidate_pubKey_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_022_approveCandidate(self):
		try:
			(process, response) = invoke_function_candidate("approveCandidate",test_config.approveCandidate_pubKey_3)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
			
	def test_abnormal_023_approveCandidate(self):
		try:
			(process, response) = invoke_function_candidate("approveCandidate",test_config.approveCandidate_pubKey_4)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_024_approveCandidate(self):
		try:
			(process, response) = invoke_function_candidate("approveCandidate",test_config.approveCandidate_pubKey_5)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])



class test_governance_api_3(ParametrizedTestCase):
	def setUp(self):
		if self._testMethodName == "test_init":
			return
		logger.open( "test_governance_api/" +self._testMethodName + ".log",self._testMethodName)
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		
	def tearDown(self):
		if self._testMethodName == "test_init":
			return
		logger.close(self.result())	

	def test_base_025_rejectCandidate(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.rejectCandidate_pubKey_1,test_config.rejectCandidate_walletAddress_1,test_config.rejectCandidate_ontCount_1,test_config.rejectCandidate_ontID_1,test_config.rejectCandidate_user_1,errorcode=0)
			if process:
				API.node().wait_gen_block()
				(process, response) = nodeCountCheck(response,8)
				(process, response) = invoke_function_candidate("rejectCandidate",test_config.rejectCandidate_pubKey_1,0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_026_rejectCandidate(self):
		try:
			(process, response) = invoke_function_candidate("rejectCandidate",test_config.rejectCandidate_pubKey_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_027_rejectCandidate(self):
		try:
			(process, response) = invoke_function_candidate("rejectCandidate",test_config.rejectCandidate_pubKey_3)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
			
	def test_abnormal_028_rejectCandidate(self):
		try:
			(process, response) = invoke_function_candidate("rejectCandidate",test_config.rejectCandidate_pubKey_4)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_029_rejectCandidate(self):
		try:
			(process, response) = invoke_function_candidate("rejectCandidate",test_config.rejectCandidate_pubKey_5)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])



class test_governance_api_4(ParametrizedTestCase):
	def setUp(self):
		#restart all node
		if self._testMethodName == "test_init":
			return
		logger.open( "test_governance_api/" +self._testMethodName + ".log",self._testMethodName)
		init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		
	def tearDown(self):
		if self._testMethodName == "test_init":
			return
		logger.close(self.result())
		
	def test_base_030_blackNode(self):
		try:
			time.sleep(10)
			(process, response) = invoke_function_register("registerCandidate",test_config.blackNode_pubKey_1,test_config.blackNode_walletAddress_1,test_config.blackNode_ontCount_1,test_config.blackNode_ontID_1,test_config.blackNode_user_1,0)
			API.node().wait_gen_block()
			if process:
				(process, response) = invoke_function_node("blackNode",test_config.blackNode_pubKey_1,0)
				if process:
					(process, response) = nodeCountCheck(response,8)
					API.node().wait_gen_block()
					(process, response) = invoke_function_commitDpos(0)
					API.node().wait_gen_block()
					(process, response) = nodeCountCheck(response,7)
				else:
					nodeCountCheck(response,8)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_031_blackNode(self):
		try:
			(process, response) = invoke_function_node("blackNode",test_config.blackNode_pubKey_2,0)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_032_blackNode(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.blackNode_pubKey_1,test_config.blackNode_walletAddress_1,test_config.blackNode_ontCount_2,test_config.blackNode_ontID_1,test_config.blackNode_user_1,0)#成为共识节点
			API.node().wait_gen_block()
			(process, response) = invoke_function_candidate("approveCandidate",test_config.blackNode_pubKey_1,0)
			API.node().wait_gen_block()
			if process:
				(process, response) = invoke_function_commitDpos(0)
				time.sleep(1)
				(process, response) = nodeCountCheck(response,8)
				API.node().wait_gen_block()
				(process, response) = invoke_function_node("blackNode",test_config.blackNode_pubKey_3,0)
				if process:
					(process, response) = nodeCountCheck(response,8)
					API.node().wait_gen_block()
					(process, response) = invoke_function_commitDpos(0)
					API.node().wait_gen_block()
					(process, response) = nodeCountCheck(response,7)
				else:
					nodeCountCheck(response,8)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
			
	def test_normal_033_blackNode(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.blackNode_pubKey_1,test_config.blackNode_walletAddress_1,test_config.blackNode_ontCount_1,test_config.blackNode_ontID_1,test_config.blackNode_user_1,0)
			API.node().wait_gen_block()
			(process, response) = invoke_function_candidate("approveCandidate",test_config.blackNode_pubKey_1,0)
			API.node().wait_gen_block()
			if process:
				(process, response) = invoke_function_node("blackNode",test_config.blackNode_pubKey_4,0)
				if process:
					(process, response) = nodeCountCheck(response,8)
					API.node().wait_gen_block()
					(process, response) = invoke_function_commitDpos(0)
					API.node().wait_gen_block()
					(process, response) = nodeCountCheck(response,7)
				else:
					nodeCountCheck(response,8)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_034_blackNode(self):
		try:
			(process, response) = invoke_function_node("blackNode",test_config.blackNode_pubKey_5)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abormal_035_blackNode(self):
		try:
			(process, response) = invoke_function_node("blackNode",test_config.blackNode_pubKey_6)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])



class test_governance_api_5(ParametrizedTestCase):
	def setUp(self):
		if self._testMethodName == "test_init":
			return
		logger.open( "test_governance_api/" +self._testMethodName + ".log",self._testMethodName)
		init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		
	def tearDown(self):
		if self._testMethodName == "test_init":
			return
		logger.close(self.result())
		
	def test_base_036_whiteNode(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.whiteNode_pubKey_1,test_config.whiteNode_walletAddress_1,test_config.whiteNode_ontCount_1,test_config.whiteNode_ontID_1,test_config.whiteNode_user_1,0)
			API.node().wait_gen_block()
			if process:
				(process, response) = nodeCountCheck(response,8)
				(process, response) = invoke_function_node("blackNode",test_config.whiteNode_pubKey_1,0)
				if process:
					API.node().wait_gen_block()
					(process, response) = invoke_function_commitDpos(0)
					API.node().wait_gen_block()
					(process, response) = nodeCountCheck(response,7)
					(process, response) = invoke_function_candidate("whiteNode",test_config.whiteNode_pubKey_1, 0)
					API.node().wait_gen_block()
					(process, response) = nodeCountCheck(response,7)
				else:
					nodeCountCheck(response,7)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_037_whiteNode(self):
		try:
			(process, response) = invoke_function_candidate("whiteNode",test_config.whiteNode_pubKey_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_038_whiteNode(self):
		try:
			(process, response) = invoke_function_candidate("whiteNode",test_config.whiteNode_pubKey_3)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_039_whiteNode(self):
		try:
			(process, response) = invoke_function_candidate("whiteNode",test_config.whiteNode_pubKey_4)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_040_whiteNode(self):
		try:
			(process, response) = invoke_function_candidate("whiteNode",test_config.whiteNode_pubKey_5)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])	



class test_governance_api_6(ParametrizedTestCase):
	def setUp(self):
		#restart all node
		if self._testMethodName == "test_init":
			return
		logger.open( "test_governance_api/" +self._testMethodName + ".log",self._testMethodName)
		init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		# register ONTID

		
	def tearDown(self):
		if self._testMethodName == "test_init":
			return
		logger.close(self.result())	
		
	def test_base_041_quitNode(self):
		try:
			#time.sleep(10)
			(process, response) = invoke_function_register("registerCandidate",test_config.quitNode_pubKey_1,test_config.quitNode_walletAddress_1,test_config.quitNode_ontCount_2,test_config.quitNode_ontID_1,test_config.quitNode_user_1,0)#准备共识节点
			API.node().wait_gen_block()
			(process, response) = invoke_function_candidate("approveCandidate",test_config.quitNode_pubKey_1,0)
			API.node().wait_gen_block()
			if process:#正式开始测试
				(process, response) = invoke_function_commitDpos(0)
				API.node().wait_gen_block()
				(process, response) = nodeCountCheck(response,8)
				(process, response) = invoke_function_quitNode("quitNode",test_config.quitNode_pubKey_1,test_config.quitNode_walletAddress_1,test_config.quitNode_pubKey_1_node,errorcode=0)
				if process:
					API.node().wait_gen_block()
					(process, response) = invoke_function_commitDpos(0)
					API.node().wait_gen_block()
					(process, response) = nodeCountCheck(response,8)
					if process:
						API.node().wait_gen_block()
						(process, response) = invoke_function_commitDpos(0)
						API.node().wait_gen_block()
						(process, response) = nodeCountCheck(response,7)
				else:
					nodeCountCheck(response,7)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_042_quitNode(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.quitNode_pubKey_pre,test_config.quitNode_walletAddress_1,test_config.quitNode_ontCount_1,test_config.quitNode_ontID_1,test_config.quitNode_user_1,0)#准备候选节点
			API.node().wait_gen_block()
			(process, response) = invoke_function_candidate("approveCandidate",test_config.quitNode_pubKey_pre,0)
			API.node().wait_gen_block()
			if process:#正式开始测试
				(process, response) = nodeCountCheck(response,8)
				(process, response) = invoke_function_quitNode("quitNode",test_config.quitNode_pubKey_2,test_config.quitNode_walletAddress_1,test_config.quitNode_pubKey_2_node,0)
				if process:
					API.node().wait_gen_block()
					(process, response) = invoke_function_commitDpos(0)
					API.node().wait_gen_block()
					(process, response) = nodeCountCheck(response,7)
				else:
					nodeCountCheck(response,7)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_043_quitNode(self):
		try:
			(process, response) = invoke_function_quitNode("quitNode",test_config.quitNode_pubKey_3,test_config.quitNode_walletAddress,node_index=test_config.quitNode_pubKey_3_node)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
			
	def test_abnormal_044_quitNode(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.quitNode_pubKey_pre,test_config.quitNode_walletAddress_1,test_config.quitNode_ontCount_1,test_config.quitNode_ontID_1,test_config.quitNode_user_1,0)#准备注册节点
			if process:#正式开始测试
				API.node().wait_gen_block()
				(process, response) = invoke_function_quitNode("quitNode",test_config.quitNode_pubKey_4,test_config.quitNode_walletAddress,node_index=test_config.quitNode_pubKey_4_node)
			else:
				nodeCountCheck(response,7)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_045_quitNode(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.quitNode_pubKey_5,test_config.quitNode_walletAddress_1,test_config.quitNode_ontCount_1,test_config.quitNode_ontID_1,test_config.quitNode_user_1,0)#准备黑名单节点
			API.node().wait_gen_block()
			(process, response) = invoke_function_node("blackNode",test_config.quitNode_pubKey_5,0)
			if process:#正式开始测试
				API.node().wait_gen_block()
				(process, response) = nodeCountCheck(response,7)
				(process, response) = invoke_function_quitNode("quitNode",test_config.quitNode_pubKey_5,test_config.quitNode_walletAddress,node_index=test_config.quitNode_pubKey_5_node)
			else:
				nodeCountCheck(response,7)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_046_quitNode(self):
		try:
			(process, response) = invoke_function_quitNode("quitNode",test_config.quitNode_pubKey_6,test_config.quitNode_walletAddress,node_index=test_config.quitNode_pubKey_6_node)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_047_quitNode(self):
		try:
			(process, response) = invoke_function_quitNode("quitNode",test_config.quitNode_pubKey_7,test_config.quitNode_walletAddress,node_index=test_config.quitNode_pubKey_7_node)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])	



class test_governance_api_7(ParametrizedTestCase):
	def setUp(self):
		#restart all node
		if self._testMethodName == "test_init":
			return
		logger.open( "test_governance_api/" +self._testMethodName + ".log",self._testMethodName)
		init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(10)

	def tearDown(self):
		if self._testMethodName == "test_init":
			return
		logger.close(self.result())
				

	def test_base_048_VoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_1,test_config.voteForPeer_voteList_1,test_config.voteForPeer_voteCount_1,0,test_config.voteForPeer_walletNode_1)
			nodeCountCheck(response,7)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_049_VoteForPeer(self):
		try:
			(process, response) = native_transfer_ont(test_config.voteForPeer_walletAddress_1,test_config.voteForPeer_walletAddress_2,500,node_index1=test_config.voteForPeer_walletNode_1,errorcode1=0)
			if process:
				time.sleep(10)
				(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_2,test_config.voteForPeer_voteList_1,test_config.voteForPeer_voteCount_1,node_index=test_config.voteForPeer_walletNode_1)
				time.sleep(2)
				nodeCountCheck(response,7)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_050_VoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_3,test_config.voteForPeer_voteList_1,test_config.voteForPeer_voteCount_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
			
	def test_abnormal_051_VoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_4,test_config.voteForPeer_voteList_1,test_config.voteForPeer_voteCount_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_052_VoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_1,test_config.voteForPeer_voteList_1,test_config.voteForPeer_voteCount_1,0,test_config.voteForPeer_walletNode_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_053_VoteForPeer(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.voteForPeer_pubKey_pre,test_config.voteForPeer_walletAddress_pre,test_config.voteForPeer_ontCount_1,test_config.voteForPeer_ontID_1,test_config.voteForPeer_user_1,0)
			time.sleep(15)
			(process, response) = invoke_function_candidate("approveCandidate",test_config.voteForPeer_pubKey_pre,0)
			time.sleep(15)
			if process:
				(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_1,test_config.voteForPeer_voteList_2,test_config.voteForPeer_voteList_2_count,0,node_index=test_config.voteForPeer_walletNode_1)
				time.sleep(2)
				nodeCountCheck(response,7)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_054_VoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_1,test_config.voteForPeer_voteList_3,test_config.voteForPeer_voteList_2_count,node_index=test_config.voteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_055_VoteForPeer(self):
		try:
			(process, response) = invoke_function_register("registerCandidate",test_config.voteForPeer_pubKey_pre,test_config.voteForPeer_walletAddress_pre,test_config.voteForPeer_ontCount_1,test_config.voteForPeer_ontID_1,test_config.voteForPeer_user_1,0)
			if process:
				time.sleep(15)
				(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_1,test_config.voteForPeer_voteList_4,test_config.voteForPeer_voteList_2_count,node_index=test_config.voteForPeer_walletNode_1)
				time.sleep(2)
				nodeCountCheck(response,7)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_056_VoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_1,test_config.voteForPeer_voteList_5,test_config.voteForPeer_voteList_2_count,node_index=test_config.voteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_057_VoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_1,test_config.voteForPeer_voteList_6,test_config.voteForPeer_voteList_2_count,node_index=test_config.voteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_058_VoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_1,test_config.voteForPeer_voteList_1,test_config.voteForPeer_voteCount_1,0,node_index=test_config.voteForPeer_walletNode_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_059_VoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_1,test_config.voteForPeer_voteList_1,test_config.voteForPeer_voteCount_2,node_index=test_config.voteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_060_VoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_1,test_config.voteForPeer_voteList_1,test_config.voteForPeer_voteCount_3,node_index=test_config.voteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_061_VoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_1,test_config.voteForPeer_voteList_1,test_config.voteForPeer_voteCount_4,node_index=test_config.voteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_062_VoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_1,test_config.voteForPeer_voteList_1,test_config.voteForPeer_voteCount_5,node_index=test_config.voteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_063_VoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_1,test_config.voteForPeer_voteList_6,test_config.voteForPeer_voteCount_5,node_index=test_config.voteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])	
'''
	#temporarily add
	def test_abnormal_065_VoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_1,test_config.voteForPeer_voteList_all1,test_config.voteForPeer_voteCount_all,node_index=test_config.voteForPeer_walletNode_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
			
	def test_abnormal_066_VoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.voteForPeer_walletAddress_1,test_config.voteForPeer_voteList_all_err,test_config.voteForPeer_voteCount_all_err,node_index=test_config.voteForPeer_walletNode_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])	
'''



class test_governance_api_8(ParametrizedTestCase):
	def setUp(self):
		#restart all node
		if self._testMethodName == "test_init":
			return
		logger.open( "test_governance_api/" +self._testMethodName + ".log",self._testMethodName)
		init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		#pass
		# register ONTID
		
	def tearDown(self):
		if self._testMethodName == "test_init":
			return
		logger.close(self.result())
		

	def test_base_064_unVoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.unVoteForPeer_walletAddress_1,test_config.unVoteForPeer_voteList_1,test_config.unVoteForPeer_voteCount_1,0,test_config.unVoteForPeer_walletNode_1)#准备工作，先投票
			if process:#实际开始
				(process, response) = invoke_function_vote("unVoteForPeer",test_config.unVoteForPeer_walletAddress_1,test_config.unVoteForPeer_voteList_1,test_config.unVoteForPeer_voteCount_1,0,node_index=test_config.unVoteForPeer_walletNode_1)
				time.sleep(2)
				nodeCountCheck(response,7)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_065_unVoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.unVoteForPeer_walletAddress_1,test_config.unVoteForPeer_voteList_1,test_config.unVoteForPeer_voteCount_1,0,test_config.unVoteForPeer_walletNode_1)#准备工作，先投票
			if process:#实际开始
				time.sleep(10)
				(process, response) = invoke_function_vote("unVoteForPeer",test_config.unVoteForPeer_walletAddress_2,test_config.unVoteForPeer_voteList_1,test_config.unVoteForPeer_voteCount_1,node_index=test_config.unVoteForPeer_walletNode_1)
				time.sleep(2)
				nodeCountCheck(response,7)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_066_unVoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("unVoteForPeer",test_config.unVoteForPeer_walletAddress_3,test_config.unVoteForPeer_voteList_1,test_config.unVoteForPeer_voteCount_1,node_index=test_config.unVoteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
			
	def test_abnormal_067_unVoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("unVoteForPeer",test_config.unVoteForPeer_walletAddress_4,test_config.unVoteForPeer_voteList_1,test_config.unVoteForPeer_voteCount_1,node_index=test_config.unVoteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_068_unVoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.unVoteForPeer_walletAddress_1,test_config.unVoteForPeer_voteList_1,test_config.unVoteForPeer_voteCount_1,0,test_config.unVoteForPeer_walletNode_1)#准备工作，先投票
			if process:#实际开始
				time.sleep(10)
				(process, response) = invoke_function_vote("unVoteForPeer",test_config.unVoteForPeer_walletAddress_1,test_config.unVoteForPeer_voteList_1,test_config.unVoteForPeer_voteCount_1,0,node_index=test_config.unVoteForPeer_walletNode_1)
				time.sleep(2)
				nodeCountCheck(response,7)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_069_unVoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("unVoteForPeer",test_config.unVoteForPeer_walletAddress_1,test_config.unVoteForPeer_voteList_2,test_config.unVoteForPeer_voteCount_1,node_index=test_config.unVoteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_070_unVoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("unVoteForPeer",test_config.unVoteForPeer_walletAddress_1,test_config.unVoteForPeer_voteList_3,test_config.unVoteForPeer_voteCount_1,node_index=test_config.unVoteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_071_unVoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("unVoteForPeer",test_config.unVoteForPeer_walletAddress_1,test_config.unVoteForPeer_voteList_4,test_config.unVoteForPeer_voteCount_3,node_index=test_config.unVoteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_072_unVoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("unVoteForPeer",test_config.unVoteForPeer_walletAddress_1,test_config.unVoteForPeer_voteList_5,test_config.unVoteForPeer_voteCount_3,node_index=test_config.unVoteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_073_unVoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("voteForPeer",test_config.unVoteForPeer_walletAddress_1,test_config.unVoteForPeer_voteList_1,test_config.unVoteForPeer_voteCount_1,0,test_config.unVoteForPeer_walletNode_1)#准备工作，先投票
			if process:#实际开始
				time.sleep(10)
				(process, response) = invoke_function_vote("unVoteForPeer",test_config.unVoteForPeer_walletAddress_1,test_config.unVoteForPeer_voteList_1,test_config.unVoteForPeer_voteCount_1,0,node_index=test_config.unVoteForPeer_walletNode_1)
				time.sleep(2)
				nodeCountCheck(response,7)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_074_unVoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("unVoteForPeer",test_config.unVoteForPeer_walletAddress_1,test_config.unVoteForPeer_voteList_1,test_config.unVoteForPeer_voteCount_2,node_index=test_config.unVoteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_075_unVoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("unVoteForPeer",test_config.unVoteForPeer_walletAddress_1,test_config.unVoteForPeer_voteList_1,test_config.unVoteForPeer_voteCount_3,node_index=test_config.unVoteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_076_unVoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("unVoteForPeer",test_config.unVoteForPeer_walletAddress_1,test_config.unVoteForPeer_voteList_1,test_config.unVoteForPeer_voteCount_4,node_index=test_config.unVoteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_077_unVoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("unVoteForPeer",test_config.unVoteForPeer_walletAddress_1,test_config.unVoteForPeer_voteList_1,test_config.unVoteForPeer_voteCount_5,node_index=test_config.unVoteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_078_unVoteForPeer(self):
		try:
			(process, response) = invoke_function_vote("unVoteForPeer",test_config.unVoteForPeer_walletAddress_1,test_config.unVoteForPeer_voteList_5,test_config.unVoteForPeer_voteCount_5,node_index=test_config.unVoteForPeer_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])	



class test_governance_api_9(ParametrizedTestCase):
	def setUp(self):
		if self._testMethodName == "test_init":
			return
		logger.open( "test_governance_api/" +self._testMethodName + ".log",self._testMethodName)
		init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(10)
		(process, response) = invoke_function_vote("voteForPeer",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_1,test_config.withdraw_voteCount_Pre,0,test_config.withdraw_walletNode_1)
		(process, response) = invoke_function_vote("voteForPeer",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_2,test_config.withdraw_voteCount_Pre,0,test_config.withdraw_walletNode_1)
		time.sleep(5)
		(process, response) = invoke_function_vote("unVoteForPeer",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_1,test_config.withdraw_voteCount_Pre,0,node_index=test_config.withdraw_walletNode_1)
		time.sleep(5)
		(process, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		
	def tearDown(self):
		if self._testMethodName == "test_init":
			return
		logger.close(self.result())
		
	def test_base_079_withdraw(self):
		try:
			# getStorageVoteInfo(Config.NODES[0]["pubkey"],Config.NODES[7]["address"])
			# getStorageVoteInfo(Config.NODES[1]["pubkey"],Config.NODES[7]["address"])
			# (process, response) = invoke_function_vote("voteForPeer",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_1,test_config.withdraw_voteCount_Pre,0,test_config.withdraw_walletNode_1)
			# (process, response) = invoke_function_vote("voteForPeer",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_2,test_config.withdraw_voteCount_Pre,0,test_config.withdraw_walletNode_1)
			# time.sleep(5)
			# getStorageVoteInfo(Config.NODES[0]["pubkey"],Config.NODES[7]["address"])
			# getStorageVoteInfo(Config.NODES[1]["pubkey"],Config.NODES[7]["address"])
			# (process, response) = invoke_function_vote("unVoteForPeer",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_1,test_config.withdraw_voteCount_Pre,0,node_index=test_config.withdraw_walletNode_1)
			time.sleep(5)
			(process, response) = invoke_function_commitDpos(0)
			time.sleep(5)
			(process, response) = invoke_function_commitDpos(0)
			time.sleep(5)
			(process, response) = invoke_function_commitDpos(0)
			time.sleep(5)
			getStorageVoteInfo(Config.NODES[0]["pubkey"],Config.NODES[7]["address"])
			getStorageVoteInfo(Config.NODES[1]["pubkey"],Config.NODES[7]["address"])
			(process, response) = invoke_function_vote("withdraw",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_1,test_config.withdraw_voteCount_1,0,node_index=test_config.withdraw_walletNode_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_080_withdraw(self):
		try:
			(process, response) = invoke_function_vote("withdraw",test_config.withdraw_walletAddress_2,test_config.withdraw_voteList_1,test_config.withdraw_voteCount_1,node_index=test_config.withdraw_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_081_withdraw(self):
		try:
			(process, response) = invoke_function_vote("withdraw",test_config.withdraw_walletAddress_3,test_config.withdraw_voteList_1,test_config.withdraw_voteCount_1,node_index=test_config.withdraw_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
			
	def test_abnormal_082_withdraw(self):
		try:
			(process, response) = invoke_function_vote("withdraw",test_config.withdraw_walletAddress_4,test_config.withdraw_voteList_1,test_config.withdraw_voteCount_1,0,node_index=test_config.withdraw_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_083_withdraw(self):
		try:
			(process, response) = invoke_function_vote("withdraw",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_1,test_config.withdraw_voteCount_1,node_index=test_config.withdraw_walletNode_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_084_withdraw(self):
		try:
			(process, response) = invoke_function_vote("withdraw",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_2,test_config.withdraw_voteCount_1,node_index=test_config.withdraw_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_085_withdraw(self):
		try:
			(process, response) = invoke_function_vote("withdraw",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_3,test_config.withdraw_voteCount_1,node_index=test_config.withdraw_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_086_withdraw(self):
		try:
			(process, response) = invoke_function_vote("withdraw",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_4,test_config.withdraw_voteCount_1,node_index=test_config.withdraw_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_087_withdraw(self):
		try:
			(process, response) = invoke_function_vote("withdraw",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_5,test_config.withdraw_voteCount_1,node_index=test_config.withdraw_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_088_withdraw(self):
		try:
			(process, response) = invoke_function_commitDpos(0)
			time.sleep(5)
			(process, response) = invoke_function_commitDpos(0)
			time.sleep(5)
			getStorageVoteInfo(Config.NODES[0]["pubkey"],Config.NODES[7]["address"])
			getStorageVoteInfo(Config.NODES[1]["pubkey"],Config.NODES[7]["address"])
			(process, response) = invoke_function_vote("withdraw",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_1,test_config.withdraw_voteCount_1,0,node_index=test_config.withdraw_walletNode_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_089_withdraw(self):
		try:
			(process, response) = invoke_function_vote("withdraw",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_1,test_config.withdraw_voteCount_2,node_index=test_config.withdraw_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_090_withdraw(self):
		try:
			(process, response) = invoke_function_vote("withdraw",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_1,test_config.withdraw_voteCount_3,node_index=test_config.withdraw_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_091_withdraw(self):
		try:
			(process, response) = invoke_function_vote("withdraw",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_1,test_config.withdraw_voteCount_4,node_index=test_config.withdraw_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_092_withdraw(self):
		try:
			(process, response) = invoke_function_vote("withdraw",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_1,test_config.withdraw_voteCount_5,node_index=test_config.withdraw_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_093_withdraw(self):
		try:
			(process, response) = invoke_function_vote("withdraw",test_config.withdraw_walletAddress_1,test_config.withdraw_voteList_5,test_config.withdraw_voteCount_5,node_index=test_config.withdraw_walletNode_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])



class test_governance_api_10(ParametrizedTestCase):
	def test_init(self):
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		#pass
	def setUp(self):
		if self._testMethodName == "test_init":
			return
		logger.open( "test_governance_api/" +self._testMethodName + ".log",self._testMethodName)
		
	def tearDown(self):
		if self._testMethodName == "test_init":
			return
		logger.close(self.result())
	
	def test_base_094_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_095_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_2,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_normal_096_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_3,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
			
	def test_normal_097_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_4,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_098_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_5,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_abnormal_099_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_6,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_100_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_101_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_2,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_102_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_3,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_103_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_4,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_abnormal_104_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_5,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_normal_105_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_abnormal_106_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_2,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_abnormal_107_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_3,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_normal_108_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_4,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_normal_109_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_abnormal_110_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_2,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_normal_111_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_3,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
    
    

    
	def test_normal_112_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_4,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_abnormal_113_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_5,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_abnormal_114_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_6,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_normal_115_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_normal_116_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_2,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_abnormal_117_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_3,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_abnormal_118_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_4,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_abnormal_119_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_5,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_normal_120_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_normal_121_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_2,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_abnormal_122_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_3,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
			
	def test_abnormal_123_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_4,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_124_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_5,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_125_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_126_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_2,test_config.updateConfig_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_127_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_3,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_128_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_4,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_129_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_5,test_config.updateConfig_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_130_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_131_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_2)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_132_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_3)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
    
	def test_abnormal_133_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_4)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_134_updateConfig(self):
		try:
			(process, response) = invoke_function_update("updateConfig",test_config.updateConfig_param0_1,test_config.updateConfig_param1_1,test_config.updateConfig_param2_1,test_config.updateConfig_param3_1,test_config.updateConfig_param4_1,test_config.updateConfig_param5_1,test_config.updateConfig_param6_1,test_config.updateConfig_param7_5)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])



class test_governance_api_11(ParametrizedTestCase):
	def setUp(self):
		if self._testMethodName == "test_init":
			return
		logger.open( "test_governance_api/" +self._testMethodName + ".log",self._testMethodName)

	def tearDown(self):
		if self._testMethodName == "test_init":
			return
		logger.close(self.result())
		
	def test_base_135_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_136_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_2,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_137_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_3,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1,errorkey="error_code",errorcode=900)
			self.ASSERT(not process, "")
		except Exception as e:
			# self.ASSERT(True, "")
			logger.print(e.args[0])
	
	def test_normal_138_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_4,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_139_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_5,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_140_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_141_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_2,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_142_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_3,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_143_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_4,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_144_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_5,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_145_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_146_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_2,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_147_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_3,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_148_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_4,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_149_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_5,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_150_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_151_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_2,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_152_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_3,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_153_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_4,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_154_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_5,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_155_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_6,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_156_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_157_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_2,test_config.updateGlobalParam_param5_2,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_158_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_3,test_config.updateGlobalParam_param5_3,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_159_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_4,test_config.updateGlobalParam_param5_4,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_160_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_5,test_config.updateGlobalParam_param5_5,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_161_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_6,test_config.updateGlobalParam_param5_6,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_162_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_163_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_2,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	def test_abnormal_164_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_3,test_config.updateGlobalParam_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_165_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_4,test_config.updateGlobalParam_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_166_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_5,test_config.updateGlobalParam_param7_1)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_167_updateGlobalParam(self): 
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_1)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_normal_168_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_1,test_config.updateGlobalParam_param7_2)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_169_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_2,test_config.updateGlobalParam_param7_3)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_170_updateGlobalParam(self):
		try:
			(process, response) = invoke_function_update("updateGlobalParam",test_config.updateGlobalParam_param0_1,test_config.updateGlobalParam_param1_1,test_config.updateGlobalParam_param2_1,test_config.updateGlobalParam_param3_1,test_config.updateGlobalParam_param4_1,test_config.updateGlobalParam_param5_1,test_config.updateGlobalParam_param6_3,test_config.updateGlobalParam_param7_4)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])



class test_governance_api_12(ParametrizedTestCase):
	def setUp(self):
		if self._testMethodName == "test_init":
			return
		logger.open( "test_governance_api/" +self._testMethodName + ".log",self._testMethodName)

	def tearDown(self):
		if self._testMethodName == "test_init":
			return
		logger.close(self.result())
		
	def test_base_171_updateSplitCurve(self):
		try:
			(process, response) = invoke_function_SplitCurve("updateSplitCurve",test_config.updateSplitCurve_array_1)
			getStorageConf("splitCurve")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_172_updateSplitCurve(self):
		try:
			(process, response) = invoke_function_SplitCurve("updateSplitCurve",test_config.updateSplitCurve_array_2)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_173_updateSplitCurve(self):
		try:
			(process, response) = invoke_function_SplitCurve("updateSplitCurve",test_config.updateSplitCurve_array_3)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

	def test_abnormal_174_updateSplitCurve(self):
		try:
			(process, response) = invoke_function_SplitCurve("updateSplitCurve",test_config.updateSplitCurve_array_4)
			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])



class test_governance_api_13(ParametrizedTestCase):
		
	def setUp(self):
		if self._testMethodName == "test_init":
			return
		logger.open( "test_governance_api/" +self._testMethodName + ".log",self._testMethodName)
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		(process, response) = invoke_function_register("registerCandidate", test_config.transferPenalty_pubKey_1,
													   test_config.transferPenalty_walletAddress_pre,
													   test_config.transferPenalty_ontCount_1,
													   test_config.transferPenalty_ontID_1,
													   test_config.transferPenalty_user_1, 0)
		API.node().wait_gen_block()
		(process, response) = invoke_function_node("blackNode", test_config.transferPenalty_pubKey_1, 0)
		API.node().wait_gen_block()
		#time.sleep(15)

	def tearDown(self):
		logger.close(self.result())
		
	def test_base_175_transferPenalty(self):
		try:
			API.native().commit_dpos()
			API.node().wait_gen_block()
			(process, response)=API.rpc().getbalance(test_config.transferPenalty_walletAddress_1)
			ong=response["result"]["ong"]
			ont=response["result"]["ont"]
			(process, response) = invoke_function_TransferPenalty("transferPenalty",test_config.transferPenalty_pubKey_1,test_config.transferPenalty_walletAddress_1)
			API.node().wait_gen_block()
			time.sleep(5)
			if process:
				(process, response1)=API.rpc().getbalance(test_config.transferPenalty_walletAddress_1)
				ontAdd=int(response1["result"]["ont"])-int(ont)
				if ontAdd>0:
					process=True
				else:
					process=False

			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_176_transferPenalty(self):
		try:
			API.native().commit_dpos()
			API.node().wait_gen_block()
			(process, response)=API.rpc().getbalance(test_config.transferPenalty_walletAddress_1)
			ong=response["result"]["ong"]
			ont=response["result"]["ont"]
			(process, response) = invoke_function_TransferPenalty("transferPenalty",test_config.transferPenalty_pubKey_2,test_config.transferPenalty_walletAddress_1)
			API.node().wait_gen_block()
			time.sleep(5)
			if process:
				(process, response1)=API.rpc().getbalance(test_config.transferPenalty_walletAddress_1)
				ontAdd=int(response1["result"]["ont"])-int(ont)
				if ontAdd>0:
					process=True
				else:
					process=False

			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_177_transferPenalty(self):
		try:
			API.native().commit_dpos()
			API.node().wait_gen_block()
			(process, response)=API.rpc().getbalance(test_config.transferPenalty_walletAddress_1)
			ong=response["result"]["ong"]
			ont=response["result"]["ont"]
			(process, response) = invoke_function_TransferPenalty("transferPenalty",test_config.transferPenalty_pubKey_3,test_config.transferPenalty_walletAddress_1)
			API.node().wait_gen_block()
			time.sleep(5)
			if process:
				(process, response1)=API.rpc().getbalance(test_config.transferPenalty_walletAddress_1)
				ontAdd=int(response1["result"]["ont"])-int(ont)
				if ontAdd>0:
					process=True
				else:
					process=False

			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_178_transferPenalty(self):
		try:
			API.native().commit_dpos()
			API.node().wait_gen_block()
			(process, response)=API.rpc().getbalance(test_config.transferPenalty_walletAddress_1)
			ong=response["result"]["ong"]
			ont=response["result"]["ont"]
			(process, response) = invoke_function_candidate("whiteNode",test_config.transferPenalty_pubKey_1, 0)
			API.node().wait_gen_block()
			time.sleep(5)
			if process:
				(process, response) = invoke_function_commitDpos(0)
				(process, response) = invoke_function_TransferPenalty("transferPenalty",test_config.transferPenalty_pubKey_1,test_config.transferPenalty_walletAddress_1)
				if process:
					(process, response1)=API.rpc().getbalance(test_config.transferPenalty_walletAddress_1)
					ontAdd=int(response1["result"]["ont"])-int(ont)
					if ontAdd>0:
						process=True
					else:
						process=False


			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_179_transferPenalty(self):
		try:
			API.native().commit_dpos()
			API.node().wait_gen_block()
			(process, response)=API.rpc().getbalance(test_config.transferPenalty_walletAddress_1)
			ong=response["result"]["ong"]
			ont=response["result"]["ont"]
			(process, response) = invoke_function_TransferPenalty("transferPenalty",test_config.transferPenalty_pubKey_5,test_config.transferPenalty_walletAddress_1)
			API.node().wait_gen_block()
			time.sleep(5)
			if process:
				(process, response1)=API.rpc().getbalance(test_config.transferPenalty_walletAddress_1)
				ontAdd=int(response1["result"]["ont"])-int(ont)
				if ontAdd>0:
					process=True
				else:
					process=False


			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_180_transferPenalty(self):
		try:
			API.native().commit_dpos()
			API.node().wait_gen_block()
			(process, response)=API.rpc().getbalance(test_config.transferPenalty_walletAddress_1)
			ong=response["result"]["ong"]
			ont=response["result"]["ont"]
			(process, response) = invoke_function_TransferPenalty("transferPenalty",test_config.transferPenalty_pubKey_6,test_config.transferPenalty_walletAddress_1)
			API.node().wait_gen_block()
			time.sleep(5)
			if process:
				(process, response1)=API.rpc().getbalance(test_config.transferPenalty_walletAddress_1)
				ontAdd=int(response1["result"]["ont"])-int(ont)
				if ontAdd>0:
					process=True
				else:
					process=False

			self.ASSERT(not process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_181_transferPenalty(self):
		try:
			API.native().commit_dpos()
			API.node().wait_gen_block()
			(process, response)=API.rpc().getbalance(test_config.transferPenalty_walletAddress_1)
			ong=response["result"]["ong"]
			ont=response["result"]["ont"]
			(process, response) = invoke_function_TransferPenalty("transferPenalty",test_config.transferPenalty_pubKey_1,test_config.transferPenalty_walletAddress_1)
			API.node().wait_gen_block()
			time.sleep(5)
			if process:
				(process, response1)=API.rpc().getbalance(test_config.transferPenalty_walletAddress_1)
				ontAdd=int(response1["result"]["ont"])-int(ont)
				if ontAdd>0:
					process=True
				else:
					process=False

			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_normal_182_transferPenalty(self):
		try:
			API.native().commit_dpos()
			API.node().wait_gen_block()
			(process, response)=API.rpc().getbalance(test_config.transferPenalty_walletAddress_2)
			ong=response["result"]["ong"]
			ont=response["result"]["ont"]
			(process, response) = invoke_function_TransferPenalty("transferPenalty",test_config.transferPenalty_pubKey_1,test_config.transferPenalty_walletAddress_2)
			API.node().wait_gen_block()
			time.sleep(5)
			if process:
				(process, response1)=API.rpc().getbalance(test_config.transferPenalty_walletAddress_2)
				ontAdd=int(response1["result"]["ont"])-int(ont)
				if ontAdd>0:
					process=True
				else:
					process=False


			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
	
	def test_abnormal_183_transferPenalty(self):
		try:
			(process, response) = invoke_function_TransferPenalty("transferPenalty",test_config.transferPenalty_pubKey_1,test_config.transferPenalty_walletAddress_3,errorkey="error_code",errorcode=900)

			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
			self.ASSERT(True, "")
	
	def test_abnormal_184_transferPenalty(self):
		try:
			
			(process, response) = invoke_function_TransferPenalty("transferPenalty",test_config.transferPenalty_pubKey_1,test_config.transferPenalty_walletAddress_4,errorkey="error_code",errorcode=900)
			
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
			self.ASSERT(True, "")
			
####################################################
if __name__ == '__main__':
	unittest.main()