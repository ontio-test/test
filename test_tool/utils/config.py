# -*- coding: utf-8 -*-
import json
import os
from utils.hexstring import *

class Config():
	realdir = os.path.dirname(os.path.realpath(__file__))
	UTILS_PATH = realdir
	UTILS_PATH = UTILS_PATH.replace("\\\\", "/")
	UTILS_PATH = UTILS_PATH.replace("\\", "/")
	ROOT_PATH = UTILS_PATH.replace("/utils", "")
	print(ROOT_PATH)
	cfg_file = open(ROOT_PATH + "/config.json", "rb")
	cfg_json = json.loads(cfg_file.read().decode("utf-8"))
	cfg_file.close()

	#ERRCODE
	'''
	ONT_ERR_CODE = {
        0 : "SUCCESS",
	    41001 : "SESSION_EXPIRED: invalided or expired session",
	    41002 : "SERVICE_CEILING: reach service limit",
	    41003 : "ILLEGAL_DATAFORMAT: illegal dataformat",
	    41004 : "INVALID_VERSION: invalid version",
	    42001 : "INVALID_METHOD: invalid method",
	    42002 : "INVALID_PARAMS: invalid params",
	    43001 : "INVALID_TRANSACTION: invalid transaction",
	    43002 : "INVALID_ASSET: invalid asset",
	    43003 : "INVALID_BLOCK: invalid block",
	    44001 : "UNKNOWN_TRANSACTION: unknown transaction",
	    44002 : "UNKNOWN_ASSET: unknown asset",
	    44003 : "UNKNOWN_BLOCK: unknown block",
	    45001 : "INTERNAL_ERROR: internel error",
	    47001 : "SMARTCODE_ERROR: smartcode error"
	}
	'''
	ERR_CODE = {
        0 : "SUCCESS",
	    54001 : "ONT_RPC_ERROR: Connect Error",
	    54002 : "ONT_RESTFUL_ERROR: Connect Error",
	    54003 : "ONT_WEBSOCKET_ERROR: Connect Error",
	    54004 : "ONT_CLI_ERROR: Connect Error",
	    54005 : "TEST_SERVICE_ERROR: Connect Error",
	    54006 : "GEN_BLOCK_TIMEOUT: can not generate block"
	}

	TOOLS_PATH = ROOT_PATH + "/" + "tools"
	UTILS_PATH = ROOT_PATH + "/" + "utils"
	TESTS_PATH = ROOT_PATH + "/" + "test"
	RESOURCE_PATH = ROOT_PATH + "/resource"
	WALLET_PATH = RESOURCE_PATH + "/wallet"
	BASEAPI_PATH = ROOT_PATH + "/api/requests"
	NODE_PATH = cfg_json["NODE_PATH"]
	LOG_PATH = ROOT_PATH + "/logs"
	THREAD = 1

	TEST_SERVICE_PORT = 23635
	#init nodes
	NODES = cfg_json["NODES"]
	for node_index in range(len(NODES)):
		#str_node_index = "0" + str(node_index) if node_index < 10 else str(node_index)
		walletfile = NODES[node_index]["wallet"]
		cfg_file = open(WALLET_PATH + "/" + walletfile, "rb")
		walletdata = json.loads(cfg_file.read().decode("utf-8"))
		accounts = walletdata["accounts"]
		for account in accounts:
			if account["isDefault"] == True:
				NODES[node_index]["address"] = account["address"]
				NODES[node_index]["ontid"] = "did:ont:" + account["address"]
				NODES[node_index]["pubkey"] = account["publicKey"]
				break
		cfg_file.close()

	DEFAULT_GAS_PRICE = 0
	DEFAULT_GAS_LIMIT = 1000000000

	RPC_HEADERS = {'content-type': 'application/json'}
	#RPC CONFIG
	RPC_URL = cfg_json["RPC_URL"]

	#Restful CONFIG
	RESTFUL_URL = cfg_json["RESTFUL_URL"]
	
	#WebSocket CONFIG
	WS_URL = cfg_json["WS_URL"]

	#CLIRPC_URL CONFIG
	CLIRPC_URL = cfg_json["CLIRPC_URL"]

	DEFAULT_NODE_ARGS = cfg_json["DEFAULT_NODE_ARGS"]

	MULTI_SIGNED_ADDRESS = cfg_json["MULTI_SIGNED_ADDRESS"]
	
	INIT_AMOUNT_ONG = cfg_json["INIT_AMOUNT_ONG"]

	GEN_BLOCK_TIMEOUT = 40
	
#####################################################################################
	ontid_map = {}
	node_Admin = 0
	ontID_Admin = ByteToHex(bytes(NODES[node_Admin]["ontid"], encoding = "utf8")) if node_Admin < len(NODES) else ""
 
	node_A = 1
	ontID_A = ByteToHex(bytes(NODES[node_A]["ontid"], encoding = "utf8")) if node_A < len(NODES) else ""

	node_B = 2
	ontID_B = ByteToHex(bytes(NODES[node_B]["ontid"], encoding = "utf8")) if node_B < len(NODES) else ""

	node_C = 3
	ontID_C = ByteToHex(bytes(NODES[node_C]["ontid"], encoding = "utf8")) if node_C < len(NODES) else ""

	node_D = 4
	ontID_D = ByteToHex(bytes(NODES[node_D]["ontid"], encoding = "utf8")) if node_D < len(NODES) else ""

	node_E = 5
	ontID_E = ByteToHex(bytes(NODES[node_E]["ontid"], encoding = "utf8")) if node_E < len(NODES) else ""

	node_F = 6
	ontID_F = ByteToHex(bytes(NODES[node_F]["ontid"], encoding = "utf8")) if node_F < len(NODES) else ""

	node_G = 7
	ontID_G = ByteToHex(bytes(NODES[node_G]["ontid"], encoding = "utf8")) if node_G < len(NODES) else ""
	
	node_H = 8
	ontID_H = ByteToHex(bytes(NODES[node_H]["ontid"], encoding = "utf8")) if node_H < len(NODES) else ""
	
	node_index = 0
	for node in NODES:
		ontid_map[ByteToHex(bytes(node["ontid"], encoding = "utf8"))] = node_index
		node_index = node_index + 1
 
	roleA_hex = ByteToHex(b"roleA")
	roleB_hex = ByteToHex(b"roleB")    
	roleC_hex = ByteToHex(b"roleC")

	AdminNum = 5
	AdminPublicKeyList = [NODES[0]["pubkey"],NODES[1]["pubkey"],NODES[2]["pubkey"],NODES[3]["pubkey"],NODES[4]["pubkey"],NODES[5]["pubkey"],NODES[6]["pubkey"]]