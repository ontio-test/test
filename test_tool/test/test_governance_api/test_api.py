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

from utils.config import *
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.common import Common
from api.apimanager import API

def init(node_index=7, candidate=False, register_ontid=False, restart=False, pub_key="1", ont_count="10000"):
	'''
	restart all nodes
	register ONTID
	create role and bind ONTID with role
	be candidate or not
	'''
	
	# restart all nodes
	if restart:
		API.node().stop_all_nodes()
		API.node().start_nodes(range(0, 8), Config.DEFAULT_NODE_ARGS, clear_chain = True, clear_log = True)
		
		API.native().init_ont_ong(node_count=8)

	# register ONTID
	if register_ontid:
		API.native().regid_with_publickey(0, sleep=0)
		API.native().regid_with_publickey(node_index, sleep=0)

	API.node().wait_gen_block()

	if candidate:
		# create role and bind ONTID with role
		(process, response) = API.native().bind_role_function("0700000000000000000000000000000000000000", ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),["registerCandidate"])

		(process, response) = API.native().bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES[7]["ontid"], encoding = "utf8"))])
		API.node().wait_gen_block()

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
		node_index = Config.ontid_map[admin_address]
		request["NODE_INDEX"] = node_index		
	
	return API.contract().call_contract(Task(name="init_admin", ijson=request), twice = True)


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
		node_index = Config.ontid_map[owner_user]
		request["NODE_INDEX"] = node_index

	return API.contract().call_contract(Task(name="delegate_user_role", ijson=request), twice = True)

	
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
		node_index = Config.ontid_map[call_user]
		request["NODE_INDEX"] = node_index
		
	return API.contract().call_contract(Task(name="withdraw_user_role", ijson=request), twice = True)


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
		node_index = Config.ontid_map[callerOntID]
		request["NODE_INDEX"] = node_index
		
	return API.contract().call_contract(Task(name="invoke_function", ijson=request), twice = True)

	
	
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
		
	return API.contract().call_contract(Task(name="invoke_function_test", ijson=request), twice = True)

def invoke_function_vote(func_,walletAddress,voteList,voteCount,errorcode=0,node_index=None):
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
	return API.contract().call_contract(Task(name="invoke_function_vote", ijson=request), twice = True)

def invoke_function_update(func_,param0,param1,param2,param3,param4,param5,param6,param7,errorcode=0):
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
	(result,response)=	API.contract().call_multisig_contract(Task(name="invoke_function_update", ijson=request),Config.AdminNum,Config.AdminPublicKeyList)
	time.sleep(5)
	getStorageConf(filename)
	return (result,response)

def invoke_function_register(func_,pubKey,walletAddress,ontCount,ontID,user,errorcode = 0):
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
		
	return API.contract().call_contract(Task(name="invoke_function_register", ijson=request), twice = True)

def invoke_function_candidate(func_,pubKey,errorcode=0):
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
		
	return API.contract().call_multisig_contract(Task(name="invoke_function_candidate", ijson=request),Config.AdminNum,Config.AdminPublicKeyList)

def invoke_function_node(func_,pubKey,errorcode=0):
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

	return API.contract().call_multisig_contract(Task(name="invoke_function_node", ijson=request),Config.AdminNum,Config.AdminPublicKeyList)

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

	return API.contract().call_multisig_contract(Task(name="invoke_function_commitDpos", ijson=request),Config.AdminNum,Config.AdminPublicKeyList)

def invoke_function_quitNode(func_,pubKey,walletAddress,node_index=None,errorcode=0):
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

	return API.contract().call_contract(Task(name="invoke_function_quitNode", ijson=request), twice = True)
def invoke_function_TransferPenalty(func_,pubKey,walletAddress,errorcode=0):
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

	return API.contract().call_multisig_contract(Task(name="invoke_function_TransferPenalty", ijson=request),Config.AdminNum,Config.AdminPublicKeyList)

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
	return API.contract().call_multisig_contract(Task(name="invoke_function_SplitCurve", ijson=request),Config.AdminNum,Config.AdminPublicKeyList)
	
def nodeCountCheck(InResponse,nodeCount):
	(result1, response1)=API.rpc().getstorage("0700000000000000000000000000000000000000",ByteToHex(b"governanceView"))
	if not result1:
		return (False,{"error_info":"getstorage governanceView error !"})
	viewvalue=""
	viewvalue=response1["result"][0:8]
	print(viewvalue)
	(result1, response1)=API.rpc().getstorage("0700000000000000000000000000000000000000",ByteToHex(b"peerPool")+viewvalue)
	if not result1:
		return (False,{"error_info":"getstorage peerPool error ! viewValue:"+viewValue})
	resCheck = Common.bl_reserver(response1["result"][0:2])
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
		
def getStorageConf(confName):
	return API.rpc().getstorage("0700000000000000000000000000000000000000",ByteToHex(confName.encode("utf-8")))
	
def getStorageVoteInfo(pubkey,address):
	test=ByteToHex(b"voteInfo")+pubkey+Common.bl_address(address)
	print(pubkey)
	print(address)
	(result1, response1)=API.rpc().getstorage("0700000000000000000000000000000000000000",test)
	
def native_transfer_ont(pay_address,get_address,amount, node_index1 = None,errorcode1=0):
	return API.native().transfer_ont(pay_address, get_address, str(amount), node_index=node_index1, errorcode=errorcode1)
	
def native_transfer_multi(pay_address,get_address,amount, node_index = None,errorcode=0):
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
	return API.contract().call_contract(Task(name="transfer", ijson=request), twice = True)
#InResponse={}
#getStorageVoteInfo(Config.NODES[0]["pubkey"],Config.NODES[7]["address"])
#getStorageVoteInfo(Config.NODES[0]["pubkey"],Config.NODES[7]["address"])
#nodeCountCheck(InResponse,7)
#getStorageConf("vbftConfig")
#getStorageConf("globalParam")
#getStorageConf("splitCurve")