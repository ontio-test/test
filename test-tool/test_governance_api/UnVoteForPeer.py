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
walletAddress_1 = "AV6qj3uZngw1rxzNUANBHybnKPibXhWB2h" #自己的钱包地址
walletAddress_2 = "AV6qj3uZngw1rxzNUANBHybnKPibXhWB2h" #其他人的钱包地址
walletAddress_3 = "AV6qj3uZngw1rxzNUANBHybnKPibXhWB2h" #乱码
walletAddress_4 = "AV6qj3uZngw1rxzNUANBHybnKPibXhWB2h" #留空
voteList_1 = "120203b82732103c4de05f371897e29caa717774dbd5a670bc1a9b4bbb4ad8d2027783" #投过票的节点公钥数组
voteList_2 = "120203b82732103c4de05f371897e29caa717774dbd5a670bc1a9b4bbb4ad8d2027783" #未投过票的节点公钥数组
voteList_3 = "120203b82732103c4de05f371897e29caa717774dbd5a670bc1a9b4bbb4ad8d2027783" #投过票+未投过票的节点公钥数组
voteList_4 = "120203b82732103c4de05f371897e29caa717774dbd5a670bc1a9b4bbb4ad8d2027783" #乱码
voteList_5 = "120203b82732103c4de05f371897e29caa717774dbd5a670bc1a9b4bbb4ad8d2027783" #留空
voteCount_1 = "2" #与公钥数组一一对应的不同票数的数组，数组总值低于钱包内存在的ont数量
voteCount_2 = "2" #与公钥数组一一对应的不同票数的数组，数组总值高于钱包内存在的ont数量
voteCount_3 = "2" #比公钥数组数量少的票数数组
voteCount_4 = "2" #乱码
voteCount_5 = "2" #留空
####################################################

# test cases
class TestunVoteForPeer(ParametrizedTestCase):
    def test_64_unVoteForPeer(self):
        logger.open("64_unVoteForPeer.log", "64_unVoteForPeer")
        (result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_65_unVoteForPeer(self):
        logger.open("65_unVoteForPeer.log", "65_unVoteForPeer")
        (result, response) = invoke_function_vote("unVoteForPeer",walletAddress_2,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_66_unVoteForPeer(self):
        logger.open("66_unVoteForPeer.log", "66_unVoteForPeer")
        (result, response) = invoke_function_vote("unVoteForPeer",walletAddress_3,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    def test_67_unVoteForPeer(self):
        logger.open("67_unVoteForPeer.log", "67_unVoteForPeer")
        (result, response) = invoke_function_vote("unVoteForPeer",walletAddress_4,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_68_unVoteForPeer(self):
        logger.open("68_unVoteForPeer.log", "68_unVoteForPeer")
        (result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_69_unVoteForPeer(self):
        logger.open("69_unVoteForPeer.log", "69_unVoteForPeer")
        (result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_2,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_70_unVoteForPeer(self):
        logger.open("70_unVoteForPeer.log", "70_unVoteForPeer")
        (result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_3,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_71_unVoteForPeer(self):
        logger.open("71_unVoteForPeer.log", "71_unVoteForPeer")
        (result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_4,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_72_unVoteForPeer(self):
        logger.open("72_unVoteForPeer.log", "72_unVoteForPeer")
        (result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_5,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_73_unVoteForPeer(self):
        logger.open("73_unVoteForPeer.log", "73_unVoteForPeer")
        (result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_74_unVoteForPeer(self):
        logger.open("74_unVoteForPeer.log", "74_unVoteForPeer")
        (result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_1,voteCount_2)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_75_unVoteForPeer(self):
        logger.open("75_unVoteForPeer.log", "75_unVoteForPeer")
        (result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_1,voteCount_3)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_76_unVoteForPeer(self):
        logger.open("76_unVoteForPeer.log", "76_unVoteForPeer")
        (result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_1,voteCount_4)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_77_unVoteForPeer(self):
        logger.open("77_unVoteForPeer.log", "77_unVoteForPeer")
        (result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_1,voteCount_5)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_78_unVoteForPeer(self):
        logger.open("78_unVoteForPeer.log", "78_unVoteForPeer")
        (result, response) = invoke_function_vote("unVoteForPeer",walletAddress_1,voteList_5,voteCount_5)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()