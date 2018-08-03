# -*- coding:utf-8 -*-
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys
import getopt

sys.path.append('..')
sys.path.append('../..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error

from utils.parametrizedtestcase import ParametrizedTestCase
from api.apimanager import API
from utils.common import Common 

def transfer(contract_address,pay_address,get_address,amount, node_index = None,errorcode=47001,errorkey="error"):
	if len(get_address)!=34 :
		send_get_address=ByteToHex(bytes(get_address, encoding = "utf8"))
	else:
		send_get_address=Common.bl_address(get_address)
		if send_get_address=="0000000000000000000000000000000000000000":
			send_get_address=ByteToHex(bytes(get_address, encoding = "utf8"))
	if len(pay_address)!=34 :
		send_pay_address=ByteToHex(bytes(pay_address, encoding = "utf8"))
	else:
		send_pay_address=Common.bl_address(pay_address)
		if send_pay_address=="0000000000000000000000000000000000000000":
			send_pay_address=ByteToHex(bytes(pay_address, encoding = "utf8"))
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signeovminvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": contract_address,
				"version": 1,
				"params": [
					{
						"type": "string",
						"value": "transfer"
					},
					
					{
						"type": "array",
						"value":  [
							{
								"type": "bytearray",
								
								"value": send_pay_address
							},
							{
								"type": "bytearray",
								"value": send_get_address
							},
							{
								"type": "int",
								"value": amount
							}
						]
					}
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}
	if len(contract_address)<=5:
		logger.error("contract address error! now is contract address:\"" + contract_address+"\"")
		return (False,{"error":10000,"desc":"contract address error!"})
	return API.contract().call_contract(Task(name="transfer", ijson=request), twice = True,sleep=0)
def approve(contract_address,pay_address,get_address, amount,node_index = None,errorcode=47001,errorkey="error"):
	if len(get_address)!=34 :
		send_get_address=ByteToHex(bytes(get_address, encoding = "utf8"))
	else:
		send_get_address=Common.bl_address(get_address)
		if send_get_address=="0000000000000000000000000000000000000000":
			send_get_address=ByteToHex(bytes(get_address, encoding = "utf8"))
	if len(pay_address)!=34 :
		send_pay_address=ByteToHex(bytes(pay_address, encoding = "utf8"))
	else:
		send_pay_address=Common.bl_address(pay_address)
		if send_pay_address=="0000000000000000000000000000000000000000":
			send_pay_address=ByteToHex(bytes(pay_address, encoding = "utf8"))
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signeovminvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": contract_address,
				"version": 1,
				"params": [
					{
						"type": "string",
						"value": "approve"
					},
					
					{
						"type": "array",
						"value":  [
							{
								"type": "bytearray",
								
								"value": send_pay_address
							},
							{
								"type": "bytearray",
								"value": send_get_address
							},
							{
								"type": "int",
								"value": amount
							}
						]
					}
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}
	if len(contract_address)<=5:
		logger.error("contract address error! now is contract address:\"" + contract_address+"\"")
		return (False,{"error":10000,"desc":"contract address error!"})
	return API.contract().call_contract(Task(name="approve", ijson=request), twice = True,sleep=0)
def transferFrom(contract_address,sender,pay_address,get_address, amount,node_index = None,senderType=False,errorcode=47001,errorkey="error"):
	if len(pay_address)!=34 :
		send_pay_address=ByteToHex(bytes(pay_address, encoding = "utf8"))
	else:
		send_pay_address=Common.bl_address(pay_address)
		if send_pay_address=="0000000000000000000000000000000000000000":
			send_pay_address=ByteToHex(bytes(pay_address, encoding = "utf8"))
	#if not senderType:
	if len(sender)!=34 :
		sender=ByteToHex(bytes(sender, encoding = "utf8"))
	else:
		sender=Common.bl_address(sender)
		if sender=="0000000000000000000000000000000000000000":
			sender=ByteToHex(bytes(sender, encoding = "utf8"))
	if len(get_address)!=34 :
		getaddress=ByteToHex(bytes(get_address, encoding = "utf8"))
	else:
		getaddress=Common.bl_address(get_address)
		if getaddress=="0000000000000000000000000000000000000000":
			getaddress=ByteToHex(bytes(get_address, encoding = "utf8"))
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signeovminvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": contract_address,
				"version": 1,
				"params": [
					{
						"type": "string",
						"value": "transferFrom"
					},
					
					{
						"type": "array",
						"value":  [
							{
								"type": "bytearray",
								
								"value": sender
							},
							{
								"type": "bytearray",
								
								"value": send_pay_address
							},
							{
								"type": "bytearray",
								"value": getaddress
							},
							{
								"type": "int",
								"value": amount
							}
						]
					}
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}
	return API.contract().call_contract(Task(name="transferFrom", ijson=request), twice = True,sleep=0)
def name(contract_address,node_index = None,errorcode=47001):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signeovminvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": contract_address,
				"version": 1,
				"params": [
					{
						"type": "string",
						"value": "name"
					},
					{
						"type": "string",
						"value": "name"
					}
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return API.contract().call_contract(Task(name="name", ijson=request), twice = True,sleep=0)
def symbol(contract_address,node_index = None,errorcode=47001):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signeovminvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": contract_address,
				"version": 1,
				"params": [
					{
						"type": "string",
						"value": "symbol"
					},
					{
						"type": "string",
						"value": "name"
					}
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return API.contract().call_contract(Task(name="symbol", ijson=request), twice = True,sleep=0)
def decimals(contract_address,node_index = None,errorcode=47001):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signeovminvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": contract_address,
				"version": 1,
				"params": [
					{
						"type": "string",
						"value": "decimals"
					},
					{
						"type": "string",
						"value": "name"
					}
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return API.contract().call_contract(Task(name="decimals", ijson=request), twice = True,sleep=0)
def totalSupply(contract_address,node_index = None,errorcode=47001):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signeovminvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": contract_address,
				"version": 1,
				"params": [
					{
						"type": "string",
						"value": "totalSupply"
					},
					{
						"type": "string",
						"value": "name"
					}
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return API.contract().call_contract(Task(name="totalSupply", ijson=request), twice = True,sleep=0)
def balanceOf(contract_address,address,node_index = None,errorcode=47001):
	if len(address)!=34 :
		send_get_address=ByteToHex(bytes(address, encoding = "utf8"))
	else:
		send_get_address=Common.bl_address(address)
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signeovminvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": contract_address,
				"version": 1,
				"params": [
					{
						"type": "string",
						"value": "balanceOf"
					},
					
					{
						"type": "array",
						"value":  [
							{
								"type": "bytearray",
								
								"value": send_get_address
							}
						]
					}
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return API.contract().call_contract(Task(name="balanceOf", ijson=request), twice = True,sleep=0)
def allowance(contract_address,pay_address,get_address,node_index = None,errorcode=47001,errorkey="error"):
	if len(get_address)!=34 :
		send_get_address=ByteToHex(bytes(get_address, encoding = "utf8"))
	else:
		send_get_address=Common.bl_address(get_address)
	if len(pay_address)!=34 :
		send_pay_address=ByteToHex(bytes(pay_address, encoding = "utf8"))
	else:
		send_pay_address=Common.bl_address(pay_address)
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signeovminvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": contract_address,
				"version": 1,
				"params": [
					{
						"type": "string",
						"value": "allowance"
					},
					
					{
						"type": "array",
						"value":  [
							{
								"type": "bytearray",
								
								"value": send_pay_address
							},
							{
								"type": "bytearray",
								"value": send_get_address
							}
						]
					}
				]
			}
		},

		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}
	return API.contract().call_contract(Task(name="allowance", ijson=request), twice = True,sleep=0)

def transfer1(contract_address,pay_address,get_address,amount, node_index = None,errorcode=47001,errorkey="error"):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0100000000000000000000000000000000000000",
				"method": "transfer",
				"version": 1,
				"params": [[[
					pay_address,
					get_address,
					amount
				]]]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}
	return API.contract().call_contract(Task(name="transfer", ijson=request), twice = True,sleep=0)
def approve1(contract_address,pay_address,get_address, amount,node_index = None,errorcode=47001,errorkey="error"):
	request =  {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0100000000000000000000000000000000000000",
				"method": "approve",
				"version": 1,
				"params": [
					pay_address,
					get_address,
					amount
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}
	return API.contract().call_contract(Task(name="approve", ijson=request), twice = True,sleep=0)
def transferFrom1(contract_address,sender,pay_address,get_address, amount,node_index = None,senderType=False,errorcode=47001,errorkey="error"):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0100000000000000000000000000000000000000",
				"method": "transferFrom",
				"version": 1,
				"params": [
					sender,
					pay_address,
					get_address,
					amount
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}
	return API.contract().call_contract(Task(name="transferFrom", ijson=request), twice = True,sleep=0)
def name1(contract_address,node_index = None,errorcode=47001):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0100000000000000000000000000000000000000",
				"method": "name",
				"version": 1,
				"params": [
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return API.contract().call_contract(Task(name="name", ijson=request), twice = True,sleep=0)
def symbol1(contract_address,node_index = None,errorcode=47001):
	request = {
		"REQUEST":{
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0100000000000000000000000000000000000000",
				"method": "symbol",
				"version": 1,
				"params": [
				]
			},
			},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return API.contract().call_contract(Task(name="symbol", ijson=request), twice = True,sleep=0)
def decimals1(contract_address,node_index = None,errorcode=47001):
	request ={
		"REQUEST":{
		"Qid": "t",
		"Method": "signativeinvoketx",
		"Params": {
			"gas_price": 0,
			"gas_limit": 1000000000,
			"address": "0100000000000000000000000000000000000000",
			"method": "decimals",
			"version": 1,
			"params": [
			]
		},
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return API.contract().call_contract(Task(name="decimals", ijson=request), twice = True,sleep=0)
def totalSupply1(contract_address,node_index = None,errorcode=47001):
	request =  {
			"REQUEST":{
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0100000000000000000000000000000000000000",
				"method": "totalSupply",
				"version": 1,
				"params": [
				]
			},
			},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return API.contract().call_contract(Task(name="totalSupply", ijson=request), twice = True,sleep=0)
def balanceOf1(contract_address,address,node_index = None,errorcode=47001,errorkey="error"):
	request ={
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0100000000000000000000000000000000000000",
				"method": "balanceOf",
				"version": 1,
				"params": [
					address
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}

	return API.contract().call_contract(Task(name="balanceOf", ijson=request), twice = True,sleep=0)
def allowance1(contract_address,pay_address,get_address,node_index = None,errorcode=47001,errorkey="error"):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0100000000000000000000000000000000000000",
				"method": "allowance",
				"version": 1,
				"params": [
					pay_address,
					get_address
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	if (errorkey =="error_code"):
		request["SIGN_RESPONSE"]={errorkey : errorcode}

	return API.contract().call_contract(Task(name="allowance", ijson=request), twice = True,sleep=0)