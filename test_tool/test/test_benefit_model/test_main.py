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
from api.apimanager import API

from test_benefit_model.test_api import test_api
from test_benefit_model.test_config import test_config

####################################################
# test cases
# 请准备 9个节点进行测试
		
class test_benefit_model_1(ParametrizedTestCase):
	def setUp(self):
		logger.open("test_benefit_model/" + self._testMethodName+".log",self._testMethodName)
		if self._testMethodName == "test_init":
			return

		API.node().stop_all_nodes()
		API.node().start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
		
		for i in range(7):
			API.native().regid_with_publickey(i, sleep = 0)

		API.native().init_ont_ong(sleep = 0)
		
		time.sleep(5)
		self.m_current_node = 0
		self.m_stop_2_nodes = [5,6]
		self.m_new_2_nodes = [7, 8]
		self.m_checknode = 4
		self.m_dbft_nodes = [5,6] #拜占庭节点

	def tearDown(self):
		logger.close(self.result())
		
	def test_base_001_benefit(self):
		process = False
		try:
			address1 = Config.NODES[1]["address"]
			(process, response) = API.rpc().getbalance(address1)
			self.BLOCK(process, "get balance error")

			ong1=int(response["result"]["ong"])
			
			(process, response) = API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[0]["address"], "1", gas_price = test_config.PRICE_TEST)
			
			#判断是否分润，至少需要等待1个共识时间
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "can't gen block")
			API.node().wait_gen_block()
			(process, response) = API.rpc().getbalance(address1)
			self.BLOCK(process, "get balance error")

			ong2=int(response["result"]["ong"])
			logger.info("before cost[1]: " + str(ong1))
			logger.info("after cost[1]: " + str(ong2))
			self.ASSERT(ong2 != ong1, "get balance error")

		except Exception as e:
			logger.error(e.args[0])
		
	#blocked
	def test_normal_002_benefit(self):
		process = False
		try:
			address1 = Config.NODES[self.m_checknode]["address"]
			(process, response) = API.rpc().getbalance(address1)
			self.BLOCK(process, "get balance error")

			ong1=int(response["result"]["ong"])
			
			(process, response) = API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[0]["address"], "1", gas_price = test_config.PRICE_TEST)
			
			#判断是否分润，至少需要等待1个共识时间
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			(process, response) = API.rpc().getbalance(address1)
			self.BLOCK(process, "get balance error")
			ong2=int(response["result"]["ong"])
			print("before cost[1]: " + str(ong1))
			print("after cost[1]: " + str(ong2))
			self.ASSERT(ong2 != ong1, "get balance error")
			
		except Exception as e:
			logger.print(e.args[0])
			process = False
		
	def test_abnormal_003_benefit(self):
		try:
			address = Config.NODES[self.m_checknode]["address"]
			# logger.open("test_003_benefit.log", "test_003_benefit")
			process = True
			(process, response)=API.rpc().getbalance(address)
			self.BLOCK(process, "get balance error[1]")

			ong1=int(response["result"]["ong"])
			ont1=int(response["result"]["ont"])
		
			API.node().transfer_ont(0, 0 , 9999999999999999999, test_config.PRICE_TEST)

			#判断是否分润，至少需要等待1个共识时间
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			(process, response) = API.rpc().getbalance(address)
			self.BLOCK(process, "get balance error[2]")
			
			ong2 = int(response["result"]["ong"])
			ont2 = int(response["result"]["ont"])
		
			self.ASSERT((ong2 - ong1) == 0, "error")

		except Exception as e:
			logger.print(e.args[0])
			process = False
 
	#
	def test_normal_004_benefit(self):
		try:
			process = False
			address_stop = Config.NODES[self.m_stop_2_nodes[0]]["address"]
			(process, response) = API.rpc().getbalance(address_stop)
			self.BLOCK(process, "get balance error[1]")

			ong_stop1 = int(response["result"]["ong"])
			
			API.node().stop_nodes(self.m_stop_2_nodes)
			address1 = Config.NODES[1]["address"]
			(process, response) = API.rpc().getbalance(address1)
			self.BLOCK(process, "get balance error[2]")

			ong1=int(response["result"]["ong"])
			(process, response) = API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[0]["address"], "1", gas_price = test_config.PRICE_TEST)
			
			#判断是否分润，至少需要等待1个共识时间
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			(process, response) = API.rpc().getbalance(address1)
			self.BLOCK(process, "get balance error[3]")
			ong2=int(response["result"]["ong"])
			self.BLOCK(ong2 != ong1, "no benefit[1]")
			
			#start_nodes(self.m_stop_2_nodes)
			#time.sleep(10)
			
			(process, response) = API.rpc().getbalance(address_stop)
			self.BLOCK(process, "get balance error[4]")
			ong_stop2 = int(response["result"]["ong"])
			print("no benefit, before cost[1]: " + str(ong_stop1))
			print("no benefit, after cost[1]: " + str(ong_stop2))
			self.ASSERT(ong_stop2 != ong_stop1, "benefit[2]")
				
		except Exception as e:
			logger.print(e.args[0])
			process = False
 	
	
	def test_normal_005_benefit(self):
		try:
			process = False
			#启动拜占庭节点
			API.node().stop_nodes(self.m_dbft_nodes)
			API.node().start_nodes(self.m_dbft_nodes, Config.DEFAULT_NODE_ARGS, True, True, program = "ontology-bft_1")

			(process, response) = API.native().update_global_param("0", "1000", "32", "1", "50", "50", "5", "5")
			self.BLOCK(process, "updateGlobalParam error")
			
			(process, response) = API.rpc().getbalance(Config.NODES[self.m_checknode]["address"])
			self.BLOCK(process, "get balance error")
			ong1 = int(response["result"]["ong"])
			(process, response) = API.rpc().getbalance(Config.NODES[self.m_dbft_nodes[0]]["address"])
			self.BLOCK(process, "get balance error")
			dbft_ong1 = int(response["result"]["ong"])
					
			#进行第一轮共识
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			(process, response) = API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[0]["address"], "1", gas_price = test_config.PRICE_TEST)

			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			
			(process, response) = API.rpc().getbalance(Config.NODES[self.m_checknode]["address"])
			self.BLOCK(process, "get balance error")
			ong2 = int(response["result"]["ong"])
			(process, response) = API.rpc().getbalance(Config.NODES[self.m_dbft_nodes[0]]["address"])
			self.BLOCK(process, "get balance error")
			dbft_ong2 = int(response["result"]["ong"])
			
			#第二轮判断
			except_benifit = int(test_api.get_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 10000, [10000, 10000, 10000, 10000, 10000, 10000, 10000]))
			self.ASSERT((dbft_ong2 != dbft_ong1), "bft node benefit error")
			self.ASSERT((ong2 != ong1), "normal node benefit error")
			
		except Exception as e:
			logger.print(e.args[0])
 
	
	def test_normal_006_benefit(self):
		try:
			process = False
 
			(process, response) = API.native().update_global_param("0", "1000", "32", "1", "50", "50", "5", "5")
			self.BLOCK(process, "updateGlobalParam error")
			
			(process, response) = API.rpc().getbalance(Config.NODES[self.m_checknode]["address"])
			self.BLOCK(process, "get balance error")
			ong1 = int(response["result"]["ong"])
			
			(process, response) = API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[0]["address"], "1", gas_price = test_config.PRICE_TEST)
			
			(process, response) = API.rpc().getbalance(Config.NODES[self.m_checknode]["address"])
			self.BLOCK(process, "get balance error")
			ong2 = int(response["result"]["ong"])
			
			#第一轮判断
			self.ASSERT(ong1 == ong2, "benefit error")
		
			#进行第一轮共识
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			(process, response) = API.rpc().getbalance(Config.NODES[self.m_checknode]["address"])
			self.BLOCK(process, "get balance error")
			ong3 = int(response["result"]["ong"])
			
			#第二轮判断
			except_benifit = int(test_api.get_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 10000, [10000, 10000, 10000, 10000, 10000, 10000, 10000]))
			self.ASSERT((ong3 - ong2) == except_benifit, "first benefit error")
			
		except Exception as e:
			logger.print(e.args[0])

	
	#前提: 7个节点initpos 都是 1000
	def test_normal_007_benefit(self):
		try:
			process = False
		
			address1 = Config.NODES[self.m_checknode]["address"]
			(process, response) = API.rpc().getbalance(address1)
			self.BLOCK(process, "get balance error[1]")

			ong1=int(response["result"]["ong"])
			
			(process, response) = API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[0]["address"], "1", gas_price = test_config.PRICE_TEST)
			
			#判断是否分润，至少需要等待1个共识时间
			except_benifit = int(test_api.get_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 1000, [1000, 1000, 1000, 1000, 1000, 1000, 1000]))
			logger.print("except_benifit: " + str(except_benifit))
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()	
			(process, response) = API.rpc().getbalance(address1)
			self.BLOCK(process, "get balance error[2]")

			ong2=int(response["result"]["ong"])
			print("before cost[1]: " + str(ong1))
			print("after cost[1]: " + str(ong2))
			self.ASSERT((int(ong2 - ong1) == int(except_benifit)), "")
		
		except Exception as e:
			logger.print(e.args[0])

	
	#第7个节点为新加入节点
	def test_normal_008_benefit(self):
		
		try:
			
			process = False
			
			candidate_initong = 1000 #候选节点初始ong
			
			candidate_pos = 1000 #候选节点初始pos
			new_node = self.m_new_2_nodes[0] #新加入节点
			
			
			(process, response) = API.native().update_global_param("0", "1000", "32", "1", "50", "50", "5", "5", sleep = 0)
			self.BLOCK(process, "updateGlobalParam error")
			API.node().wait_gen_block()
			
			address4 = Config.NODES[self.m_checknode]["address"]
			(process, response) = API.rpc().getbalance(address4)
			self.BLOCK(process, "get balance error")
			ong1 = int(response["result"]["ong"])
			
			##for debug
			for i in range(7):
				print("get balance[0]: " + str(i))
				API.rpc().getbalance(Config.NODES[i]["address"])

			print("get balance[0.2]: " + str("AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK"))
			API.rpc().getbalance("AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK")	
			####################################################################################
			#发生一笔交易，并第一次分红
			process = API.native().transfer_ont(pay_address = Config.NODES[0]["address"],
												get_address = Config.NODES[0]["address"], 
												amount = "1", 
												node_index = 0,
												gas_price = test_config.PRICE_TEST, 
												sleep = 0)
			self.BLOCK(process, "transfer_ont error")
			time.sleep(15)
			print("get balance[0.1]: " + str(i))
			API.rpc().getbalance(Config.NODES[0]["address"])
			
			(process, response) = API.native().commit_dpos(sleep = 0)
			time.sleep(15)
			self.BLOCK(process, "commit_dpos error")
			
			##for debug
			for i in range(7):
				print("get balance[1]: " + str(i))
				API.rpc().getbalance(Config.NODES[i]["address"])

			#2.消耗的0.2ong的50%被平均分给七个节点
			except_benifit = int(test_api.get_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 10000, [10000, 10000, 10000, 10000, 10000, 10000, 10000]))
			except_benifit2 = int(test_api.get_benifit_value(20000 * test_config.PRICE_TEST * 0.5 * 0.5, 10000, [10000, 10000, 10000, 10000, 10000, 10000, 10000]))
			except_benifit3 = int(test_api.get_benifit_value(20000 * test_config.PRICE_TEST * 0.5 * 0.5 *0.5, 10000, [10000, 10000, 10000, 10000, 10000, 10000, 10000]))
			except_benifit4 = int(test_api.get_candidate_benifit_value(20000 * test_config.PRICE_TEST * 0.5 * 0.5 *0.5, candidate_pos, [candidate_pos]))
			logger.print("except_benifit[1]: " + str(except_benifit))
			logger.print("except_benifit[2]: " + str(except_benifit2))
			logger.print("except_benifit[3]: " + str(except_benifit3))
			logger.print("except_benifit[4]: " + str(except_benifit4))
			(process, response) = API.rpc().getbalance(address4)
			self.BLOCK(process, "get balance error")
			ong2 = int(response["result"]["ong"])

			logger.info("before cost[1]: " + str(ong1))
			logger.info("after cost[1]: " + str(ong2))
			process = (int(ong2 - ong1) == int(except_benifit))
			self.ASSERT(process, "first benefit error")
			
			####################################################################################
			#添加候选节点1
			
			(process, response) = test_api.add_candidate_node(new_node, init_ong = candidate_initong)
			self.ASSERT(process, "add candidate node error")
			print("get balance[1.1]: " + str(0))
			API.rpc().getbalance(Config.NODES[0]["address"])
			
			#4.消耗的0.2ong的50%被分配给刚加入的候选节点
			(process, response) = API.rpc().getbalance(Config.NODES[new_node]["address"])
			self.ASSERT(process, "get balance error")
			ong3 = int(response["result"]["ong"])
			
			#区块到达分红数量要求
			#print("33333333333333: ")
			#nodeCountCheck([], 7)
			time.sleep(15)
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			time.sleep(15)

			for i in range(7):
				print("get balance[2]: " + str(i))
				API.rpc().getbalance(Config.NODES[i]["address"])

			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			time.sleep(15)

			#print("44444444444444: ")
			#nodeCountCheck([], 7)
			#4.消耗的0.2ong的50%被分配给刚加入的候选节点
			(process, response) = API.rpc().getbalance(address4)
			self.BLOCK(process, "get balance error")
			ong2 = int(response["result"]["ong"])

			(process, response) = API.rpc().getbalance(Config.NODES[new_node]["address"])
			self.BLOCK(process, "get balance error")
			ong4 = int(response["result"]["ong"])
			
			logger.info("normal node before cost[1]: " + str(ong1))
			logger.info("normal node after cost[2]: " + str(ong2))
			logger.info("normal except: " + str(except_benifit3 + except_benifit2 + except_benifit))

			logger.info("cadidate node before cost[2]: " + str(ong3))
			logger.info("cadidate node after cost[2]: " + str(ong4))
			process = abs((int(ong4 - ong3) - int(except_benifit4))) < 10

			##for debug
			for i in range(7):
				print("get balance[3]: " + str(i))
				API.rpc().getbalance(Config.NODES[i]["address"])

			print("get balance[3.1]: " + str("AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK"))
			API.rpc().getbalance("AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK")	

			self.ASSERT(process, "benefit error")

		except Exception as e:
			logger.print(e.args[0])
			process = False

	#第7个节点为新加入节点
	def test_normal_009_benefit(self):
		try:
			process = False
			
			candidate_pos = 1000 #候选节点初始pos
			
			new_node1 = self.m_new_2_nodes[0]
			new_node2 = self.m_new_2_nodes[1]
			address1 = Config.NODES[self.m_checknode]["address"]
 
			API.native().update_global_param("0", "1000", "32", "1", "50", "50", "5", "5")
			
			#发生一笔交易
			(process, response) = API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[0]["address"], "1", gas_price = test_config.PRICE_TEST)
			time.sleep(5)

			#添加候选节点1
			(process, response) = test_api.add_candidate_node(new_node1, init_pos = candidate_pos)
			self.BLOCK(process, "add candidate error")
		
			#区块到达分红数量要求,获取共识前后的ong值
			(process, response) = API.rpc().getbalance(address1)
			self.BLOCK(process, "get balance error")
			normal_ong1 = int(response["result"]["ong"])
			(process, response) = API.rpc().getbalance(Config.NODES[new_node1]["address"])
			self.BLOCK(process, "get balance error")
			candidate1_ong_1 = int(response["result"]["ong"])
	
			#第一次分红，只分红共识节点的，因为候选节点要在下个周期才分红
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			#第二次分红，候选节点也分红
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			
			API.node().wait_gen_block()

			(process, response) = API.rpc().getbalance(address1)
			self.BLOCK(process, "get balance error")
			normal_ong2 = int(response["result"]["ong"])
			(process, response) = API.rpc().getbalance(Config.NODES[new_node1]["address"])
			self.BLOCK(process, "get balance error")
			candidate1_ong_2 = int(response["result"]["ong"])
			
			#计算分红值
			except_benifit1 = int(test_api.get_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 10000, [10000, 10000, 10000, 10000, 10000, 10000, 10000]))
			except_benifit2 = int(test_api.get_benifit_value(20000 * test_config.PRICE_TEST * 0.5 * 0.5, 10000, [10000, 10000, 10000, 10000, 10000, 10000, 10000]))
			except_candidate_benifit1 = int(test_api.get_candidate_benifit_value(20000 * test_config.PRICE_TEST * 0.5 * 0.5, candidate_pos, [candidate_pos]))
			
			#判断分红值
			#消耗的0.2ong的50%被平均分给七个节点，50%被分配给刚加入的候选节点
			logger.print("before cost[1]: " + str(normal_ong1))
			logger.print("after cost[1]: " + str(normal_ong2))
			process = abs(int(normal_ong2 - normal_ong1) - int(except_benifit1 + except_benifit2)) < 10
			self.ASSERT(process, "first benefit error[normal node][1]")
			
			process = abs(int(candidate1_ong_2 - candidate1_ong_1) - int(except_candidate_benifit1)) < 10
			self.ASSERT(process, "first benefit error[candidate node][2]")
		
			#添加候选节点2
			(process, response) = test_api.add_candidate_node(new_node2)
			self.BLOCK(process, "add candidate node error")

			#第一次共识，确保下次一起分红，因为候选节点要在下个周期才分红
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			
			#4.消耗的0.2ong的50%被分配给刚加入的候选节点
			(process, response) = API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[0]["address"], "1", gas_price = test_config.PRICE_TEST)
			self.BLOCK(process, "transfer ont error")
			time.sleep(5)
		
			
			#区块到达分红数量要求
			(process, response) = API.rpc().getbalance(address1)
			self.BLOCK(process, "get balance error")
			normal_ong3 = int(response["result"]["ong"])
			(process, response) = API.rpc().getbalance(Config.NODES[new_node2]["address"])
			self.BLOCK(process, "get balance error")
			candidate2_ong_1 = int(response["result"]["ong"])
			
			#第二次分红，候选节点也分红
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			(process, response) = API.rpc().getbalance(address1)
			self.BLOCK(process, "get balance error")
			normal_ong4 = int(response["result"]["ong"])
			
			(process, response) = API.rpc().getbalance(Config.NODES[new_node2]["address"])
			self.BLOCK(process, "get balance error")
			candidate2_ong_2 = int(response["result"]["ong"])
			
			#计算分红值
			except_benifit1 = int(test_api.get_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 10000, [10000, 10000, 10000, 10000, 10000, 10000, 10000]))
			except_candidate_benifit1 = int(test_api.get_candidate_benifit_value(20000 * test_config.PRICE_TEST * 0.5, candidate_pos, [candidate_pos, candidate_pos]))
			#判断分红值
			#消耗的0.2ong的50%被平均分给七个节点，50%被分配给刚加入的候选节点

			logger.print("before cost[2]: " + str(normal_ong3))
			logger.print("after cost[2]: " + str(normal_ong4))
			process = abs(int(normal_ong4 - normal_ong3) - int(except_benifit1)) < 10
			self.ASSERT(process, "first benefit error[normal node][3]")
			
			#在10以内的误差
			process = abs((int(candidate2_ong_2 - candidate2_ong_1) - int(except_candidate_benifit1))) < 10
			self.ASSERT(process, "first benefit error[candidate node][4]")
			
		except Exception as e:
			logger.print(e.args[0])

		
	def test_normal_010_benefit(self):
		try:
			address = Config.NODES[2]["address"]
			process = False

			API.native().update_global_param("0", "1000", "32", "1", "50", "50", "5", "5")

			new_node = self.m_new_2_nodes[0] #新加入节点
			
			address4 = Config.NODES[self.m_checknode]["address"]
			(process, response) = API.rpc().getbalance(address4)
			self.BLOCK(process, "get balance error")
			ong1 = int(response["result"]["ong"])

			test_api.add_candidate_node(new_node, init_pos = 20000)
			time.sleep(10)

			#第一次共识，没有ong分润，但是候选节点会成为共识节点
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			(process, response) = API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[0]["address"], "1", gas_price = test_config.PRICE_TEST)
			time.sleep(5)
 
			(process, response) = API.rpc().getbalance(address4)
			self.BLOCK(process, "get balance error")
			normal_ong = int(response["result"]["ong"])
			(process, response) = API.rpc().getbalance(Config.NODES[new_node]["address"])
			self.BLOCK(process, "get balance error")
			candidate_ong = int(response["result"]["ong"])
			
			#第二次共识，有ong分润
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			except_benifit1 = int(test_api.get_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 10000, [10000, 10000, 10000, 10000, 10000, 10000, 10000]))
			except_benifit3 = int(test_api.get_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 20000, [20000, 10000, 10000, 10000, 10000, 10000, 10000]))
			except_candidate_benifit1 = int(test_api.get_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 10000, [10000]))
			except_candidate_benifit2 = int(test_api.get_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 20000, [20000]))
			logger.info("except_benifit1:" + str(except_benifit1))
			logger.info("except_benifit3:" + str(except_benifit3))
			logger.info("except_candidate_benifit1:" + str(except_candidate_benifit1))
			logger.info("except_candidate_benifit2:" + str(except_candidate_benifit2))
			
			(process, response) = API.rpc().getbalance(address4)
			self.BLOCK(process, "get balance error")
			normal_ong2 = int(response["result"]["ong"])
			(process, response) = API.rpc().getbalance(Config.NODES[new_node]["address"])
			self.BLOCK(process, "get balance error")
			candidate_ong2 = int(response["result"]["ong"])
			
			logger.info("normal_ong2: " + str(normal_ong2))
			logger.info("candidate_ong2: " + str(candidate_ong2))
			process = abs((int(candidate_ong2 - candidate_ong) - int(except_benifit3))) < 10
			self.ASSERT(process, "benefit error")
		
		except Exception as e:
			logger.print(e.args[0])

