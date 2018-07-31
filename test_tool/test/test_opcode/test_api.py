# -*- coding:utf-8 -*-
import os
import sys

sys.path.append('..')
sys.path.append('../..')

from utils.taskdata import TaskData, Task
from utils.hexstring import *

from api.apimanager import API

def invoke_function_opCode(contract_address, function_str, param_1, param_2, sleep=0):
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
                                "type": "int",
                                "value": param_1
                            },
                            {
                                "type": "int",
                                "value": param_2
                            }
                        ]
                    }
                ]
            }
        },
        "RESPONSE":{"error" : 0}
    }
    return API.contract().call_contract(Task(name="invoke_function_opCode", ijson=request), twice = True, sleep=sleep)