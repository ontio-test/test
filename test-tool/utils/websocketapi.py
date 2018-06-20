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

class WebSocketApi:
	def heartbeat(self):
		task = Task(Config.BASEAPI_PATH + "/ws/heartbeat.json")
		task.set_type("ws")
		return run_single_task(task)
		
	def subscribe(self, contractaddrlist, sevent = False, sjsonblock = False, srawblock = False, sblocktxhashs = False):
		task = Task(Config.BASEAPI_PATH + "/ws/subscribe.json")
		task.set_type("ws")
		taskrequest = task.request()
		taskrequest["ConstractsFilter"] = contractaddrlist
		taskrequest["SubscribeEvent"] = sevent
		taskrequest["SubscribeJsonBlock"] = sjsonblock
		taskrequest["SubscribeRawBlock"] = srawblock
		taskrequest["SubscribeBlockTxHashs"] = sblocktxhashs
		task.set_request(taskrequest)
		return run_single_task(task)

	def getgenerateblocktime(self, param = None):
		task = Task(Config.BASEAPI_PATH + "/ws/getgenerateblocktime.json")
		task.set_type("ws")

		if param and isinstance(param, dict):
			taskrequest = task.request()
			for key in param:
				taskrequest[key] = param[key]
			task.set_request(taskrequest)

		return run_single_task(task)

	def getconnectioncount(self, param = None):
		task = Task(Config.BASEAPI_PATH + "/ws/getconnectioncount.json")
		task.set_type("ws")
		if param and isinstance(param, dict):
			taskrequest = task.request()
			for key in param:
				taskrequest[key] = param[key]
			task.set_request(taskrequest)

		return run_single_task(task)

	def getblocktxsbyheight(self, height):
		task = Task(Config.BASEAPI_PATH + "/ws/getconnectioncount.json")
		task.set_type("ws")

		taskrequest = task.request()
		taskrequest["Height"] = height
		task.set_request(taskrequest)
		return run_single_task(task)

	def getblockbyheight(self, height, raw = 0):
		task = Task(Config.BASEAPI_PATH + "/ws/getblockbyheight.json")
		task.set_type("ws")

		taskrequest = task.request()
		taskrequest["Raw"] = raw
		taskrequest["Height"] = height
		task.set_request(taskrequest)
		return run_single_task(task)

	def getblockbyhash(self, _hash, raw = 0):
		task = Task(Config.BASEAPI_PATH + "/ws/getblockbyheight.json")
		task.set_type("ws")

		taskrequest = task.request()
		taskrequest["Raw"] = raw
		taskrequest["Hash"] = _hash
		task.set_request(taskrequest)
		return run_single_task(task)

	def getblockheight(self):
		task = Task(Config.BASEAPI_PATH + "/ws/getblockheight.json")
		task.set_type("ws")

		return run_single_task(task)

	def getblockhashbyheight(self, height):
		task = Task(Config.BASEAPI_PATH + "/ws/getblockhash.json")
		task.set_type("ws")

		taskrequest = task.request()
		taskrequest["Height"] = height
		task.set_request(taskrequest)
		return run_single_task(task)

	def gettransaction(self, _hash, raw = 0):
		task = Task(Config.BASEAPI_PATH + "/ws/gettransaction.json")
		task.set_type("ws")

		taskrequest = task.request()
		taskrequest["Hash"] = _hash
		taskrequest["Raw"] = raw
		task.set_request(taskrequest)
		return run_single_task(task)

	def sendrawtransaction(self, _hex, pre = 0):
		task = Task(Config.BASEAPI_PATH + "/ws/gettransaction.json")
		task.set_type("ws")

		taskrequest = task.request()
		taskrequest["Data"] = _hex
		taskrequest["PreExec"] = pre
		task.set_request(taskrequest)
		return run_single_task(task)

	def getstorage(self, _hex, key):
		task = Task(Config.BASEAPI_PATH + "/ws/gettransaction.json")
		task.set_type("ws")

		taskrequest = task.request()
		taskrequest["Hash"] = _hex
		taskrequest["Key"] = key
		task.set_request(taskrequest)
		return run_single_task(task)

	def getbalancebyaddr(self, addr):
		task = Task(Config.BASEAPI_PATH + "/ws/getbalance.json")
		task.set_type("ws")

		taskrequest = task.request()
		taskrequest["Addr"] = addr
		task.set_request(taskrequest)
		return run_single_task(task)

	def getcontract(self, _hash):
		task = Task(Config.BASEAPI_PATH + "/ws/getcontract.json")
		task.set_type("ws")

		taskrequest = task.request()
		taskrequest["Hash"] = _hash
		task.set_request(taskrequest)
		return run_single_task(task)

	def getsmartcodeeventbyheight(self, height):
		task = Task(Config.BASEAPI_PATH + "/ws/getsmartcodeeventbyheight.json")
		task.set_type("ws")

		taskrequest = task.request()
		taskrequest["Height"] = height
		task.set_request(taskrequest)
		return run_single_task(task)

	def getsmartcodeeventbyhash(self, _hash):
		task = Task(Config.BASEAPI_PATH + "/ws/getsmartcodeeventbyhash.json")
		task.set_type("ws")

		taskrequest = task.request()
		taskrequest["Hash"] = _hash
		task.set_request(taskrequest)
		return run_single_task(task)

	def getblockheightbytxhash(self, _hash):
		task = Task(Config.BASEAPI_PATH + "/ws/getblockheightbytxhash.json")
		task.set_type("ws")

		taskrequest = task.request()
		taskrequest["Hash"] = _hash
		task.set_request(taskrequest)
		return run_single_task(task)

	def getmerkleproof(self, _hash):
		task = Task(Config.BASEAPI_PATH + "/ws/getmerkleproof.json")
		task.set_type("ws")

		taskrequest = task.request()
		taskrequest["Hash"] = _hash
		task.set_request(taskrequest)
		return run_single_task(task)

	def getsessioncount(self):
		task = Task(Config.BASEAPI_PATH + "/ws/getsessioncount.json")
		task.set_type("ws")

		return run_single_task(task)

	def getgasprice(self):
		task = Task(Config.BASEAPI_PATH + "/ws/getgasprice.json")
		task.set_type("ws")

		return run_single_task(task)

	def getallowance(self, asset, _from, to):
		task = Task(Config.BASEAPI_PATH + "/ws/getallowance.json")
		task.set_type("ws")

		taskrequest = task.request()
		taskrequest["Asset"] = asset
		taskrequest["From"] = _from
		taskrequest["To"] = to
		task.set_request(taskrequest)
		return run_single_task(task)