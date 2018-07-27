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
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.commonapi import *
from utils.parametrizedtestcase import ParametrizedTestCase
from test_api import *

####################################################
#test cases
class TestConsensus(ParametrizedTestCase):

	def test_main(self):
		result = False
		logger.open("TestGover3.log", "TestGover3")
		try:
			if (not pause("ensure that node A is not in the nodes network and node B is in the nodes network and node A has more than 10000 ont.")):
				raise Error("pre-condition unsatisfied")

			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
			consensus_rounds = (int) (getblockcount() / blocks_per_round)
			print ("************", consensus_rounds)

			# step 1 wallet A vote for node B
			(result, response) = vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price])
			print (response)
			#if not result:
			#	raise Error("vote error")

			# step 2 wallet A unvote in the second round
			while(True):
				if (getblockcount() / blocks_per_round - consensus_rounds == 1):
					(result, response) = unvote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price])
					break
				else:
					print (getblockcount())
					time.sleep(5)
					print("waiting...")
					continue	
			#if not result:
			#	raise Error("unvote error")


			# step 3 wallet A withdraw ont in the third round
			while(True):
				if (getblockcount() / blocks_per_round - consensus_rounds == 2):
					(result, response) = withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price])
					break
				else:
					print (getblockcount())
					time.sleep(5)
					continue	
			#if not result:
			#	raise Error("withdraw_ont error")

			# this should be failed
			(result, response) = withdraw_ont(wallet_A_address, [node_B_puiblic_key], ["1"])
			#if not result:
			#	raise Error("withdraw_ont error")

		
		except Exception as e:
			print(e.msg)
		logger.close(result)
####################################################
if __name__ == '__main__':
	unittest.main()	    