class test_benefit_model_2(ParametrizedTestCase):
	def setUp(self):
		logger.open( "test_benefit_model/" + self._testMethodName+".log",self._testMethodName)
		if self._testMethodName == "test_init":
			return

		self.m_checknode = 4
		time.sleep(2)
		print("stop all")
		API.node().stop_all_nodes()
		print("start all")
		API.node().start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
		for i in range(7):
			API.native().regid_with_publickey(i)
		API.native().init_ont_ong()

	def tearDown(self):
		logger.close(self.result())
		
	def test_normal_011_benefit(self):
		try:
			process = False
			vote_node = 13 #投票节点
			peer_node1 = 7 #被投票节点1
			peer_node2 = 8 #被投票节点2
			peer_node3 = 9 #被投票节点3
			unpeer_node = 10 #未被投票节点
 
			API.native().update_global_param("0", "1000", "32", "10", "50","50", "5", "5")
	
			API.node().start_nodes([vote_node], Config.DEFAULT_NODE_ARGS, True, True)
			(process, response) = API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[vote_node]["address"], "5000000", gas_price = 0)
			(process, response) = API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[vote_node]["address"], "1000", gas_price = 0)

			for i in range(7, 13):
				test_api.add_candidate_node(i, init_pos = 5000, from_node = i - 7)
			
			#投票给三个节点成为共识节点
			(process, response) = API.native().vote_for_peer(Config.NODES[vote_node]["address"], [Config.NODES[peer_node1]["pubkey"], Config.NODES[peer_node2]["pubkey"], Config.NODES[peer_node3]["pubkey"]], ["15000", "15000", "15000"])
			self.BLOCK(process, "vote error")
			
			#先共识一次，确保节点都会在下一次共识分红
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			
			#交易
			(process, response) = API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[0]["address"], "1", gas_price = test_config.PRICE_TEST)

			(process, response) = API.rpc().getbalance(Config.NODES[peer_node1]["address"])
			self.BLOCK(process, "get balance error")
			normal_ong = int(response["result"]["ong"])
			(process, response) = API.rpc().getbalance(Config.NODES[unpeer_node]["address"])
			self.BLOCK(process, "get balance error")
			candidate_ong = int(response["result"]["ong"])
			
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			(process, response) = API.rpc().getbalance(Config.NODES[peer_node1]["address"])
			self.BLOCK(process, "get balance error")
			normal_ong2 = int(response["result"]["ong"])
			(process, response) = API.rpc().getbalance(Config.NODES[unpeer_node]["address"])
			self.BLOCK(process, "get balance error")
			candidate_ong2 = int(response["result"]["ong"])
			
			except_benifit1 = int(test_api.get_candidate_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 5000, [5000, 5000, 5000, 10000, 10000, 10000]))
			except_benifit2 = int(test_api.get_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 20000, [20000, 20000, 20000, 10000, 10000, 10000, 10000]))
			logger.info("normal_ong2: " + str(normal_ong2))
			logger.info("except_benifit1: " + str(except_benifit1))
			
			logger.info("candidate_ong2: " + str(candidate_ong2))
			logger.info("except_benifit2: " + str(except_benifit2))
			self.ASSERT((normal_ong2 - normal_ong) == except_benifit2, "benefit normal node error")
			self.ASSERT((candidate_ong2 - candidate_ong) == except_benifit1, "benefit candidate node error")

			
		except Exception as e:
			logger.error(e.args[0])

			
	def test_normal_012_benefit(self):
		try:
			address = Config.NODES[self.m_checknode]["address"]
			process = False
			unpeer_node = 10 #未被投票节点

			API.native().update_global_param("0", "1000","32", "10", "100","0", "5", "5")
			
			
			for i in range(7, 14):
				test_api.add_candidate_node(i, init_pos = 5000, from_node = i - 7)
			
			#先共识一次，确保节点都会在下一次共识分红
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			#交易
			(process, response) = API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[0]["address"], "1", gas_price = test_config.PRICE_TEST)

			(process, response) = API.rpc().getbalance(address)
			self.BLOCK(process, "get balance error")
			normal_ong = int(response["result"]["ong"])
			(process, response) = API.rpc().getbalance(Config.NODES[unpeer_node]["address"])
			self.BLOCK(process, "get balance error")
			candidate_ong = int(response["result"]["ong"])
			
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			
			(process, response) = API.rpc().getbalance(address)
			self.BLOCK(process, "get balance error")
			normal_ong2 = int(response["result"]["ong"])
			(process, response) = API.rpc().getbalance(Config.NODES[unpeer_node]["address"])
			self.BLOCK(process, "get balance error")
			candidate_ong2 = int(response["result"]["ong"])
			
			except_benifit1 = int(test_api.get_benifit_value(20000 * test_config.PRICE_TEST, 10000, [10000, 10000, 10000, 10000, 10000, 10000, 10000]))
			except_benifit2 = 0
			print("normal_ong2: " + str(normal_ong2))
			print("candidate_ong2: " + str(candidate_ong2))
			self.ASSERT((normal_ong2 - normal_ong) == except_benifit1, "benefit normal node error")
			self.ASSERT((candidate_ong2 - candidate_ong) == except_benifit2, "benefit candidate node error")
		except Exception as e:
			logger.print(e.args[0])


	def test_normal_013_benefit(self):
		try:
			address = Config.NODES[self.m_checknode]["address"]
			process = False
			unpeer_node = 10 #未被投票节点

			API.native().update_global_param("0", "1000","32", "10", "0","100", "5", "5")
			
			for i in range(7, 14):
				test_api.add_candidate_node(i, init_pos = 5000, from_node = i - 7)
			
			#先共识一次，确保节点都会在下一次共识分红
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			#交易
			(process, response) = API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[0]["address"], "1", gas_price = test_config.PRICE_TEST)

			(process, response) = API.rpc().getbalance(address)
			self.BLOCK(process, "get balance error")
			normal_ong = int(response["result"]["ong"])
			(process, response) = API.rpc().getbalance(Config.NODES[unpeer_node]["address"])
			self.BLOCK(process, "get balance error")
			candidate_ong = int(response["result"]["ong"])
			(process, response) = API.native().commit_dpos(sleep = 0)
			self.BLOCK(process, "commit_dpos error")
			API.node().wait_gen_block()
			(process, response) = API.rpc().getbalance(address)
			self.BLOCK(process, "get balance error")
			normal_ong2 = int(response["result"]["ong"])
			(process, response) = API.rpc().getbalance(Config.NODES[unpeer_node]["address"])
			self.BLOCK(process, "get balance error")
			candidate_ong2 = int(response["result"]["ong"])
			
			except_benifit1 = int(test_api.get_candidate_benifit_value(20000 * test_config.PRICE_TEST, 5000, [5000, 5000, 5000, 5000, 5000, 5000, 5000]))
			except_benifit2 = 0
			logger.info("normal_ong1: " + str(normal_ong))
			logger.info("normal_ong2: " + str(normal_ong2))
			logger.info("candidate_ong1: " + str(candidate_ong))
			logger.info("candidate_ong2: " + str(candidate_ong2))
			self.ASSERT((normal_ong2 - normal_ong) == except_benifit2, "benefit normal node error")
			self.ASSERT((candidate_ong2 - candidate_ong) == except_benifit1, "benefit candidate node error")
			
			
		except Exception as e:
			logger.print(e.args[0])
			process = False

	
