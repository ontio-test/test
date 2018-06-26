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
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.contractapi import *
from test_api import *
from utils.commonapi import call_contract

logger = LoggerInstance
NODES = Config.SERVICES
####################################################
#test cases
#regIDWithPublicKey(0)
#regIDWithPublicKey(1)
#regIDWithPublicKey(2)
#regIDWithPublicKey(3)
#regIDWithPublicKey(4)
#regIDWithPublicKey(5)
#regIDWithPublicKey(6)

contract_address = deploy_contract("governance.neo")

class TestContract(ParametrizedTestCase):
	def test_186_governace(self):
		bind_role_function("0700000000000000000000000000000000000000", Common.ontID_Admin, Common.roleA_hex, ["registerCandidate"])
		bind_user_role("0700000000000000000000000000000000000000", Common.ontID_Admin, Common.roleA_hex, [Common.ontID_A])
		
		logger.open("186_governance.log", "186_governance")
		functionName="RegisterCandidate"
		params=[{
					"type" : "bytearray",
					"value" : NODES[Common.node_A]["pubkey"]
				},{
					"type" : "bytearray",
					"value" : script_hash_bl_reserver(base58_to_address(NODES[Common.node_A]["address"]))
				},{
					"type" : "int",
					"value" : "1000"
				},{
					"type" : "bytearray",
					"value" : ByteToHex(bytes(NODES[Common.node_A]["ontid"], encoding = "utf8"))
				},{
					"type" : "int",
					"value" : "1"
				}]
				
		(result, response) = forNeo(contract_address,functionName,params,"", Common.node_A)
		logger.close(result)
		
	def test_192_governace(self):
		logger.open("192_governace.log", "192_governace")
		functionName="VoteForPeer"
		params=[{
					"type" : "bytearray",
					"value" : NODES[Common.node_A]["pubkey"]
				},{
					"type" : "bytearray",
					"value" : script_hash_bl_reserver(base58_to_address(NODES[Common.node_A]["address"]))
				},{
					"type" : "int",
					"value" : "1000"
				}]
				
		(result, response) = forNeo(contract_address,functionName,params,"", Common.node_A)
		logger.close(result)
####################################################
if __name__ == '__main__':
	unittest.main()

