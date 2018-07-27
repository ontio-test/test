# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt
import time
sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.contractapi import *
from test_api import *
from test_ontid_config import *
from utils.commonapi import call_contract

logger = LoggerInstance
contract_address = deploy_contract("ontid.json")
####################################################
#test cases
class TestContract(ParametrizedTestCase):
	def start(self, log_path):
		logger.open(log_path)

	def finish(self, task_name, log_path, result, msg):
		if result:
			logger.print("[ OK       ] ")
			logger.append_record(task_name, "pass", log_path)
		else:
			logger.print("[ Failed   ] " + msg)
			logger.append_record(task_name, "fail", log_path)
		logger.close()

	def test_128_regIDWithPublicKey(self):
		log_path = "128_regIDWithPublicKey.log"
		task_name = "128_regIDWithPublicKey.log"
		functionName="regIDWithPublicKey"
		params=[{
					"type" : "string",
					"value" : "did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab"
				},{
					"type" : "bytearray",
					"value" : node_now_pubkey
				}]
		
		self.start(log_path)
		
		(result, response) = forNeo(contract_address,functionName,params,public_key, node_index)
		self.finish(task_name, log_path, result,  "")


	def test_129_addKey(self):
		log_path = "129_addKey.log"
		task_name = "129_addKey.log"
		functionName="addKey"
		params=[{
					"type" : "string",
					"value" : "did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab"
				},{
					"type" : "bytearray",
					"value" : "0200a7eaadc780320547566c6d9e671638f8fba3a9d929422b245ff432eef9a8f2"
				},{
					"type" : "bytearray",
					"value" : node_now_pubkey
				}]
		
		self.start(log_path)
		
		(result, response) = forNeo(contract_address,functionName,params,public_key, node_index)
		self.finish(task_name, log_path, result,  "")


	def test_130_removeKey(self):
		log_path = "130_removeKey.log"
		task_name = "130_removeKey.log"
		functionName="removeKey"
		params=[{
					"type" : "string",
					"value" : "did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab"
				},{
					"type" : "bytearray",
					"value" : "0200a7eaadc780320547566c6d9e671638f8fba3a9d929422b245ff432eef9a8f2"
				},{
					"type" : "bytearray",
					"value" : node_now_pubkey
				}]
		
		self.start(log_path)
		
		(result, response) = forNeo(contract_address,functionName,params,public_key, node_index)
		self.finish(task_name, log_path, result,  "")


	def test_131_addRecovery(self):
		log_path = "131_addRecovery.log"
		task_name = "131_addRecovery.log"
		functionName="addRecovery"
		params=[{
					"type" : "string",
					"value" : "did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab"
				},{
					"type" : "bytearray",
					"value" : recoveryaddress
				},{
					"type" : "bytearray",
					"value" : node_now_pubkey
				}]
		
		self.start(log_path)
		
		(result, response) = forNeo(contract_address,functionName,params,public_key, node_index)
		self.finish(task_name, log_path, result,  "")


	def test_132_changeRecovery(self):
		log_path = "132_changeRecovery.log"
		task_name = "132_changeRecovery.log"
		functionName="changeRecovery"
		params=[{
					"type" : "string",
					"value" : "did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab"
				},{
					"type" : "bytearray",
					"value" : new_recovery_address
				},{
					"type" : "bytearray",
					"value" : old_recovery_address
				}]
		
		self.start(log_path)
		
		(result, response) = forNeo(contract_address,functionName,params,public_key, node_index, recovery_address_Array = recoveryaddress_Array)
		self.finish(task_name, log_path, result,  "")


	def test_133_regIDWithAttributes(self):
		log_path = "133_regIDWithAttributes.log"
		task_name = "133_regIDWithAttributes.log"
		functionName="regIDWithAttributes"
		params2=[{
					"type":"struct",
					"value":[
					{"type":"bytearray","value" : ByteToHex(b"test_133_regIDWithAttributes")},
					{"type":"bytearray","value" : ByteToHex(b"string")},
					{"type":"bytearray","value" : ByteToHex(b"test_133_regIDWithAttributesvalue")}]
					}
				]
		params=[{
					"type" : "string",
					"value" : "did:ont:ANo7eNzVcFZ8a2bywcsMqCf42FTiU5a4An"
				},
				{
					"type" : "bytearray",
					"value" : node_now_pubkey
				},
				{
					"type" : "array",
					"value" :params2
				}
				]
		
		self.start(log_path)
		
		(result, response) = forNeo(contract_address,functionName,params,public_key, node_index)
		self.finish(task_name, log_path, result,  "")


	def test_134_addAttributes(self):
		log_path = "134_addAttributes.log"
		task_name = "134_addAttributes.log"
		functionName="addAttributes"
		params2=[{
					"type":"struct",
					"value":[
					{"type":"bytearray","value" : ByteToHex(b"test_134_addAttributes")},
					{"type":"bytearray","value" : ByteToHex(b"string")},
					{"type":"bytearray","value" : ByteToHex(b"test_134_addAttributesvalue")}]
					}
				]
		params=[{
					"type" : "string",
					"value" : "did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab"
				},
				{
					"type" : "array",
					"value" :params2
				},
				{
					"type" : "bytearray",
					"value" : node_now_pubkey
				}
				]
		
		self.start(log_path)
		
		(result, response) = forNeo(contract_address,functionName,params,public_key, node_index)
		self.finish(task_name, log_path, result,  "")


	def test_135_removeAttribute(self):
		log_path = "135_removeAttribute.log"
		task_name = "135_removeAttribute.log"
		functionName="removeAttribute"
		params=[{
					"type" : "string",
					"value" : "did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab"
				},
				{
					"type" : "bytearray",
					"value" :ByteToHex(b"addAttributes_74")
				},
				{
					"type" : "bytearray",
					"value" : node_now_pubkey
				}
				]
		
		self.start(log_path)
		(result, response) = addAttributes("did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab", addAttributes_74,public_key,node_index,0)#先加
		(result, response) = forNeo(contract_address,functionName,params,public_key, node_index)
		self.finish(task_name, log_path, result,  "")


	def test_136_getPublicKeys(self):
		log_path = "136_getPublicKeys.log"
		task_name = "136_getPublicKeys.log"
		functionName="getPublicKeys"
		params=[{
					"type" : "string",
					"value" : "did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab"
				}
				]
		
		self.start(log_path)
		
		(result, response) = forNeo(contract_address,functionName,params,public_key, node_index)
		self.finish(task_name, log_path, result,  "")


	def test_137_getKeyState(self):
		log_path = "137_getKeyState.log"
		task_name = "137_getKeyState.log"
		functionName="getKeyState"
		params=[{
					"type" : "string",
					"value" : "did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab"
				},
				{
					"type" : "int",
					"value" : "1"
				}
				]
		
		self.start(log_path)
		
		(result, response) = forNeo(contract_address,functionName,params,public_key, node_index)
		self.finish(task_name, log_path, result,  "")



	def test_138_getAttributes(self):
		log_path = "138_getAttributes.log"
		task_name = "138_getAttributes.log"
		functionName="getAttributes"
		params=[{
					"type" : "string",
					"value" : "did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab"
				}
				]
		
		self.start(log_path)
		(result, response) = addAttributes("did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab", addAttributes_74,public_key,node_index,0)#先加
		(result, response) = forNeo(contract_address,functionName,params,public_key, node_index)
		self.finish(task_name, log_path, result,  "")


	def test_139_getDDO(self):
		log_path = "139_getDDO.log"
		task_name = "139_getDDO.log"
		functionName="getDDO"
		params=[{
					"type" : "string",
					"value" : "did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab"
				}
				]
		
		self.start(log_path)
		
		(result, response) = forNeo(contract_address,functionName,params,public_key, node_index)
		self.finish(task_name, log_path, result,  "")


	def test_140_verifySignature(self):
		log_path = "140_verifySignature.log"
		task_name = "140_verifySignature.log"
		functionName="verifySignature"
		params=[{
					"type" : "string",
					"value" : "did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab"
				},
				{
					"type" : "int",
					"value" : "1"
				}
				]
		
		self.start(log_path)
		
		(result, response) = forNeo(contract_address,functionName,params,public_key, node_index)
		self.finish(task_name, log_path, result,  "")
####################################################
if __name__ == '__main__':
	unittest.main()

