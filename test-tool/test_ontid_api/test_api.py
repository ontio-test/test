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
	node_0 = 0
	ontpubkey_0 = Config.NODES[node_0]["pubkey"]
	ontid_map[ontpubkey_0] = node_0
	
	node_1 = 1
	ontpubkey_1	= Config.NODES[node_1]["pubkey"]
	ontid_map[ontpubkey_1] = node_1
	
	node_2 = 2
	ontpubkey_2 = Config.NODES[node_2]["pubkey"]
	ontid_map[ontpubkey_2] = node_2
	
	node_3 = 3
	ontpubkey_3	= Config.NODES[node_3]["pubkey"]
	ontid_map[ontpubkey_3] = node_3
	node_4 = 4
	ontpubkey_4 = Config.NODES[node_4]["pubkey"]
	ontid_map[ontpubkey_4] = node_4
	
	node_5 = 5
	ontpubkey_5 = Config.NODES[node_5]["pubkey"]
	ontid_map[ontpubkey_5] = node_5
	
	node_6 = 6
	ontpubkey_6 = Config.NODES[node_6]["pubkey"]
	ontid_map[ontpubkey_6] = node_6

	
	roleA_hex = ByteToHex(b"roleA")
	roleB_hex = ByteToHex(b"roleB")
	

def multi_contract(task,m,pubkeyArray):
	(result, response) = sign_transction(task)#Task(name="multi", ijson=request))
	signed_tx = response["result"]["signed_tx"]
	request1 = {
		"REQUEST": {
			"qid":"1",
			"method":"sigmutilrawtx",
			"params":{
				"raw_tx":signed_tx,
				"m":m,
				"pub_keys":pubkeyArray
			}
		},
		"RESPONSE": {}
	}
	print(request1)
	request1["NODE_INDEX"]=task.node_index()
	(result, response) = sign_multi_transction(Task(name="multi", ijson=request1))
	print(response)
	signed_tx = response["result"]["signed_tx"]
	print(signed_tx)
	call_signed_contract(signed_tx, True)
	return call_signed_contract(signed_tx, False)
	
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
		
def regIDWithPublicKey(ontId, public_key, node_index = None,errorcode=47001, errorkey = "error"):
	request = {
		
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"method": "regIDWithPublicKey",
				"address": "0300000000000000000000000000000000000000",
				"version": 1,
				"params": [
					ontId,
					public_key
				]
			}
		},
		"RESPONSE":{errorkey : errorcode}
	}
	if errorkey =="error_code":
		request["SIGN_RESPONSE"]={errorkey : errorcode}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[public_key]
		request["NODE_INDEX"] = node_index	  
	
	return call_contract(Task(name="regIDWithPublicKey", ijson=request), twice = True)

def addKey(ontId, new_public_key,public_key, node_index = None,errorcode=47001,public_key_Array=[], errorkey = "error"):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"method": "addKey",
				"address": "0300000000000000000000000000000000000000",
				"version": 1,
				"params": [
					ontId,
					new_public_key,
					public_key
				]
			}
		},
		"RESPONSE":{errorkey : errorcode}
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[public_key]
		request["NODE_INDEX"] = node_index	  
	if len(public_key_Array)==0 or len(public_key_Array)>2:
		return call_contract(Task(name="addKey", ijson=request), twice = True)
	else:
		return multi_contract(Task(name="addKey", ijson=request),public_key_Array[0],public_key_Array[1])	

def removeKey(ontId, remove_public_Key,public_key, node_index = None,errorcode=47001,public_key_Array=[], errorkey = "error"):
	request = {

		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"method": "removeKey",
				"address": "0300000000000000000000000000000000000000",
				"version": 1,
				"params": [
					ontId,
					remove_public_Key,
					public_key
				]
			}
		},
		"RESPONSE":{errorkey : errorcode}
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[public_key]
		request["NODE_INDEX"] = node_index	  
	if len(public_key_Array)==0 or len(public_key_Array)>2:
		return call_contract(Task(name="removeKey", ijson=request), twice = True)
	else:
		return multi_contract(Task(name="removeKey", ijson=request),public_key_Array[0],public_key_Array[1])
	
def addRecovery(ontId, recovery_address,public_key, node_index = None,errorcode=47001, errorkey = "error"):
	request = {

		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"method": "addRecovery",
				"address": "0300000000000000000000000000000000000000",
				"version": 1,
				"params": [
					ontId,
					script_hash_bl_reserver(recovery_address),
					public_key
				]
			}
		},
		"RESPONSE":{errorkey : errorcode}
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}
	
	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[public_key]
		request["NODE_INDEX"] = node_index   
	
	return call_contract(Task(name="addRecovery", ijson=request), twice = True)
def transfer():
	request = {

		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"method": "transfer",
				"address": "0100000000000000000000000000000000000000",
				"version": 1,
				"params": [[[
					"AZKG25z2yjCUTQZtNYb9Pq4dezP4zGRFsP",
					"AS9S7j6VWUgg3sX89pok6KHeYU9DenKwbS",
					"100"
				]]]
			}
		},
		"RESPONSE":{"error" : 0}
	}
	return multi_contract(Task(name="transfer", ijson=request),3,["031b7025752886d5598e3a165a7ba4accc770955e4450ee5e14d38d35c7dfef8a5","03b36e26db8b132b551a0213ade4eeb39510847acd152490ef170604c5e4e4686d","03f8d89ab17423d9e4a57b7e7174bcf239eb42779fd942b0601b778087440d35aa"])	
