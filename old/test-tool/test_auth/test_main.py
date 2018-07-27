# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

sys.path.append('..')

#from utils.selfig import selfig
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.commonapi import *
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.contractapi import *
from test_api import *
from utils.rpcapi import *
from utils.init_ong_ont import *
from utils.config import Config

from utils.commonapi import call_contract

logger = LoggerInstance


####################################################
#test cases
class TestContract(ParametrizedTestCase):
	def setUp(self):
		time.sleep(2)
		print("stop all")
		stop_all_nodes()
		print("start all")
		start_nodes([0,1,2,3,4,5,6,7,8], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(10)
		regIDWithPublicKey(0)
		regIDWithPublicKey(1)
		regIDWithPublicKey(2)
		regIDWithPublicKey(3)
		regIDWithPublicKey(4)
		regIDWithPublicKey(5)
		regIDWithPublicKey(6)
		regIDWithPublicKey(7)
		regIDWithPublicKey(8)
		init_ont_ong()

		(self.contract_addr, self.contract_tx_hash) = deploy_contract_full("./tasks/auth.neo")
		(self.contract_addr_1, self.contract_tx_hash_1) = deploy_contract_full("./tasks/auth_2.neo")
		(self.contract_addr_2, self.contract_tx_hash_2) = deploy_contract_full("./tasks/auth_3.neo")
		(self.contract_addr_3, self.contract_tx_hash_3) = deploy_contract_full("./tasks/auth_4.neo")
		(self.contract_addr_10, self.contract_tx_hash_10) = deploy_contract_full("./tasks/auth_10.neo")
		(self.contract_addr_11, self.contract_tx_hash_11) = deploy_contract_full("./tasks/auth_11.neo")
		(self.contract_addr_12, self.contract_tx_hash_12) = deploy_contract_full("./tasks/auth_12.neo")
		(self.contract_addr_138_1, self.contract_tx_hash_138_1) = deploy_contract_full("./tasks/auth_138_A.neo")
		(self.contract_addr_138_2, self.contract_tx_hash_138_2) = deploy_contract_full("./tasks/auth_138_B.neo")
		(self.contract_addr_139, self.contract_tx_hash_139) = deploy_contract_full("./tasks/auth_139_A.neo")
		
		self.CONTRACT_ADDRESS_CORRECT = self.contract_addr               # correct
		self.CONTRACT_ADDRESS_INCORRECT_1 = self.contract_addr_1         # wrong ontid
		self.CONTRACT_ADDRESS_INCORRECT_2 = self.contract_addr_2         # null ontid
		self.CONTRACT_ADDRESS_INCORRECT_3 = self.contract_addr_3         # init twice
		self.CONTRACT_ADDRESS_INCORRECT_4 = self.contract_addr + "11"    # not real contract
		self.CONTRACT_ADDRESS_INCORRECT_5 = "45445566"              # messy code
		self.CONTRACT_ADDRESS_INCORRECT_6 = ""                      # null
		self.CONTRACT_ADDRESS_INCORRECT_10 = self.contract_addr_10       # verifytoken contract with wrong address
		self.CONTRACT_ADDRESS_INCORRECT_11 = self.contract_addr_11       # verifytoken contract with messy code address
		self.CONTRACT_ADDRESS_INCORRECT_12 = self.contract_addr_12       # verifytoken contract with wrong address

		self.CONTRACT_ADDRESS_138 = self.contract_addr_138_1             # appcall contract with correct address
		self.CONTRACT_ADDRESS_139 = self.contract_addr_139               # appcall contract with messy code address

		self.ontID_A = ByteToHex(bytes(Config.NODES[0]['ontid'], encoding = "utf8"))       # contract ontid
		self.ontID_B = ByteToHex(bytes(Config.NODES[2]['ontid'], encoding = "utf8"))     # the first ontid
		self.ontID_C = ByteToHex(b"did:ont:123")                    # messy code
		self.ontID_D = ""                
		self.ontID_E = ByteToHex(bytes(Config.NODES[3]['ontid'], encoding = "utf8"))                           # null

		self.ROLE_CORRECT = Config.roleA_hex                                              # roleA
		self.ROLE_INCORRECT_1 = ""                                                        # null
		self.ROLE_INCORRECT_2 = "7e21402324255e262a2820295f2b"                            # role "~!@#$%^&*( )_+"
		self.ROLE_INCORRECT_3 = "31313131313131"                                          # role not exist

		self.FUNCTION_A = "A"                                                             # function A
		self.FUNCTION_B = "B"                                                             # function B
		self.FUNCTION_C = "InvokeTransfer"                                                # function InvokeTransfer
		self.FUNCTION_D = "xxx"                                                           # function not exist

		self.KEY_NO_1 = "10"                                                              # wrong keyno
		self.KEY_NO_2 = "abc"                                                             # wrong keyno
		self.KEY_NO_3 = ""                                                                # null

		self.PERIOD_CORRECT = "20"                                                        # correct period
		self.PERIOD_INCORRECT_1 = "0"                                                     # period 0
		self.PERIOD_INCORRECT_2 = "-1"                                                    # wrong period -1
		self.PERIOD_INCORRECT_3 = "2.04"                                                  # wrong period 2.04
		self.PERIOD_INCORRECT_4 = "abc"                                                   # wrong period abc
		self.PERIOD_INCORRECT_5 = ""                                                      # null

		self.LEVEL_CORRECT = "1"                                                          # correct level 1
		self.LEVEL_INCORRECT_1 = "2"                                                      # wrong level 2
		self.LEVEL_INCORRECT_2 = "0"                                                      # wrong level 0
		self.LEVEL_INCORRECT_3 = "abc"                                                    # wrong level abc
		self.LEVEL_INCORRECT_4 = ""                                                       # null



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
	
	def test_01_initContractAdmin(self):		
		log_path = "01_initContractAdmin.log"
		task_name = "01_initContractAdmin"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		self.finish(task_name, log_path, result,  "")

	def test_02_initContractAdmin(self):
		log_path = "02_initContractAdmin.log"
		task_name = "02_initContractAdmin"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = init_admin(self.CONTRACT_ADDRESS_INCORRECT_1, self.ontID_A)
		self.finish(task_name, log_path, not result,  "")

	def test_03_initContractAdmin(self):
		log_path = "03_initContractAdmin.log"
		task_name = "03_initContractAdmin"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = init_admin(self.CONTRACT_ADDRESS_INCORRECT_2, self.ontID_A)
		self.finish(task_name, log_path, not result,  "")

	def test_04_initContractAdmin(self):
		log_path = "04_initContractAdmin.log"
		task_name = "04_initContractAdmin"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = init_admin(self.CONTRACT_ADDRESS_INCORRECT_3, self.ontID_A)
		self.finish(task_name, log_path, not result,  "")
	
	def test_05_verifyToken(self):
		log_path = "05_verifyToken.log"
		task_name = "05_verifyToken"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_CORRECT, self.FUNCTION_A, self.ontID_A)
		self.finish(task_name, log_path, result,  "")

	def test_06_verifyToken(self):
		log_path = "06_verifyToken.log"
		task_name = "06_verifyToken"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_CORRECT, self.FUNCTION_A, self.ontID_B)
		self.finish(task_name, log_path, not result,  "")

	def test_07_verifyToken(self):
		log_path = "07_verifyToken.log"
		task_name = "07_verifyToken"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_CORRECT, self.FUNCTION_A, self.ontID_C)
		self.finish(task_name, log_path, not result,  "")

	def test_08_verifyToken(self):
		log_path = "08_verifyToken.log"
		task_name = "08_verifyToken"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_CORRECT, self.FUNCTION_A, self.ontID_D)
		self.finish(task_name, log_path, not result,  "")

	def test_09_verifyToken(self):
		log_path = "09_verifyToken.log"
		task_name = "09_verifyToken"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_CORRECT, self.FUNCTION_A, self.ontID_A)
		self.finish(task_name, log_path, result,  "")

	def test_10_verifyToken(self):
		log_path = "10_verifyToken.log"
		task_name = "10_verifyToken"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_INCORRECT_10, self.FUNCTION_A, self.ontID_A)
		self.finish(task_name, log_path, result,  "")

	def test_11_verifyToken(self):
		log_path = "11_verifyToken.log"
		task_name = "11_verifyToken"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_INCORRECT_11, self.FUNCTION_A, self.ontID_A)
		self.finish(task_name, log_path, not result,  "")

	def test_12_verifyToken(self):
		log_path = "12_verifyToken.log"
		task_name = "12_verifyToken"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_INCORRECT_12, self.FUNCTION_A, self.ontID_A)
		self.finish(task_name, log_path, not result,  "")

	def test_13_verifyToken(self):
		log_path = "13_verifyToken.log"
		task_name = "13_verifyToken"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_CORRECT, self.FUNCTION_A, self.ontID_A)
		self.finish(task_name, log_path, result,  "")

	def test_14_verifyToken(self):
		log_path = "14_verifyToken.log"
		task_name = "14_verifyToken"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_CORRECT, "C", self.ontID_A)
		self.finish(task_name, log_path, result,  "")

	def test_15_verifyToken(self):
		log_path = "15_verifyToken.log"
		task_name = "15_verifyToken"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_CORRECT, self.FUNCTION_B, self.ontID_A)
		self.finish(task_name, log_path, result,  "")

	def test_16_verifyToken(self):
		log_path = "16_verifyToken.log"
		task_name = "16_verifyToken"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_CORRECT, "", self.ontID_A)
		self.finish(task_name, log_path, result,  "")
	
	
	def test_17_transfer(self):
		log_path = "17_transfer.log"
		task_name = "17_transfer"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = transfer(self.CONTRACT_ADDRESS_CORRECT, self.ontID_B)
		self.finish(task_name, log_path, result,  "")

	def test_18_transfer(self):
		log_path = "18_transfer.log"
		task_name = "18_transfer"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = transfer(self.CONTRACT_ADDRESS_INCORRECT_1, self.ontID_A)
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, result,  "")

	def test_19_transfer(self):
		log_path = "19_transfer.log"
		task_name = "19_transfer"
		self.start(log_path)
		# init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = transfer(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, result,  "")
	
	def test_20_transfer(self):
		log_path = "20_transfer.log"
		task_name = "20_transfer"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = transfer(self.CONTRACT_ADDRESS_INCORRECT_5, self.ontID_A)
		self.finish(task_name, log_path, not result,  "")

	def test_21_transfer(self):
		log_path = "21_transfer.log"
		task_name = "21_transfer"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = transfer(self.CONTRACT_ADDRESS_INCORRECT_6, self.ontID_A)
		self.finish(task_name, log_path, not result,  "")

	def test_22_transfer(self):
		log_path = "22_transfer.log"
		task_name = "22_transfer"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = transfer(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		self.finish(task_name, log_path, result,  "")

	def test_23_transfer(self):
		log_path = "23_transfer.log"
		task_name = "23_transfer"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = transfer(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		self.finish(task_name, log_path, result,  "")

	def test_24_transfer(self):
		log_path = "24_transfer.log"
		task_name = "24_transfer"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = transfer(self.CONTRACT_ADDRESS_CORRECT, self.ontID_C)
		self.finish(task_name, log_path, not result,  "")

	def test_25_transfer(self):
		log_path = "25_transfer.log"
		task_name = "25_transfer"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = transfer(self.CONTRACT_ADDRESS_CORRECT, self.ontID_D)
		self.finish(task_name, log_path, not result,  "")

	def test_26_transfer(self):
		log_path = "26_transfer.log"
		task_name = "26_transfer"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = transfer(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		self.finish(task_name, log_path, result,  "")

	def test_27_transfer(self):
		log_path = "27_transfer.log"
		task_name = "27_transfer"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = transfer(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, public_key=self.KEY_NO_1)
		self.finish(task_name, log_path, not result,  "")

	def test_28_transfer(self):
		log_path = "28_transfer.log"
		task_name = "28_transfer"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = transfer(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, public_key=self.KEY_NO_2)
		self.finish(task_name, log_path, not result,  "")

	def test_29_transfer(self):
		log_path = "29_transfer.log"
		task_name = "29_transfer"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = transfer(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, public_key=self.KEY_NO_3)
		self.finish(task_name, log_path, not result,  "")
	
	
	def test_30_assignFuncsToRole(self):
		log_path = "30_assignFuncsToRole.log"
		task_name = "30_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		self.finish(task_name, log_path, result,  "")

	def test_31_assignFuncsToRole(self):
		log_path = "31_assignFuncsToRole.log"
		task_name = "31_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_INCORRECT_4, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		self.finish(task_name, log_path, not result,  "")

	def test_32_assignFuncsToRole(self):
		log_path = "32_assignFuncsToRole.log"
		task_name = "32_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_INCORRECT_5, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		self.finish(task_name, log_path, not result,  "")

	def test_33_assignFuncsToRole(self):
		log_path = "33_assignFuncsToRole.log"
		task_name = "33_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_INCORRECT_6, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		self.finish(task_name, log_path, not result,  "")

	def test_34_assignFuncsToRole(self):
		log_path = "34_assignFuncsToRole.log"
		task_name = "34_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		self.finish(task_name, log_path, result,  "")

	def test_35_assignFuncsToRole(self):
		log_path = "35_assignFuncsToRole.log"
		task_name = "35_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		self.finish(task_name, log_path, result,  "")

	def test_36_assignFuncsToRole(self):
		log_path = "36_assignFuncsToRole.log"
		task_name = "36_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_B, self.ROLE_CORRECT, [self.FUNCTION_A])
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, result,  "")

	def test_37_assignFuncsToRole(self):
		log_path = "37_assignFuncsToRole.log"
		task_name = "37_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_C, self.ROLE_CORRECT, [self.FUNCTION_A])
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, result,  "")

	def test_38_assignFuncsToRole(self):
		log_path = "38_assignFuncsToRole.log"
		task_name = "38_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_D, self.ROLE_CORRECT, [self.FUNCTION_A])
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, result,  "")

	def test_39_assignFuncsToRole(self):
		log_path = "39_assignFuncsToRole.log"
		task_name = "39_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		self.finish(task_name, log_path, result,  "")

	def test_40_assignFuncsToRole(self):
		log_path = "40_assignFuncsToRole.log"
		task_name = "40_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		self.finish(task_name, log_path, result,  "")

	def test_41_assignFuncsToRole(self):
		log_path = "41_assignFuncsToRole.log"
		task_name = "41_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_INCORRECT_1, [self.FUNCTION_A])
		self.finish(task_name, log_path, not result,  "")

	def test_42_assignFuncsToRole(self):
		log_path = "42_assignFuncsToRole.log"
		task_name = "42_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_INCORRECT_2, [self.FUNCTION_A])
		self.finish(task_name, log_path, result,  "")

	def test_43_assignFuncsToRole(self):
		log_path = "43_assignFuncsToRole.log"
		task_name = "43_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		self.finish(task_name, log_path, result,  "")

	def test_44_assignFuncsToRole(self):
		log_path = "44_assignFuncsToRole.log"
		task_name = "44_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_B, self.FUNCTION_A])
		self.finish(task_name, log_path, result,  "")

	def test_45_assignFuncsToRole(self):
		log_path = "45_assignFuncsToRole.log"
		task_name = "45_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])		
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A, self.FUNCTION_B, self.FUNCTION_C])
		self.finish(task_name, log_path, result,  "")

	def test_46_assignFuncsToRole(self):
		log_path = "46_assignFuncsToRole.log"
		task_name = "46_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])		
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		self.finish(task_name, log_path, result,  "")

	def test_47_assignFuncsToRole(self):
		log_path = "47_assignFuncsToRole.log"
		task_name = "47_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])		
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_INCORRECT_2, [self.FUNCTION_A])
		self.finish(task_name, log_path, result,  "")

	def test_48_assignFuncsToRole(self):
		log_path = "48_assignFuncsToRole.log"
		task_name = "48_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_D])
		self.finish(task_name, log_path, result,  "")
	
	def test_49_assignFuncsToRole(self):
		log_path = "49_assignFuncsToRole.log"
		task_name = "49_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A, self.FUNCTION_D])
		self.finish(task_name, log_path, result,  "")

	def test_50_assignFuncsToRole(self):
		log_path = "50_assignFuncsToRole.log"
		task_name = "50_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		self.finish(task_name, log_path, result,  "")

	def test_51_assignFuncsToRole(self):
		log_path = "51_assignFuncsToRole.log"
		task_name = "51_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A], public_key = self.KEY_NO_1)
		self.finish(task_name, log_path, not result,  "")

	def test_52_assignFuncsToRole(self):
		log_path = "52_assignFuncsToRole.log"
		task_name = "52_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A], public_key = self.KEY_NO_2)
		self.finish(task_name, log_path, not result,  "")

	def test_53_assignFuncsToRole(self):
		log_path = "53_assignFuncsToRole.log"
		task_name = "53_assignFuncsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A], public_key = self.KEY_NO_3)
		self.finish(task_name, log_path, not result,  "")

	def test_54_assignOntIDsToRole(self):
		log_path = "54_assignOntIDsToRole.log"
		task_name = "54_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		self.finish(task_name, log_path, result,  "")

	def test_55_assignOntIDsToRole(self):
		log_path = "55_assignOntIDsToRole.log"
		task_name = "55_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_INCORRECT_4, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		self.finish(task_name, log_path, not result,  "")

	def test_56_assignOntIDsToRole(self):
		log_path = "56_assignOntIDsToRole.log"
		task_name = "56_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_INCORRECT_5, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		self.finish(task_name, log_path, not result,  "")

	def test_57_assignOntIDsToRole(self):
		log_path = "57_assignOntIDsToRole.log"
		task_name = "57_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_INCORRECT_6, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		self.finish(task_name, log_path, not result,  "")

	def test_58_assignOntIDsToRole(self):
		log_path = "58_assignOntIDsToRole.log"
		task_name = "58_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		self.finish(task_name, log_path, result,  "")
	
	def test_59_assignOntIDsToRole(self):
		log_path = "59_assignOntIDsToRole.log"
		task_name = "59_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		self.finish(task_name, log_path, result,  "")

	def test_60_assignOntIDsToRole(self):
		log_path = "60_assignOntIDsToRole.log"
		task_name = "60_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_B, self.ROLE_CORRECT, [self.ontID_A])
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, not result,  "")

	def test_61_assignOntIDsToRole(self):
		log_path = "61_assignOntIDsToRole.log"
		task_name = "61_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_C, self.ROLE_CORRECT, [self.ontID_A])
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, not result,  "")

	def test_62_assignOntIDsToRole(self):
		log_path = "62_assignOntIDsToRole.log"
		task_name = "62_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_D, self.ROLE_CORRECT, [self.ontID_A])
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, not result,  "")

	def test_63_assignOntIDsToRole(self):
		log_path = "63_assignOntIDsToRole.log"
		task_name = "63_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		self.finish(task_name, log_path, result,  "")

	def test_64_assignOntIDsToRole(self):
		log_path = "64_assignOntIDsToRole.log"
		task_name = "64_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_INCORRECT_3, [self.ontID_A])
		self.finish(task_name, log_path, result,  "")

	def test_65_assignOntIDsToRole(self):
		log_path = "65_assignOntIDsToRole.log"
		task_name = "65_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_INCORRECT_1, [self.ontID_A])
		self.finish(task_name, log_path, not result,  "")

	def test_66_assignOntIDsToRole(self):
		log_path = "66_assignOntIDsToRole.log"
		task_name = "66_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A, self.ontID_B])
		self.finish(task_name, log_path, result,  "")

	def test_67_assignOntIDsToRole(self):
		log_path = "67_assignOntIDsToRole.log"
		task_name = "67_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A, self.ontID_B, self.ontID_C])
		self.finish(task_name, log_path, not result,  "")

	def test_68_assignOntIDsToRole(self):
		log_path = "68_assignOntIDsToRole.log"
		task_name = "68_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_D])
		self.finish(task_name, log_path, not result,  "")

	def test_69_assignOntIDsToRole(self):
		log_path = "69_assignOntIDsToRole.log"
		task_name = "69_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		self.finish(task_name, log_path, result,  "")

	def test_70_assignOntIDsToRole(self):
		log_path = "70_assignOntIDsToRole.log"
		task_name = "70_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A], public_key=self.KEY_NO_1)
		self.finish(task_name, log_path, not result,  "")

	def test_71_assignOntIDsToRole(self):
		log_path = "71_assignOntIDsToRole.log"
		task_name = "71_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A], public_key=self.KEY_NO_2)
		self.finish(task_name, log_path, not result,  "")

	def test_72_assignOntIDsToRole(self):
		log_path = "72_assignOntIDsToRole.log"
		task_name = "72_assignOntIDsToRole"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A], public_key=self.KEY_NO_3)
		self.finish(task_name, log_path, not result,  "")

	def test_73_delegate(self):
		log_path = "73_delegate.log"
		task_name = "73_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		self.finish(task_name, log_path, result,  "")

	def test_74_delegate(self):
		log_path = "74_delegate.log"
		task_name = "74_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_INCORRECT_4, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		self.finish(task_name, log_path, not result,  "")

	def test_75_delegate(self):
		log_path = "75_delegate.log"
		task_name = "75_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_INCORRECT_5, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		self.finish(task_name, log_path, not result,  "")

	def test_76_delegate(self):
		log_path = "76_delegate.log"
		task_name = "76_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_INCORRECT_6, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		self.finish(task_name, log_path, not result,  "")

	def test_77_delegate(self):
		log_path = "77_delegate.log"
		task_name = "77_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		self.finish(task_name, log_path, result,  "")

	def test_78_delegate(self):
		log_path = "78_delegate.log"
		task_name = "78_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT)
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_B, self.ontID_E, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT, node_index=2)
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, not result,  "")

	def test_79_delegate(self):
		log_path = "79_delegate.log"
		task_name = "79_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_B, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		self.finish(task_name, log_path, not result,  "")

	def test_80_delegate(self):
		log_path = "80_delegate.log"
		task_name = "80_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_C, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		self.finish(task_name, log_path, not result,  "")

	def test_81_delegate(self):
		log_path = "81_delegate.log"
		task_name = "81_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		self.finish(task_name, log_path, result,  "")

	def test_82_delegate(self):
		log_path = "82_delegate.log"
		task_name = "82_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		self.finish(task_name, log_path, result,  "")

	def test_83_delegate(self):
		log_path = "83_delegate.log"
		task_name = "83_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_A, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		self.finish(task_name, log_path, result,  "")

	def test_84_delegate(self):
		log_path = "84_delegate.log"
		task_name = "84_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_C, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		self.finish(task_name, log_path, not result,  "")

	def test_85_delegate(self):
		log_path = "85_delegate.log"
		task_name = "85_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_D, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		self.finish(task_name, log_path, not result,  "")

	def test_86_delegate(self):
		log_path = "86_delegate.log"
		task_name = "86_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		self.finish(task_name, log_path, result,  "")

	def test_87_delegate(self):
		log_path = "87_delegate.log"
		task_name = "87_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_INCORRECT_3, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		self.finish(task_name, log_path, result,  "")

	def test_88_delegate(self):
		log_path = "88_delegate.log"
		task_name = "88_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_INCORRECT_1, self.PERIOD_CORRECT, self.LEVEL_CORRECT)		
		self.finish(task_name, log_path, result,  "")

	def test_89_delegate(self):
		log_path = "89_delegate.log"
		task_name = "89_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)		
		self.finish(task_name, log_path, result,  "")

	def test_90_delegate(self):
		log_path = "90_delegate.log"
		task_name = "90_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_INCORRECT_1, self.LEVEL_CORRECT)		
		self.finish(task_name, log_path, result,  "")
	
	def test_91_delegate(self):
		log_path = "91_delegate.log"
		task_name = "91_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_INCORRECT_2, self.LEVEL_CORRECT)		
		self.finish(task_name, log_path, not result,  "")

	def test_92_delegate(self):
		log_path = "92_delegate.log"
		task_name = "92_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_INCORRECT_3, self.LEVEL_CORRECT)		
		self.finish(task_name, log_path, not result,  "")

	def test_93_delegate(self):
		log_path = "93_delegate.log"
		task_name = "93_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_INCORRECT_4, self.LEVEL_CORRECT)		
		self.finish(task_name, log_path, not result,  "")

	def test_94_delegate(self):
		log_path = "94_delegate.log"
		task_name = "94_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_INCORRECT_5, self.LEVEL_CORRECT)		
		self.finish(task_name, log_path, not result,  "")

	def test_95_delegate(self):
		log_path = "95_delegate.log"
		task_name = "95_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)		
		self.finish(task_name, log_path, result,  "")

	def test_96_delegate(self):
		log_path = "96_delegate.log"
		task_name = "96_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_INCORRECT_1)		
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, not result,  "")

	def test_97_delegate(self):
		log_path = "97_delegate.log"
		task_name = "97_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_INCORRECT_2)		
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, not result,  "")

	def test_98_delegate(self):
		log_path = "98_delegate.log"
		task_name = "98_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_INCORRECT_3)		
		self.finish(task_name, log_path, not result,  "")

	def test_99_delegate(self):
		log_path = "99_delegate.log"
		task_name = "99_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_INCORRECT_4)		
		self.finish(task_name, log_path, not result,  "")
	
	def test_100_delegate(self):
		log_path = "100_delegate.log"
		task_name = "100_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)		
		self.finish(task_name, log_path, result,  "")
	
	def test_101_delegate(self):
		log_path = "101_delegate.log"
		task_name = "101_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT, public_key=self.KEY_NO_1)		
		self.finish(task_name, log_path, not result,  "")

	def test_102_delegate(self):
		log_path = "102_delegate.log"
		task_name = "102_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT, public_key=self.KEY_NO_2)		
		self.finish(task_name, log_path, not result,  "")

	def test_103_delegate(self):
		log_path = "103_delegate.log"
		task_name = "103_delegate"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT, public_key=self.KEY_NO_3)		
		self.finish(task_name, log_path, not result,  "")

	def test_104_withdraw(self):
		log_path = "104_withdraw.log"
		task_name = "104_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT)
		self.finish(task_name, log_path, result,  "")
	
	def test_105_withdraw(self):
		log_path = "105_withdraw.log"
		task_name = "105_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_INCORRECT_4, self.ontID_A, self.ontID_B, self.ROLE_CORRECT)
		self.finish(task_name, log_path, not result,  "")

	def test_106_withdraw(self):
		log_path = "106_withdraw.log"
		task_name = "106_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_INCORRECT_5, self.ontID_A, self.ontID_B, self.ROLE_CORRECT)
		self.finish(task_name, log_path, not result,  "")

	def test_107_withdraw(self):
		log_path = "107_withdraw.log"
		task_name = "107_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_INCORRECT_6, self.ontID_A, self.ontID_B, self.ROLE_CORRECT)
		self.finish(task_name, log_path, not result,  "")

	def test_108_withdraw(self):
		log_path = "108_withdraw.log"
		task_name = "108_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT)
		self.finish(task_name, log_path, result,  "")

	def test_109_withdraw(self):
		log_path = "109_withdraw.log"
		task_name = "109_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_B, self.ontID_B, self.ROLE_CORRECT)
		self.finish(task_name, log_path, not result,  "")

	def test_110_withdraw(self):
		log_path = "110_withdraw.log"
		task_name = "110_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT)
		self.finish(task_name, log_path, result,  "")

	def test_111_withdraw(self):
		log_path = "111_withdraw.log"
		task_name = "111_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_C, self.ontID_B, self.ROLE_CORRECT)
		self.finish(task_name, log_path, not result,  "")

	def test_112_withdraw(self):
		log_path = "112_withdraw.log"
		task_name = "112_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_D, self.ontID_B, self.ROLE_CORRECT)
		self.finish(task_name, log_path, not result,  "")

	def test_113_withdraw(self):
		log_path = "113_withdraw.log"
		task_name = "113_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT)
		self.finish(task_name, log_path, result,  "")

	def test_114_withdraw(self):
		log_path = "114_withdraw.log"
		task_name = "114_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_A, self.ROLE_CORRECT)
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, result,  "")

	def test_115_withdraw(self):
		log_path = "115_withdraw.log"
		task_name = "115_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_A, self.ROLE_CORRECT)
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, result,  "")

	def test_116_withdraw(self):
		log_path = "116_withdraw.log"
		task_name = "116_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_A, self.ROLE_CORRECT)
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, result,  "")

	def test_117_withdraw(self):
		log_path = "117_withdraw.log"
		task_name = "117_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_C, self.ROLE_CORRECT)
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, result,  "")

	def test_118_withdraw(self):
		log_path = "118_withdraw.log"
		task_name = "118_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_D, self.ROLE_CORRECT)
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, result,  "")

	def test_119_withdraw(self):
		log_path = "119_withdraw.log"
		task_name = "119_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT)
		self.finish(task_name, log_path, result,  "")

	def test_120_withdraw(self):
		log_path = "120_withdraw.log"
		task_name = "120_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_INCORRECT_3)
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, result,  "")

	def test_121_withdraw(self):
		log_path = "121_withdraw.log"
		task_name = "121_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_INCORRECT_2)
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, result,  "")

	def test_122_withdraw(self):
		log_path = "122_withdraw.log"
		task_name = "122_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_INCORRECT_1)
		result = (response["result"]["Result"] == "00")
		self.finish(task_name, log_path, result,  "")
	
	
	def test_134_withdraw(self):
		log_path = "134_withdraw.log"
		task_name = "134_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT)
		self.finish(task_name, log_path, result,  "")

	def test_135_withdraw(self):
		log_path = "135_withdraw.log"
		task_name = "135_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, public_key=self.KEY_NO_1)
		self.finish(task_name, log_path, not result,  "")

	def test_136_withdraw(self):
		log_path = "136_withdraw.log"
		task_name = "136_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, public_key=self.KEY_NO_2)
		self.finish(task_name, log_path, not result,  "")

	def test_137_withdraw(self):
		log_path = "137_withdraw.log"
		task_name = "137_withdraw"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = bind_role_function(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.FUNCTION_A])
		(result, response) = bind_user_role( self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ROLE_CORRECT, [self.ontID_A])
		(result, response) = delegate_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, self.PERIOD_CORRECT, self.LEVEL_CORRECT)
		(result, response) = withdraw_user_role(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A, self.ontID_B, self.ROLE_CORRECT, public_key=self.KEY_NO_3)
		self.finish(task_name, log_path, not result,  "")

	def test_138_appcall(self):
		log_path = "138_appcall.log"
		task_name = "138_appcall"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_138, "contractA_Func_A", self.ontID_A)
		self.finish(task_name, log_path, result,  "")

	def test_139_appcall(self):
		log_path = "139_appcall.log"
		task_name = "139_appcall"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_139, "contractA_Func_A", self.ontID_A)
		result = (response["result"]["Result"] == "323232")
		self.finish(task_name, log_path, result,  "")

	
	
	def test_140_appcall(self):
		log_path = "140_appcall.log"
		task_name = "140_appcall"
		self.start(log_path)
		init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_CORRECT, "contractA_Func_A", self.ontID_A)
		self.finish(task_name, log_path, result,  "")
	
	def test_146_verifyToken(self):
		log_path = "146_verifyToken.log"
		task_name = "146_verifyToken"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_CORRECT, self.FUNCTION_A, self.ontID_A)
		self.finish(task_name, log_path, result,  "")

	def test_147_verifyToken(self):
		log_path = "147_verifyToken.log"
		task_name = "147_verifyToken"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_CORRECT, self.FUNCTION_A, self.ontID_A, public_key=self.KEY_NO_1)
		self.finish(task_name, log_path, not result,  "")

	def test_148_verifyToken(self):
		log_path = "148_verifyToken.log"
		task_name = "148_verifyToken"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_CORRECT, self.FUNCTION_A, self.ontID_A, public_key=self.KEY_NO_2)
		self.finish(task_name, log_path, not result,  "")

	def test_149_verifyToken(self):
		log_path = "149_verifyToken.log"
		task_name = "149_verifyToken"
		self.start(log_path)
		init(register_ontid=True, restart=True)
		(result, response) = invoke_function(self.CONTRACT_ADDRESS_CORRECT, self.FUNCTION_A, self.ontID_A, public_key=self.KEY_NO_3)
		self.finish(task_name, log_path, not result,  "")
	

####################################################
if __name__ == '__main__':
	unittest.main()

