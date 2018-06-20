# -*- coding:utf-8 -*-
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

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
			if (not pause("ensure that node A  and node B is in the nodes network and node A has more than 10000 ont.")):
				raise Error("pre-condition unsatisfied")

			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()

			# step 1 before vote get balance of wallet A B
			balance_of_wallet_A_1 = getbalance_ont(wallet_A_address)
			balance_of_wallet_B_1 = getbalance_ont(wallet_B_address)
			print("A:", balance_of_wallet_A_1)
			print("B:", balance_of_wallet_B_1)

			# step 2 wallet A vote for node B
			(result, response) = vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price])
			print (response)
			#if not result:
			#	raise Error("vote error")

			# step 3 after vote get balance of wallet A
			balance_of_wallet_A_2 = getbalance_ont(wallet_A_address)
			balance_of_wallet_B_2 = getbalance_ont(wallet_B_address)
			print("2A:", balance_of_wallet_A_2)
			print("2B:", balance_of_wallet_B_2)

			# step 4 compare
			if balance_of_wallet_B_1 != balance_of_wallet_B_2:
				raise Error("balance of wallte B changed.")
			
			if balance_of_wallet_A_1 - balance_of_wallet_A_2 != int(vote_price):
				raise Error("the decrease of balance of wallte A is not %s." % vote_price)

		
		except Exception as e:
			print(e.msg)
		logger.close(result)
####################################################
if __name__ == '__main__':
	unittest.main()	    