####################################################
if __name__ == '__main__':
	'''
	print("55555555: ")
	nodeCountCheck([], 7)
	API.native().commit_dpos()
	time.sleep(15)
	print("66666666: ")
	nodeCountCheck([], 7)
	'''
	#for i in range(0, 14):
	#	print(i)
	#except_benifit3 = int(get_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 20000, [20000, 10000, 10000, 10000, 10000, 10000, 10000]))
	#print(except_benifit3)
	#(process, response) = API.rpc().getbalance(Config.NODES[7]["address"])
	unittest.main()
	
	#except_benifit1 = int(get_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 20000, [20000, 20000, 20000, 10000, 10000, 10000, 10000]))
	#except_benifit2 = int(get_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 10000, [20000, 20000, 20000, 10000, 10000, 10000, 10000]))
	
	#except_benifit3 = int(get_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 5000, [5000, 5000, 5000, 10000, 10000, 10000]))
	#except_benifit4 = int(get_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 10000, [5000, 5000, 5000, 10000, 10000, 10000]))
	#print("1111: " + str(except_benifit1))
	#print("1111: " + str(except_benifit2))
	#print("1111: " + str(except_benifit3))
	#print("1111: " + str(except_benifit4))

	'''
	except_benifit4 = int(get_benifit_value(20000 * test_config.PRICE_TEST * 0.5, 10000, [5000, 5000, 5000, 10000, 10000, 10000]))
	print("1111: " + str(except_benifit2))
	print("1111: " + str(except_benifit3))
	print("1111: " + str(except_benifit4))
	'''
	#API.native().commit_dpos()
