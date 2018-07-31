# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

sys.path.append('..')
sys.path.append('../..')
test_path = os.path.dirname(os.path.realpath(__file__))


from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
#from api.rpc import RPCApi
from utils.parametrizedtestcase import ParametrizedTestCase

#from utils.api.commonapi import *

from test_erncryption.test_api import *
from test_erncryption.test_config import test_config
from api.apimanager import API

####################################################
#test cases
class test_erncryption_1(ParametrizedTestCase):
	def test_init(self):
		API.node().stop_all_nodes()  
		API.node().start_nodes(range(0, 7), Config.DEFAULT_NODE_ARGS, clear_chain = True, clear_log = True)
		API.native().init_ont_ong()
		os.system(test_config.nodePath+ "/ontology account import -s "+test_path+"resource/wallettest.dat -w "+test_config.nodePath+"/wallet.dat")
		#deploy_contract #API.contract().deploy_contract();
		test_config.contractaddress=API.contract().deploy_contract(test_path + "/resource/transferong_ont.json")
		
	def setUp(self):
		#os.system(test_config.nodePath+ "/ontology account import -s resource/wallettest.dat -w "+test_config.nodePath+"/wallet.dat")
		logger.open("test_erncrytion/"+ self._testMethodName+".log",self._testMethodName)
		
	def tearDown(self):
		logger.close(self.result())
		
	def test_base_001_erncryption(self):
		try:
			process=all_case(test_config.contractaddress,test_config.pay_address,test_config.get_address1,test_config.node_index,test_config.nodePath)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
	
	def test_normal_002_erncryption(self):
		try:
			process=all_case(test_config.contractaddress,test_config.pay_address,test_config.get_address2,test_config.node_index,test_config.nodePath)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
	def test_normal_003_erncryption(self):
		try:
			process=all_case(test_config.contractaddress,test_config.pay_address,test_config.get_address3,test_config.node_index,test_config.nodePath)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
	
	def test_normal_004_erncryption(self):
		try:
			process=all_case(test_config.contractaddress,test_config.pay_address,test_config.get_address4,test_config.node_index,test_config.nodePath)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
		
	def test_normal_005_erncryption(self):
		try:
			process=all_case(test_config.contractaddress,test_config.pay_address,test_config.get_address5,test_config.node_index,test_config.nodePath)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
		
	def test_normal_006_erncryption(self):
		try:
			process=all_case(test_config.contractaddress,test_config.pay_address,test_config.get_address6,test_config.node_index,test_config.nodePath)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
		
	def test_normal_007_erncryption(self):
		try:
			process=all_case(test_config.contractaddress,test_config.pay_address,test_config.get_address7,test_config.node_index,test_config.nodePath)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
		
	def test_normal_008_erncryption(self):
		try:
			process=all_case(test_config.contractaddress,test_config.pay_address,test_config.get_address8,test_config.node_index,test_config.nodePath)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
		
	def test_normal_009_erncryption(self):
		try:
			process=all_case(test_config.contractaddress,test_config.pay_address,test_config.get_address9,test_config.node_index,test_config.nodePath)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
		
	def test_normal_010_erncryption(self):
		try:
			process=all_case(test_config.contractaddress,test_config.pay_address,test_config.get_address10,test_config.node_index,test_config.nodePath)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
		#test_config.contractaddress,test_config.pay_address,test_config.get_address8,test_config.node_index,test_config.nodePath
	def test_normal_011_erncryption(self):
		try:
			process=all_case(test_config.contractaddress,test_config.pay_address,test_config.get_address11,test_config.node_index,test_config.nodePath)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
			

		


####################################################
if __name__ == '__main__':
	unittest.main()

