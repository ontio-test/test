# -*- coding: utf-8 -*-
import sys
import os

sys.path.append('..')
sys.path.append('../..')

from utils.config import Config
from api.apimanager import API

class test_config():
	testpath = os.path.dirname(os.path.realpath(__file__))
	node_index = API.node().get_current_node()   ###7-25暂时不存在
	address=Config.NODES[node_index]["address"]
	cost1 = testpath + "/resource/cost_1.json"
	filterfile = testpath + "/resource/004.json"

	task004 = {
		    "DEPLOY" : True,
			"CODE_PATH" : testpath + "/resource/366780.json", 
			"REQUEST": {
		        "Qid": "t",
		        "Method": "signeovminvoketx",
		        "Params": {
		            "gas_price": 10,
		            "gas_limit": 1000000000,
		            "address": "6408c4cc6c55700e96c38db184f3c1de8a260b02",
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
		                            "value": "ad933c4478a8e6ce6804f373c536ebfdb2d5d730"
		                        },
		                        {
		                            "type": "bytearray",
		                            "value": "ad933c4478a8e6ce6804f373c536ebfdb2d5d730"
		                        },
		                        {
		                            "type": "int",
		                            "value": "10"
		                        }
		                    ]
		                }
		            ]
		        }
		    },
		    "RESPONSE": {}
		}