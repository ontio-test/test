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
from utils.init_ong_ont import *
from utils.config import *
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.commonapi import *
from utils.contractapi import *
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
	
	roleA_hex = ByteToHex(b"roleA")
	roleB_hex = ByteToHex(b"roleB")

def init(node_index=7, candidate=False, register_ontid=False, restart=False, pub_key="1", ont_count="10000"):
	'''
	restart all nodes
	register ONTID
	create role and bind ONTID with role
	be candidate or not
	'''
	
	# restart all nodes
	if restart:
		stop_nodes(range(0, 14))
		start_nodes(range(0, 14), Config.DEFAULT_NODE_ARGS, clear_chain = True, clear_log = True)
		
		time.sleep(10)
		init_ont_ong()

	# register ONTID
	if register_ontid:
		for num in range(0,14):
			regIDWithPublicKey(num)
		#regIDWithPublicKey(node_index)

	time.sleep(5)

	if candidate:
		# create role and bind ONTID with role
		(result, response) = bind_role_function("0700000000000000000000000000000000000000", ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),["registerCandidate"],node_index=0)  
		time.sleep(7) 
		(result, response) = bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES[7]["ontid"], encoding = "utf8")),ByteToHex(bytes(Config.NODES[8]["ontid"], encoding = "utf8")),ByteToHex(bytes(Config.NODES[9]["ontid"], encoding = "utf8")),ByteToHex(bytes(Config.NODES[10]["ontid"], encoding = "utf8")),ByteToHex(bytes(Config.NODES[11]["ontid"], encoding = "utf8")),ByteToHex(bytes(Config.NODES[12]["ontid"], encoding = "utf8")),ByteToHex(bytes(Config.NODES[13]["ontid"], encoding = "utf8"))],node_index=0)
		time.sleep(15) 
		
	
		for add in range(7,14):
			transferTest("ont",Config.MULTI_SIGNED_ADDRESS,Config.NODES[add]["address"],10000000,public_key_Array=[5,[Config.NODES[0]["pubkey"],Config.NODES[1]["pubkey"],Config.NODES[2]["pubkey"],Config.NODES[3]["pubkey"],Config.NODES[4]["pubkey"],Config.NODES[5]["pubkey"],Config.NODES[6]["pubkey"]]])
			
			transferTest("ong",Config.MULTI_SIGNED_ADDRESS,Config.NODES[add]["address"],1000000000000,public_key_Array=[5,[Config.NODES[0]["pubkey"],Config.NODES[1]["pubkey"],Config.NODES[2]["pubkey"],Config.NODES[3]["pubkey"],Config.NODES[4]["pubkey"],Config.NODES[5]["pubkey"],Config.NODES[6]["pubkey"]]])
			time.sleep(15)

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
						"value": "init"
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
		node_index = Common.ontid_map[admin_address]
		request["NODE_INDEX"] = node_index		
	
	return call_contract(Task(name="init_admin", ijson=request), twice = True)


def bind_role_function(contract_address, admin_address, role_str, functions, public_key="1", node_index = None):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0600000000000000000000000000000000000000",
				"method": "assignFuncsToRole",
				"version": 0,
				"params": [
					contract_address,
					admin_address,
					role_str,
					functions,
					public_key
				]
			}
		},
		"RESPONSE":{"error" : 0}
	}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[admin_address]
		request["NODE_INDEX"] = node_index
		
	return call_contract(Task(name="bind_role_function", ijson=request), twice = True)


def bind_user_role(contract_address, admin_address, role_str, ontIDs, public_key="1", node_index = None):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0600000000000000000000000000000000000000",
				"method": "assignOntIDsToRole",
				"version": 0,
				"params": [
					contract_address,
					admin_address,
					role_str,
					ontIDs,
					public_key
				]
			}
		},
		"RESPONSE":{"error" : 0}
	}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[admin_address]
		request["NODE_INDEX"] = node_index
		
	return call_contract(Task(name="bind_user_role", ijson=request), twice = True)


def delegate_user_role(contract_address, owner_user, delegate_user, delegate_role, period, level, public_key="1", node_index = None):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0600000000000000000000000000000000000000",
				"method": "delegate",
				"version": 0,
				"params": [
					contract_address,
					owner_user,
					delegate_user,
					delegate_role,
					period,
					level,
					public_key
				]
			}
		},
		"RESPONSE":{"error" : 0}
	}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[owner_user]
		request["NODE_INDEX"] = node_index

	return call_contract(Task(name="delegate_user_role", ijson=request), twice = True)

	
