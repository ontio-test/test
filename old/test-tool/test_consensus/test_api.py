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
from utils.rpcapi import *

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

def getStorageConf(confName):
	rpcapiTest=RPCApi()
	return rpcapiTest.getstorage("0700000000000000000000000000000000000000",ByteToHex(confName.encode("utf-8")))

def invoke_function_consensus(pubKey):
    request = {
        "NODE_INDEX":0,
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "commitDpos",
                "version": 0,
                "params": [
		                  ]
                    }
                },
        "RESPONSE":{"error" : 0}
    }

    return multi_contract(Task(name="invoke_function_commitDpos", ijson=request),Common.AdminNum,Common.AdminPublicKeyList)


def invoke_function_approve(pubKey):
    request = {
        "NODE_INDEX":0,
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "approveCandidate",
                "version": 0,
                "params": [
                            pubKey
		                  ]
                    }
                },
        "RESPONSE":{"error" : 0}
    }
        
    return multi_contract(Task(name="invoke_function_candidate", ijson=request),Common.AdminNum,Common.AdminPublicKeyList)


def native_transfer_ont(pay_address, get_address, amount, node_index=None, errorcode=0, gas_price=0):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0100000000000000000000000000000000000000",
                "method": "transfer",
                "version": 1,
                "params": [
                    [
                        [
                            pay_address,
                            get_address,
                            amount
                        ]
                    ]
                ]
            }
        },
        "RESPONSE": {"error": errorcode},
        "NODE_INDEX": node_index
    }
    return call_contract(Task(name="transfer", ijson=request), twice=True)

def native_transfer_ong(pay_address, get_address, amount, node_index=None, errorcode=0, gas_price=0):
    amount = str(int(amount)*1000000000)
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0200000000000000000000000000000000000000",
                "method": "transfer",
                "version": 1,
                "params": [
                    [
                        [
                            pay_address,
                            get_address,
                            amount
                        ]
                    ]
                ]
            }
        },
        "RESPONSE": {"error": errorcode},
        "NODE_INDEX": node_index
    }
    return call_contract(Task(name="transfer", ijson=request), twice=True)

def transfer(contract_address,from_address,to_address,amount, node_index = None):
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
						"type" : "string",
						"value" : ""
					},
					{
						"type": "array",
						"value":  [
							{
								"type": "bytearray",
								
								"value": script_hash_bl_reserver(base58_to_address(from_address))
							},
							{
								"type": "bytearray",
								"value": script_hash_bl_reserver(base58_to_address(to_address))
							},
							{
								"type": "int",
								"value": amount
							}
						]
					}
				]
			}
		},
		"RESPONSE":{"error" : 0},
		"NODE_INDEX":node_index
	}
	return call_contract(Task(name="transfer", ijson=request), twice = True)


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


def transfer_19(neo_contract_address, from_address, to_address, amount):
    
    request = {
            "REQUEST":  {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": neo_contract_address,
                "version": 1,
                "params": [
                    {
                        "type": "string",
                        "value": "transfer"
                    },
                    {
                        "type": "array",
                        "value": [
                            {
                                "type": "bytearray",
                                "value": from_address
                            },
                            {
                                "type": "bytearray",
                                "value": to_address
                            },
                            {
                                "type": "int",
                                "value": amount
                            }
                        ]
                    }
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request), twice = True) 


def transfer_20(neo_contract_address, from_address, to_address, amount, public_key):
    
    request = {
            "REQUEST":  {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": neo_contract_address,
                "version": 1,
                "params": [
                    {
                        "type": "string",
                        "value": "transfer"
                    },
                    {
                        "type": "array",
                        "value": [
                            {
                                "type": "bytearray",
                                "value": from_address
                            },
                            {
                                "type": "bytearray",
                                "value": to_address
                            },
                            {
                                "type": "int",
                                "value": amount
                            }
                        ]
                    }
                ]
            }
        },
        "RESPONSE": {}
    }

    (result, response) = sign_transction(Task(name="test_1", ijson=request))

    signed_tx = response["result"]["signed_tx"]

    request = {
            "REQUEST":  {
            "qid":"1",
            "method":"sigmutilrawtx",
            "params":{
                "raw_tx":signed_tx,
                "m":1,
                "pub_keys":[
                    public_key
                ]
            }
            },
            "RESPONSE": {}
    }

    sign_multi_transction(Task(name="test_1", ijson=request)) 
    signed_tx = response["result"]["signed_tx"]
    (result, response) = call_signed_contract(signed_tx, True)
    (result, response) = call_signed_contract(signed_tx, False)
    return (result, response)

