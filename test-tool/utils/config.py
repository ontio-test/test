# -*- coding: utf-8 -*-
import json

from utils.hexstring import *

class Config():
	cfg_file = open("../config.json", "rb")
	cfg_json = json.loads(cfg_file.read().decode("utf-8"))
	cfg_file.close()

	#ERRCODE
	ERR_CODE = {
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

	THREAD = 1

	TEST_SERVICE_PORT = 23635
	NODES = cfg_json["NODES"]

	RPC_HEADERS = {'content-type': 'application/json'}
	#RPC CONFIG
	RPC_URL = cfg_json["RPC_URL"]

	#Restful CONFIG
	RESTFUL_URL = cfg_json["RESTFUL_URL"]
	
	#WebSocket CONFIG
	WS_URL = cfg_json["WS_URL"]

	#CLIRPC_URL CONFIG
	CLIRPC_URL = cfg_json["CLIRPC_URL"]

	ROOT_PATH = cfg_json["ROOT_PATH"]

	TOOLS_PATH = ROOT_PATH + "/" + "tools"

	UTILS_PATH = ROOT_PATH + "/" + "utils"

	BASEAPI_PATH = UTILS_PATH + "/baseapi"

	DEFAULT_NODE_ARGS = "--ws --rest --loglevel=0 --enableconsensus --networkid=299"

	MULTI_SIGNED_ADDRESS = cfg_json["MULTI_SIGNED_ADDRESS"]
	
	INIT_AMOUNT_ONG = cfg_json["INIT_AMOUNT_ONG"]
	
#####################################################################################
	ontid_map = {}
	node_Admin = 0
	ontID_Admin = ByteToHex(bytes(NODES[node_Admin]["ontid"], encoding = "utf8"))
 
	node_A = 1
	ontID_A = ByteToHex(bytes(NODES[node_A]["ontid"], encoding = "utf8"))

	node_B = 2
	ontID_B = ByteToHex(bytes(NODES[node_B]["ontid"], encoding = "utf8"))

	node_C = 3
	ontID_C = ByteToHex(bytes(NODES[node_C]["ontid"], encoding = "utf8"))

	node_D = 4
	ontID_D = ByteToHex(bytes(NODES[node_D]["ontid"], encoding = "utf8"))

	node_E = 5
	ontID_E = ByteToHex(bytes(NODES[node_E]["ontid"], encoding = "utf8"))

	node_F = 6
	ontID_F = ByteToHex(bytes(NODES[node_F]["ontid"], encoding = "utf8"))

	node_G = 7
	ontID_G = ByteToHex(bytes(NODES[node_G]["ontid"], encoding = "utf8"))
	
	node_H = 8
	ontID_H = ByteToHex(bytes(NODES[node_H]["ontid"], encoding = "utf8"))
	
	node_index = 0
	for node in NODES:
		ontid_map[ByteToHex(bytes(node["ontid"], encoding = "utf8"))] = node_index
		node_index = node_index + 1
 
	roleA_hex = ByteToHex(b"roleA")
	roleB_hex = ByteToHex(b"roleB")    
	roleC_hex = ByteToHex(b"roleC")
