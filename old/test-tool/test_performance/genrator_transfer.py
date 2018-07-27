# -*- coding:utf-8 -*-
import re
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys
import getopt
import time
import requests
import subprocess
import copy

sys.path.append('..')

import utils.base
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.commonapi import *


sign_transction_transfer = {
    "NODE_INDEX" : 1,
    "REQUEST": {
        "Qid": "t",
        "Method": "signeovminvoketx",
        "Params": {
            "gas_price": 0,
            "gas_limit": 1000000000,
            "address": "80559e902873c5d157c4ba44f1f138f295bb2dae",
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
                            "value": "24b453d1388732a9d78228b572e05f7a082b90a9"
                        },
                        {
                            "type": "bytearray",
                            "value": "922fef396b3b3bb26600dc9caf27be5b16bc5e0f"
                        },
                        {
                            "type": "int",
                            "value": "222"
                        }
                    ]
                }
            ]
        }
    },
    "RESPONSE": {}
}

def genrator_transfer_sintx():
    contrastaddress = deploy_contract("transfer.neo")

    sign_transction_transfer["REQUEST"]["Params"]["address"] = contrastaddress

    index = 1
    sign_transction_transfertmp = copy.copy(sign_transction_transfer)
    nodeaddress = Config.NODES[index]["address"]
    sign_transction_transfertmp["NODE_INDEX"] = index
    sign_transction_transfertmp["REQUEST"]["Params"]["params"][1]["value"][0]["value"] = script_hash_bl_reserver(base58_to_address(nodeaddress))
    sign_transction_transfertmp["REQUEST"]["Params"]["params"][1]["value"][1]["value"] = script_hash_bl_reserver(base58_to_address(nodeaddress))
    sign_transction_transfertmp["REQUEST"]["Params"]["params"][1]["value"][2]["value"] = "1000"  
    (result, response) = sign_transction(Task(ijson = sign_transction_transfertmp), False, False)
    print(json.dumps(response))
	
    call_signed_contract(response["result"]["signed_tx"], pre=True)
    call_signed_contract(response["result"]["signed_tx"], pre=False)
	
	

####################################################
if __name__ == '__main__':
    genrator_transfer_sintx()
