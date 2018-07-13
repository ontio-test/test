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

logger = LoggerInstance
rpcapiTest=RPCApi()

ontCount_1 = "10000"
user_1 = "1"  #固定为"1"即可
voteCount = 500

class test_zhiliChangjing(ParametrizedTestCase):
	@classmethod
	def setUp(self):
		pass
		#restart all node
		#init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		# register ONTID
	def test(self): 
		pass
		# logger.open("test.log", "test")
		# (result, response)=nodeCountCheck([],7)
		# logger.close(result)
		
	def test_01(self):
		logger.open("test01.log", "test01")
		(result, response) = getGlobalParam()
		(result, response) = invoke_function_update("updateGlobalParam",param0=500000000000,param1=10000,param2=49,param3=20,param4=50,param5=50,param6=5,param7=5)
		(result, response) = getGlobalParam()
		logger.close(result)
		
	def test_02(self):
		logger.open("test02.log", "test02")
		(result, response) = getGlobalParam()
		(result, response) = invoke_function_update("updateGlobalParam",param0=500000000000,param1=10000,param2=49,param3=20,param4=50,param5=50,param6=5,param7=5)
		(result, response) =  getGlobalParam()
		logger.close(result)

	def test_03(self):
		logger.open("test03.log", "test03")
		(result, response) = getGlobalParam()
		(result, response) = getGovernanceView()
		(result, response) = invoke_function_SplitCurve() ##
		(result, response) = getPeerPoolItem()   ### test() 
		(result, response) = getTotalStake()
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(5)
		for num in range(7,14):
			(result, response) = invoke_function_register("registerCandidate",Config.NODES[num]["pubkey"],Config.NODES[num]["address"],ontCount_1,ByteToHex((Config.NODES[num]["ontid"]).encode("utf-8")),user_1,errorcode=0,node_index=num)  
			time.sleep(5)
			(result, response) = invoke_function_candidate("approveCandidate",Config.NODES[num]["pubkey"],errorcode=0)
			time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = nodeCountCheck(response,14)
		time.sleep(5)
		for num in range(0,7):
			(result, response) = invoke_function_quitNode("quitNode",Config.NODES[num]["pubkey"],Config.NODES[num]["address"],num,0)
			time.sleep(5)	
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response)= nodeCountCheck(response,7)
		logger.close(result)
		
	def test_04(self):
		logger.open("test04.log", "test04")
		(result, response) = getGlobalParam()
		(result, response) = getGovernanceView()
		(result, response) = getSplitCurve()
		(result, response) = getPeerPoolItem()  
		(result, response) = getTotalStake()
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(5)
		for num in range(7,14):
			(result, response) = invoke_function_candidate("approveCandidate",Config.NODES[num]["pubkey"],errorcode=0)
			time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = nodeCountCheck(response,7)
		time.sleep(5)
		for num in range(0,7):
			(result, response) = invoke_function_quitNode("quitNode",Config.NODES[num]["pubkey"],Config.NODES[num]["address"],num,0)
			time.sleep(5)	
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response)=nodeCountCheck(response,7)
		logger.close(result)
		
	def test_05(self):
		logger.open("test05.log", "test05")
		(result, response) = getGlobalParam()
		(result, response) = getGovernanceView()
		(result, response) = getSplitCurve()
		(result, response) = getPeerPoolItem()  
		(result, response) = getTotalStake()
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(5)
		for num in range(7,14):
			(result, response) = invoke_function_register("registerCandidate",Config.NODES[num]["pubkey"],Config.NODES[num]["address"],ontCount_1,ByteToHex((Config.NODES[num]["ontid"]).encode("utf-8")),user_1,errorcode=0,node_index=num)  
			time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = nodeCountCheck(response,7)
		time.sleep(5)
		for num in range(0,7):
			(result, response) = invoke_function_quitNode("quitNode",Config.NODES[num]["pubkey"],Config.NODES[num]["address"],num,0)
			time.sleep(5)	
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response)=nodeCountCheck(response,7)
		logger.close(result)
		
	def test_06(self):
		logger.open("test06.log", "test06")
		(result, response) = getGlobalParam()
		(result, response) = getGovernanceView()
		(result, response) = getSplitCurve()
		(result, response) = getPeerPoolItem()  
		(result, response) = getTotalStake()
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(5)
		for num in range(7,14):
			(result, response) = invoke_function_register("registerCandidate",Config.NODES[num]["pubkey"],Config.NODES[num]["address"],ontCount_1,ByteToHex((Config.NODES[num]["ontid"]).encode("utf-8")),user_1,errorcode=0,node_index=num)  
			time.sleep(5)
			(result, response) = invoke_function_candidate("approveCandidate",Config.NODES[num]["pubkey"],errorcode=0)
			time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = nodeCountCheck(response,14)
		time.sleep(5)
		for num in range(7,14):
			(result, response) = invoke_function_candidate("approveCandidate",Config.NODES[num]["pubkey"],errorcode=0)
			time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = nodeCountCheck(response,14)
		time.sleep(5)
		for num in range(0,7):
			(result, response) = invoke_function_quitNode("quitNode",Config.NODES[num]["pubkey"],Config.NODES[num]["address"],num,0)
			time.sleep(5)	
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response)=nodeCountCheck(response,7)
		logger.close(result)

	def test_07(self):
		logger.open("test07.log", "test07")
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(5)
		(result, response) = nodeCountCheck(response,7)
		(result, response) = invoke_function_register("registerCandidate",Config.NODES[7]["pubkey"],Config.NODES[7]["address"],ontCount_1,ByteToHex((Config.NODES[7]["ontid"]).encode("utf-8")),user_1,errorcode=0,node_index=7)  
		time.sleep(5)
		(result, response) = invoke_function_candidate("approveCandidate",Config.NODES[7]["pubkey"],errorcode=0)
		time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = nodeCountCheck(response,8)
		time.sleep(5)
		logger.close(result)
		
	def test_08(self):
		logger.open("test08.log", "test08")
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(5)
		(result, response) = nodeCountCheck(response,7)
		(result, response) = invoke_function_register("registerCandidate",Config.NODES[8]["pubkey"],Config.NODES[8]["address"],ontCount_1,ByteToHex((Config.NODES[8]["ontid"]).encode("utf-8")),user_1,errorcode=0,node_index=8)  
		time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = nodeCountCheck(response,7)
		time.sleep(5)
		logger.close(result)

	def test_09(self):
		logger.open("test09.log", "test09")
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(5)
		(result, response) = nodeCountCheck(response,7)
		(result, response) = invoke_function_register("registerCandidate",Config.NODES[9]["pubkey"],Config.NODES[9]["address"],ontCount_1,ByteToHex((Config.NODES[9]["ontid"]).encode("utf-8")),user_1,errorcode=0,node_index=9)  
		time.sleep(5)
		(result, response) = invoke_function_candidate("approveCandidate",Config.NODES[9]["pubkey"],errorcode=0)
		time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = nodeCountCheck(response,8)			
		time.sleep(5)
		
		rpcapiTest.getbalance(Config.NODES[9]["address"])
		time.sleep(5)
		
		for n in range(0,7):
			(result, response) = invoke_function_vote("voteForPeer",Config.NODES[n]["address"],voteList=[Config.NODES[9]["pubkey"]],voteCount,errorcode = 0,node_index =9) 
			time.sleep(5)		
		
		(result, response) = rpcapiTest.getbalance(Config.NODES[9]["address"])
		time.sleep(5)
		(result, response) = GetTotalStake()
		time.sleep(5)
		logger.close(result)	
		
	def test_10(self):
		logger.open("test10.log", "test10")
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(5)
		(result, response) = nodeCountCheck(response,7)
		(result, response) = invoke_function_register("registerCandidate",Config.NODES[10]["pubkey"],Config.NODES[10]["address"],ontCount_1,ByteToHex((Config.NODES[10]["ontid"]).encode("utf-8")),user_1,errorcode=0,node_index=10)  
		time.sleep(5)
		(result, response) = invoke_function_candidate("approveCandidate",Config.NODES[10]["pubkey"],errorcode=0)
		time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = nodeCountCheck(response,8)			
		time.sleep(5)
		(result, response) = getPeerPoolItem()
		time.sleep(5)
		rpcapiTest.getbalance(Config.NODES[10]["address"])
		time.sleep(5)
		
		for n in range(0,7):
			(result, response) = invoke_function_vote("voteForPeer",Config.NODES[n]["address"],voteList=[Config.NODES[10]["pubkey"]],voteCount,errorcode = 0,node_index =10) 
			time.sleep(5)		
		(result, response) = getPeerPoolItem()
		time.sleep(5)
		(result, response) = rpcapiTest.getbalance(Config.NODES[10]["address"])
		time.sleep(5)
		(result, response) = GetTotalStake()
		time.sleep(5)
		(result, response) = getVoteInfo()
		time.sleep(5)
		logger.close(result)
		
	def test_11(self):
		logger.open("test11.log", "test11")
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(5)
		(result, response) = nodeCountCheck(response,7)
		(result, response) = invoke_function_register("registerCandidate",Config.NODES[11]["pubkey"],Config.NODES[11]["address"],ontCount_1,ByteToHex((Config.NODES[11]["ontid"]).encode("utf-8")),user_1,errorcode=0,node_index=11)  
		time.sleep(5)
		(result, response) = invoke_function_candidate("approveCandidate",Config.NODES[11]["pubkey"],errorcode=0)
		time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = nodeCountCheck(response,8)			
		time.sleep(5)
		rpcapiTest.getbalance(Config.NODES[11]["address"])
		time.sleep(5)
		for n in range(0,7):
			(result, response) = invoke_function_vote("unVoteForPeer",Config.NODES[n]["address"],voteList=[Config.NODES[11]["pubkey"]],voteCount,errorcode = 0,node_index =11) 
			time.sleep(5)		
		(result, response) = getPeerPoolItem()
		time.sleep(5)
		(result, response) = rpcapiTest.getbalance(Config.NODES[11]["address"])
		time.sleep(5)
		(result, response) = GetTotalStake()
		time.sleep(5)
		logger.close(result)
		
	def test_12(self):
		logger.open("test12.log", "test12")
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(5)
		(result, response) = invoke_function_register("registerCandidate",Config.NODES[12]["pubkey"],Config.NODES[12]["address"],ontCount_1,ByteToHex((Config.NODES[12]["ontid"]).encode("utf-8")),user_1,errorcode=0,node_index=12)  
		time.sleep(5)
		(result, response) = invoke_function_candidate("approveCandidate",Config.NODES[12]["pubkey"],errorcode=0)
		time.sleep(5)	
		(result, response) = nodeCountCheck(response,8)
		(result, response) = GetPeerPoolItem() #chakan node2 status  02
		time.sleep(5)
		(result, response) = GetVoteInfo()
		time.sleep(5)
		(result, response) = invoke_function_quitNode("quitNode",Config.NODES[1]["pubkey"],Config.NODES[1]["address"],1,0)
		time.sleep(5)	
		(result, response) = GetPeerPoolItem() #chakan node2 status  03
		time.sleep(5)		
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = GetPeerPoolItem() 
		time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = GetPeerPoolItem()   #nodequit(yiding)
		time.sleep(5)
		(result, response) = nodeCountCheck(response,7)
		time.sleep(5)
		(result, response)= nodeCountCheck(response,7)
		logger.close(result)
		
	def test_13(self):
		logger.open("test13.log", "test13")
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(5)
		(result, response) = invoke_function_register("registerCandidate",Config.NODES[13]["pubkey"],Config.NODES[13]["address"],ontCount_1,ByteToHex((Config.NODES[13]["ontid"]).encode("utf-8")),user_1,errorcode=0,node_index=13)  
		time.sleep(5)
		(result, response) = invoke_function_candidate("approveCandidate",Config.NODES[13]["pubkey"],errorcode=0)
		time.sleep(5)	
		(result, response) = nodeCountCheck(response,8)
		(result, response) = GetPeerPoolItem() #chakan node14 status  01
		time.sleep(5)
		(result, response) = GetVoteInfo()
		time.sleep(5)
		(result, response) = invoke_function_quitNode("quitNode",Config.NODES[1]["pubkey"],Config.NODES[1]["address"],1,0)
		time.sleep(5)	
		(result, response) = GetPeerPoolItem() #chakan node2 status  04
		time.sleep(5)		
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = GetPeerPoolItem() 
		time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = GetPeerPoolItem()   #nodequit(yiding)
		time.sleep(5)
		(result, response) = nodeCountCheck(response,7)
		logger.close(result)
		
	def test_15(self):
		logger.open("test15.log", "test15")
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(5)
		for num in range(7,14):
			(result, response) = invoke_function_register("registerCandidate",Config.NODES[num]["pubkey"],Config.NODES[num]["address"],ontCount_1,ByteToHex((Config.NODES[num]["ontid"]).encode("utf-8")),user_1,errorcode=0,node_index=num)  
			time.sleep(5)
			(result, response) = invoke_function_candidate("approveCandidate",Config.NODES[num]["pubkey"],errorcode=0)
			time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = nodeCountCheck(response,14)
		time.sleep(5)
		(result, response) = GetPeerPoolItem() #chakan node13 status 01
		time.sleep(5)
		for n in range(0,7):
			(result, response) = invoke_function_vote("voteForPeer",Config.NODES[n]["address"],voteList=[Config.NODES[12]["pubkey"]],voteCount,errorcode = 0,node_index =12) 
			time.sleep(5)
		
		time.sleep(20)
		time.sleep(20)
		# (result, response) = invoke_function_commitDpos(0)
		# time.sleep(5)
		# (result, response) = invoke_function_commitDpos(0)
		# time.sleep(5)
		(result, response) = GetPeerPoolItem() #chakan node13 status 01
		time.sleep(5)
		logger.close(result)
	
	def test_16(self):
		logger.open("test16.log", "test16")
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(5)
		for num in range(7,14):
			(result, response) = invoke_function_register("registerCandidate",Config.NODES[num]["pubkey"],Config.NODES[num]["address"],ontCount_1,ByteToHex((Config.NODES[num]["ontid"]).encode("utf-8")),user_1,errorcode=0,node_index=num)  
			time.sleep(5)
			(result, response) = invoke_function_candidate("approveCandidate",Config.NODES[num]["pubkey"],errorcode=0)
			time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = nodeCountCheck(response,14)
		time.sleep(5)
		(result, response) = GetPeerPoolItem() #chakan node13 status 01
		time.sleep(5)
		for n in range(0,7):
			(result, response) = invoke_function_vote("voteForPeer",Config.NODES[n]["address"],voteList=[Config.NODES[12]["pubkey"]],voteCount,errorcode = 0,node_index =12) 
			time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = GetPeerPoolItem() #chakan node13 status 01
		time.sleep(5)
		logger.close(result)
		
	def test_17(self):
		logger.open("test17.log", "test17")
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(5)
		for num in range(7,14):
			(result, response) = invoke_function_register("registerCandidate",Config.NODES[num]["pubkey"],Config.NODES[num]["address"],ontCount_1,ByteToHex((Config.NODES[num]["ontid"]).encode("utf-8")),user_1,errorcode=0,node_index=num)  
			time.sleep(5)
			(result, response) = invoke_function_candidate("approveCandidate",Config.NODES[num]["pubkey"],errorcode=0)
			time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = nodeCountCheck(response,14)
		time.sleep(5)
		(result, response) = GetPeerPoolItem() #chakan node13 status 01
		time.sleep(5)
		
		time.sleep(20)
		time.sleep(20)
		# (result, response) = invoke_function_commitDpos(0)
		# time.sleep(5)
		# (result, response) = invoke_function_commitDpos(0)
		# time.sleep(5)
		(result, response) = GetPeerPoolItem() #chakan node13 status 01
		time.sleep(5)
		logger.close(result)
		
	def test_18(self):
		logger.open("test18.log", "test18")
		init(candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(5)
		for num in range(7,14):
			(result, response) = invoke_function_register("registerCandidate",Config.NODES[num]["pubkey"],Config.NODES[num]["address"],ontCount_1,ByteToHex((Config.NODES[num]["ontid"]).encode("utf-8")),user_1,errorcode=0,node_index=num)  
			time.sleep(5)
			(result, response) = invoke_function_candidate("approveCandidate",Config.NODES[num]["pubkey"],errorcode=0)
			time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = nodeCountCheck(response,14)
		time.sleep(5)
		(result, response) = GetPeerPoolItem() #chakan node13 status 01
		time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = GetPeerPoolItem() #chakan node13 status 01
		time.sleep(5)
		logger.close(result)
	
		



