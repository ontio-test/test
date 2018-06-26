# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt
import time
sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.contractapi import *
from test_api import *
#from test_ontid_config import *
from utils.commonapi import call_contract

logger = LoggerInstance

#######################################################
#node info
#ontid_map=[]
node_self = 5
ontID_self_pubKey = Config.SERVICES[node_self]["pubkey"]
#ontid_map[node_self] = ontID_self_pubKey

node_A = 1
ontID_A_pubkey = Config.SERVICES[node_A]["pubkey"]
#ontid_map[ontID_A] = ontID_A_pubkey

node_B = 6
ontID_B_pubkey = Config.SERVICES[node_B]["pubkey"]
#ontid_map[ontID_B] = ontID_B_pubkey
####################################################
#config
tc001_ontid="did:ont:AR72FVnZZ8EfeyyhGobEVWox9jwd7Uqe8d"
tc002_ontid="did:ont:AQhDgYDY42AwfBdRDu1Wnf224EXKQ5ypGc"
tc002_ontid2="did:ont:AGuu4L6LQiBGtCNXaCm35mDJGX6Hf1Fdev"
tc003_ontid="did:ont:AR7jzsPWSqJTM7hf41jDbTVUgpurVGBvfk"
tc004_ontid="did:ont:AMrKfXtwdCaxkF8cCGYodz5FXD1GcwbW7M"
tc001_pubkey1=ontID_A_pubkey
tc001_pubkey2=ontID_self_pubKey
tc002_pubkey1=ontID_A_pubkey
tc002_pubkey2=ontID_self_pubKey
tc003_pubkey1=ontID_A_pubkey
tc003_pubkey2=ontID_self_pubKey
tc004_pubkey1=ontID_A_pubkey
tc004_pubkey2=ontID_self_pubKey
tc004_pubkey3=ontID_B_pubkey
#############################################
#test cases
class TestContract(ParametrizedTestCase):
	# # @classmethod
  # # def setUpClass(self):
		# ###
    # init_server()
		
	def start(self, log_path):
		logger.open(log_path)

	def finish(self, task_name, log_path, result, msg):
		if result:
			logger.print("[ OK       ] ")
			logger.append_record(task_name, "pass", log_path)
		else:
			logger.print("[ Failed   ] " + msg)
			logger.append_record(task_name, "fail", log_path)
		logger.close()
	def test_001(self):
		log_path = "001_ontid_others.log"
		task_name = "001_ontid_others"
		self.start(log_path)
		##pre
		(result, response) = regIDWithPublicKey(tc001_ontid, tc001_pubkey2,node_self,0)
		(result, response) = addKey(tc001_ontid, tc001_pubkey1,tc001_pubkey2,node_self,0)
		#####case start
		(result, response) = removeKey(tc001_ontid, tc001_pubkey1,tc001_pubkey2,node_self,0)
		(result, response) = addKey(tc001_ontid, tc001_pubkey1,tc001_pubkey2,node_self)
		(result, response) = getKeyState(tc001_ontid, "2",tc001_pubkey2,node_self,0,"revoked")
		if not result:
			raise Error("failed")
		(result, response) = getKeyState(tc001_ontid,"1",tc001_pubkey2,node_self,0,"in use")
		if not result:
			raise Error("failed")
		self.finish(task_name, log_path, result,  "")


	def test_002(self):
		log_path = "002_ontid_others.log"
		task_name = "002_ontid_others"
		self.start(log_path)
		##pre
		(result, response) = regIDWithPublicKey(tc002_ontid, tc002_pubkey2,node_self,0)
		(result, response) = addKey(tc002_ontid, tc002_pubkey1,tc002_pubkey2,node_self,0)
		#####case start
		(result, response) = removeKey(tc002_ontid, tc002_pubkey1,tc002_pubkey2,node_self,0)
		if not result:
			raise Error("failed")
		(result, response) = regIDWithPublicKey(tc002_ontid2, tc002_pubkey1,node_A,0)
		self.finish(task_name, log_path, result,  "")


	def test_003(self):
		log_path = "003_ontid_others.log"
		task_name = "003_ontid_others"
		self.start(log_path)
		##pre
		(result, response) = regIDWithPublicKey(tc003_ontid, tc003_pubkey2,node_self,0)
		(result, response) = addKey(tc003_ontid, tc003_pubkey1,tc003_pubkey2,node_self,0)
		#####case start
		(result, response) = removeKey(tc003_ontid, tc003_pubkey1,tc003_pubkey1,node_A,0)
		self.finish(task_name, log_path, result,  "")


	def test_004(self):
		try:
			log_path = "004_ontid_others.log"
			task_name = "004_ontid_others"
			self.start(log_path)
			##pre
			(result, response) = regIDWithPublicKey(tc004_ontid, tc004_pubkey2,node_self,0)
			(result, response) = addKey(tc004_ontid, tc004_pubkey1,tc004_pubkey2,node_self,0)
			#####case start
			(result, response) = removeKey(tc004_ontid, tc004_pubkey1,tc004_pubkey1,node_A,0)
			(result, response) = addKey(tc004_ontid, tc004_pubkey3,tc004_pubkey2,node_self,0)
			(result, response) = removeKey(tc004_ontid, tc004_pubkey2,tc004_pubkey2,node_self,0)
			(result, response) = getKeyState(tc004_ontid, "1",tc004_pubkey3,node_B,0,"revoked")
			if not result:
				raise Error("failed")
				
			(result, response) = getKeyState(tc004_ontid, "2",tc004_pubkey3,node_B,0,"revoked")
			if not result:
				raise Error("failed")
				
			(result, response) = getKeyState(tc004_ontid, "3",tc004_pubkey3,node_B,0,"in use")
			if not result:
				raise Error("failed")
				
		except Error as err:
			print("failed")
			
		self.finish(task_name, log_path, result,  "")

####################################################
if __name__ == '__main__':
	unittest.main()

