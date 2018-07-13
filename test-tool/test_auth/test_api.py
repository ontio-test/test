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
import subprocess

sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.contractapi import *
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.init_ong_ont import init_ont_ong
    

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


def init(node_index=7, candidate=False, register_ontid=False, restart=False, pub_key="1", ont_count="10000"):
    '''
    restart all nodes
    register ONTID
    create role and bind ONTID with role
    be candidate or not
    '''
    '''
    # restart all nodes
    if restart:    
        stop_nodes(range(0, 8))
        start_nodes(range(0, 8), Config.DEFAULT_NODE_ARGS, clear_chain = True, clear_log = True)
        time.sleep(5)
        init_ont_ong()
        time.sleep(5)

    # register ONTID
    if register_ontid:
        for i in range(0, 8):
            time.sleep(2)
            regIDWithPublicKey(i)

    time.sleep(10)
    '''
    if candidate:
        # create role and bind ONTID with role
        (result, response) = bind_role_function("0700000000000000000000000000000000000000", ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),["registerCandidate"])
        if not result:
            raise Error("bind_role_function error")

        (result, response) = bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES["0"]["ontid"], encoding = "utf8"))])
        if not result:
            raise Error("bind_user_role error")

        (result, response) = invoke_function_register(Config.NODES[node_index]["pubkey"], Config.NODES[node_index]["address"] ,ont_count, ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), pub_key, node_index)
        if not result:
            raise Error("invoke_function_register error")
        (result, response) = invoke_function_approve(Config.NODES[node_index]["pubkey"])
        if not result:
            raise Error("invoke_function_approve error")
    

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
    
        
    return call_contract(Task(name="bind_role_function", ijson=request), twice = True)

def invoke_assignfuncstorole_neo(contract_address, admin_address, role_str, functions, public_key="1", node_index = None):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": contract_address,
                "version": 0,
                "params": [
                    {
                        "type": "string",
                        "value": "assignFuncsToRole"
                    },
                    {
                        "type": "array",
                        "value": [
                            {
                                "type" : "string",
                                "value" : contract_address
                            },
                            {
                                "type" : "bytearray",
                                "value" : admin_address
                            },
                            {
                                "type" : "bytearray",
                                "value" : role_str
                            },
                            {
                                "type" : "array",
                                "value" : [
                                    {
                                        "type" : "string",
                                        "value" : functions
                                    }
                                ]
                            },
                            {
                                "type" : "int",
                                "value" : public_key
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
    
        
    return call_contract(Task(name="bind_user_role", ijson=request), twice = True)

def invoke_assignontidstorole_neo(contract_address, admin_address, role_str, ontIDs, public_key="1", node_index = None):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": contract_address,
                "version": 0,
                "params": [
                    {
                        "type": "string",
                        "value": "assignOntIDsToRole"
                    },
                    {
                        "type": "array",
                        "value": [
                            {
                                "type" : "string",
                                "value" : contract_address
                            },
                            {
                                "type" : "bytearray",
                                "value" : admin_address
                            },
                            {
                                "type" : "bytearray",
                                "value" : role_str
                            },
                            {
                                "type" : "array",
                                "value" : [
                                    {
                                        "type" : "bytearray",
                                        "value" : ontIDs
                                    }
                                ]
                            },
                            {
                                "type" : "int",
                                "value" : public_key
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
    
        
    return call_contract(Task(name="bind_role_function", ijson=request), twice = True)


def delegate_user_role(contract_address, owner_user, delegate_user, delegate_role, period, level, public_key="1", node_index = None):
    node_index = 0 if not node_index else node_index
    request = {
        "NODE_INDEX" :node_index,
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
    

    return call_contract(Task(name="delegate_user_role", ijson=request), twice = True)

def invoke_delegate_neo(contract_address, owner_user, delegate_user, delegate_role, period, level, public_key="1", node_index = None):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": contract_address,
                "version": 0,
                "params": [
                    {
                        "type": "string",
                        "value": "delegate"
                    },
                    {
                        "type": "array",
                        "value": [
                            {
                                "type" : "string",
                                "value" : contract_address
                            },
                            {
                                "type" : "bytearray",
                                "value" : owner_user
                            },
                            {
                                "type" : "bytearray",
                                "value" : delegate_user
                            },
                            {
                                "type" : "bytearray",
                                "value" : delegate_role
                            },
                            {
                                "type" : "bytearray",
                                "value" : period
                            },
                            {
                                "type" : "int",
                                "value" : level
                            },
                            {
                                "type" : "int",
                                "value" : public_key
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
    
        
    return call_contract(Task(name="bind_role_function", ijson=request), twice = True)


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
    
        
    return call_contract(Task(name="withdraw_user_role", ijson=request), twice = True)

def invoke_withdraw_neo(contract_address, call_user, delegate_user, delegate_role, public_key="1", node_index = None):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": contract_address,
                "version": 0,
                "params": [
                    {
                        "type": "string",
                        "value": "withdraw"
                    },
                    {
                        "type": "array",
                        "value": [
                            {
                                "type" : "string",
                                "value" : contract_address
                            },
                            {
                                "type" : "bytearray",
                                "value" : call_user
                            },
                            {
                                "type" : "bytearray",
                                "value" : delegate_user
                            },
                            {
                                "type" : "bytearray",
                                "value" : delegate_role
                            },
                            {
                                "type" : "int",
                                "value" : public_key
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
    
        
    return call_contract(Task(name="bind_role_function", ijson=request), twice = True)

def transfer(contract_address, new_admin_ontid, public_key="1", node_index = None):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0600000000000000000000000000000000000000",
                "method": "transfer",
                "version": 0,
                "params": [
                    contract_address,
                    new_admin_ontid,
                    public_key
                ]
            }
        },
        "RESPONSE":{"error" : 0}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index
        
    return call_contract(Task(name="withdraw_user_role", ijson=request), twice = True)

def invoke_transfer_neo(contract_address, new_admin_ontid, public_key="1", node_index = None):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": contract_address,
                "version": 0,
                "params": [
                    {
                        "type": "string",
                        "value": "transfer"
                    },
                    {
                        "type": "array",
                        "value": [
                            {
                                "type" : "string",
                                "value" : contract_address
                            },
                            {
                                "type" : "bytearray",
                                "value" : new_admin_ontid
                            },
                            {
                                "type" : "int",
                                "value" : public_key
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
    
        
    return call_contract(Task(name="withdraw_user_role", ijson=request), twice = True)


def invoke_function(contract_address, function_str, callerOntID, public_key="1", node_index = None):
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
                        "value": [
                            {
                                "type": "string",
                                "value": ""
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
        
    return call_contract(Task(name="invoke_function", ijson=request), twice = True)

def invoke_function_register(pubKey,walletAddress,ontCount,ontID,user, node_index):
    request = {
        "NODE_INDEX":node_index,
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "registerCandidate",
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


def invoke_function_approve(pubKey):
    request = {
        "NODE_INDEX":5,
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
        
    return call_contract(Task(name="invoke_function_candidate", ijson=request), twice = True)
