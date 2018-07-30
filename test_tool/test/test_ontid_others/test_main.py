# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys
import getopt
import time


sys.path.append('..')
sys.path.append('../..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
#from utils.api.contractapi import *

from test_ontid_others.test_api import *
#from test_ontid_config import *
#from utils.api.commonapi import call_contract
from test_ontid_others.test_config import *


#######################################################
#node info
#ontid_map=[]
#############################################
#test cases
class test_ontid_others_1(ParametrizedTestCase):
	# # @classmethod
  # # def setUpClass(self):
		# ###
    # init_server()
		
		
	def setUp(self):
		logger.open( "test_ontid_others/"+self._testMethodName+".log",self._testMethodName)
		
	def tearDown(self):
		logger.close(self.result())
		
		
	def test_abnormal_001_ontidOthers(self):
		try:
			##pre
			(process, response) = regIDWithPublicKey(test_config.tc001_ontid, test_config.tc001_pubkey2,test_config.node_self,0)
			(process, response) = addKey(test_config.tc001_ontid, test_config.tc001_pubkey1,test_config.tc001_pubkey2,test_config.node_self,0)
			#####case start
			(process, response) = removeKey(test_config.tc001_ontid, test_config.tc001_pubkey1,test_config.tc001_pubkey2,test_config.node_self,0)
			(process, response) = addKey(test_config.tc001_ontid, test_config.tc001_pubkey1,test_config.tc001_pubkey2,test_config.node_self)
			(process, response) = getKeyState(test_config.tc001_ontid, "2",test_config.tc001_pubkey2,test_config.node_self,0,"revoked")
			if not process:
				raise Error("failed")
			(process, response) = getKeyState(test_config.tc001_ontid,"1",test_config.tc001_pubkey2,test_config.node_self,0,"in use")
			if not process:
				raise Error("failed")
				self.ASSERT(not process, "")
		except Error as e:
			logger.print(e.args[0])
		except Exception as e2:
			logger.print(e2.args[0]) 	
		
		
	def test_normal_002_ontidOthers(self):
		try:
			##pre
			(process, response) = regIDWithPublicKey(test_config.tc002_ontid, test_config.tc002_pubkey2,test_config.node_self,0)
			(process, response) = addKey(test_config.tc002_ontid, test_config.tc002_pubkey1,test_config.tc002_pubkey2,test_config.node_self,0)
			#####case start
			(process, response) = removeKey(test_config.tc002_ontid, test_config.tc002_pubkey1,test_config.tc002_pubkey2,test_config.node_self,0)
			if not process:
				raise Error("failed")
			(process, response) = regIDWithPublicKey(test_config.tc002_ontid2, test_config.tc002_pubkey1,test_config.node_A,0)
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.args[0])
		except Exception as e2:
			logger.print(e2.args[0])
		

	def test_normal_003_ontidOthers(self):
		try:
			##pre
			(process, response) = regIDWithPublicKey(test_config.tc003_ontid, test_config.tc003_pubkey2,test_config.node_self,0)
			(process, response) = addKey(test_config.tc003_ontid, test_config.tc003_pubkey1,test_config.tc003_pubkey2,test_config.node_self,0)
			#####case start
			(process, response) = removeKey(test_config.tc003_ontid, test_config.tc003_pubkey1,test_config.tc003_pubkey1,test_config.node_A,0)
			self.ASSERT(process, "")
		except:
			pass
		
		
	def test_normal_004_ontidOthers(self):
		try:
			##pre
			(process, response) = regIDWithPublicKey(test_config.tc004_ontid, test_config.tc004_pubkey2,test_config.node_self,0)
			(process, response) = addKey(test_config.tc004_ontid, test_config.tc004_pubkey1,test_config.tc004_pubkey2,test_config.node_self,0)
			#####case start
			(process, response) = removeKey(test_config.tc004_ontid, test_config.tc004_pubkey1,test_config.tc004_pubkey1,test_config.node_A,0)
			(process, response) = addKey(test_config.tc004_ontid, test_config.tc004_pubkey3,test_config.tc004_pubkey2,test_config.node_self,0)
			(process, response) = removeKey(test_config.tc004_ontid, test_config.tc004_pubkey2,test_config.tc004_pubkey2,test_config.node_self,0)
			(process, response) = getKeyState(test_config.tc004_ontid, "1",test_config.tc004_pubkey3,test_config.node_B,0,"revoked")
			if not process:
				raise Error("failed")
				
			(process, response) = getKeyState(test_config.tc004_ontid, "2",test_config.tc004_pubkey3,test_config.node_B,0,"revoked")
			if not process:
				raise Error("failed")
				
			(process, response) = getKeyState(test_config.tc004_ontid, "3",test_config.tc004_pubkey3,test_config.node_B,0,"in use")
			if not process:
				raise Error("failed")
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.args[0])
		except Exception as e2:
			logger.print(e2.args[0])

	
			

####################################################
if __name__ == '__main__':
	unittest.main()

