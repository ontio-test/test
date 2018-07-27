
# -*- coding: utf-8 -*-
import sys, os

sys.path.append('..')
sys.path.append('../..')

from utils.taskdata import TaskData, Task
from api.apimanager import API

def get_signed_data():
	request = {
		"REQUEST": {
		"Qid":"t",
		"Method":"signativeinvoketx",
		"Params":{
				"gas_price":0,
				"gas_limit":1000000000,
				"address":"0100000000000000000000000000000000000000",
				"method":"name",
				"version":0,
				"params":[]
			}
		},
		"RESPONSE": {
		}
	}
	return API.contract().sign_transction(Task(name="get_signed_data", ijson=request))[1]["result"]["signed_tx"]