def transfer_21(neo_contract_address, from_address, to_address, amount, public_key):
    
    request = {
            "NODE_INDEX" :1,
            "REQUEST":  {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": neo_contract_address,
                "version": 1,
                "params": [
                    {
                        "type": "string",
                        "value": "transfer"
                    },
                    {
                        "type": "array",
                        "value": [
                            {
                                "type": "bytearray",
                                "value": from_address
                            },
                            {
                                "type": "bytearray",
                                "value": to_address
                            },
                            {
                                "type": "int",
                                "value": amount
                            }
                        ]
                    }
                ]
            }
        },
        "RESPONSE": {}
    }

    (result, response) = sign_transction(Task(name="test_1", ijson=request))

    signed_tx = response["result"]["signed_tx"]

    request = {
            "REQUEST":  {
            "qid":"1",
            "method":"sigmutilrawtx",
            "params":{
                "raw_tx":signed_tx,
                "m":1,
                "pub_keys":[
                    public_key
                ]
            }
            },
            "RESPONSE": {}
    }

    sign_multi_transction(Task(name="test_1", ijson=request)) 
    signed_tx = response["result"]["signed_tx"]
    (result, response) = call_signed_contract(signed_tx, True)
    (result, response) = call_signed_contract(signed_tx, False)
    return (result, response)

def transfer_22(neo_contract_address, from_address, to_address, amount, public_key):
    
    request = {
            "NODE_INDEX" :1,
            "REQUEST":  {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": neo_contract_address,
                "version": 1,
                "params": [
                    {
                        "type": "string",
                        "value": "transfer"
                    },
                    {
                        "type": "array",
                        "value": [
                            {
                                "type": "bytearray",
                                "value": from_address
                            },
                            {
                                "type": "bytearray",
                                "value": to_address
                            },
                            {
                                "type": "int",
                                "value": amount
                            }
                        ]
                    }
                ]
            }
        },
        "RESPONSE": {}
    }

    (result, response) = sign_transction(Task(name="test_1", ijson=request))

    signed_tx = response["result"]["signed_tx"]

    request = {
            "REQUEST":  {
            "qid":"1",
            "method":"sigmutilrawtx",
            "params":{
                "raw_tx":signed_tx,
                "m":1,
                "pub_keys":[
                    public_key
                ]
            }
            },
            "RESPONSE": {}
    }

    sign_multi_transction(Task(name="test_1", ijson=request)) 
    signed_tx = response["result"]["signed_tx"]
    (result, response) = call_signed_contract(signed_tx, True)
    (result, response) = call_signed_contract(signed_tx, False)
    return (result, response)

def transfer_23(neo_contract_address, from_address, to_address, amount, public_key):
    
    request = {
            "REQUEST":  {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": neo_contract_address,
                "version": 1,
                "params": [
                    {
                        "type": "string",
                        "value": "transfer"
                    },
                    {
                        "type": "array",
                        "value": [
                            {
                                "type": "bytearray",
                                "value": from_address
                            },
                            {
                                "type": "bytearray",
                                "value": to_address
                            },
                            {
                                "type": "int",
                                "value": amount
                            }
                        ]
                    }
                ]
            }
        },
        "RESPONSE": {}
    }

    (result, response) = sign_transction(Task(name="test_1", ijson=request))

    signed_tx = response["result"]["signed_tx"]

    request = {
            "REQUEST":  {
            "qid":"1",
            "method":"sigmutilrawtx",
            "params":{
                "raw_tx":signed_tx,
                "m":1,
                "pub_keys":[
                    public_key
                ]
            }
            },
            "RESPONSE": {}
    }

    sign_multi_transction(Task(name="test_1", ijson=request)) 
    signed_tx = response["result"]["signed_tx"]
    (result, response) = call_signed_contract(signed_tx, True)
    (result, response) = call_signed_contract(signed_tx, False)
    return (result, response)