def changeRecovery(ontId, new_recovery_address,old_recovery_address,public_key, node_index = None,errorcode=47001,old_recovery_address_Array=[], errorkey = "error"):
	request = {

		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"method": "changeRecovery",
				"address": "0300000000000000000000000000000000000000",
				"version": 1,
				"params": [
					ontId,
					script_hash_bl_reserver(new_recovery_address),
					script_hash_bl_reserver(old_recovery_address)
				]
			}
		},
		"RESPONSE":{errorkey : errorcode}
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[public_key]
		request["NODE_INDEX"] = node_index
	if len(old_recovery_address_Array)==0 or len(old_recovery_address_Array)>2:
		return call_contract(Task(name="changeRecovery", ijson=request), twice = True)
	else:
		return multi_contract(Task(name="changeRecovery", ijson=request),old_recovery_address_Array[0],old_recovery_address_Array[1])

def regIDWithAttributes(ontId, attributes_array,public_key, node_index = None,errorcode=47001, errorkey = "error"):
	request = {

		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"method": "regIDWithAttributes",
				"address": "0300000000000000000000000000000000000000",
				"version": 1,
				"params": [
					ontId,
					public_key,
					attributes_array
					
				]
			}
		},
		"RESPONSE":{errorkey : errorcode}
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[public_key]
		request["NODE_INDEX"] = node_index	  
	
	return call_contract(Task(name="regIDWithAttributes", ijson=request), twice = True)
	
def addAttributes(ontId, attributes_array,public_key, node_index = None,errorcode=47001, errorkey = "error"):
	request = {

		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"method": "addAttributes",
				"address": "0300000000000000000000000000000000000000",
				"version": 1,
				"params": [
					ontId,
					attributes_array,
					public_key
				]
			}
		},
		"RESPONSE":{errorkey : errorcode}
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[public_key]
		request["NODE_INDEX"] = node_index	  
	
	return call_contract(Task(name="addAttributes", ijson=request), twice = True)
def removeAttribute(ontId, attributePath,public_key, node_index = None,errorcode=47001, errorkey = "error"):
	request = {

		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"method": "removeAttribute",
				"address": "0300000000000000000000000000000000000000",
				"version": 1,
				"params": [
					ontId,
					attributePath,
					public_key
				]
			}
		},
		"RESPONSE":{errorkey : errorcode}
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[public_key]
		request["NODE_INDEX"] = node_index	  
	
	return call_contract(Task(name="removeAttribute", ijson=request), twice = True)
	
def getPublicKeys(ontId,public_key, node_index = None,errorcode=47001, errorkey = "error"):
	request = {

		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"method": "getPublicKeys",
				"address": "0300000000000000000000000000000000000000",
				"version": 1,
				"params": [
					ontId
				]
			}
		},
		"RESPONSE":{errorkey : errorcode}
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[public_key]
		request["NODE_INDEX"] = node_index	  
	
	return call_contract(Task(name="getPublicKeys", ijson=request), twice = True)
def getKeyState(ontId,keyNum,public_key, node_index = None,errorcode=47001, errorkey = "error"):
	request = {

		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"method": "getKeyState",
				"address": "0300000000000000000000000000000000000000",
				"version": 1,
				"params": [
					ontId,
					keyNum
				]
			}
		},
		"RESPONSE":{errorkey : errorcode}
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[public_key]
		request["NODE_INDEX"] = node_index	  
	
	return call_contract(Task(name="getKeyState", ijson=request), twice = True)
		
def getAttributes(ontId,public_key, node_index = None,errorcode=47001, errorkey = "error"):
	request = {

		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"method": "getAttributes",
				"address": "0300000000000000000000000000000000000000",
				"version": 1,
				"params": [
					ontId
				]
			}
		},
		"RESPONSE":{errorkey : errorcode}
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[public_key]
		request["NODE_INDEX"] = node_index	  
	
	return call_contract(Task(name="getAttributes", ijson=request), twice = True)
		
def getDDO(ontId,public_key, node_index = None,errorcode=47001, errorkey = "error"):
	request = {

		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"method": "getDDO",
				"address": "0300000000000000000000000000000000000000",
				"version": 1,
				"params": [
					ontId
				]
			}
		},
		"RESPONSE":{errorkey : errorcode}
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[public_key]
		request["NODE_INDEX"] = node_index	  
	
	return call_contract(Task(name="getDDO", ijson=request), twice = True)
	
def verifySignature(ontId,keyNum,public_key, node_index = None,errorcode=47001, errorkey = "error"):
	request = {

		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"method": "verifySignature",
				"address": "0300000000000000000000000000000000000000",
				"version": 1,
				"params": [
					ontId,
					keyNum
				]
			}
		},
		"RESPONSE":{errorkey : errorcode}
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[public_key]
		request["NODE_INDEX"] = node_index	  
	
	return call_contract(Task(name="verifySignature", ijson=request), twice = True)
def forNeo(contract_address,functionName,params,public_key, node_index = None, recovery_address_Array=[]):
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
						"value": functionName
					},
					
					{
						"type": "array",
						"value": params
					}
				]
			}
		},
		"RESPONSE":{"error" : 0}
	}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[public_key]
		request["NODE_INDEX"] = node_index
	
	if functionName == "changeRecovery":
		return multi_contract(Task(name="forNeo", ijson=request), recovery_address_Array[0],recovery_address_Array[1])
	else:
		return call_contract(Task(name="forNeo", ijson=request), twice = True)
		
	
