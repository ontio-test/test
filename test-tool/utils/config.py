# -*- coding: utf-8 -*-
import json

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
	SERVICES = cfg_json["NODES"]

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