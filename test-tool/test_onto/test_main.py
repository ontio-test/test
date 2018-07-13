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
from utils.commonapi import *
from utils.contractapi import *
from utils.parametrizedtestcase import ParametrizedTestCase
from test_api import *
from utils.init_ong_ont import *

####################################################
#test cases
class TestOnto(ParametrizedTestCase):
    
    def setUp(self):
        '''
        time.sleep(2)
        print("stop all")
        stop_nodes([0,1,2,3,4,5,6,7])
        print("start all")
        start_nodes([0,1,2,3,4,5,6,7], Config.DEFAULT_NODE_ARGS, True, True)
        time.sleep(10)

        
        regIDWithPublicKey(0)
        regIDWithPublicKey(1)
        regIDWithPublicKey(2)
        regIDWithPublicKey(3)
        regIDWithPublicKey(4)
        regIDWithPublicKey(5)
        regIDWithPublicKey(6)
        regIDWithPublicKey(7)
        
        init_ont_ong()
        time.sleep(5)
        
        native_transfer_ont(Config.NODES[0]["address"], Config.NODES[7]["address"], "1000000", 0)
        native_transfer_ong(Config.NODES[0]["address"], Config.NODES[7]["address"], "1000", 0)
        '''
        (self.contract_addr, self.contract_tx_hash) = deploy_contract_full("./tasks/auth.neo")
        self.CONTRACT_ADDRESS_CORRECT = self.contract_addr   
        self.ontID_A = ByteToHex(bytes(Config.NODES[0]['ontid'], encoding = "utf8")) 

        time.sleep(10)
        '''
        try:
            
            # create role and bind ONTID with role
            (result, response) = bind_role_function("0700000000000000000000000000000000000000", ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),["registerCandidate"])
            if not result:
                raise Error("bind_role_function error")

            (result, response) = bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES[7]["ontid"], encoding = "utf8"))])
            if not result:
                raise Error("bind_user_role error")

            (result, response) = invoke_function_register(Config.NODES[7]["pubkey"], Config.NODES[7]["address"] ,"10000", ByteToHex(bytes(Config.NODES[7]["ontid"], encoding = "utf8")), "1", 7)
            if not result:
                raise Error("invoke_function_register error")
            
            (result, response) = invoke_function_approve(Config.NODES[7]["pubkey"])
            if not result:
                raise Error("invoke_function_approve error")
            time.sleep(10)
            
        except Exception as e:
            print(e.msg)
        '''
    
    def test_onto_1(self):
        result = False
        logger.open("test_onto_1.log", "test_onto_1")
        try:
            (result, response) = init_admin(self.CONTRACT_ADDRESS_CORRECT, self.ontID_A)

        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_onto_2(self):
        result = False
        logger.open("test_onto_2.log", "test_onto_2")
        try:
            # create role and bind ONTID with role
            (result, response) = bind_role_function("0700000000000000000000000000000000000000", ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),["registerCandidate"])
            if not result:
                raise Error("bind_role_function error")

            (result, response) = bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES[7]["ontid"], encoding = "utf8"))])
            if not result:
                raise Error("bind_user_role error")

        except Exception as e:
            print(e.msg)
        logger.close(result)



####################################################
if __name__ == '__main__':
	unittest.main()	    