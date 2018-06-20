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

def regIDWithPublicKey(node_index):
	ontid = Config.SERVICES[int(node_index)]["ontid"]
	pubkey = Config.SERVICES[int(node_index)]["pubkey"]
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
		"RESPONSE": {
		  "error":0
		}
	}
	request["NODE_INDEX"] = node_index
	return call_contract(Task(name ="regIDWithPublicKey", ijson=request), twice = True)