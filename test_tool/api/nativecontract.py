# -*- coding:utf-8 -*-
import re
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import shutil
import sys
import getopt
import time
import requests
import subprocess
import tempfile

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.parametrizedtestcase import ParametrizedTestCase
from api.contract import ContractApi
from api.node import NodeApi

CONTRACT_API = ContractApi()
NODE_API = NodeApi()

class NativeApi:
    ADMIN_NUM = 5
    ADMIN_PUBLIST = [Config.NODES[0]["pubkey"],Config.NODES[1]["pubkey"],Config.NODES[2]["pubkey"],Config.NODES[3]["pubkey"],Config.NODES[4]["pubkey"],Config.NODES[5]["pubkey"],Config.NODES[6]["pubkey"]]
    
    ##############################################
    ###0100000000000000000000000000000000000000###
    
    def allowance_ont(self, from_address, to_address, amount, node_index=None, errorcode=0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
                    "REQUEST":  {
                    "Qid": "t",
                    "Method": "signativeinvoketx",
                    "Params": {
                        "gas_price": gas_price,
                        "gas_limit": gas_limit,
                        "address": "0100000000000000000000000000000000000000",
                        "method":"allowance",
                        "version": 1,
                        "params": [
                                from_address,
                                to_address 
                        ]  
                    }
                },
                "RESPONSE": {"error": errorcode}
            }
        if node_index != None:
            request["NODE_INDEX"] = node_index
        return CONTRACT_API.call_contract(Task(name="allowance_ont", ijson=request), twice = True, sleep=sleep) 

    def approve_ont(self, from_address, to_address, amount, node_index=None, errorcode=0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
                "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
                    "address": "0100000000000000000000000000000000000000",
                    "method": "approve",
                    "version": 1,
                    "params": [
                        from_address,
                        to_address,
                        amount
                    ]
                }
            },
            "RESPONSE":{"error" : errorcode}
        }
        if node_index != None:
            request["NODE_INDEX"] = node_index
        return CONTRACT_API.call_contract(Task(name="approve_ont", ijson=request), twice = True, sleep=5) 

    def transfer_ont(self, pay_address, get_address, amount, node_index=None, errorcode=0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5, pre=True, twice=True, check_state=True):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
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
            "RESPONSE": {"error": errorcode}
        }
        if node_index != None:
            request["NODE_INDEX"] = node_index
        else:
            for index in range(len(Config.NODES)):
                if Config.NODES[index]["address"] == pay_address:      
                    request["NODE_INDEX"] = index
                    break

        return CONTRACT_API.call_contract(Task(name="transfer_ont", ijson=request), twice=twice, sleep=sleep, pre=pre, check_state=check_state)

    ##############################################
    ###0200000000000000000000000000000000000000###
    def allowance_ong(self, from_address, to_address, amount, node_index=None,errorcode=0,gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
                    "REQUEST":  {
                    "Qid": "t",
                    "Method": "signativeinvoketx",
                    "Params": {
                        "gas_price": gas_price,
                        "gas_limit": gas_limit,
                        "address": "0200000000000000000000000000000000000000",
                        "method":"allowance",
                        "version": 1,
                        "params": [
                                from_address,
                                to_address 
                        ]  
                    }
                },
                "RESPONSE": {"error": errorcode}
            }
        if node_index != None:
            request["NODE_INDEX"] = node_index

        return CONTRACT_API.call_contract(Task(name="allowance_ong", ijson=request), twice = True, sleep=sleep) 

    def approve_ong(self, from_address, to_address, amount, node_index=None, errorcode=0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
                "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
                    "address": "0200000000000000000000000000000000000000",
                    "method": "approve",
                    "version": 1,
                    "params": [
                        from_address,
                        to_address,
                        amount
                    ]
                }
            },
            "RESPONSE":{"error" : errorcode}
        }
        if node_index != None:
            request["NODE_INDEX"] = node_index
        return CONTRACT_API.call_contract(Task(name="approve_ong", ijson=request), twice = True, sleep=sleep) 

    def transfer_ong(self, pay_address, get_address, amount, node_index=None, errorcode=0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
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
            "RESPONSE": {"error": errorcode}
        }
        if node_index != None:
            request["NODE_INDEX"] = node_index
        else:
            for index in range(len(Config.NODES)):
                if Config.NODES[index]["address"] == pay_address:            
                    request["NODE_INDEX"] = index
                    break

        return CONTRACT_API.call_contract(Task(name="transfer_ong", ijson=request), twice=True, sleep=sleep)

    ##############################################
    ###0300000000000000000000000000000000000000###
    def regid_with_publickey(self, node_index, errorcode = 0, sleep=5):
        ontid = Config.NODES[int(node_index)]["ontid"]
        pubkey = Config.NODES[int(node_index)]["pubkey"]
        request = {
            "REQUEST": {
            "Qid":"t",
            "Method":"signativeinvoketx",
            "Params":{
            "gas_price":0,
            "gas_limit":1000000000,
            "address":"0300000000000000000000000000000000000000",
            "method":"regIDWithPublicKey",
            "version":0,
            "params":[
                ontid,
                pubkey
            ]
            }
            },
            "RESPONSE": {"error": errorcode}
        }
        
        request["NODE_INDEX"] = node_index
        return CONTRACT_API.call_contract(Task(name ="regIDWithPublicKey", ijson=request), twice = True, sleep=sleep)

    ##############################################
    ###0600000000000000000000000000000000000000###
    def transfer_admin(self, contract_address, new_admin_ontid, public_key="1", node_index = None, errorcode = 0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
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
            "RESPONSE":{"error" : errorcode}
        }

        if node_index != None:
            request["NODE_INDEX"] = node_index
                    
        return CONTRACT_API.call_contract(Task(name="transfer_admin", ijson=request), twice = True, sleep=sleep)

    def bind_role_function(self, contract_address, admin_address, role_str, functions, public_key="1", node_index = None, errorcode = 0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
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
            "RESPONSE":{"error" : errorcode}
        }

        if node_index != None:
            request["NODE_INDEX"] = node_index
        else:
            node_index = Config.ontid_map[admin_address]
            request["NODE_INDEX"] = node_index
        return CONTRACT_API.call_contract(Task(name="bind_role_function", ijson=request), twice = True, sleep=sleep)

    def bind_user_role(self, contract_address, admin_address, role_str, ontIDs, public_key="1", node_index = None, error_code = 0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
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
            "RESPONSE":{"error" : error_code}
        }

        if node_index != None:
            request["NODE_INDEX"] = node_index
        else:
            node_index = Config.ontid_map[admin_address]
            request["NODE_INDEX"] = node_index
            
        return CONTRACT_API.call_contract(Task(name="bind_user_role", ijson=request), twice = True, sleep=sleep)

    def delegate_user_role(self, contract_address, owner_user, delegate_user, delegate_role, period, level, public_key="1", node_index = None, errorcode = 0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
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
            "RESPONSE":{"error" : errorcode}
        }

        if node_index != None:
            request["NODE_INDEX"] = node_index
        else:
            node_index = Config.ontid_map[owner_user]
            request["NODE_INDEX"] = node_index

        return CONTRACT_API.call_contract(Task(name="delegate_user_role", ijson=request), twice = True, sleep=sleep)


    def withdraw_user_role(self, contract_address, call_user, delegate_user, delegate_role, public_key="1", node_index = None, errorcode = 0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
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
            "RESPONSE":{"error" : errorcode}
        }

        if node_index != None:
            request["NODE_INDEX"] = node_index
        else:
            node_index = Config.ontid_map[call_user]
            request["NODE_INDEX"] = node_index
            
        return CONTRACT_API.call_contract(Task(name="withdraw_user_role", ijson=request), twice = True, sleep=sleep)

    ##############################################
    ###0700000000000000000000000000000000000000###
    def vote_for_peer(self, walletAddress,voteList,voteCount,node_index=None, errorcode=0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
                    "address": "0700000000000000000000000000000000000000",
                    "method": "voteForPeer",
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
        else:
            for node in Config.NODES:
                if node["address"] == walletAddress:
                    request["NODE_INDEX"] = Config.NODES.index(node)
                    break
            
        return CONTRACT_API.call_contract(Task(name="invoke_function_vote", ijson=request), twice = True, sleep=sleep)

    def unvote_for_peer(self, wallet_address, nodes_to_vote, ballot_to_vote, node_index=None, errorcode=0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
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
            "RESPONSE": {"error" : errorcode}
        }
        if node_index != None:
            request["NODE_INDEX"] = node_index
        else:
            for node in Config.NODES:
                if node["address"] == wallet_address:
                    request["NODE_INDEX"] = Config.NODES.index(node)
                    break

        return CONTRACT_API.call_contract(Task(name="invoke_function_unvote", ijson=request), twice = True, sleep=sleep)
        
    def withdraw_ont(self, wallet_address, nodes_to_vote, ballot_to_vote, node_index=None, errorcode=0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
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
            "RESPONSE": {"error" : errorcode}
        }

        if node_index != None:
            request["NODE_INDEX"] = node_index
        else:
            for node in Config.NODES:
                if node["address"] == wallet_address:
                    request["NODE_INDEX"] = Config.NODES.index(node)
                    break

        return CONTRACT_API.call_contract(Task(name="invoke_function_withdraw", ijson=request), twice = True, sleep=sleep)
    
    def update_global_param(self, param0,param1,param2,param3,param4,param5,param6,param7,errorcode=0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
                    "address": "0700000000000000000000000000000000000000",
                    "method": "updateGlobalParam",
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

        return CONTRACT_API.call_multisig_contract(Task(name="invoke_function_updateGlobalParam", ijson=request),Config.AdminNum,Config.AdminPublicKeyList, sleep=sleep)

    def quit_node(self, node_public_key, wallet_address, node_index=None, errorcode=0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
                    "address": "0700000000000000000000000000000000000000",
                    "method": "quitNode",
                    "version": 0,
                    "params": [
                        node_public_key,
                        wallet_address
                    ]
                }
            },
            "RESPONSE": {"error" : errorcode}
        }
        if node_index != None:
            request["NODE_INDEX"] = node_index
        else:
            for node in Config.NODES:
                if node["address"] == wallet_address:
                    request["NODE_INDEX"] = Config.NODES.index(node)
                    break

        return CONTRACT_API.call_contract(Task(name="invoke_function_quitNode", ijson=request), twice = True, sleep=sleep)

    def black_node(self, node_public_key, errorcode=0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
                    "address": "0700000000000000000000000000000000000000",
                    "method": "blackNode",
                    "version": 0,
                    "params": [
                        node_public_key
                    ]
                }
            },
            "RESPONSE": {"error" : errorcode}
        }

        return CONTRACT_API.call_multisig_contract(Task(name="invoke_function_blackNode", ijson=request),Config.AdminNum,Config.AdminPublicKeyList, sleep=sleep)

    def white_node(self, node_public_key, errorcode=0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
                    "address": "0700000000000000000000000000000000000000",
                    "method": "whiteNode",
                    "version": 0,
                    "params": [
                        node_public_key
                    ]
                }
            },
            "RESPONSE": {"error" : errorcode}
        }

        return CONTRACT_API.call_multisig_contract(Task(name="invoke_function_whiteNode", ijson=request),Config.AdminNum,Config.AdminPublicKeyList, sleep=sleep)

    def commit_dpos(self, errorcode = 0, gas_price = Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep = 5):
        request = {
            "NODE_INDEX":0,
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
                    "address": "0700000000000000000000000000000000000000",
                    "method": "commitDpos",
                    "version": 0,
                    "params": [
                              ]
                        }
                    },
            "RESPONSE":{"error" : errorcode}
        }

        (result, response) = CONTRACT_API.call_multisig_contract(Task(name="commit_dpos", ijson=request),Config.AdminNum,Config.AdminPublicKeyList, sleep=sleep, check_state = False)

        if result:
            NODE_API.wait_gen_block(True)
            NODE_API.wait_gen_block(True)

        return (result, response)


    #same to invoke_function_approve
    def approve_candidate(self, pubKey, errorcode = 0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "NODE_INDEX":0,
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
                    "address": "0700000000000000000000000000000000000000",
                    "method": "approveCandidate",
                    "version": 0,
                    "params": [
                                pubKey
                              ]
                        }
                    },
            "RESPONSE":{"error" : errorcode}
        }
            
        return CONTRACT_API.call_multisig_contract(Task(name="approve_candidate", ijson=request),Config.AdminNum,Config.AdminPublicKeyList, sleep=sleep)
    
    def reject_candidate(self, pubKey, errorcode = 0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "NODE_INDEX":0,
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
                    "address": "0700000000000000000000000000000000000000",
                    "method": "rejectCandidate",
                    "version": 0,
                    "params": [
                                pubKey
                              ]
                        }
                    },
            "RESPONSE":{"error" : errorcode}
        }
            
        return CONTRACT_API.call_multisig_contract(Task(name="reject_candidate", ijson=request),Config.AdminNum,Config.AdminPublicKeyList, sleep=sleep)


    #same to invoke_function_register
    def register_candidate(self, pubKey, walletAddress, ontCount, ontID, user, node_index = None, errorcode = 0, gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": gas_limit,
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
            "RESPONSE":{"error" : errorcode}
        }
           
        if node_index != None:
            request["NODE_INDEX"] = node_index
        else:
            node_index = Config.ontid_map[ontID]
            request["NODE_INDEX"] = node_index
        
        return CONTRACT_API.call_contract(Task(name="invoke_function_register", ijson=request), twice = True, sleep=sleep)


