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
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.api.contractapi import *
from test_api import *
from test_config import *
from utils.api.commonapi import call_contract

####################################################
#test cases
class test_ontid_api_1(ParametrizedTestCase):

	def setUp(self):
		logger.open( self._testMethodName+".log",self._testMethodName)
		
	def tearDown(self):
		logger.close(self.result())
		pass


	def test_base_128_regIDWithPublicKey(self):	
		try:
			functionName="regIDWithPublicKey"
			params=[{
					"type" : "string",
					"value" : "did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab"
				},{
					"type" : "bytearray",
					"value" : node_now_pubkey
				}]
			(process, response) = forNeo(test_config.contract_address,functionName,params,test_config.public_key, test_config.node_index)
			ASSERT(process, "")
		except:
			pass


	def test_base_129_addKey(self):	
		try:
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
			(process, response) = forNeo(test_config.contract_address,functionName,params,test_config.public_key, test_config.node_index)
			ASSERT(process, "")
		except:
			pass


	def test_base_130_removeKey(self):
		try:
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
			(process, response) = forNeo(test_config.contract_address,functionName,params,test_config.public_key, test_config.node_index)
			ASSERT(process, "")
		except:
			pass


	def test_base_131_addRecovery(self):
		try:
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
			(process, response) = forNeo(test_config.contract_address,functionName,params,test_config.public_key, test_config.node_index)
			ASSERT(process, "")
		except:
			pass


	def test_base_132_changeRecovery(self):
		try:
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
			(process, response) = forNeo(test_config.contract_address,functionName,params,test_config.public_key, test_config.node_index, recovery_address_Array = test_config.recoveryaddress_Array)
			ASSERT(process, "")
		except:
			pass


	def test_base_133_regIDWithAttributes(self):
		
		try:
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
			(process, response) = forNeo(test_config.contract_address,functionName,params,test_config.public_key, test_config.node_index)
			ASSERT(process, "")
		except:
			pass


	def test_base_134_addAttributes(self):
		
		try:
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
			(process, response) = forNeo(test_config.contract_address,functionName,params,test_config.public_key, test_config.node_index)
			ASSERT(process, "")
		except:
			pass


	def test_base_135_removeAttribute(self):
		try:
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
			(process, response) = addAttributes("did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab", addAttributes_74,test_config.public_key,test_config.node_index,0)#先加
			(process, response) = forNeo(test_config.contract_address,functionName,params,test_config.public_key, test_config.node_index)
			ASSERT(process, "")
		except:
			pass


	def test_base_136_getPublicKeys(self):
		try:
			functionName="getPublicKeys"
			params=[{
					"type" : "string",
					"value" : "did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab"
				}
				]
			(process, response) = forNeo(test_config.contract_address,functionName,params,test_config.public_key, test_config.node_index)
			ASSERT(process, "")
		except:
			pass


	def test_base_137_getKeyState(self):
		try:
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
			(process, response) = forNeo(test_config.contract_address,functionName,params,test_config.public_key, test_config.node_index)
			ASSERT(process, "")
		except:
			pass



	def test_base_138_getAttributes(self):
		try:
			functionName="getAttributes"
			params=[{
					"type" : "string",
					"value" : "did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab"
				}
				]
			(process, response) = addAttributes("did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab", addAttributes_74,test_config.public_key,test_config.node_index,0)#先加
			(process, response) = forNeo(test_config.contract_address,functionName,params,test_config.public_key, test_config.node_index)
			ASSERT(process, "")
		except:
			pass


	def test_base_139_getDDO(self):
		
		try:
			functionName="getDDO"
			params=[{
					"type" : "string",
					"value" : "did:ont:AS24hCPUxkbPzrFDeeemiE13cqJviuxuab"
				}
				]
			(process, response) = forNeo(test_config.contract_address,functionName,params,test_config.public_key, test_config.node_index)
			ASSERT(process, "")
		except:
			pass


	def test_base_140_verifySignature(self):
		try:
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
			(process, response) = forNeo(test_config.contract_address,functionName,params,test_config.public_key, test_config.node_index)
			ASSERT(process, "")
		except:
			pass
####################################################
if __name__ == '__main__':
	unittest.main()

