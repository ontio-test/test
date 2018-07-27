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
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase

from api.apimanager import API
    
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
    
    return API.contract().call_contract(Task(name="init_admin", ijson=request), twice = True)


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
        
    return API.contract().call_contract(Task(name="invoke_function", ijson=request), twice = True)


