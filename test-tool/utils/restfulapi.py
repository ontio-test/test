# -*- coding:utf-8 -*-
import re
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt
import time
import requests
import subprocess

import utils.base
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.commonapi import *

class RestfulApi:
	def getgenerateblocktime(self):
		task = Task(Config.BASEAPI_PATH + "/restful/get_gen_blk_time.json")
		task.set_type("restful")
		return run_single_task(task)

	def getconnectioncount(self):
		task = Task(Config.BASEAPI_PATH + "/restful/get_conn_count.json")
		task.set_type("restful")
		return run_single_task(task)

	def getblocktxsbyheight(self, height):
		task = Task(Config.BASEAPI_PATH + "/restful/get_blk_txs_by_height.json")
		task.set_type("restful")
		taskrequest = task.request()
		taskrequest["api"] = "/api/v1/block/transactions/height/" + str(height)
		task.set_request(taskrequest)
		return run_single_task(task)

	def getblockbyheight(self, height):
		task = Task(Config.BASEAPI_PATH + "/restful/get_blk_by_height.json")
		task.set_type("restful")
		taskrequest = task.request()
		taskrequest["api"] = "/api/v1/block/details/height/" + str(height)
		task.set_request(taskrequest)
		return run_single_task(task)

	def getblockbyhash(self, _hash, raw = 0):
		task = Task(Config.BASEAPI_PATH + "/restful/get_blk_by_hash.json")
		task.set_type("restful")
		taskrequest = task.request()
		taskrequest["api"] = "/api/v1/block/details/hash/" + str(_hash) + "?raw="  + str(raw)
		task.set_request(taskrequest)
		return run_single_task(task)

	def getblockheight(self):
		task = Task(Config.BASEAPI_PATH + "/restful/get_blk_height.json")
		task.set_type("restful")
		return run_single_task(task)

	def getblockhashbyheight(self, height):
		task = Task(Config.BASEAPI_PATH + "/restful/get_blk_hash.json")
		task.set_type("restful")
		taskrequest = task.request()
		taskrequest["api"] = "/api/v1/block/hash/" + str(height)
		task.set_request(taskrequest)
		return run_single_task(task)

	def gettransactionbytxhash(self, _hash, raw = 0):
		task = Task(Config.BASEAPI_PATH + "/restful/get_tx.json")
		task.set_type("restful")
		taskrequest = task.request()
		taskrequest["api"] = "/api/v1/transaction/" + str(_hash) + "?raw=" + str(raw)
		task.set_request(taskrequest)
		return run_single_task(task)

	def postrawtx(self, rawtxdata, action = "sendrawtransaction", version = "1.0.0", pre = 0):
		task = Task(Config.BASEAPI_PATH + "/restful/post_raw_tx.json")
		task.set_type("restful")
		taskrequest = task.request()
		taskrequest["api"] = "/api/v1/transaction?preExec="+ str(pre)
		taskrequest["params"]["Action"] = action
		taskrequest["params"]["Version"] = version
		taskrequest["params"]["Data"] = rawtxdata
		task.set_request(taskrequest)
		return run_single_task(task)

	def getstorage(self, script_hash, key):
		task = Task(Config.BASEAPI_PATH + "/restful/get_storage.json")
		task.set_type("restful")
		taskrequest = task.request()
		taskrequest["api"] = "/api/v1/storage/"+ str(script_hash) + "/" + str(key)
		task.set_request(taskrequest)
		return run_single_task(task)

	def getbalance(self, addr):
		task = Task(Config.BASEAPI_PATH + "/restful/get_balance.json")
		task.set_type("restful")
		taskrequest = task.request()
		taskrequest["api"] = "/api/v1/balance/"+ str(addr)
		task.set_request(taskrequest)
		return run_single_task(task)

	def getcontract(self, script_hash):
		task = Task(Config.BASEAPI_PATH + "/restful/get_contract_state.json")
		task.set_type("restful")
		taskrequest = task.request()
		taskrequest["api"] = "/api/v1/contract/"+ str(script_hash)
		task.set_request(taskrequest)
		return run_single_task(task)

	def getsmartcodeeventbyheight(self, height):
		task = Task(Config.BASEAPI_PATH + "/restful/get_smtcode_evt_txs.json")
		task.set_type("restful")
		taskrequest = task.request()
		taskrequest["api"] = "/api/v1/smartcode/event/transactions/"+ str(height)
		task.set_request(taskrequest)
		return run_single_task(task)

	def getsmartcodeeventbyhash(self, txhash):
		task = Task(Config.BASEAPI_PATH + "/restful/get_smtcode_evts.json")
		task.set_type("restful")
		taskrequest = task.request()
		taskrequest["api"] = "/api/v1/smartcode/event/txhash/"+ str(txhash)
		task.set_request(taskrequest)
		return run_single_task(task)

	def getblockheightbytxhash(self, txhash):
		task = Task(Config.BASEAPI_PATH + "/restful/get_blk_hgt_by_txhash.json")
		task.set_type("restful")
		taskrequest = task.request()
		taskrequest["api"] = "/api/v1/block/height/txhash/"+ str(txhash)
		task.set_request(taskrequest)
		return run_single_task(task)

	def getmerkleproofbytxhash(self, _hash):
		task = Task(Config.BASEAPI_PATH + "/restful/get_merkle_proof.json")
		task.set_type("restful")
		taskrequest = task.request()
		taskrequest["api"] = "/api/v1/merkleproof/"+ str(_hash)
		task.set_request(taskrequest)
		return run_single_task(task)

	def getgasprice(self, _hash):
		task = Task(Config.BASEAPI_PATH + "/restful/get_gasprice.json")
		task.set_type("restful")
		return run_single_task(task)

	def getallowance(self, _hash):
		task = Task(Config.BASEAPI_PATH + "/restful/get_allowance.json")
		task.set_type("restful")
		return run_single_task(task)