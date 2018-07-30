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

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase

from api.apimanager import API

from test_benefit_model.test_config import test_config

class test_api:
    @staticmethod
    def get_yi(initpos, avgpos):
        xi = int(test_config.PRECISE * test_config.YITA * 2 * initpos / (avgpos * 10))
        try:
            index = test_config.XI_TABLE.index(xi)
            return test_config.YI_TABLE[index]
        except Exception as e:
            #去掉余数，并取相邻xi，算对应yi的线性值
            xi1 = int(xi/100000) * 100000
            xi_index1 = test_config.XI_TABLE.index(xi1)
            xi_index2 = xi_index1 + 1
            xi2 = test_config.XI_TABLE[xi_index2];

            yi1 = test_config.YI_TABLE[xi_index1]
            yi2 = test_config.YI_TABLE[xi_index2]
            
            xlineradio = (xi - xi1) / (xi2 - xi1)
            yi = int(xlineradio * (yi2 - yi1) + yi1)
            return yi
        return 0;
    
    @staticmethod 
    def get_benifit_value(totalgas, initpos, totalpos = [1000, 1000, 1000, 1000, 1000, 1000, 1000]):
        totalyi = 0
        totalposvalue = 0
        for pos in totalpos:
            totalposvalue = totalposvalue + pos
        
        avgpos = int(totalposvalue / len(totalpos))
        print("avgpos: " + str(avgpos))
        for pos in totalpos:
            totalyi = totalyi + test_api.get_yi(pos, avgpos)
            
        if totalyi == 0:
            return 0
        
        logger.info("get_benifit_value.totalgas: " + str(totalgas)) 
        logger.info("get_benifit_value.initpos: " + str(initpos)) 
        logger.info("get_benifit_value.avgpos: " + str(avgpos)) 
        logger.info("get_benifit_value.totalyi: " + str(totalyi)) 
        logger.info("get_benifit_value.get_yi: " + str(test_api.get_yi(initpos, avgpos)))
        logger.info("get_benifit_value: " + str(totalgas * test_api.get_yi(initpos, avgpos) / totalyi))

        return totalgas * test_api.get_yi(initpos, avgpos) / totalyi

    @staticmethod 
    def get_candidate_benifit_value(totalgas, initpos, totalpos = [1000, 1000, 1000, 1000, 1000, 1000, 1000]):
        totalposvalue = 0
        for pos in totalpos:
            totalposvalue = totalposvalue + pos
        return int(totalgas * (initpos / totalposvalue))
        
    @staticmethod
    def add_candidate_node(new_node, init_ont = 5000000, init_ong = 1000, init_pos = 1000, from_node = 0):
        #新加入节点, 并申请候选节点
        API.node().start_nodes([new_node], clear_chain = True, clear_log = True)
        
        (process, response) = API.native().regid_with_publickey(new_node)
        if not process:
            return (process, response)
        (process, response) = API.native().bind_role_function("0700000000000000000000000000000000000000", ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),["registerCandidate"])
        if not process:
            return (process, response)

        (process, response) = API.native().bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES[new_node]["ontid"], encoding = "utf8"))])
        if not process:
            return (process, response)
            
        API.node().transfer_ont(from_node, new_node, init_ont, price = 0)
        API.node().transfer_ong(from_node, new_node, init_ong, price = 0)
        
        #time.sleep(10) 
        
        (process, response) = API.native().register_candidate(Config.NODES[new_node]["pubkey"], Config.NODES[new_node]["address"], str(init_pos), ByteToHex(bytes(Config.NODES[new_node]["ontid"], encoding = "utf8")), "1")
        if not process:
            return (process, response)  
            
        (process, response) = API.native().approve_candidate(Config.NODES[new_node]["pubkey"])       
        return (process, response)

    '''
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
    '''