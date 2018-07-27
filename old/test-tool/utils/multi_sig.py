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


def multi_contract(task,m,pubkeyArray):
	(result, response) = sign_transction(task)#Task(name="multi", ijson=request))
	signed_tx = response["result"]["signed_tx"]
	
	#print(request1)
	execNum=0
	signed_raw=signed_tx
	for pubkey in pubkeyArray:
		request1 = {
			"REQUEST": {
				"qid":"1",
				"method":"sigmutilrawtx",
				"params":{
					"raw_tx":signed_raw,
					"m":m,
					"pub_keys":pubkeyArray
				}
			},
			"RESPONSE": {}
		}
		for node_index in range(len(Config.NODES)):
			if Config.NODES[node_index]["pubkey"] == pubkey:
				request1["NODE_INDEX"] = node_index	
				(result, response) = sign_multi_transction(Task(name="multi", ijson=request1))
				signed_raw = response["result"]["signed_tx"]
				print("multi sign tx:" + str(execNum)+pubkey)
				execNum=execNum+1
				break
				
		if execNum>=m:
			(result,response)=call_signed_contract(signed_raw, True)
			call_signed_contract(signed_raw, False)
			return (result,response)
			
	return (False,{"error_info":"multi times lesss than except!only "+str(execNum)})
	
	

	
def sign_multi_transction(task, judge = True, process_log = True):
	if task.node_index() != None:
		print("sign transction with other node: " + str(task.node_index()))
		task.set_type("st")
		request = task.request()
		task.set_request({
		  "method": "siginvoketx",
		  "jsonrpc": "2.0",
		  "id": 0,
		})
		task.request()["params"] = request
		(result, response) = run_single_task(task, False, process_log)
		if result:
			response = response["result"]
			return (result, response)
		else:
			task.set_type("cli")
			(result, response) = run_single_task(task, judge, process_log)
			return (result, response)
