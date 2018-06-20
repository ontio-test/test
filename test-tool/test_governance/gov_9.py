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
		logger.open("TestConsensus1.log", "TestConsensus1")
		try:
			if (not pause("ensure that node A and node B is in the nodes network and node A has more than 10000 ont.")):
				raise Error("pre-condition unsatisfied")

			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()

			# to ensure that the following operations are in the same round
			while(True):
				if getblockcount() % blocks_per_round <= 2:
					time.sleep(1)
					continue
				else:
					break

			consensus_rounds = getblockcount() / blocks_per_round

			# step 1 wallet A vote for node B
			(result, response) = vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price])
			print (response)
			#if not result:
			#	raise Error("vote_for_peer error")

			# step 2 node b quit
			(result, response) = quit_node([node_B_puiblic_key], wallet_B_address)
			#if not result:
			#	raise Error("quit_node error")

			# step 2 wait until the second round
			while(True):
				if (getblockcount() / blocks_per_round - consensus_rounds == 1):
					# should failed
					(result, response) = withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price])
					break
				else:
					time.sleep(1)
					continue	
			#if not result:
			#	raise Error("withdraw_ont error")
			
			# step 3 wallet A withdraw ont in the third round
			while(True):
				if (getblockcount() / blocks_per_round - consensus_rounds == 2):
					(result, response) = withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price])
					break
				else:
					time.sleep(1)
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