##############################################
    def transferFrom_multi(self, put_address, amount, node_index = None,errorcode=0,public_key_Array=[], errorkey = "error", gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params":{
                
                    "gas_price":gas_price,
                    "gas_limit":gas_limit,
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
        return CONTRACT_API.call_multisig_contract(Task(name="transferFrom_multi", ijson=request),public_key_Array[0],public_key_Array[1], sleep=sleep)
        
    def transfer_multi(self, assetStr,put_address, get_address,amount, node_index = None,errorcode=0,public_key_Array=[], errorkey = "error", gas_price= Config.DEFAULT_GAS_PRICE, gas_limit = Config.DEFAULT_GAS_LIMIT, sleep=5):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "sigtransfertx",
                "Params": {
                    "gas_price":gas_price,
                    "gas_limit":gas_limit,
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
        return CONTRACT_API.call_multisig_contract(Task(name="transfer_multi", ijson=request),public_key_Array[0],public_key_Array[1], sleep=sleep)

    def init_ont_ong(self, node_count = 7, sleep=0):
        for i in range(node_count):
            (result, response)=self.transfer_multi("ont",Config.MULTI_SIGNED_ADDRESS,Config.NODES[i]["address"],10000000,public_key_Array=[5,[Config.NODES[0]["pubkey"],Config.NODES[1]["pubkey"],Config.NODES[2]["pubkey"],Config.NODES[3]["pubkey"],Config.NODES[4]["pubkey"],Config.NODES[5]["pubkey"],Config.NODES[6]["pubkey"]]], sleep=sleep)
            if not result:
                return (result, response)
        if not NODE_API.wait_gen_block():
            return (False, "wait_gen_block time out[1]")

        (result, response) = self.transferFrom_multi(Config.MULTI_SIGNED_ADDRESS,Config.INIT_AMOUNT_ONG,5,public_key_Array=[5,[Config.NODES[0]["pubkey"],Config.NODES[1]["pubkey"],Config.NODES[2]["pubkey"],Config.NODES[3]["pubkey"],Config.NODES[4]["pubkey"],Config.NODES[5]["pubkey"],Config.NODES[6]["pubkey"]]], sleep=sleep)       
        if not result:
            return (result, response)
        if not NODE_API.wait_gen_block():
            return (False, "wait_gen_block time out[2]")

        for i in range(node_count):
            (result, response)=self.transfer_multi("ong",Config.MULTI_SIGNED_ADDRESS,Config.NODES[i]["address"], int(int(Config.INIT_AMOUNT_ONG) / node_count),public_key_Array=[5,[Config.NODES[0]["pubkey"],Config.NODES[1]["pubkey"],Config.NODES[2]["pubkey"],Config.NODES[3]["pubkey"],Config.NODES[4]["pubkey"],Config.NODES[5]["pubkey"],Config.NODES[6]["pubkey"]]], sleep=sleep)
            if not result:
                return (result, response)
        if not NODE_API.wait_gen_block():
            return (False, "wait_gen_block time out[2]")