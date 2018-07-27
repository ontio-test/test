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
from test_conf import testConfig
from utils.multi_sig import *

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

def get_config():
    wallet_A_address   = testConfig.wallet_A_address
    wallet_B_address   = testConfig.wallet_B_address
    vote_price 		   = testConfig.vote_price
    node_B_puiblic_key = testConfig.node_B_puiblic_key
    blocks_per_round   = testConfig.blocks_per_round
    punish_ratio       = testConfig.punish_ratio
    return (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio)


def vote_for_peer(wallet_address, nodes_to_vote, ballot_to_vote):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "voteForPeer",
                "version": 0,
                "params": [
                    wallet_address,
                    nodes_to_vote,
                    ballot_to_vote
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request), twice = True)

def vote_for_peer_index(wallet_address, nodes_to_vote, ballot_to_vote, node_index=8):
    request = {
        "NODE_INDEX":node_index,
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "voteForPeer",
                "version": 0,
                "params": [
                    wallet_address,
                    nodes_to_vote,
                    ballot_to_vote
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request), twice = True)

def unvote_for_peer(wallet_address, nodes_to_vote, ballot_to_vote):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "unVoteForPeer",
                "version": 0,
                "params": [
                    wallet_address,
                    nodes_to_vote,
                    ballot_to_vote
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request), twice = True)

def unvote_for_peer_index(wallet_address, nodes_to_vote, ballot_to_vote, node_index=8):
    request = {
        "NODE_INDEX":node_index,
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "unVoteForPeer",
                "version": 0,
                "params": [
                    wallet_address,
                    nodes_to_vote,
                    ballot_to_vote
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request), twice = True)


def withdraw_ont(wallet_address, nodes_to_vote, ballot_to_vote):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "withdraw",
                "version": 0,
                "params": [
                    wallet_address,
                    nodes_to_vote,
                    ballot_to_vote
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request), twice = True)

def withdraw_ont_index(wallet_address, nodes_to_vote, ballot_to_vote, node_index=8):
    request = {
        "NODE_INDEX":node_index,
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "withdraw",
                "version": 0,
                "params": [
                    wallet_address,
                    nodes_to_vote,
                    ballot_to_vote
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request), twice = True)

def quit_node(node_public_key, wallet_address):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 10000,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "quitNode",
                "version": 0,
                "params": [
                    node_public_key,
                    wallet_address
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request))

def quit_node_index(node_public_key, wallet_address, node_index=8):
    request = {
        "NODE_INDEX":node_index,
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 10000,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "quitNode",
                "version": 0,
                "params": [
                    node_public_key,
                    wallet_address
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request))

def black_node(node_public_key):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "blackNode",
                "version": 0,
                "params": [
                    node_public_key
                ]
            }
        },
        "RESPONSE": {}
    }

    return multi_contract(Task(name="invoke_function_candidate", ijson=request),Common.AdminNum,Common.AdminPublicKeyList)

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
        node_index = Config.ontid_map[admin_address]
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
        node_index = Config.ontid_map[admin_address]
        request["NODE_INDEX"] = node_index
        
    return call_contract(Task(name="bind_user_role", ijson=request), twice = True)


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
        
    return multi_contract(Task(name="invoke_function_candidate", ijson=request),Common.AdminNum,Common.AdminPublicKeyList)

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
	(result,response)=	multi_contract(Task(name="invoke_function_update", ijson=request),Common.AdminNum,Common.AdminPublicKeyList)
	time.sleep(5)
	return (result,response)

def native_transfer_ont(pay_address,get_address,amount, node_index = None,errorcode=47001):
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
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return call_contract(Task(name="transfer", ijson=request), twice = True)

def native_transfer_ong(pay_address,get_address,amount, node_index = None,errorcode=47001):
    _amount = int(amount) * 1000000000
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
                            str(_amount)
                        ]
                    ]
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
    return call_contract(Task(name="transfer", ijson=request), twice = True)


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

def getbalance_ont(wallet_address):
    getbalance = Task("../utils/baseapi/rpc/getbalance.json")
    getbalance.data()["REQUEST"]["params"] = [wallet_address]
    (result, response) = run_single_task(getbalance, True, False)
    return int(response["result"]["ont"])

def getblockcount():
    getbalance = Task("../utils/baseapi/rpc/getblockcount.json")
    (result, response) = run_single_task(getbalance, True, False)
    return int(response["result"])

def getMaxBlockChangeView():
    getbalance = Task("../utils/baseapi/rpc/getstorage.json")
    contract_address = "0200000000000000000000000000000000000000"
    key = "79626674436f6e666967"
    getbalance.data()["REQUEST"]["params"] = [contract_address, key]
    (result, response) = run_single_task(getbalance, True, False)
    return int(response["result"]["ont"])
