# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

sys.path.append('..')


import utils.commonapi
import utils.base
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.websocketapi import WebSocketApi
from utils.commonapi import *

logger = LoggerInstance

wsapi = WebSocketApi()

HEIGHT_CORRECT = 10
HEIGHT_BORDER = 0
HEIGHT_INCORRECT_1 = -1
HEIGHT_INCORRECT_2 = 100000
HEIGHT_INCORRECT_3 = "abc"

HASH_CORRECT = "0f8ecb5369d7efe9b9398d7077a9a920080b9d0e357eee613284a274f7e87c72"
HASH_INCORRECT_1 = "" # NULL
HASH_INCORRECT_2 = "0f8ecb5369d7efe9b9398d7077a9a920080b9d0e357eee613284a274f7e81111" # HASH NOT EXISTENT
HASH_INCORRECT_3 = "0f8ecb5369d7efe9b9398d7077a9a920080b9d0e357eee613284a274f7e87c721111"
HASH_INCORRECT_4 = 1234

TX_HASH_CORRECT = "f6240e3a92037d0f46506bb6cbd6c2d5287f1718bf8a1828df0c8f259889cc23"
TX_HASH_INCORRECT_1 = "" # NULL
TX_HASH_INCORRECT_2 = "f6240e3a92037d0f46506bb6cbd6c2d5287f1718bf8a1828df0c8f259889cc22" # TX HASH NOT EXISTENT
TX_HASH_INCORRECT_3 = "f6240e3a92037d0f46506bb6cbd6c2d5287f1718bf8a1828df0c8f259889cc2322"
TX_HASH_INCORRECT_4 = 1234
TX_HASH_INCORRECT_5 = "0c29e810ea2bfb2f3f23d1bee2d2601e72e6dfaf6988ebeb55a95dbec1896779" # FAILED

RAW_TRANSACTION_DATA_CORRECT = "00d13466235b000000000000000000ca9a3b0000000024b453d1388732a9d78228b572e05f7a082b90a94b5a14a0b2c0fa82789c91c79b41fd671195ea52fdb9781424b453d1388732a9d78228b572e05f7a082b90a953c1087472616e73666572676e58277eaf5cefc2c0ee53b5b5a57fde7818a52400014140988b088d23d4d10f8552110d5b45a8ed1ca484fcd5fc57dc73241e1228e805e9a2ab9709fef0079d6dc0855f8af57e1396e060ee536940835e5d44a6fee63f60232103e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dcac"
RAW_TRANSACTION_DATA_INCORRECT_1 = "" # NULL
RAW_TRANSACTION_DATA_INCORRECT_2 = "00d13466235b000000000000000000ca9a3b0000000024b453d1388732a9d78228b572e05f7a082b90a94b5a14a0b2c0fa82789c91c79b41fd671195ea52fdb9781424b453d1388732a9d78228b572e05f7a082b90a953c1087472616e73666572676e58277eaf5cefc2c0ee53b5b5a57fde7818a52400014140988b088d23d4d10f8552110d5b45a8ed1ca484fcd5fc57dc73241e1228e805e9a2ab9709fef0079d6dc0855f8af57e1396e060ee536940835e5d44a6fee63f60232103e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dcbb" # INCORRECT SERIALIZE
RAW_TRANSACTION_DATA_INCORRECT_3 = 1234

ACCOUNT_ADDRESS_CORRECT = "AK7wzmkdgjKxbXAJBiaW91YhUokTu9pa5X"
ACCOUNT_ADDRESS_INCORRECT_1 = "" # NULL
ACCOUNT_ADDRESS_INCORRECT_2 = "AK7wzmkdgjKxbXAJBiaW91YhUokTu9pa55" # NOT EXISTENT
ACCOUNT_ADDRESS_INCORRECT_3 = "abc"
ACCOUNT_ADDRESS_INCORRECT_4 = 1234

