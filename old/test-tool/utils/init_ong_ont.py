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
from utils.multi_sig import *


def transferFromTest(put_address, amount, node_index = None,errorcode=0,public_key_Array=[], errorkey = "error"):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params":{
			
				"gas_price":0,
				"gas_limit":1000000000,
				"address":"0200000000000000000000000000000000000000",
				"method":"transferFrom",
				"version":0,
				"params":[
						put_address,
						"0100000000000000000000000000000000000000",
						put_address,
						amount
				]
			}
		},
		"RESPONSE":{errorkey : errorcode}
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}

	request["NODE_INDEX"] = node_index	  
	return multi_contract(Task(name="transferFromTest", ijson=request),public_key_Array[0],public_key_Array[1])
	
def transferTest(assetStr,put_address, get_address,amount, node_index = None,errorcode=0,public_key_Array=[], errorkey = "error"):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "sigtransfertx",
			"Params": {
				"gas_price":0,
				"gas_limit":1000000000,
				"asset":assetStr,
				"from":put_address,
				"to":get_address,
				"amount":amount
			}
		},
		"RESPONSE":{errorkey : errorcode}
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}

	request["NODE_INDEX"] = node_index	  
	return multi_contract(Task(name="transferTest", ijson=request),public_key_Array[0],public_key_Array[1])

################
	#restart_givemoney
#################

def init_ont_ong():
	for i in range(7):
		(result, response)=transferTest("ont",Config.MULTI_SIGNED_ADDRESS,Config.NODES[i]["address"],100000000,public_key_Array=[5,[Config.NODES[0]["pubkey"],Config.NODES[1]["pubkey"],Config.NODES[2]["pubkey"],Config.NODES[3]["pubkey"],Config.NODES[4]["pubkey"],Config.NODES[5]["pubkey"],Config.NODES[6]["pubkey"]]])
		if not result:
			return (result, response)
	time.sleep(5)
	(result, response) = transferFromTest(Config.MULTI_SIGNED_ADDRESS,Config.INIT_AMOUNT_ONG,5,public_key_Array=[5,[Config.NODES[0]["pubkey"],Config.NODES[1]["pubkey"],Config.NODES[2]["pubkey"],Config.NODES[3]["pubkey"],Config.NODES[4]["pubkey"],Config.NODES[5]["pubkey"],Config.NODES[6]["pubkey"]]])		
	if not result:
		return (result, response)
	time.sleep(5)
	for i in range(7):
		(result, response)=transferTest("ong",Config.MULTI_SIGNED_ADDRESS,Config.NODES[i]["address"],1000000000000000,public_key_Array=[5,[Config.NODES[0]["pubkey"],Config.NODES[1]["pubkey"],Config.NODES[2]["pubkey"],Config.NODES[3]["pubkey"],Config.NODES[4]["pubkey"],Config.NODES[5]["pubkey"],Config.NODES[6]["pubkey"]]])
		if not result:
			return (result, response)
#init_ont_ong()