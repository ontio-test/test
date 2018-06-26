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
from utils.commonapi import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from test_api import *
from test_common import *
from test_conf import Conf

logger = LoggerInstance

##########################################################
# params
local_address = "AcVb7HZB4nMDscQHXXoqKvnNFwrpL3V1u3" #本地钱包地址
transfer_address_1 = "e3462e4422c6317a93604fef74255117ed2b5328" #小端转序钱包地址
transfer_address_2 = "922fef396b3b3bb26600dc9caf27be5b16bc5e0f" #小端转序钱包地址
amount = "10" #转账ONT数量
contract_address = "376e3c853fa816727ffc82795f80c53ac3338a25" #部署地址
##########################################################

# test cases
class TestContract(ParametrizedTestCase):
    def test_01_contract(self):
        logger.open("01_contract.log", "01_contract")
        #step 1
        txHash = ""
        task1 = Task("../utils/baseapi/rpc/getblock.json")
        (result, response) = run_single_task(task1)
		#step 2
        txHash = response["result"]["Hash"]
        task2 = Task("../utils/baseapi/rpc/getblock.json")
        task2.data()["REQUEST"]["params"][0] = txHash
        (result, response) = run_single_task(task2)
        if not result:
            raise Error("send transaction error")
        logger.close(result)

    def test_02_contract(self):
        logger.open("02_contract.log", "02_contract")
        task1 = Task("../utils/baseapi/rpc/getbalance.json")
        task1.data()["REQUEST"]["params"][0] = local_address
        (result, response) = run_single_task(task1)
        ONT_before = response['result']['ont']
         #step 1
        (result, response) = invoke_function_transfer(transfer_address_1,transfer_address_2,amount)
        if not result:
            raise Error("error")
		#step 2
        (result, response) = run_single_task(task1)
        ONT_after = response['result']['ont']
        if(int(ONT_before) - int(ONT_after) != int(amount)):
            raise Error("transfer failed")
        logger.close(result)

    def test_03_contract(self):
        logger.open("03_contract.log", "03_contract")
        #step 1
        (result_, response) = invoke_function_initAuth(contract_address)
        (result, response) = invoke_function_transfer(transfer_address_1,transfer_address_2,amount)
        if not result:
            raise Error("error")
        logger.close(result)

    def test_04_contract(self):
        logger.open("04_contract.log", "04_contract")
         #step 1
        (result, response) = invoke_function_transfer(transfer_address_1,transfer_address_2,amount)
        if not result:
            raise Error("error")
        #step 2
        node_list = ["0"]
        flag = check_node_all(node_list)
        if not flag:
            raise Error("The content of the database of all nodes is not consistent")
        logger.close(result)

    def test_05_contract(self):
        logger.open("05_contract.log", "05_contract")
        #step 1
        blockCount_before = 0
        blockCount_end = 0
        task1 = Task("../utils/baseapi/rpc/getblockcount.json")
        (result, response) = run_single_task(task1)
        blockCount_before = response['result']
        
        #step 2
        txHash = ""
        task1 = Task("../utils/baseapi/rpc/getblock.json")
        (result, response) = run_single_task(task1)

        #step 3
        while(blockCount_end <= blockCount_before):
            task1 = Task("../utils/baseapi/rpc/getblockcount.json")
            (result, response) = run_single_task(task1)
            blockCount_end = response['result'] 
        
        #step 4
        (result, response) = invoke_function_transfer(transfer_address_1,transfer_address_2,amount)
        if not result:
            raise Error("error")
        logger.close(result)

    def test_06_contract(self):
        logger.open("06_contract.log", "06_contract")
        task1 = Task("../utils/baseapi/rpc/getbalance.json")
        task1.data()["REQUEST"]["params"][0] = local_address
        (result, response) = run_single_task(task1)
        ONT_before = response['result']['ont']
         #step 1
        (result, response) = invoke_function_transfer(transfer_address_1,transfer_address_2,amount)
        if not result:
            raise Error("error")
		#step 2
        (result, response) = run_single_task(task1)
        ONT_after = response['result']['ont']
        if(int(ONT_before) - int(ONT_after) != 10):
            raise Error("transfer failed")
        logger.close(result)

    def test_07_contract(self):
        logger.open("07_contract.log", "07_contract")
        #step 1
        (result_, response) = invoke_function_initAuth(contract_address)
        (result, response) = invoke_function_transfer(transfer_address_1,transfer_address_2,amount)
        if not result:
            raise Error("error")
        logger.close(result)

    def test_08_contract(self):
        logger.open("08_contract.log", "08_contract")
        #step 1
        txHash = ""
        task1 = Task("../utils/baseapi/rpc/getblock.json")
        (result, response) = run_single_task(task1)
		#step 2
        txHash = response["result"]["Hash"]
        task2 = Task("../utils/baseapi/rpc/getblock.json")
        task2.data()["REQUEST"]["params"][0] = txHash
        (result, response) = run_single_task(task2)
        if not result:
            raise Error("send transaction error")
        logger.close(result)
    
    def test_09_contract(self):
        logger.open("09_contract.log", "09_contract")
        
        for i in range(0,9):
            #step 1
            txHash = ""
            task1 = Task("../utils/baseapi/rpc/getblock.json")
            (result, response) = run_single_task(task1)
		    #step 2
            txHash = response["result"]["Hash"]
            task2 = Task("../utils/baseapi/rpc/getblock.json")
            task2.data()["REQUEST"]["params"][0] = txHash
            (result, response) = run_single_task(task2)
            if not result:
                raise Error("send transaction error")
        logger.close(result)
    
    def test_10_contract(self):
        logger.open("10_contract.log", "10_contract")
        #step 1
        txHash = ""
        task1 = Task("../utils/baseapi/rpc/getblock.json")
        (result, response) = run_single_task(task1)
		#step 2
        txHash = response["result"]["Hash"]
        task2 = Task("../utils/baseapi/rpc/getblock.json")
        task2.data()["REQUEST"]["params"][0] = txHash
        (result, response) = run_single_task(task2)
        if not result:
            raise Error("send transaction error")
        logger.close(result)
    
    def test_11_contract(self):
        logger.open("11_contract.log", "11_contract")
        task1 = Task("../utils/baseapi/rpc/getbalance.json")
        task1.data()["REQUEST"]["params"][0] = local_address
        (result, response) = run_single_task(task1)
        ONT_before = response['result']['ont']
         #step 1
        (result, response) = invoke_function_transfer(transfer_address_1,transfer_address_2,amount)
        if not result:
            raise Error("error")
		#step 2
        (result, response) = run_single_task(task1)
        ONT_after = response['result']['ont']
        if(int(ONT_before) - int(ONT_after) != 10):
            raise Error("transfer failed")
        logger.close(result)
    
    def test_12_contract(self):
        logger.open("12_contract.log", "12_contract")
        #step 1
        (result_, response) = invoke_function_initAuth(contract_address)
        (result, response) = invoke_function_transfer(transfer_address_1,transfer_address_2,amount)
        if not result:
            raise Error("error")
        logger.close(result)
    
    def test_13_contract(self):
        logger.open("13_contract.log", "13_contract")
        
        for i in range(0,9):
            #step 1
            txHash = ""
            task1 = Task("../utils/baseapi/rpc/getblock.json")
            (result, response) = run_single_task(task1)
		    #step 2
            txHash = response["result"]["Hash"]
            task2 = Task("../utils/baseapi/rpc/getblock.json")
            task2.data()["REQUEST"]["params"][0] = txHash
            (result, response) = run_single_task(task2)
            if not result:
                raise Error("send transaction error")
        logger.close(result)
    
    def test_14_contract(self):
        logger.open("14_contract.log", "14_contract")
        #step 1
        txHash = ""
        task1 = Task("../utils/baseapi/rpc/getblock.json")
        (result, response) = run_single_task(task1)
		#step 2
        txHash = response["result"]["Hash"]
        task2 = Task("../utils/baseapi/rpc/getblock.json")
        task2.data()["REQUEST"]["params"][0] = txHash
        (result, response) = run_single_task(task2)
        if not result:
            raise Error("send transaction error")
        logger.close(result)

    def test_15_contract(self):
        logger.open("15_contract.log", "15_contract")
        task1 = Task("../utils/baseapi/rpc/getbalance.json")
        task1.data()["REQUEST"]["params"][0] = local_address
        (result, response) = run_single_task(task1)
        ONT_before = response['result']['ont']
         #step 1
        (result, response) = invoke_function_transfer(transfer_address_1,transfer_address_2,amount)
        if not result:
            raise Error("error")
		#step 2
        (result, response) = run_single_task(task1)
        ONT_after = response['result']['ont']
        if(int(ONT_before) - int(ONT_after) != 10):
            raise Error("transfer failed")
        logger.close(result)

    def test_16_contract(self):
        logger.open("16_contract.log", "16_contract")
        #step 1
        (result_, response) = invoke_function_initAuth(contract_address)
        (result, response) = invoke_function_transfer(transfer_address_1,transfer_address_2,amount)
        if not result:
            raise Error("error")
        logger.close(result)
    
    def test_17_contract(self):
        logger.open("17_contract.log", "17_contract")
         #step 1
        (result, response) = invoke_function_transfer(transfer_address_1,transfer_address_2,amount)
        if not result:
            raise Error("error")
        #step 2
        node_list = ["0"]
        flag = check_node_all(node_list)
        if not flag:
            raise Error("The content of the database of all nodes is not consistent")
        logger.close(result)


####################################################
if __name__ == '__main__':
    unittest.main()