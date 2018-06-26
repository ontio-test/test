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

class Common:
    ontid_map = {}

    node_Admin = 2
    ontID_Admin = Config.SERVICES[node_Admin]["pubkey"]
    ontid_map[ontID_Admin] = node_Admin
    
    node_A = 3
    ontID_A = Config.SERVICES[node_A]["pubkey"]
    ontid_map[ontID_A] = node_A
    
    node_B = 4
    ontID_B = Config.SERVICES[node_B]["pubkey"]
    ontid_map[ontID_B] = node_B
    
    node_C = 5
    ontID_C = Config.SERVICES[node_C]["pubkey"]
    ontid_map[ontID_C] = node_C
    
    node_D = 6
    ontID_D = Config.SERVICES[node_D]["pubkey"]
    ontid_map[ontID_D] = node_D
    
    roleA_hex = ByteToHex(b"roleA")
    roleB_hex = ByteToHex(b"roleB")
def forNeo(contract_address,pay_address,get_address, node_index = None):
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
                        "value": "transfer"
                    },
                    
					{
                        "type": "array",
                        "value":  [
							{
								"type": "bytearray",
								
								"value": script_hash_bl_reserver(base58_to_address(pay_address))
							},
							{
								"type": "bytearray",
								"value": script_hash_bl_reserver(base58_to_address(get_address))
							},
							{
								"type": "int",
								"value": "10"
							}
						]
                    }
                ]
            }
        },
        "RESPONSE":{"error" : 0},
		"NODE_INDEX":node_index
    }
    return call_contract(Task(name="forNeo", ijson=request), twice = True)