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
    ontID_Admin = ByteToHex(bytes(Config.SERVICES[node_Admin]["ontid"], encoding = "utf8"))
    ontid_map[ontID_Admin] = node_Admin
	
    node_A = 3
    ontID_A = ByteToHex(bytes(Config.SERVICES[node_A]["ontid"], encoding = "utf8"))
    ontid_map[ontID_A] = node_A
	
    node_B = 4
    ontID_B = ByteToHex(bytes(Config.SERVICES[node_B]["ontid"], encoding = "utf8"))
    ontid_map[ontID_B] = node_B
	
    node_C = 5
    ontID_C = ByteToHex(bytes(Config.SERVICES[node_C]["ontid"], encoding = "utf8"))
    ontid_map[ontID_C] = node_C
	
    node_D = 6
    ontID_D = ByteToHex(bytes(Config.SERVICES[node_D]["ontid"], encoding = "utf8"))
    ontid_map[ontID_D] = node_D
	
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
