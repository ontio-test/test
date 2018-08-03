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
sys.path.append('../..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.hexstring import *
from utils.error import Error
from api.apimanager import API

class test_api():
    @staticmethod
    def get_block_with_no_tx(contract_address):
        print("seeking block with no transaction......")
        block_count = API.rpc().getblockcount()[1]["result"]
        for i in range(block_count):
            (result, response) = test_api.invoke_func_with_1_param(contract_address, "GetBlockTransactionCount", "int", str(i), sleep = 0)
            print("---------", response)
            if response["result"]["Result"] == "00":
                print("block with no transaction :", str(i))
                return i
            time.sleep(1)

        return None
        
    @staticmethod
    def native_transfer_ont(pay_address,get_address,amount, node_index = 0,errorcode=0):
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
    	return API.contract().call_contract(Task(name="transfer", ijson=request), twice = True)

    @staticmethod
    def get_height(contract_address, node_index = None):
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
                            "value": "GetHeight"
                        },
                        {
                            "type": "array",
                            "value": [{
                                "type": "string",
                                "value": ""
                            }]
                        }
                    ]
                }
            },
            "RESPONSE": {}
        }
        
        return API.contract().call_contract(Task(name="GetHeight", ijson=request), twice = True)

    @staticmethod
    def get_header(contract_address, height, node_index = None):
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
                            "value": "GetHeader"
                        },
                        {
                            "type": "array",
                            "value": [{
                                "type": "int",
                                "value": height
                            }]
                        }
                    ]
                }
            },
            "RESPONSE": {}
        }
        
        return API.contract().call_contract(Task(name="GetHeader", ijson=request), twice = True)

    @staticmethod
    def get_block(contract_address, block_hash, node_index = None):
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
                            "value": "GetBlock"
                        },
                        {
                            "type": "array",
                            "value": [{
                                "type": "bytearray",
                                "value": block_hash
                            }]
                        }
                    ]
                }
            },
            "RESPONSE": {}
        }
        
        return API.contract().call_contract(Task(name="GetBlock", ijson=request), twice = True)

    @staticmethod
    def get_transaction(contract_address, tx_hash, node_index = None):
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
                            "value": "GetTransaction"
                        },
                        {
                            "type": "array",
                            "value": [{
                                "type": "bytearray",
                                "value": tx_hash
                            }]
                        }
                    ]
                }
            },
            "RESPONSE": {}
        }
        
        return API.contract().call_contract(Task(name="GetTransaction", ijson=request), twice = True)

    @staticmethod
    def get_contract(contract_address, script_hash, node_index = None):
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
                            "value": "GetContract"
                        },
                        {
                            "type": "array",
                            "value": [{
                                "type": "bytearray",
                                "value": script_hash
                            }]
                        }
                    ]
                }
            },
            "RESPONSE": {}
        }
        
        return API.contract().call_contract(Task(name="GetContract", ijson=request), twice = True)

    @staticmethod
    def invoke_contract_create(contract_address, script_hash, name, version, author, email, desc, node_index = None):
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
                            "value": "GetContract_Create"
                        },
                        {
                            "type": "array",
                            "value": [
                                {
                                    "type": "bytearray",
                                    "value": script_hash
                                },
                                {
                                    "type": "bool",
                                    "value": "true"
                                },
                                {
                                    "type": "string",
                                    "value": name
                                },
                                {
                                    "type": "string",
                                    "value": version
                                },
                                {
                                    "type": "string",
                                    "value": author
                                },
                                {
                                    "type": "string",
                                    "value": email
                                },
                                {
                                    "type": "string",
                                    "value": desc
                                }
                            ]
                        }
                    ]
                }
            },
            "RESPONSE": {}
        }
            
        return API.contract().call_contract(Task(name="GetContract_Create", ijson=request), twice = True)


    @staticmethod
    def invoke_contract_migrate(contract_address, script_hash, name, version, author, email, desc, node_index = None, sleep = 5):
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
                            "value": "GetContract_Migrate"
                        },
                        {
                            "type": "array",
                            "value": [
                                {
                                    "type": "bytearray",
                                    "value": script_hash
                                },
                                {
                                    "type": "bool",
                                    "value": "true"
                                },
                                {
                                    "type": "string",
                                    "value": name
                                },
                                {
                                    "type": "string",
                                    "value": version
                                },
                                {
                                    "type": "string",
                                    "value": author
                                },
                                {
                                    "type": "string",
                                    "value": email
                                },
                                {
                                    "type": "string",
                                    "value": desc
                                }
                            ]
                        }
                    ]
                }
            },
            "RESPONSE": {}
        }
            
        return API.contract().call_contract(Task(name="GetContract_Migrate", ijson=request), twice = True, sleep = sleep)


    @staticmethod
    def invoke_func_with_1_param(contract_address, func_name, param_type, param_value, node_index = None, twice=True, sleep =5):
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
                            "value": func_name
                        },
                        {
                            "type": "array",
                            "value": [{
                                "type": param_type,
                                "value": param_value
                            }]
                        }
                    ]
                }
            },
            "RESPONSE": {}
        }
        
        return API.contract().call_contract(Task(name=func_name, ijson=request), twice = twice, sleep = sleep)

    @staticmethod
    def invoke_func_with_0_param(contract_address, func_name, node_index = None):
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
                            "value": func_name
                        },
                        {
                            "type": "array",
                            "value": [{
                                "type": "string",
                                "value": ""
                            }]
                        }
                    ]
                }
            },
            "RESPONSE": {}
        }
        
        return API.contract().call_contract(Task(name=func_name, ijson=request), twice = True)

    @staticmethod
    def invoke_func_with_2_param(contract_address, func_name, param_type_1, param_value_1, param_type_2, param_value_2, node_index = None):
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
                            "value": func_name
                        },
                        {
                            "type": "array",
                            "value": [
                                {
                                    "type": param_type_1,
                                    "value": param_value_1
                                },
                                {
                                    "type": param_type_2,
                                    "value": param_value_2
                                }
                            ]
                        }
                    ]
                }
            },
            "RESPONSE": {}
        }
        
        return API.contract().call_contract(Task(name=func_name, ijson=request), twice = True)


    @staticmethod
    def invoke_storage_get(contract_address, node_index = None):
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
                            "value": "Get_93"
                        },
                        {
                            "type": "array",
                            "value": [
                                {
                                    "type": "bytearray",
                                    "value": "313131"
                                },
                                {
                                    "type": "bytearray",
                                    "value": "313131"
                                },
                                {
                                    "type": "bytearray",
                                    "value": "3838383838"
                                }
                            ]
                        }
                    ]
                }
            },
            "RESPONSE": {}
        }
        
        return API.contract().call_contract(Task(name="Get_Storage", ijson=request), twice = True)

    @staticmethod
    def invoke_storage_put(contract_address, node_index = None):
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
                            "value": "Put_107"
                        },
                        {
                            "type": "array",
                            "value": [
                                {
                                    "type": "bytearray",
                                    "value": "313131"
                                },
                                {
                                    "type": "bytearray",
                                    "value": "313131"
                                },
                                {
                                    "type": "bytearray",
                                    "value": "3838383838"
                                }
                            ]
                        }
                    ]
                }
            },
            "RESPONSE": {}
        }
        
        return API.contract().call_contract(Task(name="Put_Storage", ijson=request), twice = True)


