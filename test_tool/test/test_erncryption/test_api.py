# -*- coding:utf-8 -*-
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys
import getopt
import time

sys.path.append('..')
sys.path.append('../..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
#from utils.api.commonapi import *
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.common import Common
from api.apimanager import API

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
                        "type": "array",
                        "value":  [
							{
								"type": "bytearray",
								
								"value": Common.bl_address(pay_address)
							},
							{
								"type": "bytearray",
								"value": Common.bl_address(get_address)
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
    return API.contract().call_contract(Task(name="forNeo", ijson=request), twice = True)
def sample(contract_address,pay_address,get_address,node_index,charge=False,nodePath=""):

	#getont/ong
	(result1, response)=API.rpc().getbalance(get_address)
	transfervalue1ont=int(response["result"]["ont"])
	transfervalue1ong=int(response["result"]["ong"])
	##case
	if(charge):
		os.system("echo 123456 | "+nodePath+ "/ontology asset transfer --from="+pay_address+" --to=1 --amount=10 --gasprice=0 --gaslimit=30000 --asset=ont -w "+nodePath+"/wallet.dat")
		API.node().wait_gen_block(True)
		os.system("echo 123456 | "+nodePath+ "/ontology asset transfer --from="+pay_address+" --to=1 --amount=0.00000001 --gasprice=0 --gaslimit=30000 --asset=ong -w "+nodePath+"/wallet.dat")
	else:
		(result, response) = forNeo(contract_address,pay_address,get_address, node_index)
	#API.node().wait_gen_block()
	API.node().wait_gen_block(True)
	
	
	#getont/ong
	(result2, response1)=API.rpc().getbalance(get_address)
	transfervalue2ont=int(response1["result"]["ont"])
	transfervalue2ong=int(response1["result"]["ong"])
	changevalue=10
	result1=(transfervalue2ont-transfervalue1ont==changevalue)
	result2=(transfervalue2ong-transfervalue1ong==changevalue)
	print(result1)
	print(result2)
		
	return result1&result2
def all_case(contractaddress,pay_address,get_address,node_index,nodePath1):
	
	result1=sample(contractaddress,pay_address,get_address,node_index,nodePath=nodePath1)
	
	result2=sample(contractaddress,get_address,pay_address,node_index,True,nodePath=nodePath1)
	
	return result1&result2