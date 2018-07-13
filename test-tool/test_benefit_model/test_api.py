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



def invoke_transfer(contract_address, from_address, to_address, amount, node_index = None):
    request = {
        "DEPLOY" : false,
        "CODE_PATH" : "tasks/ont_1_42.neo", 
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 10000,
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

def invoke_function_vote(func_,walletAddress,voteList,voteCount):
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
          	                [voteList],
                            [voteCount]
		                ]
                    }
                },
        "RESPONSE":{"error" : 0}
    }
        
    return call_contract(Task(name="invoke_function_vote", ijson=request), twice = True)

def invoke_function_update(func_,param0,param1,param2,param3,param4,param5,param6,param7):
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
        "RESPONSE":{"error" : 0}
    }
        
    return call_contract(Task(name="invoke_function_update", ijson=request), twice = True)

def invoke_function_register(func_,pubKey,walletAddress,ontCount,ontID,user):
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
        "RESPONSE":{"error" : 0}
    }
        
    return call_contract(Task(name="invoke_function_register", ijson=request), twice = True)

def invoke_function_candidate(func_,pubKey):
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
        "RESPONSE":{"error" : 0}
    }
        
    return call_contract(Task(name="invoke_function_candidate", ijson=request), twice = True)

def invoke_function_node(func_,pubKey):
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
        "RESPONSE":{"error" : 0}
    }

    return call_contract(Task(name="invoke_function_node", ijson=request), twice = True)

def invoke_function_quitNode(func_,pubKey,walletAddress):
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
        "RESPONSE":{"error" : 0}
    }

    return call_contract(Task(name="invoke_function_quitNode", ijson=request), twice = True)

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
    return call_contract(Task(name="invoke_function_SplitCurve", ijson=request), twice = True)