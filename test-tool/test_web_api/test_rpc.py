# -*- coding:utf-8 -*-

import re
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys
import getopt
import time
import requests
import subprocess

sys.path.append('..')

import utils.base
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.rpcapi import RPCApi
from utils.commonapi import *

####################################################
logger = LoggerInstance
rpcApi = RPCApi()
####################################################

address_true = "4df8a82026db08aebaf3d989cf8b2515873f8019"
address_false = "4df8a82026db08aebaf3d989cf8b2515873f8019"
txhash_true = "a4b67b932d06d0999b588088faafdd9f129ebf01b316b38a9177b3714779ff57"
txhash_false = "a4b67b932d06d0999b588088faafdd9f129ebf01b316b38a9177b3714779ff57"
height_true = 5
value_99999 = 99999
value_overflow = 99999999

hex_true =""
hex_false = ""

getstorage_hash_true = ""
getstorage_hash_false = ""
getstorage_key = ""

getblocksysfee_index_true = ""
getblocksysfee_index_false = ""

getcontractstate_hash_true = ""
getcontractstate_hash_false = ""

getsmartcodeevent_height = 5

getbalance_address_true = ""
getbalance_address_false= ""

######################################################
# test cases

class TestRpc(ParametrizedTestCase):

	def test_01_getblock(self):
		logger.open("01_getblock.log", "01_getblock")
		(result, response) = rpcApi.getblock(height = None, blockhash = txhash_true, verbose = None)
		logger.close(result)

	def test_02_getblock(self):
		logger.open("02_getblock.log", "02_getblock")
		(result, response) = rpcApi.getblock(height = None, blockhash = txhash_false, verbose = None)
		logger.close(not result)
	
	def test_03_getblock(self):
		logger.open("03_getblock.log", "03_getblock")
		(result, response) = rpcApi.getblock(height = height_true, blockhash = None, verbose = None)
		logger.close(result)
	
	def test_04_getblock(self):
		logger.open("04_getblock.log", "04_getblock")
		(result, response) = rpcApi.getblock(height = 0, blockhash = None, verbose = None)
		logger.close(result)
		
	def test_05_getblock(self):
		logger.open("05_getblock.log", "05_getblock")
		(result, response) = rpcApi.getblock(height = value_99999, blockhash = None, verbose = None)
		logger.close(not result)

	def test_06_getblock(self):
		logger.open("06_getblock.log", "06_getblock")
		(result, response) = rpcApi.getblock(height = value_overflow, blockhash = None, verbose = None)
		logger.close(not result)

	def test_07_getblock(self):
		logger.open("07_getblock.log", "07_getblock")
		(result, response) = rpcApi.getblock(height = height_true, blockhash = None, verbose = 0)
		logger.close(result)

	def test_08_getblock(self):
		logger.open("08_getblock.log", "08_getblock")
		(result, response) = rpcApi.getblock(height = height_true, blockhash = None, verbose = 1)
		logger.close(result)

	def test_09_getblock(self):
		logger.open("09_getblock.log", "09_getblock")
		(result, response) = rpcApi.getblock(height = height_true, blockhash = None, verbose = -1)
		logger.close(not result)
	
	def test_10_getblock(self):
		logger.open("10_getblock.log", "10_getblock")
		(result, response) = rpcApi.getblock(height = height_true, blockhash = None, verbose = 2)
		logger.close(not result)
	
	def test_11_getblock(self):
		logger.open("11_getblock.log", "11_getblock")
		(result, response) = rpcApi.getblock(height = height_true, blockhash = None, verbose = "abc")
		logger.close(not result)
	
	def test_12_getblock(self):
		logger.open("12_getblock.log", "12_getblock")
		(result, response) = rpcApi.getblock(height = height_true, blockhash = None, verbose = None)
		logger.close(result)

	def test_13_getblockhash(self):
		logger.open("13_getblockhash.log", "13_getblockhash")
		(result, response) = rpcApi.getblockhash(height = height_true)
		logger.close(result)
	
	def test_14_getblockhash(self):
		logger.open("14_getblockhash.log", "14_getblockhash")
		(result, response) = rpcApi.getblockhash(height = 0)
		logger.close(result)
	
	def test_15_getblockhash(self):
		logger.open("15_getblockhash.log", "15_getblockhash")
		(result, response) = rpcApi.getblockhash(height = value_99999)
		logger.close(not result)

	def test_16_getblockhash(self):
		logger.open("16_getblockhash.log", "16_getblockhash")
		(result, response) = rpcApi.getblockhash(height = value_overflow)
		logger.close(not result)

	def test_17_getblockhash(self):
		logger.open("17_getblockhash.log", "17_getblockhash")
		(result, response) = rpcApi.getblockhash(height = "abc")
		logger.close(not result)

	def test_18_getblockhash(self):
		logger.open("18_getblockhash.log", "18_getblockhash")
		(result, response) = rpcApi.getblockhash(height = -1)
		logger.close(not result)
	
	def test_19_getblockhash(self):
		logger.open("19_getblockhash.log", "19_getblockhash")
		(result, response) = rpcApi.getblockhash(height = None)
		logger.close(not result)

	def test_20_getbestblockhash(self):
		logger.open("20_getbestblockhash.log", "20_getbestblockhash")
		(result, response) = rpcApi.getbestblockhash()
		logger.close(result)

	# can not test
	def test_21_getbestblockhash(self):
		logger.open("21_getbestblockhash.log", "21_getbestblockhash")
		(result, response) = rpcApi.getblockhash()
		logger.close(not result)
	
	def test_22_getblockcount(self):
		logger.open("22_getblockcount.log", "22_getblockcount")
		(result, response) = rpcApi.getblockcount()
		logger.close(not result)

	# can not test
	def test_23_getblockcount(self):
		logger.open("23_getblockcount.log", "23_getblockcount")
		(result, response) = rpcApi.getblockcount()
		logger.close(not result)

	def test_24_getconnectioncount(self):
		logger.open("24_getconnectioncount.log", "24_getconnectioncount")
		(result, response) = rpcApi.getconnectioncount()
		logger.close(not result)

	# can not test
	def test_25_getconnectioncount(self):
		logger.open("25_getconnectioncount.log", "25_getconnectioncount")
		(result, response) = rpcApi.getconnectioncount()
		logger.close(not result)
	
	def test_26_getgenerateblocktime(self):
		logger.open("26_getgenerateblocktime.log", "26_getgenerateblocktime")
		(result, response) = rpcApi.getgenerateblocktime()
		logger.close(result)
	
	# can not test
	def test_26_getconnectioncount_1(self):
		logger.open("27_getconnectioncount.log", "27_getconnectioncount")
		(result, response) = rpcApi.getconnectioncount()
		logger.close(not result)

	def test_27_getrawtransaction(self):
		logger.open("27_getrawtransaction.log", "27_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(txhash_true)
		logger.close(result)
	
	def test_28_getrawtransaction(self):
		logger.open("28_getrawtransaction.log", "28_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(txhash_false)
		logger.close(not result)

	def test_29_getrawtransaction(self):
		logger.open("29_getrawtransaction.log", "29_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction("abc")
		logger.close(not result)

	def test_30_getrawtransaction(self):
		logger.open("30_getrawtransaction.log", "30_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(1)
		logger.close(not result)
	
	def test_31_getrawtransaction(self):
		logger.open("31_getrawtransaction.log", "31_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(None)
		logger.close(not result)
	
	def test_32_getrawtransaction(self):
		logger.open("32_getrawtransaction.log", "32_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(txhash_true, 1)
		logger.close(result)
	
	def test_33_getrawtransaction(self):
		logger.open("33_getrawtransaction.log", "33_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(txhash_true, 0)
		logger.close(result)

	def test_34_getrawtransaction(self):
		logger.open("34_getrawtransaction.log", "34_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(txhash_true, -1)
		logger.close(not result)

	def test_35_getrawtransaction(self):
		logger.open("35_getrawtransaction.log", "35_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(txhash_true, 2)
		logger.close(not result)

	def test_36_getrawtransaction(self):
		logger.open("36_getrawtransaction.log", "36_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(txhash_true, "abc")
		logger.close(not result)

	def test_37_getrawtransaction(self):
		logger.open("37_getrawtransaction.log", "37_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(None)
		logger.close(result)
	
	def test_38_sendrawtransaction(self):
		logger.open("38_sendrawtransaction.log", "38_sendrawtransaction")
		(result, response) = rpcApi.sendrawtransaction(hex_true)
		logger.close(result)
	
	def test_39_sendrawtransaction(self):
		logger.open("39_sendrawtransaction.log", "39_sendrawtransaction")
		(result, response) = rpcApi.sendrawtransaction(hex_false)
		logger.close(not result)
	
	def test_40_sendrawtransaction(self):
		logger.open("40_sendrawtransaction.log", "40_sendrawtransaction")
		(result, response) = rpcApi.sendrawtransaction(None)
		logger.close(not result)
	
	def test_41_getstorage(self):
		logger.open("41_getstorage.log", "41_getstorage")
		(result, response) = rpcApi.getstorage(getstorage_hash_true, getstorage_key)
		logger.close(result)

	def test_42_getstorage(self):
		logger.open("42_getstorage.log", "42_getstorage")
		(result, response) = rpcApi.getstorage(getstorage_hash_false, getstorage_key)
		logger.close(not result)

	def test_43_getstorage(self):
		logger.open("43_getstorage.log", "43_getstorage")
		(result, response) = rpcApi.getstorage("abc", getstorage_key)
		logger.close(not result)

	def test_44_getstorage(self):
		logger.open("44_getstorage.log", "44_getstorage")
		(result, response) = rpcApi.getstorage(1, getstorage_key)
		logger.close(not result)

	def test_45_getstorage(self):
		logger.open("45_getstorage.log", "45_getstorage")
		(result, response) = rpcApi.getstorage(None, getstorage_key)
		logger.close(not result)

	def test_46_getstorage(self):
		logger.open("46_getstorage.log", "46_getstorage")
		(result, response) = rpcApi.getstorage(getstorage_hash_true, getstorage_key)
		logger.close(result)

	def test_47_getstorage(self):
		logger.open("47_getstorage.log", "47_getstorage")
		(result, response) = rpcApi.getstorage(getstorage_hash_true, "getstorage_key_error")
		logger.close(not result)

	def test_48_getstorage(self):
		logger.open("48_getstorage.log", "48_getstorage")
		(result, response) = rpcApi.getstorage(getstorage_hash_true, "abc")
		logger.close(not result)

	def test_49_getstorage(self):
		logger.open("49_getstorage.log", "49_getstorage")
		(result, response) = rpcApi.getstorage(getstorage_hash_true, 123)
		logger.close(not result)
	
	def test_50_getstorage(self):
		logger.open("50_getstorage.log", "50_getstorage")
		(result, response) = rpcApi.getstorage(getstorage_hash_true)
		logger.close(not result)
	

	def test_51_getversion(self):
		logger.open("51_getversion.log", "51_getversion")
		(result, response) = rpcApi.getversion()
		logger.close(result)

	# can not test
	def test_52_getversion(self):
		logger.open("52_getversion.log", "52_getversion")
		(result, response) = rpcApi.getversion()
		logger.close(not result)

	def test_53_getblocksysfee(self):
		logger.open("52_getversion.log", "52_getversion")
		(result, response) = rpcApi.getblocksysfee(getblocksysfee_index_true)
		logger.close(result)

	# can not test
	def test_54_getblocksysfee(self):
		logger.open("54_getblocksysfee.log", "54_getblocksysfee")
		(result, response) = rpcApi.getblocksysfee(getblocksysfee_index_true)
		logger.close(result)

	def test_55_getblocksysfee(self):
		logger.open("55_getblocksysfee.log", "55_getblocksysfee")
		(result, response) = rpcApi.getblocksysfee(getblocksysfee_index_false)
		logger.close(not result)

	def test_56_getblocksysfee(self):
		logger.open("56_getblocksysfee.log", "56_getblocksysfee")
		(result, response) = rpcApi.getblocksysfee("abc")
		logger.close(not result)

	def test_57_getblocksysfee(self):
		logger.open("57_getblocksysfee.log", "57_getblocksysfee")
		(result, response) = rpcApi.getblocksysfee(None)
		logger.close(not result)

	def test_58_getcontractstate(self):
		logger.open("58_getcontractstate.log", "58_getcontractstate")
		(result, response) = rpcApi.getcontractstate(getcontractstate_hash_true)
		logger.close(result)

	def test_59_getcontractstate(self):
		logger.open("59_getcontractstate.log", "59_getcontractstate")
		(result, response) = rpcApi.getcontractstate(getcontractstate_hash_false)
		logger.close(not result)

	def test_60_getcontractstate(self):
		logger.open("60_getcontractstate.log", "60_getcontractstate")
		(result, response) = rpcApi.getcontractstate("abc")
		logger.close(not result)

	def test_61_getcontractstate(self):
		logger.open("61_getcontractstate", "61_getcontractstate")
		(result, response) = rpcApi.getcontractstate(123)
		logger.close(not result)

	def test_62_getcontractstate(self):
		logger.open("62_getcontractstate.log", "62_getcontractstate")
		(result, response) = rpcApi.getcontractstate(None, 1)
		logger.close(not result)

	def test_63_getcontractstate(self):
		logger.open("63_getcontractstate.log", "63_getcontractstate")
		(result, response) = rpcApi.getcontractstate(getcontractstate_hash_true, 1)
		logger.close(result)

	def test_64_getcontractstate(self):
		logger.open("64_getcontractstate.log", "64_getcontractstate")
		(result, response) = rpcApi.getcontractstate(getcontractstate_hash_true, -1)
		logger.close(not result)

	def test_65_getcontractstate(self):
		logger.open("65_getcontractstate.log", "65_getcontractstate")
		(result, response) = rpcApi.getcontractstate(getcontractstate_hash_true, 2)
		logger.close(not result)

	def test_66_getcontractstate(self):
		logger.open("66_getcontractstate.log", "66_getcontractstate")
		(result, response) = rpcApi.getcontractstate(getcontractstate_hash_true, "abc")
		logger.close(not result)

	def test_67_getcontractstate(self):
		logger.open("67_getcontractstate.log", "67_getcontractstate")
		(result, response) = rpcApi.getcontractstate(getcontractstate_hash_true, 0)
		logger.close(result)

	def test_68_getcontractstate(self):
		logger.open("68_getcontractstate.log", "68_getcontractstate")
		(result, response) = rpcApi.getcontractstate(getcontractstate_hash_true, None)
		logger.close(result)

	def test_69_getmempooltxstate(self):
		logger.open("69_getmempooltxstate.log", "69_getmempooltxstate")
		(result, response) = rpcApi.getmempooltxstate(txhash_true)
		logger.close(result)

	def test_70_getmempooltxstate(self):
		logger.open("70_getmempooltxstate.log", "70_getmempooltxstate")
		(result, response) = rpcApi.getmempooltxstate(txhash_false)
		logger.close(not result)

	def test_71_getmempooltxstate(self):
		logger.open("71_getmempooltxstate.log", "71_getmempooltxstate")
		(result, response) = rpcApi.getmempooltxstate("abc")
		logger.close(not result)

	def test_72_getmempooltxstate(self):
		logger.open("72_getmempooltxstate.log", "72_getmempooltxstate")
		(result, response) = rpcApi.getmempooltxstate(123)
		logger.close(not result)

	def test_73_getmempooltxstate(self):
		logger.open("73_getmempooltxstate.log", "73_getmempooltxstate")
		(result, response) = rpcApi.getmempooltxstate(None)
		logger.close(not result)
	
	def test_74_getsmartcodeevent(self):
		logger.open("74_getsmartcodeevent.log", "74_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent(getsmartcodeevent_height)
		logger.close(result)

	def test_75_getsmartcodeevent(self):
		logger.open("75_getsmartcodeevent.log", "75_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent(99999999)
		logger.close(not result)

	def test_76_getsmartcodeevent(self):
		logger.open("76_getsmartcodeevent.log", "76_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent("abc")
		logger.close(not result)

	def test_77_getsmartcodeevent(self):
		logger.open("77_getsmartcodeevent.log", "77_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent(None)
		logger.close(not result)
	
	def test_78_getsmartcodeevent(self):
		logger.open("78_getsmartcodeevent.log", "78_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent(txhash_true)
		logger.close(result)

	def test_79_getsmartcodeevent(self):
		logger.open("79_getsmartcodeevent.log", "79_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent(txhash_false)
		logger.close(not result)
	
	def test_80_getblockheightbytxhash(self):
		logger.open("80_getblockheightbytxhash.log", "80_getblockheightbytxhash")
		(result, response) = rpcApi.getsmartcodeevent(txhash_true)
		logger.close(result)

	def test_81_getblockheightbytxhash(self):
		logger.open("81_getblockheightbytxhash.log", "81_getblockheightbytxhash")
		(result, response) = rpcApi.getsmartcodeevent(txhash_false)
		logger.close(not result)

	def test_82_getblockheightbytxhash(self):
		logger.open("82_getblockheightbytxhash.log", "82_getblockheightbytxhash")
		(result, response) = rpcApi.getsmartcodeevent("abc")
		logger.close(not result)

	def test_83_getblockheightbytxhash(self):
		logger.open("83_getblockheightbytxhash.log", "83_getblockheightbytxhash")
		(result, response) = rpcApi.getsmartcodeevent(123)
		logger.close(not result)
	
	def test_84_getblockheightbytxhash(self):
		logger.open("84_getblockheightbytxhash.log", "84_getblockheightbytxhash")
		(result, response) = rpcApi.getsmartcodeevent(None)
		logger.close(not result)

	def test_85_getbalance(self):
		logger.open("85_getbalance.log", "85_getbalance")
		(result, response) = rpcApi.getbalance(getbalance_address_true)
		logger.close(result)
	
	def test_86_getbalance(self):
		logger.open("85_getbalance.log", "85_getbalance")
		(result, response) = rpcApi.getbalance(getbalance_address_false)
		logger.close(not result)
	
	def test_87_getbalance(self):
		logger.open("85_getbalance.log", "85_getbalance")
		(result, response) = rpcApi.getbalance("abc")
		logger.close(not result)

	def test_88_getbalance(self):
		logger.open("85_getbalance.log", "85_getbalance")
		(result, response) = rpcApi.getbalance(None)
		logger.close(not result)
	
	def test_89_getmerkleproof(self):
		logger.open("89_getmerkleproof.log", "89_getmerkleproof")
		(result, response) = rpcApi.getmerkleproof(txhash_true)
		logger.close(result)

	def test_90_getmerkleproof(self):
		logger.open("90_getmerkleproof.log", "90_getmerkleproof")
		(result, response) = rpcApi.getmerkleproof(txhash_false)
		logger.close(not result)

	def test_91_getmerkleproof(self):
		logger.open("91_getmerkleproof.log", "91_getmerkleproof")
		(result, response) = rpcApi.getmerkleproof("abc")
		logger.close(result)

	def test_92_getmerkleproof(self):
		logger.open("92_getmerkleproof.log", "92_getmerkleproof")
		(result, response) = rpcApi.getmerkleproof("123")
		logger.close(not result)
	
	def test_93_getmerkleproof(self):
		logger.open("93_getmerkleproof.log", "93_getmerkleproof")
		(result, response) = rpcApi.getmerkleproof(None)
		logger.close(not result)

	def test_94_getmerkleproof(self):
		logger.open("94_getmerkleproof.log", "94_getmerkleproof")
		task = Task("tasks/94_getmerkleproof.json")
		(result, response) =  run_single_task(task)
		logger.close(not result)

	def test_95_getmerkleproof(self):
		logger.open("95_getmerkleproof.log", "95_getmerkleproof")
		task = Task("tasks/95_getmerkleproof.json")
		(result, response) =  run_single_task(task)
		logger.close(not result)

	# can not test
	def test_96_getmerkleproof(self):
		logger.open("96_getmerkleproof.log", "96_getmerkleproof")
		task = Task("tasks/96_getmerkleproof.json")
		(result, response) =  run_single_task(task)
		logger.close(not result)
	
	def test_97_getmerkleproof(self):
		logger.open("97_getmerkleproof.log", "97_getmerkleproof")
		task = Task("tasks/97_getmerkleproof.json")
		(result, response) =  run_single_task(task)
		logger.close(not result)	

if __name__ == '__main__':
    unittest.main()