def transfer_24(neo_contract_address, from_address, to_address, amount, public_key_1, public_key_2, public_key_3, public_key_4):
    
    request = {
            "REQUEST":  {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": neo_contract_address,
                "version": 1,
                "params": [
                    {
                        "type": "string",
                        "value": "transfer"
                    },
                    {
                        "type": "array",
                        "value": [
                            {
                                "type": "bytearray",
                                "value": from_address
                            },
                            {
                                "type": "bytearray",
                                "value": to_address
                            },
                            {
                                "type": "int",
                                "value": amount
                            }
                        ]
                    }
                ]
            }
        },
        "RESPONSE": {}
    }

    (result, response) = sign_transction(Task(name="test_1", ijson=request))

    signed_tx = response["result"]["signed_tx"]

    request = {
            "NODE_INDEX" :1,
            "REQUEST":  {
            "qid":"1",
            "method":"sigmutilrawtx",
            "params":{
                "raw_tx":signed_tx,
                "m":4,
                "pub_keys":[
                    public_key_1,
                    public_key_2,
                    public_key_3,
                    public_key_4
                ]
            }
            },
            "RESPONSE": {}
    }
    sign_multi_transction(Task(name="test_1", ijson=request)) 
    signed_tx = response["result"]["signed_tx"]

    request = {
            "NODE_INDEX" :2,
            "REQUEST":  {
            "qid":"1",
            "method":"sigmutilrawtx",
            "params":{
                "raw_tx":signed_tx,
                "m":4,
                "pub_keys":[
                    public_key_1,
                    public_key_2,
                    public_key_3,
                    public_key_4
                ]
            }
            },
            "RESPONSE": {}
    }
    sign_multi_transction(Task(name="test_1", ijson=request)) 
    signed_tx = response["result"]["signed_tx"]

    request = {
            "NODE_INDEX" :3,
            "REQUEST":  {
            "qid":"1",
            "method":"sigmutilrawtx",
            "params":{
                "raw_tx":signed_tx,
                "m":4,
                "pub_keys":[
                    public_key_1,
                    public_key_2,
                    public_key_3,
                    public_key_4
                ]
            }
            },
            "RESPONSE": {}
    }
    sign_multi_transction(Task(name="test_1", ijson=request)) 
    signed_tx = response["result"]["signed_tx"]

    request = {
            "NODE_INDEX" :4,
            "REQUEST":  {
            "qid":"1",
            "method":"sigmutilrawtx",
            "params":{
                "raw_tx":signed_tx,
                "m":4,
                "pub_keys":[
                    public_key_1,
                    public_key_2,
                    public_key_3,
                    public_key_4
                ]
            }
            },
            "RESPONSE": {}
    }
    sign_multi_transction(Task(name="test_1", ijson=request)) 
    signed_tx = response["result"]["signed_tx"]


    (result, response) = call_signed_contract(signed_tx, True)
    (result, response) = call_signed_contract(signed_tx, False)
    return (result, response)

