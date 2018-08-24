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

import utils.connect
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from api.rpc import RPCApi

RPC_API = RPCApi()

class NodeApi:
	def wait_gen_block(self, work = False):
		if not work:
			return True
			
		lastheight = RPC_API.getblockcount()
		times = 0
		while True:
			time.sleep(1)
			times = times + 1
			currentheight = RPC_API.getblockcount()
			if (lastheight != currentheight):
				return True
			if (times > Config.GEN_BLOCK_TIMEOUT):
				return False

	def wait_tx_result(self, txhash):
		for i in range(Config.GEN_BLOCK_TIMEOUT):
			time.sleep(1)
			(ret, response) = RPC_API.getsmartcodeevent(tx_hash=txhash, process_log = False)
			if ret:
				try:
					logger.info("tx hash:" + str(txhash) + " " + json.dumps(response))
					state = response["result"]["State"]
					if state == 1:
						logger.info("tx hash:" + str(txhash) +" state = 1")
						return True
					else:
						return False
				except Exception as e:
					logger.print("tx hash:" + str(txhash) + " no tx state info, may be block not generate yet...")
				continue
			else:
				logger.error("tx hash:" + str(txhash) +" getsmartcodeevent error")
				return False

		logger.error("tx hash:" + str(txhash) + " state timeout!")
		return False

	def get_current_node(self):
		currentip = urllib.request.urlopen('http://ip.42.pl/raw').read()
		if not currentip:
			return None
		currentip = (str(currentip).strip("'b"))
		for node_index in range(len(Config.NODES)):
			node = Config.NODES[node_index] 
			if node["ip"] == currentip:
				return node_index
		return None

	def findSystemNode(self):
		PubKeyList=[]
		PubKeyDict={}
		for i in range(len(Config.NODES)):
			ontid = Config.NODES[i]["ontid"]
			pubkey = Config.NODES[i]["pubkey"]
			PubKeyList.append(pubkey)
			PubKeyDict[pubkey]=i
		test=max(PubKeyList)
		print(test)
		print(PubKeyDict[test])
		return PubKeyDict[test]

	def _check_md5(self, node_list, request):
		md5 = None
		isSame = True
		if node_list:
			for index in node_list:
				ip = Config.NODES[int(index)]["ip"]
				response = utils.connect.con_test_service(ip, request)
				if not response or "result" not in response:
					logger.print("no md5: "+ ip)
					isSame = False
				else:
					logger.print(response["result"] + " [" + ip + "]")
					if not md5:
						md5 = response["result"]
					elif md5 != response["result"]:
						isSame = False
		else:
			isSame = False
		return isSame

	#检查节点服务器State数据库是否一致
	def check_node_state(self, node_list):
		request = {
			"method": "get_states_md5",
			"jsonrpc": "2.0",
			"id": 0,
		}
		return _check_md5(node_list, request)

	def check_node_ledgerevent(self, node_list):
		request = {
			"method": "get_ledgerevent_md5",
			"jsonrpc": "2.0",
			"id": 0,
		}
		return _check_md5(node_list, request)

	def check_node_block(self, node_list):
		request = {
			"method": "get_block_md5",
			"jsonrpc": "2.0",
			"id": 0,
		}
		return _check_md5(node_list, request)

	#检查节点服务器State数据库是否一致
	def check_node_all(self, node_list):
		return (self.check_node_state(node_list) and self.check_node_ledgerevent(node_list) and self.check_node_block(node_list))

	#
	def start_nodes(self, indexs, start_params = Config.DEFAULT_NODE_ARGS, clear_chain = False, clear_log = False, program = "ontology", config = "config.json"):
		for index in indexs:
			self.start_node(index, start_params, clear_chain, clear_log, program, config)
		time.sleep(10)

	def start_node(self, index, start_params = Config.DEFAULT_NODE_ARGS, clear_chain = False, clear_log = False, program = "ontology", config = "config.json"):
		logger.info("start node: " + str(index) + " start_params:" + start_params + " clear_chain:" + str(clear_chain) + " clear_log:" + str(clear_log))
		request = {
			"method": "start_node",
			"jsonrpc": "2.0",
			"id": 0,
			"params" : {
				"clear_chain" : clear_chain,
				"clear_log" : clear_log,
				"name" : program,
				"node_args" : start_params,
				"config" : config
			}
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)
		return response

	def stop_all_nodes(self):
		for node_index in range(len(Config.NODES)):
			self.stop_nodes([node_index])

	def stop_nodes(self, indexs):
		for index in indexs:
			self.stop_node(index)

	def stop_node(self, index):
		logger.info("stop node: " + str(index))
		request = {
			"method": "stop_node",
			"jsonrpc": "2.0",
			"id": 0
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response

	#
	def replace_configs(self, indexs, config = None):
		for index in indexs:
			self.replace_config(index, config)
			
	def replace_config(self, index, config = None):
		if not config:
			config = {
						"SeedList": ["139.219.140.190:20338",
						"139.219.138.144:20338",
						"139.219.128.181:20338",
						"139.219.133.116:20338"],
						"ConsensusType": "vbft",
						"VBFT": {
							"n": 7,
							"c": 2,
							"k": 7,
							"l": 112,
							"block_msg_delay": 10000,
							"hash_msg_delay": 10000,
							"peer_handshake_timeout": 10,
							"max_block_change_view": 200,
							"admin_ont_id": "did:ont:TA5dRCZE8pRcCMPLdF4uUYkT1zynkwCKGW",
							"min_init_stake": 10000,
							"vrf_value": "1c9810aa9822e511d5804a9c4db9dd08497c31087b0daafa34d768a3253441fa20515e2f30f81741102af0ca3cefc4818fef16adb825fbaa8cad78647f3afb590e",
							"vrf_proof": "c57741f934042cb8d8b087b44b161db56fc3ffd4ffb675d36cd09f83935be853d8729f3f5298d12d6fd28d45dde515a4b9d7f67682d182ba5118abf451ff1988",
							"peers": [{
								"index": 1,
								"peerPubkey": "12020258a22a27047610cd58cfc2d02aeda8381dd6f430dc5ddedb854b803271ab69f4",
								"address": "TA5dRCZE8pRcCMPLdF4uUYkT1zynkwCKGW",
								"initPos": 10000
							},
							{
								"index": 2,
								"peerPubkey": "120202d4b6ecc913b7f826055f3d7931657e494d5c45768e6c95ec139a912db03bac67",
								"address": "TA6CtF4hZwqAmXdc6opa4B79fRS17YJjX5",
								"initPos": 10000
							},
							{
								"index": 3,
								"peerPubkey": "12020390c9f71385bf0b21bf4c9feae5693c08b38bab078171c63398c06d174b19a413",
								"address": "TA5Uov3Pp9Ufej17NoV4NcXNZi8zFCAgEP",
								"initPos": 10000
							},
							{
								"index": 4,
								"peerPubkey": "120203483420b24240f9db477fb117d857bc6e537a1486eb803e2e702f7bb353eea481",
								"address": "TA82XAPQXtVzncQMczcY9SVytjb2VuTQy4",
								"initPos": 10000
							},
							{
								"index": 5,
								"peerPubkey": "1202032d9267a8542fcae0c5cca6d97f046a7c6a077e1237ee85aa607e83dbf1ef47ea",
								"address": "TA7TSQ5aJcA8sU5MpqJNyTG1r13AQYLYpR",
								"initPos": 10000
							},
							{
								"index": 6,
								"peerPubkey": "12020388e9f62a0d5c070d67b94bd7ec17957a950f953a401e2a2323f58d72431f3541",
								"address": "TA6HoPXWkxznDi3bSur1YaNaPy6Hr4XhM6",
								"initPos": 10000
							},
							{
								"index": 7,
								"peerPubkey": "120202657eab0d3060e47e7df105d5b2f360e826d2d4f406b99f9bd796f0ad6339bd86",
								"address": "TA8youx3VAU9yBSn5oxLR2V1dSGBkL2epq",
								"initPos": 10000
							}]
						}
					}

		request = {
			"method": "replace_node_config",
			"jsonrpc": "2.0",
			"id": 0,
			"params" : config
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response

	def transfer_ont(self, from_index, to_index, amount, price = 0):
		request = {
			"method": "transfer",
			"jsonrpc": "2.0",
			"id": 0,
			"params" : {
				"from" : Config.NODES[from_index]["address"],
				"to" : Config.NODES[to_index]["address"],
				"amount" : amount,
				"price" : price
			}
		}

		ip = Config.NODES[from_index]["ip"]
		response = utils.connect.con_test_service(ip, request)
		time.sleep(5)
		return response

	def transfer_ong(self, from_index, to_index, amount, price = 0):
		request = {
			"method": "transfer_ong",
			"jsonrpc": "2.0",
			"id": 0,
			"params" : {
				"from" : Config.NODES[from_index]["address"],
				"to" : Config.NODES[to_index]["address"],
				"amount" : amount,
				"price" : price
			}
		}

		ip = Config.NODES[from_index]["ip"]
		response = utils.connect.con_test_service(ip, request)
		time.sleep(5)
		return response

	def withdrawong(self, index):
		request = {
			"method": "withdrawong",
			"jsonrpc": "2.0",
			"id": 0
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response

	def exec_cmd(self, cmd, index):
		request = {
			"method": "exec_cmd",
			"jsonrpc": "2.0",
			"id": 0,
			"params" : {
				"cmd":cmd
			}
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response

	def stop_sigsvr(self, index):
		logger.info("stop sig_server: " + str(index))
		request = {
			"method": "stop_sigsvr",
			"jsonrpc": "2.0",
			"id": 0
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response

	def start_sigsvr(self, wallet, index):
		logger.info("start sig_server: " + str(index))
		request = {
			"method": "start_sigsvr",
			"jsonrpc": "2.0",
			"id": 0,
			"params":{
				"wallet" : wallet
			}
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response

	def stop_test_service(self, index):
		print("stop test_service: " + str(index))
		request = {
			"method": "stop_test_service",
			"jsonrpc": "2.0",
			"id": 0
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response

	def get_version_ontology(self, index=0):
		request = {
			"method": "get_version_ontology",
			"jsonrpc": "2.0",
			"id": 0
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response

	def get_version_wallet(self, index=0):
		request = {
			"method": "get_version_wallet",
			"jsonrpc": "2.0",
			"id": 0
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response

	def get_version_onto_config(self, index=0):
		request = {
			"method": "get_version_onto_config",
			"jsonrpc": "2.0",
			"id": 0
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response

	def get_version_test_config(self, index=0):
		request = {
			"method": "get_version_test_config",
			"jsonrpc": "2.0",
			"id": 0
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response

	def get_version_sigsvr(self, index=0):
		request = {
			"method": "get_version_sigsvr",
			"jsonrpc": "2.0",
			"id": 0
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response

	def get_version_abi(self, index=0):
		request = {
			"method": "get_version_abi",
			"jsonrpc": "2.0",
			"id": 0
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response

	def get_version_test_service(self, index=0):
		request = {
			"method": "get_version_test_service",
			"jsonrpc": "2.0",
			"id": 0
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response

	
	def heart_beat(self, index=0):
		print("getting heart beat...")
		request = {
			"method": "heart_beat",
			"jsonrpc": "2.0",
			"id": 0
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response

	def check_xmode_ontology(self, index=0):
		request = {
			"method": "check_xmode_ontology",
			"jsonrpc": "2.0",
			"id": 0
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response

	def check_xmode_sigsvr(self, index=0):
		request = {
			"method": "check_xmode_sigsvr",
			"jsonrpc": "2.0",
			"id": 0
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response

	def check_xmode_tools(self, index=0):
		request = {
			"method": "check_xmode_tools",
			"jsonrpc": "2.0",
			"id": 0
		}

		ip = Config.NODES[index]["ip"]
		response = utils.connect.con_test_service(ip, request)

		return response
		

	def stop_sigsvrs(self, indexes):
		for index in indexes:
			self.stop_sigsvr(index)


	def start_sigsvrs(self, wallet, indexes):
		for index in indexes:
			self.start_sigsvr(wallet, index)
