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
		logger.open("TestGover14.log", "TestGover14")
		try:
			if (not pause("ensure that node A and node B is in the nodes network and node A has more than 10000 ont.")):
				raise Error("pre-condition unsatisfied")

			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()			
			'''
			# to ensure that the following operations are in the same round
			while(True):
				if getblockcount() % blocks_per_round <= 2:
					time.sleep(1)
					continue
				else:
					break
			'''

			# step 1 wallet A vote for node B
			(result, response) = vote_for_peer(wallet_A_address, ["03e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dc"], ["190000"])
			print (response)
			#if not result:
			#	raise Error("vote_for_peer error")

			# step 1 wallet A vote for node B
			(result, response) = vote_for_peer(wallet_A_address, ["03e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dc"], ["10000"])
			print (response)
			#if not result:
			#	raise Error("vote_for_peer error")
			
			
		
		except Exception as e:
			print(e.msg)
		logger.close(result)
####################################################
if __name__ == '__main__':
	unittest.main()	    