def transfer_25(neo_contract_address, from_address, to_address, amount, public_key_1, public_key_2, public_key_3, public_key_4):
    
    request = {
        "NODE_INDEX":0,
            "REQUEST":  {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": neo_contract_address,
                "version": 1,
                "params": [
                    {
                        "type": "string",
                        "value": "transfer"
                    },
                    {
                        "type": "array",
                        "value": [
                            {
                                "type": "bytearray",
                                "value": from_address
                            },
                            {
                                "type": "bytearray",
                                "value": to_address
                            },
                            {
                                "type": "int",
                                "value": amount
                            }
                        ]
                    }
                ]
            }
        },
        "RESPONSE": {}
    }

    (result, response) = sign_transction(Task(name="test_1", ijson=request))

    signed_tx = response["result"]["signed_tx"]

    request = {
            "NODE_INDEX" :1,
            "REQUEST":  {
            "qid":"1",
            "method":"sigmutilrawtx",
            "params":{
                "raw_tx":signed_tx,
                "m":4,
                "pub_keys":[
                    public_key_1,
                    public_key_2,
                    public_key_3,
                    public_key_4
                ]
            }
            },
            "RESPONSE": {}
    }
    sign_multi_transction(Task(name="test_1", ijson=request)) 
    signed_tx = response["result"]["signed_tx"]

    request = {
            "NODE_INDEX" :2,
            "REQUEST":  {
            "qid":"1",
            "method":"sigmutilrawtx",
            "params":{
                "raw_tx":signed_tx,
                "m":4,
                "pub_keys":[
                    public_key_1,
                    public_key_2,
                    public_key_3,
                    public_key_4
                ]
            }
            },
            "RESPONSE": {}
    }
    sign_multi_transction(Task(name="test_1", ijson=request)) 
    signed_tx = response["result"]["signed_tx"]

    request = {
            "NODE_INDEX" :3,
            "REQUEST":  {
            "qid":"1",
            "method":"sigmutilrawtx",
            "params":{
                "raw_tx":signed_tx,
                "m":4,
                "pub_keys":[
                    public_key_1,
                    public_key_2,
                    public_key_3,
                    public_key_4
                ]
            }
            },
            "RESPONSE": {}
    }
    sign_multi_transction(Task(name="test_1", ijson=request)) 
    signed_tx = response["result"]["signed_tx"]

    request = {
            "NODE_INDEX" :4,
            "REQUEST":  {
            "qid":"1",
            "method":"sigmutilrawtx",
            "params":{
                "raw_tx":signed_tx,
                "m":4,
                "pub_keys":[
                    public_key_1,
                    public_key_2,
                    public_key_3,
                    public_key_4
                ]
            }
            },
            "RESPONSE": {}
    }
    sign_multi_transction(Task(name="test_1", ijson=request)) 
    signed_tx = response["result"]["signed_tx"]


    (result, response) = call_signed_contract(signed_tx, True)
    (result, response) = call_signed_contract(signed_tx, False)
    return (result, response)



def approve_31(neo_contract_address, from_address, to_address, amount):
    request = {
            "REQUEST":  {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0100000000000000000000000000000000000000",
                "method":"approve",
                "version": 1,
                "params": [
                    
                        from_address,
                        to_address,
                        amount
                    
                ]
                
            }
        },
        "RESPONSE": {}
    }
    return call_contract(Task(name="test_1", ijson=request), twice = True) 

def approve_32(neo_contract_address, from_address, to_address, amount):
    request = {
            "NODE_INDEX":3,
            "REQUEST":  {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0100000000000000000000000000000000000000",
                "method":"approve",
                "version": 1,
                "params": [
                    
                        from_address,
                        to_address,
                        amount
                    
                ]
                
            }
        },
        "RESPONSE": {}
    }
    return call_contract(Task(name="test_1", ijson=request), twice = True) 


def allowance(neo_contract_address, from_address, to_address, amount):

    request = {
                "REQUEST":  {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": 0,
                    "gas_limit": 1000000000,
                    "address": "0100000000000000000000000000000000000000",
                    "method":"allowance",
                    "version": 1,
                    "params": [
                        
                            from_address,
                            to_address
                        
                    ]
                    
                }
            },
            "RESPONSE": {}
        }
    return call_contract(Task(name="test_1", ijson=request), twice = True) 

def allowance_32(from_address, to_address):

    request = {
                "NODE_INDEX":3,
                "REQUEST":  {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": 0,
                    "gas_limit": 1000000000,
                    "address": "0100000000000000000000000000000000000000",
                    "method":"allowance",
                    "version": 1,
                    "params": [
                        
                            from_address,
                            to_address
                        
                    ]
                    
                }
            },
            "RESPONSE": {}
        }
    return call_contract(Task(name="test_1", ijson=request), twice = True) 
