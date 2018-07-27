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

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.commonapi import *
from utils.parametrizedtestcase import ParametrizedTestCase

def transfer(contract_address,pay_address,get_address,amount, node_index = None,errorcode=47001,errorkey="error"):
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
								
								"value": script_hash_bl_reserver(base58_to_address(pay_address))
							},
							{
								"type": "bytearray",
								"value": script_hash_bl_reserver(base58_to_address(get_address))
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
	return call_contract(Task(name="transfer", ijson=request), twice = True)
def approve(contract_address,pay_address,get_address, amount,node_index = None,errorcode=47001,errorkey="error"):
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
								
								"value": script_hash_bl_reserver(base58_to_address(pay_address))
							},
							{
								"type": "bytearray",
								"value": script_hash_bl_reserver(base58_to_address(get_address))
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
	return call_contract(Task(name="approve", ijson=request), twice = True)
def transferFrom(contract_address,sender,pay_address,get_address, amount,node_index = None,senderType=False,errorcode=47001,errorkey="error"):
	if not senderType:
		sender=script_hash_bl_reserver(base58_to_address(sender))
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
								
								"value": script_hash_bl_reserver(base58_to_address(pay_address))
							},
							{
								"type": "bytearray",
								"value": script_hash_bl_reserver(base58_to_address(get_address))
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
	return call_contract(Task(name="transferFrom", ijson=request), twice = True)
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
					}
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return call_contract(Task(name="name", ijson=request), twice = True)
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
					}
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return call_contract(Task(name="symbol", ijson=request), twice = True)
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
					}
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return call_contract(Task(name="decimals", ijson=request), twice = True)
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
					}
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return call_contract(Task(name="totalSupply", ijson=request), twice = True)
def balanceOf(contract_address,address,node_index = None,errorcode=47001):
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
								
								"value": script_hash_bl_reserver(base58_to_address(address))
							}
						]
					}
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return call_contract(Task(name="balanceOf", ijson=request), twice = True)
def allowance(contract_address,pay_address,get_address,node_index = None,errorcode=47001,errorkey="error"):
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
								
								"value": script_hash_bl_reserver(base58_to_address(pay_address))
							},
							{
								"type": "bytearray",
								"value": script_hash_bl_reserver(base58_to_address(get_address))
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
	return call_contract(Task(name="allowance", ijson=request), twice = True)

def transfer1(contract_address,pay_address,get_address,amount, node_index = None,errorcode=47001,errorkey="error"):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0200000000000000000000000000000000000000",
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
	return call_contract(Task(name="transfer", ijson=request), twice = True)
def approve1(contract_address,pay_address,get_address, amount,node_index = None,errorcode=47001,errorkey="error"):
	request =  {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0200000000000000000000000000000000000000",
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
	return call_contract(Task(name="approve", ijson=request), twice = True)
def transferFrom1(contract_address,sender,pay_address,get_address, amount,node_index = None,senderType=False,errorcode=47001,errorkey="error"):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0200000000000000000000000000000000000000",
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
	return call_contract(Task(name="transferFrom", ijson=request), twice = True)
def name1(contract_address,node_index = None,errorcode=47001):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0200000000000000000000000000000000000000",
				"method": "name",
				"version": 1,
				"params": [
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return call_contract(Task(name="name", ijson=request), twice = True)
def symbol1(contract_address,node_index = None,errorcode=47001):
	request = {
		"REQUEST":{
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0200000000000000000000000000000000000000",
				"method": "symbol",
				"version": 1,
				"params": [
				]
			},
			},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return call_contract(Task(name="symbol", ijson=request), twice = True)
def decimals1(contract_address,node_index = None,errorcode=47001):
	request ={
		"REQUEST":{
		"Qid": "t",
		"Method": "signativeinvoketx",
		"Params": {
			"gas_price": 0,
			"gas_limit": 1000000000,
			"address": "0200000000000000000000000000000000000000",
			"method": "decimals",
			"version": 1,
			"params": [
			]
		},
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return call_contract(Task(name="decimals", ijson=request), twice = True)
def totalSupply1(contract_address,node_index = None,errorcode=47001):
	request =  {
			"REQUEST":{
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0200000000000000000000000000000000000000",
				"method": "totalSupply",
				"version": 1,
				"params": [
				]
			},
			},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return call_contract(Task(name="totalSupply", ijson=request), twice = True)
def balanceOf1(contract_address,address,node_index = None,errorcode=47001,errorkey="error"):
	request ={
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0200000000000000000000000000000000000000",
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

	return call_contract(Task(name="balanceOf", ijson=request), twice = True)
def allowance1(contract_address,pay_address,get_address,node_index = None,errorcode=47001,errorkey="error"):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0200000000000000000000000000000000000000",
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

	return call_contract(Task(name="allowance", ijson=request), twice = True)