def withdraw_user_role(contract_address, call_user, delegate_user, delegate_role, public_key="1", node_index = None):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0600000000000000000000000000000000000000",
				"method": "withdraw",
				"version": 0,
				"params": [
					contract_address,
					call_user,
					delegate_user,
					delegate_role,
					public_key
				]
			}
		},
		"RESPONSE":{"error" : 0}
	}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[call_user]
		request["NODE_INDEX"] = node_index
		
	return call_contract(Task(name="withdraw_user_role", ijson=request), twice = True)


def invoke_function(contract_address, function_str, callerOntID, public_key="1", argvs = [{"type": "string","value": ""}], node_index = None):
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
						"value": function_str
					},
					{
						"type": "array",
						"value": [
							{
								"type": "bytearray",
								"value": callerOntID
							},
							{
								"type": "int",
								"value": public_key
							}
						]
					},
					{
						"type": "array",
						"value": argvs
					}
				]
			}
		},
		"RESPONSE":{"error" : 0}
	}

	if node_index != None:
		request["NODE_INDEX"] = node_index
	else:
		node_index = Common.ontid_map[callerOntID]
		request["NODE_INDEX"] = node_index
		
	return call_contract(Task(name="invoke_function", ijson=request), twice = True)

	
	
def invoke_function_test(contract_address, function_str, argvs = [{"type": "string","value": ""}], node_index = None):
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
						"value": function_str
					},
					{
						"type": "array",
						"value": argvs
	 				}
				]
			}
		},
		"RESPONSE":{"error" : 0}
	}
		
	return call_contract(Task(name="invoke_function_test", ijson=request), twice = True)

def invoke_function_vote(func_,walletAddress,voteList,voteCount,errorcode=47001,node_index=None):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0700000000000000000000000000000000000000",
				"method": func_,
				"version": 0,
				"params": [
							walletAddress,
		  					voteList,
							voteCount
						]
					}
				},
		"RESPONSE":{"error" : errorcode}
	}
	if node_index != None:
		request["NODE_INDEX"] = node_index
	return call_contract(Task(name="invoke_function_vote", ijson=request), twice = True)

def invoke_function_update(func_,param0,param1,param2,param3,param4,param5,param6,param7,errorcode=47001):
	if(func_=="updateConfig"):
		filename="vbftConfig"
	else:
		filename="globalParam"
	getStorageConf(filename)
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0700000000000000000000000000000000000000",
				"method": func_,
				"version": 0,
				"params": [
							param0,
							param1,
							param2,
							param3,
							param4,
							param5,
							param6,
							param7
						  ]
					}
				},
		"RESPONSE":{"error" : errorcode}
	}
	(result,response)=	multi_contract(Task(name="invoke_function_update", ijson=request),Common.AdminNum,Common.AdminPublicKeyList)
	time.sleep(5)
	getStorageConf(filename)
	return (result,response)

def invoke_function_register(func_,pubKey,walletAddress,ontCount,ontID,user,errorcode = 47001,node_index=0):
	request = {
		"NODE_INDEX":node_index,
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0700000000000000000000000000000000000000",
				"method": func_,
				"version": 0,
				"params": [
							pubKey,
							walletAddress,
							ontCount,
							ontID,
							user
						  ]
					}
				},
		"RESPONSE":{"error" : errorcode}
	}
		
	return call_contract(Task(name="invoke_function_register", ijson=request), twice = True)

def invoke_function_candidate(func_,pubKey,errorcode=47001):
	request = {
		"NODE_INDEX":7,
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0700000000000000000000000000000000000000",
				"method": func_,
				"version": 0,
				"params": [
							pubKey
						  ]
					}
				},
		"RESPONSE":{"error" : errorcode}
	}
		
	return multi_contract(Task(name="invoke_function_candidate", ijson=request),Common.AdminNum,Common.AdminPublicKeyList)

def invoke_function_node(func_,pubKey,errorcode=47001):
	request = {
		"NODE_INDEX":0,
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0700000000000000000000000000000000000000",
				"method": func_,
				"version": 0,
				"params": [
							[pubKey]
						  ]
					}
				},
		"RESPONSE":{"error" : errorcode}
	}

	return multi_contract(Task(name="invoke_function_node", ijson=request),Common.AdminNum,Common.AdminPublicKeyList)

