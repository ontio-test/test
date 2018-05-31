# -*- coding:utf-8 -*-
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt
import time

import utils.base
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase

logger = LoggerInstance




def cmp(expect_data, cmp_data):
	if isinstance(expect_data, dict):
		"""若为dict格式"""
		if not cmp_data or not isinstance(cmp_data, dict):
			return False
		for key in expect_data:
			cmp_key = key
			if cmp_key not in cmp_data:
				if cmp_key.capitalize() not in cmp_data:
					return False
				else:
					cmp_key = cmp_key.capitalize()
			if not cmp(expect_data[key], cmp_data[cmp_key]):
				return False
		return True
	elif isinstance(expect_data, list):
		"""若为list格式"""
		if not cmp_data or not isinstance(cmp_data, list):
			return False

		if len(expect_data) > len(cmp_data):
			return False
		for src_list, dst_list in zip(sorted(expect_data), sorted(cmp_data)):
			if not cmp(src_list, dst_list):
				return False
		return True
	else:
		if str(expect_data) != str(cmp_data):
			return False
		else:
			return True

def call_contract(task, judge = True):
	taskdata = task.data()
	if isinstance(taskdata, dict):
		taskdata = [taskdata]

	for task_item in taskdata:
		try:
			#step 1: signed tx
			expect_response = None
			if "RESPONSE" in task_item:
				expect_response = task_item["RESPONSE"]

			logger.print("[-------------------------------]")
			logger.print("[ RUN      ] "+ "contract" + "." + task.name())
			task.set_type("cli")
			(result, response) = run_single_task(task, True, False)
			task.data()["RESPONSE"] = response
			logger.print("[ 1. SIGNED TX ] " + json.dumps(task_item, indent = 4))

			#step 2: call contract
			signed_tx = None
			if not response is None and "result" in response and not response["result"] is None and "signed_tx" in response["result"]:
				signed_tx = response["result"]["signed_tx"]

			if signed_tx == None or signed_tx == '':
				raise Error("no signed tx")

			sendrawtxtask = Task("../utils/baseapi/rpc/sendrawtransaction.json")
			sendrawtxtask.data()["REQUEST"]["params"][0] = signed_tx
			(result, response) = run_single_task(sendrawtxtask, True, False)

			sendrawtxtask.data()["RESPONSE"] = response
			sendrawtxtask.data()["EXPECT RESPONSE"] = expect_response

			if not response is None and ("result" in response and "Result" in response["result"]):
				response["result"]["Result String"] = HexToByte(response["result"]["Result"]).decode('iso-8859-1')
			
			logger.print("[ 2. CALL CONTRACT ] " + json.dumps(sendrawtxtask.data(), indent = 4))

			if response is None or "error" not in response or str(response["error"]) != '0':
				raise Error("call contract error")

			if judge and expect_response:
				result = cmp(expect_response, response)
				if not result:
					raise Error("not except result")

			return (result, response)

		except Error as err:
			return (False, err.msg)

def run_single_task(task, need_judge = True, process_log = True):
	connecttype = task.type()
	name = task.name()
	start_time = time.time()

	if process_log:
		logger.print("[-------------------------------]")
		logger.print("[ RUN      ] "+ connecttype + "." + name)
	cfg_content = task.data()
	cfg_request = cfg_content["REQUEST"]
	cfg_response = cfg_content["RESPONSE"]
	if process_log:
		logger.print("[ PARAMS   ]" + json.dumps(cfg_content, indent = 4))

	#(result, response) = self.multithread_run(logger, cfg_request, cfg_response)
	node_index = cfg_content["node_index"] if "node_index" in cfg_content else None
	node_ip = None
	if node_index:
		node_ip = Config.SERVICES[int(node_index)]

	response = utils.base.con(connecttype, node_ip, cfg_request)
	if process_log:
		logger.print("[ RESULT   ]" + json.dumps(response, indent = 4))

	end_time = time.time()
	time_consumed = (end_time - start_time) * 1000
	
	result = True
	if need_judge:
		result = cmp(cfg_response, response)
		if process_log:
			if result:
				logger.print("[ OK       ] " + connecttype + "."+ name +" (%d ms)" % (time_consumed))
			else:
				logger.print("[ Failed   ] " + connecttype + "."+ name +" (%d ms)"% (time_consumed))
			logger.print("[-------------------------------]")
			logger.print("")
	return (result, response)

#run task1 and task2, compare task1's result and task2's result 
def run_pair_task(task1, task2, compare_src_key = None, compare_dist_key = None):
	result = True

	(result1, response1) = run_single_task(task1)
	if not result1:
		return result1

	(result2, response2) = run_single_task(task2)
	if not result2:
		return result2

	compare_src_data = response1
	if compare_src_key:
		compare_src_keys = compare_src_key.split('/')
		for key in compare_src_keys:
			if compare_src_data:
				compare_src_data = compare_src_data[key]
			else:
				break

		####split dist key
		compare_dist_data = response2
		if compare_dist_key:
			compare_dist_keys = compare_dist_key.split('/')
			for key in compare_dist_keys:
				if compare_dist_data:
					compare_dist_data = compare_dist_data[key]
				else:
					break
		result = cmp(compare_src_data, compare_dist_data)
	else:
		result = True

	return result

