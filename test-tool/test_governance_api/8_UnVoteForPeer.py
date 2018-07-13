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
from utils.parametrizedtestcase import ParametrizedTestCase
from test_api import *
from test_common import *
#from test_conf import Conf

logger = LoggerInstance



##########################################################
# params
nodeNow=7
nodeOthers=6
pubKey_pre = Config.NODES[7]["pubkey"] #准备用
walletAddress_pre= Config.NODES[7]["address"]
ontCount_1="10000"
ontID_1=ByteToHex((Config.NODES[7]["ontid"]).encode("utf-8"))
user_1 = "1" #正常的公钥序号


walletAddress_1 = Config.NODES[nodeNow]["address"] #自己的钱包地址
walletNode_1=nodeNow
walletAddress_2 = "AYcJKK6Bxhq7H6J9fmdAVmiESi6XjRZHAE" #其他人的钱包地址
walletNode_2=nodeOthers
walletAddress_3 = "abcd1234" #乱码
walletAddress_4 = "" #留空

voteList_1 =[Config.NODES[0]["pubkey"],Config.NODES[1]["pubkey"]] #投过票的节点公钥数组
voteList_2 =[Config.NODES[2]["pubkey"],Config.NODES[3]["pubkey"]] #未投过票的节点公钥数组
voteList_3 = [Config.NODES[0]["pubkey"],Config.NODES[2]["pubkey"]] #投过票+未投过票的节点公钥数组
voteList_4 =["abcd1234"] #乱码
voteList_5 = [""]#留空
voteCount_1 = ["100","100"]#与公钥数组一一对应的不同票数的数组，数组总值低于之前给他们投的ont数量
voteCount_2 = ["10000","100"] #与公钥数组一一对应的不同票数的数组，票数值高于之前给他们投的票数
voteCount_3 = ["100"]#比公钥数组数量少的票数数组
voteCount_4 = ["qwer","100"] #乱码
voteCount_5 =  ["",""] #留空
####################################################

# test cases
class TestunVoteForPeer(ParametrizedTestCase):
	def setUp(self):
		#restart all node
		init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(15)
		#pass
		# register ONTID
	def test(self):
		pass
	def test_64_unVoteForPeer(self):
		logger.open("64_unVoteForPeer.log", "64_unVoteForPeer")
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_1,0,walletNode_1)#准备工作，先投票
		
		if result:#实际开始
			time.sleep(10)
			(result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_1,voteCount_1,0,node_index=walletNode_1)
			time.sleep(2)
			nodeCountCheck(response,7)
		logger.close(result)

	def test_65_unVoteForPeer(self):
		logger.open("65_unVoteForPeer.log", "65_unVoteForPeer")
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_1,0,walletNode_1)#准备工作，先投票

		if result:#实际开始
			time.sleep(10)
			(result, response) = invoke_function_vote("unVoteForPeer",walletAddress_2,voteList_1,voteCount_1,node_index=walletNode_1)
			time.sleep(2)
			nodeCountCheck(response,7)

		logger.close(result)
	
	def test_66_unVoteForPeer(self):
		logger.open("66_unVoteForPeer.log", "66_unVoteForPeer")
		(result, response) = invoke_function_vote("unVoteForPeer",walletAddress_3,voteList_1,voteCount_1,node_index=walletNode_1)


		logger.close(result)
	def test_67_unVoteForPeer(self):
		logger.open("67_unVoteForPeer.log", "67_unVoteForPeer")
		(result, response) = invoke_function_vote("unVoteForPeer",walletAddress_4,voteList_1,voteCount_1,node_index=walletNode_1)


		logger.close(result)
	
	def test_68_unVoteForPeer(self):
		logger.open("68_unVoteForPeer.log", "68_unVoteForPeer")
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_1,0,walletNode_1)#准备工作，先投票
		if result:#实际开始
			time.sleep(10)
			(result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_1,voteCount_1,0,node_index=walletNode_1)
			time.sleep(2)
			nodeCountCheck(response,7)
		logger.close(result)
	
	def test_69_unVoteForPeer(self):
		logger.open("69_unVoteForPeer.log", "69_unVoteForPeer")
		(result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_2,voteCount_1,node_index=walletNode_1)


		logger.close(result)

	def test_70_unVoteForPeer(self):
		logger.open("70_unVoteForPeer.log", "70_unVoteForPeer")
		(result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_3,voteCount_1,node_index=walletNode_1)


		logger.close(result)

	def test_71_unVoteForPeer(self):
		logger.open("71_unVoteForPeer.log", "71_unVoteForPeer")
		(result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_4,voteCount_3,node_index=walletNode_1)


		logger.close(result)

	def test_72_unVoteForPeer(self):
		logger.open("72_unVoteForPeer.log", "72_unVoteForPeer")
		(result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_5,voteCount_3,node_index=walletNode_1)


		logger.close(result)
	
	def test_73_unVoteForPeer(self):
		logger.open("73_unVoteForPeer.log", "73_unVoteForPeer")
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_1,0,walletNode_1)#准备工作，先投票
		if result:#实际开始
			time.sleep(10)
			(result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_1,voteCount_1,0,node_index=walletNode_1)
			time.sleep(2)
			nodeCountCheck(response,7)

		logger.close(result)
	
	def test_74_unVoteForPeer(self):
		logger.open("74_unVoteForPeer.log", "74_unVoteForPeer")
		(result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_1,voteCount_2,node_index=walletNode_1)


		logger.close(result)
	
	def test_75_unVoteForPeer(self):
		logger.open("75_unVoteForPeer.log", "75_unVoteForPeer")
		(result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_1,voteCount_3,node_index=walletNode_1)


		logger.close(result)
	
	def test_76_unVoteForPeer(self):
		logger.open("76_unVoteForPeer.log", "76_unVoteForPeer")
		(result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_1,voteCount_4,node_index=walletNode_1)


		logger.close(result)
	
	def test_77_unVoteForPeer(self):
		logger.open("77_unVoteForPeer.log", "77_unVoteForPeer")
		(result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_1,voteCount_5,node_index=walletNode_1)


		logger.close(result)
	
	def test_78_unVoteForPeer(self):
		logger.open("78_unVoteForPeer.log", "78_unVoteForPeer")
		(result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_5,voteCount_5,node_index=walletNode_1)


		logger.close(result)
	
####################################################
if __name__ == '__main__':
	unittest.main()