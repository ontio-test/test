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
nodeOther=6
pubKey_pre = Config.NODES[7]["pubkey"] #准备用
walletAddress_pre= Config.NODES[7]["address"]
ontCount_1="10000"
ontID_1=ByteToHex((Config.NODES[7]["ontid"]).encode("utf-8"))
user_1 = "1" #正常的公钥序号
voteCount_Pre=["100","100"]#投票预备
walletNode_1=7

walletAddress_1 = Config.NODES[nodeNow]["address"] #自己的钱包地址
walletAddress_2 = "AYcJKK6Bxhq7H6J9fmdAVmiESi6XjRZHAE" #其他人的钱包地址
walletAddress_3 = "abcd1234" #乱码
walletAddress_4 = "" #留空


voteList_1 = [Config.NODES[0]["pubkey"],Config.NODES[1]["pubkey"]] #取消过投票的节点公钥数组
voteList_2 = [Config.NODES[2]["pubkey"],Config.NODES[3]["pubkey"]] #未取消过投票的节点公钥数组
voteList_3 = [Config.NODES[4]["pubkey"],Config.NODES[5]["pubkey"]]#未投过票的节点公钥数组
voteList_4 = ["abcd1234"] #乱码
voteList_5 = [""]#留空
voteCount_1 = ["99","100"]#与公钥数组一一对应的不同票数的数组，票数值低于之前取消的票数
voteCount_2 = ["100","101"] #与公钥数组一一对应的不同票数的数组，票数值高于之前取消的票数
voteCount_3 = ["100"] #比公钥数组数量少的票数数组
voteCount_4 = ["abcd1234"] #乱码
voteCount_5 = [""]#留空
####################################################

# test cases
class Testwithdraw(ParametrizedTestCase):

	def setUp(self):
		init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(10)
		pass
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_Pre,0,walletNode_1)
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_2,voteCount_Pre,0,walletNode_1)
		time.sleep(5)
		(result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_1,voteCount_Pre,0,node_index=walletNode_1)
		time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
	def test_79_withdraw(self):
		logger.open("79_withdraw.log", "79_withdraw")
		# getStorageVoteInfo(Config.NODES[0]["pubkey"],Config.NODES[7]["address"])
		# getStorageVoteInfo(Config.NODES[1]["pubkey"],Config.NODES[7]["address"])
		# (result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_Pre,0,walletNode_1)
		# #(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_2,voteCount_Pre,0,walletNode_1)
		# time.sleep(5)
		# getStorageVoteInfo(Config.NODES[0]["pubkey"],Config.NODES[7]["address"])
		# getStorageVoteInfo(Config.NODES[1]["pubkey"],Config.NODES[7]["address"])
		# (result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_1,voteCount_Pre,0,node_index=walletNode_1)
		# time.sleep(5)
		# (result, response) = invoke_function_commitDpos(0)
		# time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		getStorageVoteInfo(Config.NODES[0]["pubkey"],Config.NODES[7]["address"])
		getStorageVoteInfo(Config.NODES[1]["pubkey"],Config.NODES[7]["address"])
		(result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_1,voteCount_1,0,node_index=walletNode_1)
		logger.close(result)

	def test_80_withdraw(self):
		logger.open("80_withdraw.log", "80_withdraw")
		(result, response) = invoke_function_vote("withdraw",walletAddress_2,voteList_1,voteCount_1,node_index=walletNode_1)
	

		logger.close(result)
	
	def test_81_withdraw(self):
		logger.open("81_withdraw.log", "81_withdraw")
		(result, response) = invoke_function_vote("withdraw",walletAddress_3,voteList_1,voteCount_1,node_index=walletNode_1)
	

		logger.close(result)
	def test_82_withdraw(self):
		logger.open("82_withdraw.log", "82_withdraw")
		(result, response) = invoke_function_vote("withdraw",walletAddress_4,voteList_1,voteCount_1,0,node_index=walletNode_1)
	

		logger.close(result)
	
	def test_83_withdraw(self):
		logger.open("83_withdraw.log", "83_withdraw")
		(result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_1,voteCount_1,node_index=walletNode_1)
	

		logger.close(result)
	
	def test_84_withdraw(self):
		logger.open("84_withdraw.log", "84_withdraw")
		(result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_2,voteCount_1,node_index=walletNode_1)
	

		logger.close(result)

	def test_85_withdraw(self):
		logger.open("85_withdraw.log", "85_withdraw")
		(result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_3,voteCount_1,node_index=walletNode_1)
	

		logger.close(result)

	def test_86_withdraw(self):
		logger.open("86_withdraw.log", "86_withdraw")
		(result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_4,voteCount_1,node_index=walletNode_1)
	

		logger.close(result)

	def test_87_withdraw(self):
		logger.open("87_withdraw.log", "87_withdraw")
		(result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_5,voteCount_1,node_index=walletNode_1)
	

		logger.close(result)
	
	def test_88_withdraw(self):
		logger.open("88_withdraw.log", "88_withdraw")
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		(result, response) = invoke_function_commitDpos(0)
		time.sleep(5)
		getStorageVoteInfo(Config.NODES[0]["pubkey"],Config.NODES[7]["address"])
		getStorageVoteInfo(Config.NODES[1]["pubkey"],Config.NODES[7]["address"])
		(result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_1,voteCount_1,0,node_index=walletNode_1)
	

		logger.close(result)
	
	def test_89_withdraw(self):
		logger.open("89_withdraw.log", "89_withdraw")
		(result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_1,voteCount_2,node_index=walletNode_1)
	

		logger.close(result)
	
	def test_90_withdraw(self):
		logger.open("90_withdraw.log", "90_withdraw")
		(result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_1,voteCount_3,node_index=walletNode_1)
	

		logger.close(result)
	
	def test_91_withdraw(self):
		logger.open("91_withdraw.log", "91_withdraw")
		(result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_1,voteCount_4,node_index=walletNode_1)
	

		logger.close(result)
	
	def test_92_withdraw(self):
		logger.open("92_withdraw.log", "92_withdraw")
		(result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_1,voteCount_5,node_index=walletNode_1)
	

		logger.close(result)
	
	def test_93_withdraw(self):
		logger.open("93_withdraw.log", "93_withdraw")
		(result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_5,voteCount_5,node_index=walletNode_1)
	

		logger.close(result)
	
####################################################
if __name__ == '__main__':
	unittest.main()