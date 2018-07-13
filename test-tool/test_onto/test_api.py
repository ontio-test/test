# -*- coding:utf-8 -*-
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys
import getopt

sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.commonapi import *
from utils.parametrizedtestcase import ParametrizedTestCase
from test_conf import testConfig
from utils.multi_sig import *

class Common:
	AdminNum=5
	AdminPublicKeyList=[Config.NODES[0]["pubkey"],Config.NODES[1]["pubkey"],Config.NODES[2]["pubkey"],Config.NODES[3]["pubkey"],Config.NODES[4]["pubkey"],Config.NODES[5]["pubkey"],Config.NODES[6]["pubkey"]]
	ontid_map = {}

	node_Admin = 0
	ontID_Admin = ByteToHex(bytes(Config.NODES[node_Admin]["ontid"], encoding = "utf8"))
	ontid_map[ontID_Admin] = node_Admin
	
	node_A = 1
	ontID_A = ByteToHex(bytes(Config.NODES[node_A]["ontid"], encoding = "utf8"))
	ontid_map[ontID_A] = node_A
	
	node_B = 2
	ontID_B = ByteToHex(bytes(Config.NODES[node_B]["ontid"], encoding = "utf8"))
	ontid_map[ontID_B] = node_B
	
	node_C = 3
	ontID_C = ByteToHex(bytes(Config.NODES[node_C]["ontid"], encoding = "utf8"))
	ontid_map[ontID_C] = node_C
	
	node_D = 4
	ontID_D = ByteToHex(bytes(Config.NODES[node_D]["ontid"], encoding = "utf8"))
	ontid_map[ontID_D] = node_D
	
	node_E = 5
	ontID_E = ByteToHex(bytes(Config.NODES[node_E]["ontid"], encoding = "utf8"))
	ontid_map[ontID_E] = node_E
	
	node_F = 6
	ontID_F = ByteToHex(bytes(Config.NODES[node_F]["ontid"], encoding = "utf8"))
	ontid_map[ontID_F] = node_F
	
	roleA_hex = ByteToHex(b"roleA")
	roleB_hex = ByteToHex(b"roleB")

def init_admin(contract_address, admin_address, node_index = None):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": contract_address,
                "version": 1,
                "params": [
                    {
                        "type": "string",
                        "value": "initContractAdmin"
                    },
                    {
                        "type": "array",
                        "value": [
                            {
                                "type" : "string",
                                "value" : ""
                            }
                        ]
                    },
                    {
                        "type": "array",
                        "value": [
                            {
                                "type" : "string",
                                "value" : ""
                            }
                        ]
                    }
                ]
            }
        },
        "RESPONSE":{"error" : 0}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index
    else:
        node_index = Config.ontid_map[admin_address]
        request["NODE_INDEX"] = node_index      
    
    return call_contract(Task(name="init_admin", ijson=request), twice = True)