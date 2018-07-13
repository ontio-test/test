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
class TestConsensus_1_4(ParametrizedTestCase):
    
    def setUp(self):
        
        time.sleep(2)
        print("stop all")
        stop_nodes([0,1,2,3,4,5,6,7,8])
        print("start all")
        start_nodes([0,1,2,3,4,5,6,7,8], Config.DEFAULT_NODE_ARGS, True, True)
        time.sleep(10)

        
        regIDWithPublicKey(0)
        regIDWithPublicKey(1)
        regIDWithPublicKey(2)
        regIDWithPublicKey(3)
        regIDWithPublicKey(4)
        regIDWithPublicKey(5)
        regIDWithPublicKey(6)
        regIDWithPublicKey(7)
        regIDWithPublicKey(8)
        
        init_ont_ong()
        time.sleep(5)
        
        native_transfer_ont(Config.NODES[0]["address"], Config.NODES[7]["address"], "1000000", 0)
        native_transfer_ong(Config.NODES[0]["address"], Config.NODES[7]["address"], "1000", 0)
        native_transfer_ont(Config.NODES[0]["address"], Config.NODES[8]["address"], "1000000", 0)
        native_transfer_ong(Config.NODES[0]["address"], Config.NODES[8]["address"], "1000", 0)

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
    
    def test_gov_1(self):
        result = False
        logger.open("TestGover1.log", "TestGover1")
        
        try:

            (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()

            # step 1 before vote get balance of wallet A B
            balance_of_wallet_A_1 = getbalance_ont(wallet_A_address)
            balance_of_wallet_B_1 = getbalance_ont(wallet_B_address)
            print("A:", balance_of_wallet_A_1)
            print("B:", balance_of_wallet_B_1)

            # step 2 wallet A vote for node B
            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
            #if not result:
            #	raise Error("vote error")

            time.sleep(10)

            # step 3 after vote get balance of wallet A B
            balance_of_wallet_A_2 = getbalance_ont(wallet_A_address)
            balance_of_wallet_B_2 = getbalance_ont(wallet_B_address)
            print("2A:", balance_of_wallet_A_2)
            print("2B:", balance_of_wallet_B_2)

            # step 4 compare
            if balance_of_wallet_B_1 != balance_of_wallet_B_2:
                raise Error("balance of wallte B changed.")
            
            if balance_of_wallet_A_1 - balance_of_wallet_A_2 != int(vote_price):
                raise Error("the decrease of balance of wallet A is not %s." % vote_price)

        except Exception as e:
            print(e.msg)
        
        logger.close(result)

    def test_gov_2(self):
        result = False
        logger.open("TestGover2.log", "TestGover2")
        try:
            
            (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
            
            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
            print (response)
            if not result:
            	raise Error("vote_for_peer error")
            
            # step 2 wallet A unvote in the same round
            (result, response) = unvote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            if not result:
            	raise Error("unvote_for_peer error")
            
            # invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            # step 3 wallet A withdraw ont
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            if not result:
            	raise Error("withdraw_ont error")
            
            # this should be failed
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], ["1"])
            if result:
            	raise Error("withdraw_ont error")
            
        except Exception as e:
            print(e.msg)
        logger.close(not result)

    def test_gov_3(self):
        result = False
        logger.open("TestGover3.log", "TestGover3")
        try:

            (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()

            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            print (response)
            #if not result:
            #	raise Error("vote error")

            # step 2 wallet A unvote in the second round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = unvote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])

            # step 3 wallet A withdraw ont in the third round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            #if not result:
            #	raise Error("withdraw_ont error")

            # this should be failed
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], ["1"])
            #if not result:
            #	raise Error("withdraw_ont error")


        except Exception as e:
            print(e.msg)
        logger.close(not result)

    def test_gov_4(self):
        result = False
        logger.open("TestGover4.log", "TestGover4")
        try:

            (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
            vote_price = "20000"
            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            print (response)
            #if not result:
            #	raise Error("vote_for_peer error")

            # step 2 wallet A unvote in the second round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = unvote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            #if not result:
            #	raise Error("unvote_for_peer error")

            # step 3 wallet A withdraw ont in the third round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            #if not result:
            #	raise Error("withdraw_ont error")

            # step 4 wallet A withdraw ont in the forth round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            #if not result:
            #	raise Error("withdraw_ont error")

            # this should be failed
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], ["1"])
            #if not result:
            #	raise Error("withdraw_ont error")

        except Exception as e:
            print(e.msg)
        logger.close(not result)

    def test_gov_15(self):
        result = False
        logger.open("TestGover15.log", "TestGover15")
        try:
            (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()		
            
            invoke_function_update("updateGlobalParam","2000000000","10000","32","10","50","50","50","50")

            time.sleep(15)
            
            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(Config.NODES[8]["address"], [node_B_puiblic_key], ["90000"], 8)
            print (response)
            #if not result:
            #	raise Error("vote_for_peer error")
            
            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], ["10000"])
            print (response)
            #if not result:
            #	raise Error("vote_for_peer error")

        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_gov_16(self):
        result = False
        logger.open("TestGover16.log", "TestGover16")
        try:
            (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()		

            invoke_function_update("updateGlobalParam","2000000000","10000","32","10","50","50","50","50")

            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(Config.NODES[8]["address"], [node_B_puiblic_key], ["90000"], 8)
            print (response)
            #if not result:
            #	raise Error("vote_for_peer error")

            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], ["10001"])
            print (response)
            #if not result:
            #	raise Error("vote_for_peer error")

        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_gov_17(self):
        result = False
        logger.open("TestGover17.log", "TestGover17")
        try:
            (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()		

            invoke_function_update("updateGlobalParam","2000000000","10000","32","10","50","50","50","50")

            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(Config.NODES[8]["address"], [node_B_puiblic_key], ["90000"], 8)
            print (response)
            #if not result:
            #	raise Error("vote_for_peer error")

            (result, response) = unvote_for_peer_index(Config.NODES[8]["address"], [node_B_puiblic_key], ["10000"], 8)

            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)

            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], ["10001"])
            print (response)
            #if not result:
            #	raise Error("vote_for_peer error")

            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = withdraw_ont_index(Config.NODES[8]["address"], [node_B_puiblic_key], ["10000"], 8)

            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], ["1000"])
        except Exception as e:
            print(e.msg)
        logger.close(result)


