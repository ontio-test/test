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

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.common import Common
from api.apimanager import API

from test_muti_contract.test_api import test_api
from test_muti_contract.test_config import test_config

####################################################
# test cases
class test_muti_contract(ParametrizedTestCase):
	def setUp(self):
		logger.open("test_muti_contract/" + self._testMethodName + ".log", self._testMethodName)
		if self._testMethodName == "test_init":
			return True

		print("stop all")
		API.node().stop_all_nodes()
		print("start all")
		API.node().start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
		for index in range(0, 7):
			API.native().regid_with_publickey(index, sleep = 0)
		API.native().init_ont_ong()
		API.node().wait_gen_block()

	def tearDown(self):
		logger.close(self.result())		
		time.sleep(2)

	def test_base_001_mutiContract(self):
		try:
			process = False
 
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")
			# setp 1 绑定用户A拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address, Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")

			# setp 2 用户A访问A函数
			(process, response) = API.contract().invoke_function(contract_address, "A", Config.ontID_A)
			if not process:
				raise Error("invoke_function error")
			
			process = (response["result"]["Result"] != "00")
			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_normal_002_mutiContract(self):
		try:
			process = False
 
				
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定用户A拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 2 用户A访问A函数
			(process, response) = API.contract().invoke_function(contract_address, "C", Config.ontID_A)
			if not process:
				raise Error("invoke_function error")
		
			process = (response["result"]["Result"] != "00")
			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_abnormal_003_mutiContract(self):
		try:
			process = False
 
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定用户A拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 2 用户A访问A函数
			(process, response) = API.contract().invoke_function(contract_address, "B", Config.ontID_A)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] == "00")

			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])


	def test_normal_004_mutiContract(self):
		try:
			process = False
 
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定用户A拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
			# setp 2 绑定用户A拥有roleB角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleB_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
			# setp 3 用户A访问A函数
			(process, response) = API.contract().invoke_function(contract_address, "B", Config.ontID_A)
			if not process:
				raise Error("invoke_function error")
			
			process = (response["result"]["Result"] != "00")
				
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])
		
	def test_normal_005_mutiContract(self):
		try:
			process = False
 
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定角色绑定到用户
			(process, response) = API.native().bind_user_role(contract_address, Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
			
			(process, response) = API.native().bind_user_role(contract_address, Config.ontID_A, Config.roleB_hex, [Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 用户B授权用户A拥有角色B的权限
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_B, Config.ontID_A, Config.roleB_hex, "100", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 2 用户A访问B函数
			(process, response) = API.contract().invoke_function(contract_address, "B", Config.ontID_A)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] != "00")
				
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_abnormal_006_mutiContract(self):
		try:
			process = False
 
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定roleA角色绑定到用户A
			(process, response) = API.native().bind_user_role(contract_address, Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 绑定roleB角色绑定到用户B
			(process, response) = API.native().bind_user_role(contract_address, Config.ontID_A, Config.roleB_hex, [Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 用户B授权用户A拥有角色B的权限 5 秒
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_B, Config.ontID_A, Config.roleB_hex, "5", "1")
			if not process:
				raise Error("bind_user_role error")
			
			print("wait.......60s")
			time.sleep(60)			

			# setp 2 用户A访问B函数
			(process, response) = API.contract().invoke_function(contract_address, "B", Config.ontID_A)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] == "00")
				
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])
		
	def test_normal_007_mutiContract(self):
		try:
			process = False
 
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定roleA角色绑定到用户A
			(process, response) = API.native().bind_user_role(contract_address, Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 绑定roleB角色绑定到用户B
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleB_hex, [Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 用户B授权用户A拥有角色B的权限
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_B, Config.ontID_A, Config.roleB_hex, "5", "1")
			if not process:
				raise Error("bind_user_role error")
				
			print("wait.......60s")
			time.sleep(60)
			
			# setp 2 用户A访问C函数
			(process, response) = API.contract().invoke_function(contract_address, "C", Config.ontID_A)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] != "00")
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])				

	def test_abnormal_008_mutiContract(self):
		try:
			process = False
 
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定用户A拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 2 绑定用户B拥有roleB角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleB_hex, [Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
	
			# setp 3 用户B授权用户A拥有角色B的权限
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_B, Config.ontID_A, Config.roleB_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 4 收回授权用户A拥有的roleB角色
			(process, response) = API.native().withdraw_user_role(contract_address, Config.ontID_B, Config.ontID_A, Config.roleB_hex)
			if not process:
				raise Error("bind_user_role error")
						
			# setp 5 用户A访问B函数
			(process, response) = API.contract().invoke_function(contract_address, "B", Config.ontID_A)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] == "00")
			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_normal_009_mutiContract(self):
		try:
			process = False
 
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定用户A拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 绑定用户B拥有roleB角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleB_hex, [Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 用户B授权用户A拥有角色B的权限
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_B, Config.ontID_A, Config.roleB_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 收回授权用户A拥有的roleB角色
			(process, response) = API.native().withdraw_user_role(contract_address, Config.ontID_B, Config.ontID_A, Config.roleB_hex)
			if not process:
				raise Error("bind_user_role error")
			
			# setp 2 用户A访问B函数
			(process, response) = API.contract().invoke_function(contract_address, "C", Config.ontID_A)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] != "00")
			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])
   
	def test_abnormal_010_mutiContract(self):
		try:
			process = False
 
				
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定roleA角色绑定到用户A
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 用户A授权用户A拥有roleA的权限
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex, "5", "1")
			
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])
	'''   
	def test_11(self):
		try:
		process = False
		try:
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定roleA角色绑定到用户A
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 用户A授权用户A拥有roleA的权限
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex, "5", "1")
			if not process:
				raise Error("bind_user_role error")
			
			print("wait 60s.....")
			time.sleep(60)

			# setp 2 用户A访问C函数
			(process, response) = API.contract().invoke_function(contract_address, "B", Config.ontID_A)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] == "00")
		
		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass

	def test_12(self):
		try:
		process = False
		try:
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定roleA角色绑定到用户A
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 用户A授权用户A拥有roleA的权限
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex, "5", "1")
			if not process:
				raise Error("bind_user_role error")
			
			print("wait 60s.....")
			time.sleep(60)

			# setp 2 用户A访问C函数
			(process, response) = API.contract().invoke_function(contract_address, "A", Config.ontID_A)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] != "00")
		
		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass
		
	def test_13(self):
		try:
		process = False
		try:
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定roleA角色绑定到用户A
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 2 授权用户A拥有roleA角色，level1
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 3 收回授权用户A拥有的roleA角色
			(process, response) = API.native().withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex)
			if not process:
				raise Error("bind_user_role error")
			
			# setp 4 用户A访问A函数
			(process, response) = API.contract().invoke_function(contract_address, "A", Config.ontID_A)
			if not process:
				raise Error("invoke_function error")

			process = (response["result"]["Result"] != "00")
		
		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass

	def test_14(self):
		try:
		process = False
		try:
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定roleA角色绑定到用户A
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 2 授权用户A拥有roleA角色，level1
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 3 收回授权用户A拥有的roleA角色
			(process, response) = API.native().withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex)
			if not process:
				raise Error("bind_user_role error")
			
			# setp 4 用户A访问C函数
			(process, response) = API.contract().invoke_function(contract_address, "C", Config.ontID_A)
			if not process:
				raise Error("invoke_function error")

			process = (response["result"]["Result"] != "00")
		
		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass

	def test_15(self):
		try:
		process = False
		try:
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定roleA角色绑定到用户A
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 2 授权用户A拥有roleA角色，level1
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 3 收回授权用户A拥有的roleA角色
			(process, response) = API.native().withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex)
			if not process:
				raise Error("bind_user_role error")
			
			# setp 4 用户A访问C函数
			(process, response) = API.contract().invoke_function(contract_address, "B", Config.ontID_A)
			if not process:
				raise Error("invoke_function error")

			process = (response["result"]["Result"] == "00")
		
		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass
	'''
	def test_abnormal_016_mutiContract(self):
		try:
			process = False
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定roleA角色绑定到用户A,B
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 2 用户A授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
			   
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	'''	
	def test_17(self):
		try:
		process = False
		try:
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定roleA角色绑定到用户A,B
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 2 用户A授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 3 用户A收回用户B拥有的roleA角色，level1的授权
			(process, response) = API.native().withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex)
			if not process:
				raise Error("bind_user_role error")
			
			# setp 4 用户B访问A函数
			(process, response) = API.contract().invoke_function(contract_address, "B", Config.ontID_B)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] == "00")
		
		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass

	def test_18(self):
		try:
		process = False
		try:
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")
			
			# setp 1 绑定roleA角色绑定到用户A, B
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 2 用户A授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "5", "1")
			if not process:
				raise Error("bind_user_role error")
			
			print("wait 60s...")
			time.sleep(60)
			
			# setp 2 用户B访问B函数
			(process, response) = API.contract().invoke_function(contract_address, "A", Config.ontID_B)
			if not process:
				raise Error("invoke_function error")
			process = (response["result"]["Result"] != "00")
		
		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass
		
	def test_19(self):
		try:
		process = False
		try:
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")
			
			# setp 1 绑定roleA角色绑定到用户A, B
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 2 用户A授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "5", "1")
			if not process:
				raise Error("bind_user_role error")
			
			print("wait 60s...")
			time.sleep(60)
			
			# setp 2 用户B访问B函数
			(process, response) = API.contract().invoke_function(contract_address, "B", Config.ontID_B)
			if not process:
				raise Error("invoke_function error")
			process = (response["result"]["Result"] == "00")
		
		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass

	def test_20(self):
		try:
		process = False
		try:
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 2 绑定用户A拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
						
			# setp 3 用户A授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 4 用户A授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10", "1")
			if not process:
				raise Error("bind_user_role error")
			
			print("wait 60s...")
			time.sleep(60)
			
			# setp 2 用户B访问A函数
			(process, response) = API.contract().invoke_function(contract_address, "A", Config.ontID_B)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] == "00")
			
		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass

	def test_21(self):
		try:
		process = False
		try:
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定用户A拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
						
			# setp 2 用户A授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 3 用户A授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "100", "1")
			if not process:
				raise Error("bind_user_role error")
			
			time.sleep(60)
			
			# setp 4 用户B访问A函数
			(process, response) = API.contract().invoke_function(contract_address, "A", Config.ontID_B)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] != "00")
		
		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass

	def test_22(self):
		try:
		process = False
		try:
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定用户A拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
						
			# setp 2 用户A授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "20", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 3 用户A授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "30", "1")
			if not process:
				raise Error("bind_user_role error")
			
			time.sleep(60)
			
			# setp 4 用户B访问A函数
			(process, response) = API.contract().invoke_function(contract_address, "A", Config.ontID_B)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] == "00")
		
		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass
		
	def test_23(self):
		try:
		process = False
		try:
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定用户A拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
						
			# setp 2 用户A授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "20", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 3 用户A授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "30", "1")
			if not process:
				raise Error("bind_user_role error")
			
			time.sleep(60)
			
			# setp 4 用户B访问A函数
			(process, response) = API.contract().invoke_function(contract_address, "B", Config.ontID_B)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] == "00")
		
		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass

	def test_24(self):
		try:
		process = False
		try:
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定用户A拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
						
			# setp 2 用户A授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 3 用户A授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 4 用户A撤回用户B拥有的roleA角色
			(process, response) = API.native().withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex)
			if not process:
				raise Error("bind_user_role error")
			
			# setp 5 用户B不可以访问A函数
			(process, response) = API.contract().invoke_function(contract_address, "A", Config.ontID_B)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] == "00")

		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass
	'''	
	def test_abnormal_025_mutiContract(self):
		try:
			process = False
 
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定用户A，用户B拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
						
			# setp 2 用户A授权用户C拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 3 用户B授权用户C拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_B, Config.ontID_C, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
				
			process = (response["result"]["Result"] == "00")
			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])
	'''
	def test_26(self):
		try:
		process = False
		try:
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定用户A，用户B拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
						
			# setp 2 用户A授权用户C拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 3 用户B授权用户C拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_B, Config.ontID_C, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
						
			# setp 4 用户A撤回用户C拥有的roleA角色
			(process, response) = API.native().withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex)
			if not process:
				raise Error("bind_user_role error")
			
			# setp 5 用户C访问A函数
			(process, response) = API.contract().invoke_function(contract_address, "B", Config.ontID_C)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] == "00")
		
		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass

	def test_27(self):
		try:
		process = False
		try:
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定用户A，用户B拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
						
			# setp 1 用户A授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex, "10", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 用户B授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_B, Config.ontID_C, Config.roleA_hex, "100", "1")
			if not process:
				raise Error("bind_user_role error")
						
			time.sleep(60)
			
			# setp 2 用户C访问A函数
			(process, response) = API.contract().invoke_function(contract_address, "A", Config.ontID_C)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] != "00")
		
		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass

	def test_28(self):
		try:
		process = False
		try:
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定用户A，用户B拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
						
			# setp 1 用户A授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex, "10", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 用户B授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_B, Config.ontID_C, Config.roleA_hex, "20", "1")
			if not process:
				raise Error("bind_user_role error")
						
			time.sleep(60)
			
			# setp 2 用户C访问A函数
			(process, response) = API.contract().invoke_function(contract_address, "A", Config.ontID_C)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] == "00")
		
		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass
		
	def test_29(self):
		try:
		process = False
		try:
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定用户A，用户B拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
						
			# setp 1 用户A授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 用户B授权用户B拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_B, Config.ontID_C, Config.roleA_hex, "10", "1")
			if not process:
				raise Error("bind_user_role error")
						
			time.sleep(60)
			
			# setp 2 用户C访问A函数
			(process, response) = API.contract().invoke_function(contract_address, "A", Config.ontID_C)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] != "00")
		
		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass
	'''
	def test_normal_030_mutiContract(self):
		try:
			process = False
 
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定用户A，用户B拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 绑定用户A，用户B拥有roleB角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleB_hex, [Config.ontID_A, Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
						
			# setp 1 用户A授权用户C拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 用户B授权用户C拥有roleB角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_B, Config.ontID_C, Config.roleB_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
						
			# setp 1 用户A撤回用户C拥有的roleA角色
			(process, response) = API.native().withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex)
			if not process:
				raise Error("bind_user_role error")

			# setp 2 用户C访问B函数
			(process, response) = API.contract().invoke_function(contract_address, "B", Config.ontID_C)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] != "00")
		
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])
		
	def test_abnormal_031_mutiContract(self):
		try:
			process = False
 
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定用户A，用户B拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 绑定用户A，用户B拥有roleB角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleB_hex, [Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
						
			# setp 1 用户A授权用户C拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 1 用户B授权用户C拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_B, Config.ontID_C, Config.roleB_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
						
			# setp 1 用户A撤回用户C拥有的roleB角色
			(process, response) = API.native().withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleB_hex)
			if not process:
				raise Error("bind_user_role error")
				
			process = (response["result"]["Result"] == "00")

			# # setp 2 用户C访问B函数
			# (process, response) = API.contract().invoke_function(contract_address, "B")
			# if not process:
			#	 raise Error("invoke_function error")
			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])
	'''
	def test_32(self):
		try:
		process = False
		try:
			
			contract_address = test_api.set_premise(test_config.testpath + "/resource/1-32/A.neo")

			# setp 1 绑定用户A，用户B拥有roleA角色
			(process, response) = API.native().bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
			if not process:
				raise Error("bind_user_role error")
			
			# setp 2 用户A授权用户C拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# setp 3 用户B授权用户C拥有roleA角色
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_B, Config.ontID_C, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
						
			# setp 4 用户A撤回用户C拥有的roleA角色
			(process, response) = API.native().withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex)
			if not process:
				raise Error("bind_user_role error")

			# setp 5 用户C访问B函数
			(process, response) = API.contract().invoke_function(contract_address, "B", Config.ontID_C)
			if not process:
				raise Error("invoke_function error")
			
			process = (response["result"]["Result"] == "00")
	
		except Exception as e:
			print(e.msg)
			self.ASSERT(process, "")
		except:
			pass
	'''
	def test_normal_033_mutiContract(self):
		try:
			process = False
 
			(contract_address_A, contract_address_B) = test_api.set_premise_a(test_config.testpath + "/resource/33-37/A.neo", test_config.testpath + "/resource/33-37/B.neo")

			# A用户去调用A方法
			(process, response) = API.contract().invoke_function(contract_address_A, "contractA_Func_A",Config.ontID_A)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] != "00")
			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_abnormal_034_mutiContract(self):
		try:
			process = False
 
			(contract_address_A, contract_address_B) = test_api.set_premise_a(test_config.testpath + "/resource/33-37/A.neo", test_config.testpath + "/resource/33-37/B.neo")

			# B用户去调用A方法
			(process, response) = API.contract().invoke_function(contract_address_A, "contractA_Func_A", Config.ontID_B)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] == "00")		
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])
		
	def test_normal_035_mutiContract(self):
		try:
			process = False
 
			(contract_address_A, contract_address_B) = test_api.set_premise_a(test_config.testpath + "/resource/33-37/A.neo", test_config.testpath + "/resource/33-37/B.neo")
			
			# setp 1 用户A授权用户B拥有角色A的权限
			(process, response) = API.native().delegate_user_role(contract_address_B, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")

			# B用户去调用A方法
			(process, response) = API.contract().invoke_function(contract_address_A, "contractA_Func_A", Config.ontID_B)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] != "00")		
		
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_abnormal_036_mutiContract(self):
		try:
			process = False
 
			(contract_address_A, contract_address_B) = test_api.set_premise_a(test_config.testpath + "/resource/33-37/A.neo", test_config.testpath + "/resource/33-37/B.neo")

			# setp 1 用户A授权用户B拥有角色A的权限
			(process, response) = API.native().delegate_user_role(contract_address_B, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "5", "1")
			if not process:
				raise Error("bind_user_role error")

			# ==================================================================
			print("wait 60s...")
			time.sleep(60)

			# B用户去调用A方法
			(process, response) = API.contract().invoke_function(contract_address_A, "contractA_Func_A", Config.ontID_B)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] == "00")		
		
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])
			
	'''
	def test_abnormal_037_mutiContract(self):
		pass
	'''

	def test_normal_038_mutiContract(self):
		try:
			process = False

			(contract_address) = test_api.set_premise_b(test_config.testpath + "/resource/38-43_48-59/A.neo")

			# 用户A调用智能合约A中的A方法
			(process, response) = API.contract().invoke_function(contract_address, "transfer", Config.ontID_A, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_B]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] != "00")		
			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_normal_039_mutiContract(self):
		try:
			process = False

			contract_address = test_api.set_premise_b(test_config.testpath + "/resource/38-43_48-59/A.neo")

			# setp 1 用户A授权用户B拥有角色A的权限
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error") 

			# 用户B调用智能合约A中的A方法
			(process, response) = API.contract().invoke_function(contract_address, "transfer", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_B]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] != "00")		
		
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_abnormal_040_mutiContract(self):
		try:
			process = False

			contract_address = test_api.set_premise_b(test_config.testpath + "/resource/38-43_48-59/A.neo")

			# setp 1 用户A授权用户B拥有角色A的权限
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")  

			# 用户B调用智能合约A中的A方法
			(process, response) = API.contract().invoke_function(contract_address, "transfer", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_B]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])
				
			process = (not process or response["result"]["Result"] == "00")		
		
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])
		
	def test_abnormal_041_mutiContract(self):
		try:
			process = False
 
			contract_address = test_api.set_premise_b(test_config.testpath + "/resource/38-43_48-59/A.neo")

			# setp 1 用户A授权用户B拥有角色A的权限
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")

			# 用户B调用智能合约A中的A方法
			(process, response) = API.contract().invoke_function(contract_address, "approve", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_B]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])

			process = (not process or response["result"]["Result"] == "00")		
					
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])
	   
	def test_normal_042_mutiContract(self):
		try:
			process = False

			contract_address = test_api.set_premise_b(test_config.testpath + "/resource/38-43_48-59/A.neo")
			# setp 1 用户A授权用户B拥有角色A的权限
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")
						
			# ==================================================================
			# time.sleep(5)

			# 用户A授权用户C拥有10 ont
			
			(process, response) = API.contract().invoke_function(contract_address, "approve", Config.ontID_A, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_C]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])
			
			# 用户B调用智能合约A中的A方法
			(process, response) = API.contract().invoke_function(contract_address, "allowance", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_C]["address"]))
																				}])
			
			if not process:
				raise Error("invoke_function error")

			process = (response["result"]["Result"] != "00" and response["result"]["Result"] != "")		  
		
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])
		
	def test_normal_043_mutiContract(self):
		try:
			process = False
 
			contract_address = test_api.set_premise_b(test_config.testpath + "/resource/38-43_48-59/A.neo")

			# setp 1 用户A授权用户B拥有角色A的权限
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")

			# ==================================================================
			# time.sleep(5)

			# 用户B调用智能合约A中的A方法 approve
			(process, response) = API.contract().invoke_function(contract_address, "approve", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_B]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_C]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])
			
			# 用户B调用智能合约A中的A方法 allowance
			(process, response) = API.contract().invoke_function(contract_address, "allowance", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_B]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_C]["address"]))
																				}])
			if not process:
				raise Error("invoke_function error")

			process = (response["result"]["Result"] != "00" and response["result"]["Result"] != "")		
					
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_normal_044_mutiContract(self):
		try:
			process = False

			(contract_addressA, contract_addressB) = test_api.set_premise_c(test_config.testpath + "/resource/44-47/A.neo", test_config.testpath + "/resource/44-47/B.neo")

			# setp 1 用户A授权用户B拥有角色A的权限
			(process, response) = API.native().delegate_user_role(contract_addressA, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")  

			# 用户B调用智能合约A中的A方法
			(process, response) = API.contract().invoke_function(contract_addressA, "A", Config.ontID_B)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] != "00")		
			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_normal_045_mutiContract(self):
		try:
			process = False

			(contract_addressA, contract_addressB) = test_api.set_premise_c(test_config.testpath + "/resource/44-47/A.neo", test_config.testpath + "/resource/44-47/B.neo")

			# 用户A调用智能合约A中的A方法
			(process, response) = API.contract().invoke_function(contract_addressA, "A", Config.ontID_A)		
				
			#process = (process or response["result"]["Result"] == "00")		
			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_normal_046_mutiContract(self):
		try:
			process = False
 
			(contract_addressA, contract_addressB) = test_api.set_premise_c(test_config.testpath + "/resource/44-47/A.neo", test_config.testpath + "/resource/44-47/B.neo")

			# setp 1 用户B授权用户A拥有角色B的权限
			(process, response) = API.native().delegate_user_role(contract_addressB, Config.ontID_B, Config.ontID_A, Config.roleB_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")  

			# 用户B调用智能合约A中的A方法
			(process, response) = API.contract().invoke_function(contract_addressA, "A", Config.ontID_A)
			if not process:
				raise Error("invoke_function error")
				
			process = (response["result"]["Result"] != "00")		
		
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_normal_047_mutiContract(self):
		try:
			process = False
 
			(contract_addressA, contract_addressB) = test_api.set_premise_c(test_config.testpath + "/resource/44-47/A.neo", test_config.testpath + "/resource/44-47/B.neo")

			# setp 1 用户A授权用户B调用方法A的权限
			#(process, response) = API.native().delegate_user_role(contract_addressA, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
			#if not process:
			#	raise Error("bind_user_role error")  

			# 用户B调用智能合约A中的A方法
			(process, response) = API.contract().invoke_function(contract_addressA, "A2", Config.ontID_B)

			process = (response["result"]["Result"] != "00")		
			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])
		
	def test_abnormal_048_mutiContract(self):
		try:
			process = False
 
			contract_address = test_api.set_premise_b(test_config.testpath + "/resource/38-43_48-59/A.neo")

			#用户A授权用户B调用智能合约A方法A的权限，level1
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "1000", "1")
			if not process:
				raise Error("bind_user_role error")
			
			# 用户A调用智能合约A中的A方法approve用户A给用户C 10 ont
			(process, response) = API.contract().invoke_function(contract_address, "approve", Config.ontID_A, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_B]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])
			if not process:
				raise Error("invoke_function error")			
			

			# 用户B调用智能合约A中的A方法,让用户A使用transferFrom方法获取用户A从用户B的账户上转账来的 10 ONT
			(process, response) = API.contract().invoke_function(contract_address, "transferFrom", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_B]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])

																				
			process = (not process or response["result"]["Result"] == "00")		

			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_normal_049_mutiContract(self):
		try:
			process = False

			contract_address = test_api.set_premise_b(test_config.testpath + "/resource/38-43_48-59/A.neo")

			# setp 1 用户A授权用户B拥有角色A的权限
			(process, response) = API.native().delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
			if not process:
				raise Error("bind_user_role error")  

			# 用户B调用智能合约A中的A方法,让用户A使用balanceof方法获取用户A的账户余额
			(process, response) = API.contract().invoke_function(contract_address, "balanceOf", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				}])

			process = (process and response["result"]["Result"] != "00")	
			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])
		
	def test_abnormal_050_mutiContract(self):
		try:
			process = False
 
			contract_address = API.contract().deploy_contract(test_config.testpath + "/resource/38-43_48-59/A2.neo")

			# 用户B调用智能合约A中的A方法从用户A的账户中转账10 ont 给用户C
			(process, response) = API.contract().invoke_function(contract_address, "transfer", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_C]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])
			process = (not process or response["result"]["Result"] == "00")	
		
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_abnormal_051_mutiContract(self):
		try:
			process = False
 
			contract_address = API.contract().deploy_contract(test_config.testpath + "/resource/38-43_48-59/A2.neo")

			# 用户B调用智能合约A中的A方法从用户A的账户中approve10 ont 给用户C
			(process, response) = API.contract().invoke_function(contract_address, "approve", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_C]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])
			process = (not process or response["result"]["Result"] == "00")	

			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_abnormal_052_mutiContract(self):
		try:
			process = False
 
			contract_address = API.contract().deploy_contract(test_config.testpath + "/resource/38-43_48-59/A2.neo")

			# 用户A调用智能合约A中的A方法approve用户A给用户C 10 ont
			(process, response) = API.contract().invoke_function(contract_address, "approve", Config.ontID_A, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_C]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])
			if not process:
				raise Error("invoke_function error")			
			

			# 用户B调用智能合约A中的A方法提取用户A给用户C的10 ont
			(process, response) = API.contract().invoke_function(contract_address, "transferFrom", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_B]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_C]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])
			process = (not process or response["result"]["Result"] == "00")	
			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_normal_053_mutiContract(self):
		try:
			process = False
 
			contract_address = API.contract().deploy_contract(test_config.testpath + "/resource/38-43_48-59/A2.neo")
	
			# 用户B调用智能合约A中的A方法查询用户A的账户ont余额
			(process, response) = API.contract().invoke_function(contract_address, "balanceOf", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				}])
			process = (process and response["result"]["Result"] != "00")	
		
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_normal_054_mutiContract(self):
		try:
			process = False
 
			contract_address = API.contract().deploy_contract(test_config.testpath + "/resource/38-43_48-59/A2.neo")

			# 用户B调用智能合约A中的A方法查询用户A给用户C的ont还有多少没有接收
			(process, response) = API.contract().invoke_function(contract_address, "allowance", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_C]["address"]))
																				}])
			process = (process and response["result"]["Result"] != "00")	

			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_abnormal_055_mutiContract(self):
		try:
			process = False
 
			contract_address = API.contract().deploy_contract(test_config.testpath + "/resource/38-43_48-59/A2.neo")

			# 用户B调用智能合约A中的A方法从用户A的账户中转账10 ONG 给用户C
			(process, response) = API.contract().invoke_function(contract_address, "transfer_ong", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_C]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])
			process = (not process or response["result"]["Result"] == "00")		   
			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_abnormal_056_mutiContract(self):
		try:
			process = False

			contract_address = API.contract().deploy_contract(test_config.testpath + "/resource/38-43_48-59/A2.neo")

			# 用户B调用智能合约A中的A方法从用户A的账户中approve10 ong 给用户C
			(process, response) = API.contract().invoke_function(contract_address, "approve_ong", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_C]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])
			process = (not process or response["result"]["Result"] == "00")	

			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_abnormal_057_mutiContract(self):
		try:
			process = False

			contract_address = API.contract().deploy_contract(test_config.testpath + "/resource/38-43_48-59/A2.neo")

			# 用户A调用智能合约A中的A方法approve用户A给用户C 10 ong
			(process, response) = API.contract().invoke_function(contract_address, "approve_ong", Config.ontID_A, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_C]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])
			if not process:
				raise Error("invoke_function error")			
				

			# 用户B调用智能合约A中的A方法提取用户A给用户C的10 ong
			(process, response) = API.contract().invoke_function(contract_address, "transferFrom_ong", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_B]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_C]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])
			process = (not process or response["result"]["Result"] == "00")	

			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_normal_058_mutiContract(self):
		try:
			process = False

			contract_address = API.contract().deploy_contract(test_config.testpath + "/resource/38-43_48-59/A2.neo")
	
			# 用户B调用智能合约A中的A方法查询用户A的账户ont余额
			(process, response) = API.contract().invoke_function(contract_address, "balanceOf_ong", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				}])
			process = (process and response["result"]["Result"] != "00")	

			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

	def test_normal_059_mutiContract(self):
		try:
			process = False
 
			contract_address = API.contract().deploy_contract(test_config.testpath + "/resource/38-43_48-59/A2.neo")

			# 用户B调用智能合约A中的A方法查询用户A给用户C的ont还有多少没有接收
			(process, response) = API.contract().invoke_function(contract_address, "allowance_ong", Config.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": Common.bl_address((Config.NODES[Config.node_C]["address"]))
																				}])
			process = (process and response["result"]["Result"] != "00")	

			
			self.ASSERT(process, "")
		except Error as e:
			logger.print(e.msg)
		except Exception as e2:
			logger.print(e2.args[0])

####################################################
if __name__ == '__main__':
	unittest.main()