CONTRACT_ADDRESS_CORRECT = "ae19450e552cfd40288e8c28559a33a248c3935c"
CONTRACT_ADDRESS_INCORRECT_1 = "" # NULL
CONTRACT_ADDRESS_INCORRECT_2 = "ae19450e552cfd40288e8c28559a33a248c39366" # NOT EXISTENT
CONTRACT_ADDRESS_INCORRECT_3 = "abc"
CONTRACT_ADDRESS_INCORRECT_4 = 1234

KEY_CORRECT = ""
KEY_INCORRECT_1 = "" # NULL
KEY_INCORRECT_2 = "" # NOT EXISTENT
KEY_INCORRECT_3 = "abc"
KEY_INCORRECT_4 = 1234 

class TestWebAPI(ParametrizedTestCase):
	def start(self, log_path):
		logger.open(log_path)

	def normal_finish(self, task_name, log_path, result, msg):
		if result:
			logger.print("[ OK       ] ")
			logger.append_record(task_name, "pass", log_path)
		else:
			logger.print("[ Failed   ] " + msg)
			logger.append_record(task_name, "fail", log_path)
		logger.close()

	def abnormal_finish(self, task_name, log_path, result, msg):
		if not result:
			logger.print("[ OK       ] ")
			logger.append_record(task_name, "pass", log_path)
		else:
			logger.print("[ Failed   ] " + msg)
			logger.append_record(task_name, "fail", log_path)
		logger.close()

	def test_01_heartbeat(self):
		log_path = "01_heartbeat.log"
		task_name = "01_heartbeat"
		self.start(log_path)
		(result, response) = wsapi.heartbeat()
		self.normal_finish(task_name, log_path, result, "")

	def test_02_heartbeat(self):
		log_path = "02_heartbeat.log"
		task_name = "02_heartbeat"
		self.start(log_path)
		(result, response) = wsapi.heartbeat()
		self.abnormal_finish(task_name, log_path, result, "")

	def test_03_heartbeat(self):
		log_path = "03_heartbeat.log"
		task_name = "03_heartbeat"
		self.start(log_path)
		(result, response) = wsapi.heartbeat()
		self.abnormal_finish(task_name, log_path, result, "")

	def test_04_subscribe(self):
		log_path = "04_subscribe.log"
		task_name = "04_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_CORRECT])
		self.normal_finish(task_name, log_path, result, "")

	def test_05_subscribe(self):
		log_path = "05_subscribe.log"
		task_name = "05_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_INCORRECT_2])
		self.abnormal_finish(task_name, log_path, result, "")
	
	def test_06_subscribe(self):
		log_path = "06_subscribe.log"
		task_name = "06_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_INCORRECT_3])
		self.abnormal_finish(task_name, log_path, result, "")

	def test_07_subscribe(self):
		log_path = "07_subscribe.log"
		task_name = "07_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_CORRECT], sevent=True)
		self.normal_finish(task_name, log_path, result, "")

	def test_08_subscribe(self):
		log_path = "08_subscribe.log"
		task_name = "08_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_CORRECT], sevent=False)
		self.normal_finish(task_name, log_path, result, "")

	def test_09_subscribe(self):
		log_path = "09_subscribe.log"
		task_name = "09_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_CORRECT], sevent=None)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_10_subscribe(self):
		log_path = "10_subscribe.log"
		task_name = "10_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe(None, sevent=True)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_11_subscribe(self):
		log_path = "11_subscribe.log"
		task_name = "11_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe(None, sevent=0)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_12_subscribe(self):
		log_path = "12_subscribe.log"
		task_name = "12_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_CORRECT], sjsonblock=True)
		self.normal_finish(task_name, log_path, result, "")

	def test_13_subscribe(self):
		log_path = "13_subscribe.log"
		task_name = "13_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_CORRECT], sjsonblock=False)
		self.normal_finish(task_name, log_path, result, "")

	def test_14_subscribe(self):
		log_path = "14_subscribe.log"
		task_name = "14_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_CORRECT], sjsonblock=None)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_15_subscribe(self):
		log_path = "15_subscribe.log"
		task_name = "15_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_CORRECT], sjsonblock=0)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_16_subscribe(self):
		log_path = "16_subscribe.log"
		task_name = "16_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_CORRECT], srawblock=True)
		self.normal_finish(task_name, log_path, result, "")

	def test_17_subscribe(self):
		log_path = "17_subscribe.log"
		task_name = "17_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_CORRECT], srawblock=False)
		self.normal_finish(task_name, log_path, result, "")

	def test_18_subscribe(self):
		log_path = "18_subscribe.log"
		task_name = "18_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_CORRECT], srawblock=None)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_19_subscribe(self):
		log_path = "19_subscribe.log"
		task_name = "19_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_CORRECT], srawblock=0)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_20_subscribe(self):
		log_path = "20_subscribe.log"
		task_name = "20_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_CORRECT], sblocktxhashs=True)
		self.normal_finish(task_name, log_path, result, "")

	def test_21_subscribe(self):
		log_path = "21_subscribe.log"
		task_name = "21_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_CORRECT], sblocktxhashs=False)
		self.normal_finish(task_name, log_path, result, "")

	def test_22_subscribe(self):
		log_path = "22_subscribe.log"
		task_name = "22_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_CORRECT], sblocktxhashs=None)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_23_subscribe(self):
		log_path = "23_subscribe.log"
		task_name = "23_subscribe"
		self.start(log_path)
		(result, response) = wsapi.subscribe([CONTRACT_ADDRESS_CORRECT], sblocktxhashs=0)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_24_getgenerateblocktime(self):
		log_path = "24_getgenerateblocktime.log"
		task_name = "24_getgenerateblocktime"
		self.start(log_path)
		(result, response) = wsapi.getgenerateblocktime()
		self.normal_finish(task_name, log_path, result, "")

	def test_25_getgenerateblocktime(self):
		log_path = "25_getgenerateblocktime.log"
		task_name = "25_getgenerateblocktime"
		self.start(log_path)
		(result, response) = wsapi.getgenerateblocktime({"height":"1"})
		self.abnormal_finish(task_name, log_path, result, "")

	def test_26_getconnectioncount(self):
		log_path = "26_getconnectioncount.log"
		task_name = "26_getconnectioncount"
		self.start(log_path)
		(result, response) = wsapi.getconnectioncount()
		self.normal_finish(task_name, log_path, result, "")

	def test_27_getconnectioncount(self):
		log_path = "27_getconnectioncount.log"
		task_name = "27_getconnectioncount"
		self.start(log_path)
		(result, response) = wsapi.getconnectioncount()
		self.abnormal_finish(task_name, log_path, result, "")

	def test_28_getconnectioncount(self):
		log_path = "28_getconnectioncount.log"
		task_name = "28_getconnectioncount"
		self.start(log_path)
		(result, response) = wsapi.getconnectioncount({"height":"1"})
		self.abnormal_finish(task_name, log_path, result, "")

	def test_29_getblocktxsbyheight(self):
		log_path = "29_getblocktxsbyheight.log"
		task_name = "29_getblocktxsbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblocktxsbyheight(HEIGHT_CORRECT)
		self.normal_finish(task_name, log_path, result, "")
	
	def test_30_getblocktxsbyheight(self):
		log_path = "30_getblocktxsbyheight.log"
		task_name = "30_getblocktxsbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblocktxsbyheight(HEIGHT_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_31_getblocktxsbyheight(self):
		log_path = "31_getblocktxsbyheight.log"
		task_name = "31_getblocktxsbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblocktxsbyheight(HEIGHT_BORDER)
		self.normal_finish(task_name, log_path, result, "")

	def test_32_getblocktxsbyheight(self):
		log_path = "32_getblocktxsbyheight.log"
		task_name = "32_getblocktxsbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblocktxsbyheight(HEIGHT_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_33_getblocktxsbyheight(self):
		log_path = "33_getblocktxsbyheight.log"
		task_name = "33_getblocktxsbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblocktxsbyheight(HEIGHT_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_34_getblocktxsbyheight(self):
		log_path = "34_getblocktxsbyheight.log"
		task_name = "34_getblocktxsbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblocktxsbyheight(HEIGHT_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_35_getblockbyheight(self):
		log_path = "35_getblockbyheight.log"
		task_name = "35_getblockbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblockbyheight(HEIGHT_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_36_getblockbyheight(self):
		log_path = "36_getblockbyheight.log"
		task_name = "36_getblockbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblockbyheight(HEIGHT_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_37_getblockbyheight(self):
		log_path = "37_getblockbyheight.log"
		task_name = "37_getblockbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblockbyheight(HEIGHT_BORDER)
		self.normal_finish(task_name, log_path, result, "")

	def test_38_getblockbyheight(self):
		log_path = "38_getblockbyheight.log"
		task_name = "38_getblockbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblockbyheight(HEIGHT_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_39_getblockbyheight(self):
		log_path = "39_getblockbyheight.log"
		task_name = "39_getblockbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblockbyheight(HEIGHT_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_40_getblockbyheight(self):
		log_path = "40_getblockbyheight.log"
		task_name = "40_getblockbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblockbyheight(HEIGHT_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_41_getblockbyhash(self):
		log_path = "41_getblockbyhash.log"
		task_name = "41_getblockbyhash"
		self.start(log_path)
		(result, response) = wsapi.getblockbyhash(HASH_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_42_getblockbyhash(self):
		log_path = "42_getblockbyhash.log"
		task_name = "42_getblockbyhash"
		self.start(log_path)
		(result, response) = wsapi.getblockbyhash(HASH_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_43_getblockbyhash(self):
		log_path = "43_getblockbyhash.log"
		task_name = "43_getblockbyhash"
		self.start(log_path)
		(result, response) = wsapi.getblockbyhash(HASH_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_44_getblockbyhash(self):
		log_path = "44_getblockbyhash.log"
		task_name = "44_getblockbyhash"
		self.start(log_path)
		(result, response) = wsapi.getblockbyhash(HASH_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_45_getblockbyhash(self):
		log_path = "45_getblockbyhash.log"
		task_name = "45_getblockbyhash"
		self.start(log_path)
		(result, response) = wsapi.getblockbyhash(HASH_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_46_getblockbyhash(self):
		log_path = "46_getblockbyhash.log"
		task_name = "46_getblockbyhash"
		self.start(log_path)
		(result, response) = wsapi.getblockbyhash(HASH_INCORRECT_4)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_47_getblockheight(self):
		log_path = "47_getblockheight.log"
		task_name = "47_getblockheight"
		self.start(log_path)
		(result, response) = wsapi.getblockheight()
		self.normal_finish(task_name, log_path, result, "")

	def test_48_getblockheight(self):
		log_path = "48_getblockheight.log"
		task_name = "48_getblockheight"
		self.start(log_path)
		(result, response) = wsapi.getblockheight()
		self.abnormal_finish(task_name, log_path, result, "")

	def test_49_getblockhashbyheight(self):
		log_path = "49_getblockhashbyheight.log"
		task_name = "49_getblockhashbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblockhashbyheight(HEIGHT_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_50_getblockhashbyheight(self):
		log_path = "50_getblockhashbyheight.log"
		task_name = "50_getblockhashbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblockhashbyheight(HEIGHT_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_51_getblockhashbyheight(self):
		log_path = "51_getblockhashbyheight.log"
		task_name = "51_getblockhashbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblockhashbyheight(HEIGHT_BORDER)
		self.normal_finish(task_name, log_path, result, "")

	def test_52_getblockhashbyheight(self):
		log_path = "52_getblockhashbyheight.log"
		task_name = "52_getblockhashbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblockhashbyheight(HEIGHT_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_53_getblockhashbyheight(self):
		log_path = "53_getblockhashbyheight.log"
		task_name = "53_getblockhashbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblockhashbyheight(HEIGHT_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_54_getblockhashbyheight(self):
		log_path = "54_getblockhashbyheight.log"
		task_name = "54_getblockhashbyheight"
		self.start(log_path)
		(result, response) = wsapi.getblockhashbyheight(HEIGHT_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_55_gettransaction(self):
		log_path = "55_gettransaction.log"
		task_name = "55_gettransaction"
		self.start(log_path)
		(result, response) = wsapi.gettransaction(TX_HASH_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_56_gettransaction(self):
		log_path = "56_gettransaction.log"
		task_name = "56_gettransaction"
		self.start(log_path)
		(result, response) = wsapi.gettransaction(TX_HASH_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_57_gettransaction(self):
		log_path = "57_gettransaction.log"
		task_name = "57_gettransaction"
		self.start(log_path)
		(result, response) = wsapi.gettransaction(TX_HASH_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_58_gettransaction(self):
		log_path = "58_gettransaction.log"
		task_name = "58_gettransaction"
		self.start(log_path)
		(result, response) = wsapi.gettransaction(TX_HASH_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_59_gettransaction(self):
		log_path = "59_gettransaction.log"
		task_name = "59_gettransaction"
		self.start(log_path)
		(result, response) = wsapi.gettransaction(TX_HASH_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_60_gettransaction(self):
		log_path = "60_gettransaction.log"
		task_name = "60_gettransaction"
		self.start(log_path)
		(result, response) = wsapi.gettransaction(TX_HASH_INCORRECT_4)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_61_sendrawtransaction(self):
		log_path = "61_sendrawtransaction.log"
		task_name = "61_sendrawtransaction"
		self.start(log_path)
		(result, response) = wsapi.sendrawtransaction(RAW_TRANSACTION_DATA_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_62_sendrawtransaction(self):
		log_path = "62_sendrawtransaction.log"
		task_name = "62_sendrawtransaction"
		self.start(log_path)
		(result, response) = wsapi.sendrawtransaction(RAW_TRANSACTION_DATA_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_63_sendrawtransaction(self):
		log_path = "63_sendrawtransaction.log"
		task_name = "63_sendrawtransaction"
		self.start(log_path)
		(result, response) = wsapi.sendrawtransaction(RAW_TRANSACTION_DATA_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_64_sendrawtransaction(self):
		log_path = "64_sendrawtransaction.log"
		task_name = "64_sendrawtransaction"
		self.start(log_path)
		(result, response) = wsapi.sendrawtransaction(RAW_TRANSACTION_DATA_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_65_sendrawtransaction(self):
		log_path = "65_sendrawtransaction.log"
		task_name = "65_sendrawtransaction"
		self.start(log_path)
		(result, response) = wsapi.sendrawtransaction(RAW_TRANSACTION_DATA_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_66_get_version(self):
		log_path = "66_get_version.log"
		task_name = "66_get_version"
		self.start(log_path)
		task = Task(Config.BASEAPI_PATH + "/ws/getversion.json")
		task.set_type("ws")
		param = None
		if param and isinstance(param, dict):
			taskrequest = task.request()
			for key in param:
				taskrequest[key] = param[key]
			task.set_request(taskrequest)
		(result, response) = run_single_task(task)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_67_get_version(self):
		log_path = "67_get_version.log"
		task_name = "67_get_version"
		self.start(log_path)
		task = Task(Config.BASEAPI_PATH + "/ws/getversion.json")
		task.set_type("ws")
		param = None
		if param and isinstance(param, dict):
			taskrequest = task.request()
			for key in param:
				taskrequest[key] = param[key]
			task.set_request(taskrequest)
		(result, response) = run_single_task(task)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_68_get_version(self):
		log_path = "68_get_version.log"
		task_name = "68_get_version"
		self.start(log_path)
		task = Task(Config.BASEAPI_PATH + "/ws/getversion.json")
		task.set_type("ws")
		param = {"height":""}
		if param and isinstance(param, dict):
			taskrequest = task.request()
			for key in param:
				taskrequest[key] = param[key]
			task.set_request(taskrequest)
		(result, response) = run_single_task(task)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_69_get_version(self):
		log_path = "69_get_version.log"
		task_name = "69_get_version"
		self.start(log_path)
		task = Task(Config.BASEAPI_PATH + "/ws/getversion.json")
		task.set_type("ws")
		param = {"height":"abc"}
		if param and isinstance(param, dict):
			taskrequest = task.request()
			for key in param:
				taskrequest[key] = param[key]
			task.set_request(taskrequest)
		(result, response) = run_single_task(task)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_70_getbalancebyaddr(self):
		log_path = "70_getbalancebyaddr.log"
		task_name = "70_getbalancebyaddr"
		self.start(log_path)
		(result, response) = wsapi.getbalancebyaddr(ACCOUNT_ADDRESS_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_71_getbalancebyaddr(self):
		log_path = "71_getbalancebyaddr.log"
		task_name = "71_getbalancebyaddr"
		self.start(log_path)
		(result, response) = wsapi.getbalancebyaddr(ACCOUNT_ADDRESS_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_72_getbalancebyaddr(self):
		log_path = "72_getbalancebyaddr.log"
		task_name = "72_getbalancebyaddr"
		self.start(log_path)
		(result, response) = wsapi.getbalancebyaddr(ACCOUNT_ADDRESS_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_73_getbalancebyaddr(self):
		log_path = "73_getbalancebyaddr.log"
		task_name = "73_getbalancebyaddr"
		self.start(log_path)
		(result, response) = wsapi.getbalancebyaddr(ACCOUNT_ADDRESS_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_74_getcontract(self):
		log_path = "74_getcontract.log"
		task_name = "74_getcontract"
		self.start(log_path)
		(result, response) = wsapi.getcontract(ACCOUNT_ADDRESS_INCORRECT_4)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_75_getcontract(self):
		log_path = "75_getcontract.log"
		task_name = "75_getcontract"
		self.start(log_path)
		(result, response) = wsapi.getcontract(CONTRACT_ADDRESS_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_76_getcontract(self):
		log_path = "76_getcontract.log"
		task_name = "76_getcontract"
		self.start(log_path)
		(result, response) = wsapi.getcontract(CONTRACT_ADDRESS_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_77_getcontract(self):
		log_path = "77_getcontract.log"
		task_name = "77_getcontract"
		self.start(log_path)
		(result, response) = wsapi.getcontract(CONTRACT_ADDRESS_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_78_getcontract(self):
		log_path = "78_getcontract.log"
		task_name = "78_getcontract"
		self.start(log_path)
		(result, response) = wsapi.getcontract(CONTRACT_ADDRESS_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_79_getcontract(self):
		log_path = "79_getcontract.log"
		task_name = "79_getcontract"
		self.start(log_path)
		(result, response) = wsapi.getcontract(CONTRACT_ADDRESS_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_80_getcontract(self):
		log_path = "80_getcontract.log"
		task_name = "80_getcontract"
		self.start(log_path)
		(result, response) = wsapi.getcontract(CONTRACT_ADDRESS_INCORRECT_4)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_81_getsmartcodeeventbyheight(self):
		log_path = "81_getsmartcodeeventbyheight.log"
		task_name = "81_getsmartcodeeventbyheight"
		self.start(log_path)
		(result, response) = wsapi.getsmartcodeeventbyheight(HEIGHT_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_82_getsmartcodeeventbyheight(self):
		log_path = "82_getsmartcodeeventbyheight.log"
		task_name = "82_getsmartcodeeventbyheight"
		self.start(log_path)
		(result, response) = wsapi.getsmartcodeeventbyheight(HEIGHT_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_83_getsmartcodeeventbyheight(self):
		log_path = "83_getsmartcodeeventbyheight.log"
		task_name = "83_getsmartcodeeventbyheight"
		self.start(log_path)
		(result, response) = wsapi.getsmartcodeeventbyheight(HEIGHT_BORDER)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_84_getsmartcodeeventbyheight(self):
		log_path = "84_getsmartcodeeventbyheight.log"
		task_name = "84_getsmartcodeeventbyheight"
		self.start(log_path)
		(result, response) = wsapi.getsmartcodeeventbyheight(HEIGHT_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_85_getsmartcodeeventbyheight(self):
		log_path = "85_getsmartcodeeventbyheight.log"
		task_name = "85_getsmartcodeeventbyheight"
		self.start(log_path)
		(result, response) = wsapi.getsmartcodeeventbyheight(HEIGHT_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_86_getsmartcodeeventbyheight(self):
		log_path = "86_getsmartcodeeventbyheight.log"
		task_name = "86_getsmartcodeeventbyheight"
		self.start(log_path)
		(result, response) = wsapi.getsmartcodeeventbyheight(HEIGHT_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_87_getsmartcodeeventbyhash(self):
		log_path = "87_getsmartcodeeventbyhash.log"
		task_name = "87_getsmartcodeeventbyhash"
		self.start(log_path)
		(result, response) = wsapi.getsmartcodeeventbyhash(HASH_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_88_getsmartcodeeventbyhash(self):
		log_path = "88_getsmartcodeeventbyhash.log"
		task_name = "88_getsmartcodeeventbyhash"
		self.start(log_path)
		(result, response) = wsapi.getsmartcodeeventbyhash(TX_HASH_INCORRECT_5)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_89_getsmartcodeeventbyhash(self):
		log_path = "89_getsmartcodeeventbyhash.log"
		task_name = "89_getsmartcodeeventbyhash"
		self.start(log_path)
		(result, response) = wsapi.getsmartcodeeventbyhash(HASH_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_90_getsmartcodeeventbyhash(self):
		log_path = "90_getsmartcodeeventbyhash.log"
		task_name = "90_getsmartcodeeventbyhash"
		self.start(log_path)
		(result, response) = wsapi.getsmartcodeeventbyhash(HASH_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_91_getsmartcodeeventbyhash(self):
		log_path = "91_getsmartcodeeventbyhash.log"
		task_name = "91_getsmartcodeeventbyhash"
		self.start(log_path)
		(result, response) = wsapi.getsmartcodeeventbyhash(HASH_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_92_getsmartcodeeventbyhash(self):
		log_path = "92_getsmartcodeeventbyhash.log"
		task_name = "92_getsmartcodeeventbyhash"
		self.start(log_path)
		(result, response) = wsapi.getsmartcodeeventbyhash(HASH_INCORRECT_4)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_93_getblockheightbytxhash(self):
		log_path = "93_getblockheightbytxhash.log"
		task_name = "93_getblockheightbytxhash"
		self.start(log_path)
		(result, response) = wsapi.getblockheightbytxhash(HASH_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_94_getblockheightbytxhash(self):
		log_path = "94_getblockheightbytxhash.log"
		task_name = "94_getblockheightbytxhash"
		self.start(log_path)
		(result, response) = wsapi.getblockheightbytxhash(TX_HASH_INCORRECT_5)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_95_getblockheightbytxhash(self):
		log_path = "95_getblockheightbytxhash.log"
		task_name = "95_getblockheightbytxhash"
		self.start(log_path)
		(result, response) = wsapi.getblockheightbytxhash(HASH_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_96_getblockheightbytxhash(self):
		log_path = "96_getblockheightbytxhash.log"
		task_name = "96_getblockheightbytxhash"
		self.start(log_path)
		(result, response) = wsapi.getblockheightbytxhash(HASH_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")					

	def test_97_getblockheightbytxhash(self):
		log_path = "97_getblockheightbytxhash.log"
		task_name = "97_getblockheightbytxhash"
		self.start(log_path)
		(result, response) = wsapi.getblockheightbytxhash(HASH_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")		

	def test_98_getblockheightbytxhash(self):
		log_path = "98_getblockheightbytxhash.log"
		task_name = "98_getblockheightbytxhash"
		self.start(log_path)
		(result, response) = wsapi.getblockheightbytxhash(HASH_INCORRECT_4)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_99_getmerkleproof(self):
		log_path = "99_getmerkleproof.log"
		task_name = "99_getmerkleproof"
		self.start(log_path)
		(result, response) = wsapi.getmerkleproof(HASH_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_100_getmerkleproof(self):
		log_path = "100_getmerkleproof.log"
		task_name = "100_getmerkleproof"
		self.start(log_path)
		(result, response) = wsapi.getmerkleproof(TX_HASH_INCORRECT_5)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_101_getmerkleproof(self):
		log_path = "101_getmerkleproof.log"
		task_name = "101_getmerkleproof"
		self.start(log_path)
		(result, response) = wsapi.getmerkleproof(HASH_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_102_getmerkleproof(self):
		log_path = "102_getmerkleproof.log"
		task_name = "102_getmerkleproof"
		self.start(log_path)
		(result, response) = wsapi.getmerkleproof(HASH_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_103_getmerkleproof(self):
		log_path = "103_getmerkleproof.log"
		task_name = "103_getmerkleproof"
		self.start(log_path)
		(result, response) = wsapi.getmerkleproof(HASH_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_104_getmerkleproof(self):
		log_path = "104_getmerkleproof.log"
		task_name = "104_getmerkleproof"
		self.start(log_path)
		(result, response) = wsapi.getmerkleproof(HASH_INCORRECT_4)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_105_getsessioncount(self):
		log_path = "105_getsessioncount.log"
		task_name = "105_getsessioncount"
		self.start(log_path)
		(result, response) = wsapi.getsessioncount()
		self.normal_finish(task_name, log_path, result, "")

	def test_106_getsessioncount(self):
		log_path = "106_getsessioncount.log"
		task_name = "106_getsessioncount"
		self.start(log_path)
		(result, response) = wsapi.getsessioncount()
		self.abnormal_finish(task_name, log_path, result, "")

	def test_107_getstorage(self):
		log_path = "107_getstorage.log"
		task_name = "107_getstorage"
		self.start(log_path)
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_CORRECT, KEY_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_108_getstorage(self):
		log_path = "108_getstorage.log"
		task_name = "108_getstorage"
		self.start(log_path)
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_INCORRECT_2, KEY_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_109_getstorage(self):
		log_path = "109_getstorage.log"
		task_name = "109_getstorage"
		self.start(log_path)
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_INCORRECT_3, KEY_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_110_getstorage(self):
		log_path = "110_getstorage.log"
		task_name = "110_getstorage"
		self.start(log_path)
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_INCORRECT_4, KEY_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_111_getstorage(self):
		log_path = "111_getstorage.log"
		task_name = "111_getstorage"
		self.start(log_path)
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_INCORRECT_1, KEY_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_112_getstorage(self):
		log_path = "112_getstorage.log"
		task_name = "112_getstorage"
		self.start(log_path)
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_CORRECT, KEY_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_113_getstorage(self):
		log_path = "113_getstorage.log"
		task_name = "113_getstorage"
		self.start(log_path)
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_CORRECT, KEY_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_114_getstorage(self):
		log_path = "114_getstorage.log"
		task_name = "114_getstorage"
		self.start(log_path)
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_CORRECT, KEY_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_115_getstorage(self):
		log_path = "115_getstorage.log"
		task_name = "115_getstorage"
		self.start(log_path)
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_CORRECT, KEY_INCORRECT_4)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_116_getstorage(self):
		log_path = "116_getstorage.log"
		task_name = "116_getstorage"
		self.start(log_path)
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_CORRECT, KEY_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

####################################################
if __name__ == '__main__':
	suite = unittest.main()