class TestConsensus_5_14(ParametrizedTestCase):
    
    def setUp(self):
        time.sleep(2)
        print("stop all")
        stop_nodes([0,1,2,3,4,5,6,7,8])
        print("start all")
        start_nodes([0,1,2,3,4,5,6,7,8], Config.DEFAULT_NODE_ARGS, True, True)
        time.sleep(10)

        regIDWithPublicKey(0)
        regIDWithPublicKey(1)
        regIDWithPublicKey(2)
        regIDWithPublicKey(3)
        regIDWithPublicKey(4)
        regIDWithPublicKey(5)
        regIDWithPublicKey(6)
        regIDWithPublicKey(7)
        regIDWithPublicKey(8)
        
        init_ont_ong()
        
        time.sleep(5)
        native_transfer_ont(Config.NODES[0]["address"], Config.NODES[7]["address"], "1000000", 0)
        native_transfer_ong(Config.NODES[0]["address"], Config.NODES[7]["address"], "1000", 0)
        native_transfer_ont(Config.NODES[0]["address"], Config.NODES[8]["address"], "1000000", 0)
        native_transfer_ong(Config.NODES[0]["address"], Config.NODES[8]["address"], "1000", 0)
        try:
            # create role and bind ONTID with role
            (result, response) = bind_role_function("0700000000000000000000000000000000000000", ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),["registerCandidate"])
            if not result:
                raise Error("bind_role_function error")

            (result, response) = bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES[7]["ontid"], encoding = "utf8"))])
            if not result:
                raise Error("bind_user_role error")

            (result, response) = bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES[8]["ontid"], encoding = "utf8"))])
            if not result:
                raise Error("bind_user_role error")

            (result, response) = invoke_function_register(Config.NODES[7]["pubkey"], Config.NODES[7]["address"] ,"10000", ByteToHex(bytes(Config.NODES[7]["ontid"], encoding = "utf8")), "1", 7)
            if not result:
                raise Error("invoke_function_register error")
            
            (result, response) = invoke_function_approve(Config.NODES[7]["pubkey"])
            if not result:
                raise Error("invoke_function_approve error")

            (result, response) = invoke_function_register(Config.NODES[8]["pubkey"], Config.NODES[8]["address"] ,"10000", ByteToHex(bytes(Config.NODES[8]["ontid"], encoding = "utf8")), "1", 8)
            if not result:
                raise Error("invoke_function_register error")
            
            (result, response) = invoke_function_approve(Config.NODES[8]["pubkey"])
            if not result:
                raise Error("invoke_function_approve error")
                
            time.sleep(10)
        except Exception as e:
            print(e.msg)
    
    def test_gov_5(self):
        result = False
        logger.open("TestGover5.log", "TestGover5")
        try:
            (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()

            # step 1 before vote get balance of wallet A B
            balance_of_wallet_A_1 = getbalance_ont(wallet_A_address)
            balance_of_wallet_B_1 = getbalance_ont(wallet_B_address)
            print("A:", balance_of_wallet_A_1)
            print("B:", balance_of_wallet_B_1)

            # step 2 wallet A vote for node B
            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            print (response)
            #if not result:
            #	raise Error("vote error")

            # step 3 after vote get balance of wallet A
            balance_of_wallet_A_2 = getbalance_ont(wallet_A_address)
            balance_of_wallet_B_2 = getbalance_ont(wallet_B_address)
            print("2A:", balance_of_wallet_A_2)
            print("2B:", balance_of_wallet_B_2)

            # step 4 compare
            if balance_of_wallet_B_1 != balance_of_wallet_B_2:
                raise Error("balance of wallte B changed.")

            if balance_of_wallet_A_1 - balance_of_wallet_A_2 != int(vote_price):
                raise Error("the decrease of balance of wallte A is not %s." % vote_price)


        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_gov_6(self):
        result = False
        logger.open("TestGover6.log", "TestGover6")
        try:
            (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            print (response)
            if not result:
                raise Error("vote error")

            # step 2 wallet A unvote in the same round
            (result, response) = unvote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            if not result:
                raise Error("vote error")

            # step 3 wallet A withdraw ont
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            if not result:
                raise Error("vote error")
            
            # this should be failed
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], ["1"])
            #print ("*****", response)
            #if not result:
            #	raise Error("vote error")

        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_gov_7(self):
        result = False
        logger.open("TestGover7.log", "TestGover7")
        try:
            (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
            
            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            print (response)
            #if not result:
            #	raise Error("vote error")

            # step 2 wallet A unvote in the second round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = unvote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])

            #if not result:
            #	raise Error("unvote error")


            # step 3 wallet A withdraw ont in the third round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            #if not result:
            #	raise Error("withdraw_ont error")

            # this should be failed
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], ["1"])
            #if not result:
            #	raise Error("withdraw_ont error")

        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_gov_8(self):
        result = False
        logger.open("TestGover8.log", "TestGover8")
        try:
            (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()

            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            print (response)
            #if not result:
            #	raise Error("vote_for_peer error")

            # step 2 wallet A unvote in the second round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = unvote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            #if not result:
            #	raise Error("unvote_for_peer error")

            # step 3 wallet A withdraw ont in the third round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            #if not result:
            #	raise Error("withdraw_ont error")

            # this should be failed
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], ["1"])
            #if not result:
            #	raise Error("withdraw_ont error")


        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_gov_9(self):
        result = False
        logger.open("TestGover9.log", "TestGover9")
        try:
            (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
            
            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            print (response)
            #if not result:
            #	raise Error("vote_for_peer error")

            # step 2 node b quit
            (result, response) = quit_node_index(node_B_puiblic_key, wallet_B_address, 7)
            #if not result:
            #	raise Error("quit_node error")

            # step 2 wait until the second round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            #if not result:
            #	raise Error("withdraw_ont error")

            (result, response) = unvote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            
            # step 3 wallet A withdraw ont in the third round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            #if not result:
            #	raise Error("withdraw_ont error")
            
            # this should be failed
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], ["1"])
            #if not result:
            #	raise Error("withdraw_ont error")

        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_gov_10(self):
        result = False
        logger.open("TestGover10.log", "TestGover10")
        try:
            (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()

            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            print (response)
            #if not result:
            #	raise Error("vote_for_peer error")

            # step 2 wait until the second round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = quit_node_index(node_B_puiblic_key, wallet_B_address, 7)
            
            # step 3 wallet A withdraw ont in the third round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            #if not result:
            #	raise Error("withdraw_ont error")
            (result, response) = unvote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            # step 3 wallet A withdraw ont in the forth round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            # this should be failed
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], ["1"])
            #if not result:
            #	raise Error("withdraw_ont error")
            
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_gov_11(self):
        result = False
        logger.open("TestGover11.log", "TestGover11")
        try:
            (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
            vote_price = "20000"
            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            print (response)
            #if not result:
            #	raise Error("vote_for_peer error")

            # step 2 wait until the second round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = quit_node_index(node_B_puiblic_key, wallet_B_address, 7)
            
            # step 3 wallet A withdraw ont in the third round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            #if not result:
            #	raise Error("withdraw_ont error")

            (result, response) = unvote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            # step 3 wallet A withdraw ont in the fifth round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            #if not result:
            #	raise Error("withdraw_ont error")

            # this should be failed
            (result, response) = withdraw_ont(wallet_A_address, [node_B_puiblic_key], ["1"])
            #if not result:
            #	raise Error("withdraw_ont error")

        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_gov_12(self):
        result = False
        logger.open("TestGover12.log", "TestGover12")
        try:
            (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
            
            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            print (response)
            #if not result:
            #	raise Error("vote error")

            # step 2 black node b 
            black_node([node_B_puiblic_key])
            #if not result:
            #	raise Error("black_node error")

            (result, response) = unvote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(10)
            # step 3 withdraw ont
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            #if not result:
            #	raise Error("withdraw_ont error")
            
            # this should be failed
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], ["1000"])
            #if not result:
            #	raise Error("withdraw_ont error")

        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_gov_13(self):
        result = False
        logger.open("TestGover13.log", "TestGover13")
        try:
            (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
            invoke_function_update("updateGlobalParam","2000000000","10000","32","1","50","50","50","50")
            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            print (response)
            #if not result:
            #	raise Error("vote_for_peer error")
            
            # step 2 wait until the second round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = black_node([node_B_puiblic_key])
            
            # step 3 wallet A withdraw ont in the third round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            #if not result:
            #	raise Error("withdraw_ont error")
            (result, response) = unvote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            
            # step 4 wallet A withdraw ont in the forth round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [str(int(punish_ratio*3000))])	
            #if not result:
            #	raise Error("withdraw_ont error")
            
            # this should be failed
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], ["1"])
            #if not result:
            #	raise Error("withdraw_ont error")

        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_gov_14(self):
        result = False
        logger.open("TestGover14.log", "TestGover14")
        try:
            (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()			
            invoke_function_update("updateGlobalParam","2000000000","10000","32","1","50","50","50","50")
            # step 1 wallet A vote for node B
            (result, response) = vote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            print (response)
            #if not result:
            #	raise Error("vote_for_peer error")
            
            # step 2 wait until the second round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = black_node([node_B_puiblic_key])

            # step 3 wallet A withdraw ont in the third round
            # should failed
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [vote_price])
            #if not result:
            #	raise Error("withdraw_ont error")
            
            (result, response) = unvote_for_peer_index(wallet_A_address, [node_B_puiblic_key], [vote_price])

            # step 4 wallet A withdraw ont in the forth round
            invoke_function_consensus(Config.NODES[0]["pubkey"])
            time.sleep(5)
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], [str(int(punish_ratio*3000))])
            #if not result:
            #	raise Error("withdraw_ont error")

            # this should be failed
            (result, response) = withdraw_ont_index(wallet_A_address, [node_B_puiblic_key], ["1"])
            #if not result:
            #	raise Error("withdraw_ont error")


        except Exception as e:
            print(e.msg)
        logger.close(result)



####################################################
if __name__ == '__main__':
	unittest.main()	    