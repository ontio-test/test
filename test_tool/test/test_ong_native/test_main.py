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
sys.path.append('../..')


from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger 
from utils.hexstring import *
from utils.error import Error

from utils.parametrizedtestcase import ParametrizedTestCase

from test_ong_native.test_api import *
from test_ong_native.test_config import * 
from api.apimanager import API 


####################################################
#test cases
class test_ong_native_1(ParametrizedTestCase):
	def test_init(self):
		API.node().stop_all_nodes()  
		API.node().start_nodes(range(0, 7), Config.DEFAULT_NODE_ARGS, clear_chain = True, clear_log = True)
		API.native().init_ont_ong()
		test_config.contract_address = API.contract().deploy_contract(test_config.neo1filename)
		test_config.sender5= API.contract().deploy_contract(test_config.neo2filename) 
		test_config.sender2 = test_config.contract_address

		
	def setUp(self):
		logger.open( "test_ong_native/"+self._testMethodName+".log",self._testMethodName)
		if self._testMethodName == "test_init":
			return 
		
	def tearDown(self):
		logger.close(self.result())
	
	def test_base_001_transfer(self):
		try:
			(process, response) = transfer(test_config.contract_address,test_config.from1,test_config.get_address,test_config.amount, test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
	def test_abnormal_002_transfer(self):
		try:
			(process, response) = transfer(test_config.contract_address,test_config.from2,test_config.get_address,test_config.amount, test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_abnormal_003_transfer(self):
		try:
			(process, response) = transfer(test_config.contract_address,test_config.from3,test_config.get_address,test_config.amount, test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_normal_004_transfer(self):
		try:
			(process, response) = transfer(test_config.contract_address,test_config.pay_address,test_config.to1,test_config.amount, test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_abnormal_005_transfer(self):
		try:
			(process, response) = transfer(test_config.contract_address,test_config.pay_address,test_config.to2,test_config.amount, test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_abnormal_006_transfer(self):
		try:
			(process, response) = transfer(test_config.contract_address,test_config.pay_address,test_config.to3,test_config.amount, test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_normal_007_transfer(self):
		try:
			(process, response) = transfer(test_config.contract_address,test_config.pay_address,test_config.get_address,test_config.amount1, test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_normal_008_transfer(self):
		try:
			(process, response) = transfer(test_config.contract_address,test_config.pay_address,test_config.get_address,test_config.amount2, test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_normal_009_transfer(self):
		try:
			(process, response) = transfer(test_config.contract_address,test_config.pay_address,test_config.get_address,test_config.amount3, test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_010_transfer(self):
		try:
			(process, response) = transfer(test_config.contract_address,test_config.pay_address,test_config.get_address,test_config.amount4, test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_base_013_approve(self):
		try:
			(process, response) = approve(test_config.contract_address,test_config.from1,test_config.get_address, test_config.amount,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
	def test_abnormal_014_approve(self):
		try:
			(process, response) = approve(test_config.contract_address,test_config.from4,test_config.get_address, test_config.amount,test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_normal_015_approve(self):
		try:
			(process, response) = approve(test_config.contract_address,test_config.pay_address,test_config.to1, test_config.amount,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_normal_016_approve(self):
		try:
			(process, response) = approve(test_config.contract_address,test_config.pay_address,test_config.to2, test_config.amount,test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_normal_017_approve(self):
		try:
			(process, response) = approve(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount1,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_normal_018_approve(self):
		try:
			(process, response) = approve(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount2,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_abnormal_019_approve(self):
		try:
			(process, response) = approve(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount4,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_normal_020_approve(self):
		try:
			(process, response) = approve(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount3,test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_base_023_transferFrom(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount,test_config.node_index,0)
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(process, response) = transferFrom(test_config.contract_address,test_config.sender1,test_config.pay_address,test_config.get_address, test_config.amount,2,test_config.sender1Type,errorcode=0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
		
	def test_normal_024_transferFrom(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,Common.address_to_base58(Common.bl_reserver(test_config.contract_address)), test_config.amount,test_config.node_index,0)#先approve
			if process:
				API.node().wait_gen_block()
				time.sleep(8)
			(process, response) = transferFrom(test_config.contract_address,Common.address_to_base58(Common.bl_reserver(test_config.contract_address)),test_config.pay_address,Common.address_to_base58(Common.bl_reserver(test_config.contract_address)), test_config.amount,test_config.sender2_node,test_config.sender2Type,errorcode=0)
			API.node().wait_gen_block()
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_025_transferFrom(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount,test_config.node_index,0)#先approve
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(process, response) = transferFrom(test_config.contract_address,test_config.sender3,test_config.pay_address,test_config.get_address, test_config.amount,test_config.sender3_node,test_config.sender3Type)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_026_transferFrom(self):
		try:
			(process, response) = transferFrom(test_config.contract_address,test_config.sender4,test_config.pay_address,test_config.get_address, test_config.amount,test_config.sender4_node,test_config.sender4Type)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_027_transferFrom(self):
		try:
			(process, response) = transferFrom(test_config.contract_address,test_config.sender5,test_config.pay_address,test_config.get_address, test_config.amount,test_config.sender5_node,test_config.sender5Type)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_abnormal_028_transferFrom(self):
		try:
			(process, response) = transferFrom(test_config.contract_address,test_config.sender6,test_config.pay_address,test_config.get_address, test_config.amount,test_config.sender6_node,test_config.sender6Type)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_abnormal_029_transferFrom(self):
		try:
			(process, response) = transferFrom(test_config.contract_address,test_config.sender7,test_config.pay_address,test_config.get_address, test_config.amount,test_config.sender7_node,test_config.sender7Type)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_normal_030_transferFrom(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.from5,test_config.get_address, test_config.amount,test_config.node_index,0)#先approve
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(proces, response) = transferFrom(test_config.contract_address,test_config.sender,test_config.from5,test_config.get_address, test_config.amount,test_config.sender_node,test_config.senderType,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_031_transferFrom(self):
		try:
			(process, response) = transferFrom(test_config.contract_address,test_config.sender,test_config.from6,test_config.get_address, test_config.amount,test_config.sender_node,test_config.senderType)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
	def test_abnormal_032_transferFrom(self):
		try:
			#(process, response) = approve1(test_config.contract_address,test_config.from3,test_config.get_address, test_config.amount,test_config.node_index,0)#先approve
			(process, response) = transferFrom(test_config.contract_address,test_config.sender,test_config.from3,test_config.get_address, test_config.amount,test_config.sender_node,test_config.senderType)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_normal_033_transferFrom(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.to4, test_config.amount+"000000000",test_config.node_index,0)#先approve
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(process, response) = transferFrom(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.to4, test_config.amount,test_config.sender_node,test_config.senderType,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_034_transferFrom(self):
		try:
			(process, response) = transferFrom(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.to5, test_config.amount,test_config.sender_node,test_config.senderType)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_035_transferFrom(self):
		try:
			(process, response) = transferFrom(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.to3, test_config.amount,test_config.sender_node,test_config.senderType)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
	def test_normal_036_transferFrom(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount+"000000000",test_config.node_index,0)
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(process, response) = transferFrom(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.get_address, test_config.amount1,test_config.sender_node,test_config.senderType,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_normal_037_transferFrom(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount,test_config.node_index,0)
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(process, response) = transferFrom(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.get_address, test_config.amount2,test_config.sender_node,test_config.senderType,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_abnormal_038_transferFrom(self):
		try:
			(process, response) = transferFrom(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.get_address, test_config.amount4,test_config.sender_node,test_config.senderType)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_039_transferFrom(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.get_address, "1",test_config.node_index,0)
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(process, response) = transferFrom(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.get_address, test_config.amount7,test_config.sender_node,test_config.senderType)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
	def test_abnormal_040_transferFrom(self):
		try:
			(process, response) = transferFrom(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.get_address, test_config.amount3,test_config.sender_node,test_config.senderType)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_base_043_name(self):
		try:
			(process, response) = name(test_config.contract_address,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_base_044_symbol(self):
		try:
			(process, response) = symbol(test_config.contract_address,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_base_045_decimals(self):
		try:
			(process, response) = decimals(test_config.contract_address,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_base_046_totalSupply(self):
		try:
			(process, response) = totalSupply(test_config.contract_address,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_base_047_balanceOf(self):
		try:
			(process, response) = balanceOf(test_config.contract_address,test_config.address1,test_config.node_index,errorcode=0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_048_balanceOf(self):
		try:
			(process, response) = balanceOf(test_config.contract_address,test_config.address2,test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_abnormal_049_balanceOf(self):
		try:
			(process, response) = balanceOf(test_config.contract_address,test_config.address3,test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_base_050_allowance(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.from1,test_config.get_address, test_config.amount,test_config.node_index,0)#先approve
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(process, response) = allowance(test_config.contract_address,test_config.from1,test_config.get_address,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_normal_051_allowance(self):
		try:
			(process, response) = allowance(test_config.contract_address,test_config.from4,test_config.get_address,test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_052_allowance(self):
		try:
			(process, response) = allowance(test_config.contract_address,test_config.from3,test_config.get_address,test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_normal_053_allowance(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.to1, test_config.amount,test_config.node_index,0)#先approve
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(process, response) = allowance(test_config.contract_address,test_config.pay_address,test_config.to1,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_normal_054_allowance(self):
		try:
			(process, response) =allowance(test_config.contract_address,test_config.pay_address,test_config.to2,test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_055_allowance(self):
		try:
			(process, response) = allowance(test_config.contract_address,test_config.pay_address,test_config.to3,test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_base_056_transfer1(self):
		try:
			(process, response) = transfer1(test_config.contract_address,test_config.from1,test_config.get_address,test_config.amount, test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_abnormal_057_transfer1(self):
		try:
			(process, response) = transfer1(test_config.contract_address,test_config.from2,test_config.get_address,test_config.amount, test_config.node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_058_transfer1(self):
		try:
			(process, response) = transfer1(test_config.contract_address,test_config.from3,test_config.get_address,test_config.amount, test_config.node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_normal_059_transfer1(self):
		try:
			(process, response) = transfer1(test_config.contract_address,test_config.pay_address,test_config.to1,test_config.amount, test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_abnormal_060_transfer1(self):
		try:
			(process, response) = transfer1(test_config.contract_address,test_config.pay_address,test_config.to2,test_config.amount, test_config.node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_061_transfer1(self):
		try:
			(process, response) = transfer1(test_config.contract_address,test_config.pay_address,test_config.to3,test_config.amount, test_config.node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_normal_062_transfer1(self):
		try:
			(process, response) = transfer1(test_config.contract_address,test_config.pay_address,test_config.get_address,test_config.amount1, test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_normal_063_transfer1(self):
		try:
			(process, response) = transfer1(test_config.contract_address,test_config.pay_address,test_config.get_address,test_config.amount2, test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_064_transfer1(self):
		try:
			(process, response) = transfer1(test_config.contract_address,test_config.pay_address,test_config.get_address,test_config.amount3, test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_065_transfer1(self):
		try:
			(process, response) = transfer1(test_config.contract_address,test_config.pay_address,test_config.get_address,test_config.amount4, test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_066_transfer1(self):
		try:
			(process, response) = transfer1(test_config.contract_address,test_config.pay_address,test_config.get_address,test_config.amount5, test_config.node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_067_transfer1(self):
		try:
			(process, response) = transfer1(test_config.contract_address,test_config.pay_address,test_config.get_address,test_config.amount6, test_config.node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_base_068_approve1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.from1,test_config.get_address, test_config.amount,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_069_approve1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.from4,test_config.get_address, test_config.amount,test_config.node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_normal_070_approve1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.to1, test_config.amount,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_071_approve1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.to2, test_config.amount,test_config.node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_normal_072_approve1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount1,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_normal_073_approve1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount2,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_074_approve1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount4,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_075_approve1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount3,test_config.node_index)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_076_approve1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount5,test_config.node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_077_approve1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount6,test_config.node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_base_078_transferFrom1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount,test_config.node_index,0)
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender1,test_config.pay_address,test_config.get_address, test_config.amount,test_config.sender1_node,test_config.sender1Type,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_normal_079_transferFrom1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount,test_config.node_index,0)
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender2,test_config.pay_address,test_config.get_address, test_config.amount,test_config.sender2_node,test_config.sender2Type,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_080_transferFrom1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.contract_address, test_config.amount,test_config.node_index,0)
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender3,test_config.pay_address,test_config.contract_address, test_config.amount,test_config.sender3_node,test_config.sender3Type)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_081_transferFrom1(self):
		try:
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender4,test_config.pay_address,test_config.get_address, test_config.amount,test_config.sender4_node,test_config.sender4Type)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_082_transferFrom1(self):
		try:
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender5,test_config.pay_address,test_config.get_address, test_config.amount,test_config.sender5_node,test_config.sender5Type)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_083_transferFrom1(self):
		try:
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender6,test_config.pay_address,test_config.get_address, test_config.amount,test_config.sender6_node,test_config.sender6Type,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_084_transferFrom1(self):
		try:
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender7,test_config.pay_address,test_config.get_address, test_config.amount,test_config.sender7_node,test_config.sender7Type,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_normal_085_transferFrom1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.from5,test_config.get_address, test_config.amount,test_config.node_index,0)
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender,test_config.from5,test_config.get_address, test_config.amount,test_config.sender_node,test_config.senderType,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_086_transferFrom1(self):
		try:
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender,test_config.from6,test_config.get_address, test_config.amount,test_config.sender_node,test_config.senderType,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_087_transferFrom1(self):
		try:
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender,test_config.from3,test_config.get_address, test_config.amount,test_config.sender_node,test_config.senderType,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_normal_088_transferFrom1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.to4, test_config.amount,test_config.node_index,0)
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.to4, test_config.amount,test_config.sender_node,test_config.senderType,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_089_transferFrom1(self):
		try:
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.to5, test_config.amount,test_config.sender_node,test_config.senderType,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_090_transferFrom1(self):
		try:
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.to3, test_config.amount,test_config.sender_node,test_config.senderType,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_normal_091_transferFrom1(self):
		try:

			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount1,test_config.node_index,0)
			if process:
				API.node().wait_gen_block()
				time.sleep(9)
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.get_address, test_config.amount1,test_config.sender_node,test_config.senderType,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_normal_092_transferFrom1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.get_address, test_config.amount2,test_config.node_index,0)
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.get_address, test_config.amount2,test_config.sender_node,test_config.senderType,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_093_transferFrom1(self):
		try:
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.get_address, test_config.amount4,test_config.node_index,test_config.senderType)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_094_transferFrom1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.get_address, "1",test_config.node_index,0)
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.get_address, test_config.amount7,test_config.sender_node,test_config.senderType)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_095_transferFrom1(self):
		try:
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.get_address, test_config.amount3,test_config.sender_node,test_config.senderType)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_096_transferFrom1(self):
		try:
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.get_address, test_config.amount5,test_config.sender_node,test_config.senderType,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_abnormal_097_transferFrom1(self):
		try:
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender,test_config.pay_address,test_config.get_address, test_config.amount6,test_config.sender_node,test_config.senderType,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

	def test_base_098_name1(self):
		try:
			(process, response) = name1(test_config.contract_address,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_base_099_symbol1(self):
		try:
			(process, response) = symbol1(test_config.contract_address,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_base_100_decimals1(self):
		try:
			(process, response) = decimals1(test_config.contract_address,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_base_101_totalSupply1(self):
		try:
			(process, response) = totalSupply1(test_config.contract_address,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_base_102_balanceOf1(self):
		try:
			(process, response) = balanceOf1(test_config.contract_address,test_config.address1,test_config.node_index,errorcode=0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_103_balanceOf1(self):
		try:
			(process, response) = balanceOf1(test_config.contract_address,test_config.address2,test_config.node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_104_balanceOf1(self):
		try:
			(process, response) = balanceOf1(test_config.contract_address,test_config.address3,test_config.node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		

######################################
	def test_base_105_allowance1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.from1,test_config.get_address, test_config.amount,test_config.node_index,0)
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(process, response) = allowance1(test_config.contract_address,test_config.from1,test_config.get_address,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_106_allowance1(self):
		try:
			(process, response) = allowance1(test_config.contract_address,test_config.from4,test_config.get_address,test_config.node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_107_allowance1(self):
		try:
			(process, response) = allowance1(test_config.contract_address,test_config.from3,test_config.get_address,test_config.node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_normal_108_allowance1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.pay_address,test_config.to1, test_config.amount,test_config.node_index,0)
			if process:
				API.node().wait_gen_block()
				time.sleep(5)
			(process, response) = allowance1(test_config.contract_address,test_config.pay_address,test_config.to1,test_config.node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_109_allowance1(self):
		try:
			(process, response) = allowance1(test_config.contract_address,test_config.pay_address,test_config.to2,test_config.node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_110_allowance1(self):
		try:
			(process, response) = allowance1(test_config.contract_address,test_config.pay_address,test_config.to3,test_config.node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_111_transfer1(self):
		try:
			(process, response) = transfer1(test_config.contract_address,test_config.from7,test_config.get_address,test_config.amount, 6)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_112_approve1(self):
		try:
			(process, response) = approve1(test_config.contract_address,test_config.from7,test_config.get_address, test_config.amount,6)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_113_transferFrom1(self):
		try:
			(process, response) = transferFrom1(test_config.contract_address,test_config.sender8,test_config.pay_address,test_config.get_address, test_config.amount,0,test_config.sender8Type)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_114_balanceOf1(self):
		try:
			(process, response) = balanceOf1(test_config.contract_address,test_config.address4,0,errorcode=0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		


	def test_abnormal_115_allowance1(self):
		try:
			(process, response) = allowance1(test_config.contract_address,test_config.pay_address,test_config.get_address,0,errorcode=0)
			self.ASSERT(process, "")
		except Exception as e:
			logger.print (e.args[0]) 
		
		

####################################################
if __name__ == '__main__':
	unittest.main()