def invoke_function_commitDpos(nodeIndex=0):
	request = {
		"NODE_INDEX":nodeIndex,
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

def invoke_function_quitNode(func_,pubKey,walletAddress,node_index=0,errorcode=47001):
	request = {
		"NODE_INDEX":node_index,
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0700000000000000000000000000000000000000",
				"method": func_,
				"version": 0,
				"params": [
							pubKey,
							walletAddress
						  ]
					}
				},
		"RESPONSE":{"error" : errorcode}
	}

	return call_contract(Task(name="invoke_function_quitNode", ijson=request), twice = True)
def invoke_function_TransferPenalty(func_,pubKey,walletAddress,errorcode=47001):
	request = {
		"NODE_INDEX":0,
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0700000000000000000000000000000000000000",
				"method": func_,
				"version": 0,
				"params": [
							pubKey,
							walletAddress
						  ]
					}
				},
		"RESPONSE":{"error" : errorcode}
	}

	return multi_contract(Task(name="invoke_function_TransferPenalty", ijson=request),Common.AdminNum,Common.AdminPublicKeyList)

def invoke_function_SplitCurve(func_,array):
	request = {
		"NODE_INDEX":0,
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0700000000000000000000000000000000000000",
				"method": func_,
				"version": 0,
				"params": [
							array
						  ]
					}
				},
		"RESPONSE":{"error" : 0}
	}
	return multi_contract(Task(name="invoke_function_SplitCurve", ijson=request),Common.AdminNum,Common.AdminPublicKeyList)
	
def nodeCountCheck(InResponse,nodeCount):
	rpcapiTest=RPCApi()
	(result1, response1)=rpcapiTest.getstorage("0700000000000000000000000000000000000000",ByteToHex(b"governanceView"))
	if not result1:
		return (False,{"error_info":"getstorage governanceView error !"})
	viewvalue=""
	viewvalue=response1["result"][0:8]
	print(viewvalue)
	(result1, response1)=rpcapiTest.getstorage("0700000000000000000000000000000000000000",ByteToHex(b"peerPool")+viewvalue)
	if not result1:
		return (False,{"error_info":"getstorage peerPool error ! viewValue:"+viewValue})
	resCheck=script_hash_bl_reserver(response1["result"][0:2])
	print(resCheck)
	resInt= bytes.fromhex(resCheck)
	print(resInt.hex())
	if isinstance(InResponse,dict):
		InResponse["nodeCountNow"]=int(resInt.hex(), 16)
	else:
		InResponse={"response":InResponse,"nodeCountNow":int(resInt.hex(), 16)}
	
	if (nodeCount==int(resInt.hex(), 16)):
		return (True,InResponse)
	else:
		return (False,InResponse)
		
def getStorageConf(confName):                 ##########
	rpcapiTest=RPCApi()
	return rpcapiTest.getstorage("0700000000000000000000000000000000000000",ByteToHex(confName.encode("utf-8")))
	
def getStorageVoteInfo(pubkey,address):
	rpcapiTest=RPCApi()
	test=ByteToHex(b"voteInfo")+pubkey+script_hash_bl_reserver(base58_to_address(address))
	print(pubkey)
	print(address)
	(result1, response1)=rpcapiTest.getstorage("0700000000000000000000000000000000000000",test)
	
def native_transfer(pay_address,get_address,amount, node_index = None,errorcode=47001):
	amount=amount*1000000000
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
				"params": [[
					pay_address,
					get_address,
					amount
				]]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return call_contract(Task(name="transfer", ijson=request), twice = True)	
def native_transfer_multi(pay_address,get_address,amount, node_index = None,errorcode=47001):
	amount=amount*1000000000
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
				"params": [[
					pay_address,
					get_address,
					str(amount)
				]]
			}
		},
		"RESPONSE":{"error" : errorcode},
	}
	return call_contract(Task(name="transfer", ijson=request), twice = True)
#InResponse={}
#getStorageVoteInfo(Config.NODES[0]["pubkey"],Config.NODES[7]["address"])
#getStorageVoteInfo(Config.NODES[0]["pubkey"],Config.NODES[7]["address"])
#nodeCountCheck(InResponse,7)
#getStorageConf("vbftConfig")
#getStorageConf("globalParam")
#getStorageConf("splitCurve")