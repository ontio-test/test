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
voteList_1 = "120203b82582103c4de05f355897e29caa556274dbd5a670bc1a9b4bbb4ad8d2027783" #已经在网络中的共识节点公钥数组
voteList_2 = "120203b82582103c4de05f355897e29caa556274dbd5a670bc1a9b4bbb4ad8d2027783" #已经在网络中的候选节点公钥数组
voteList_3 = "120203b82582103c4de05f355897e29caa556274dbd5a670bc1a9b4bbb4ad8d2027783" #未申请的节点公钥数组
voteList_4 = "120203b82582103c4de05f355897e29caa556274dbd5a670bc1a9b4bbb4ad8d2027783" #已经申请的节点公钥数组
voteList_5 = "120203b82582103c4de05f355897e29caa556274dbd5a670bc1a9b4bbb4ad8d2027783" #乱码
voteList_6 = "120203b82582103c4de05f355897e29caa556274dbd5a670bc1a9b4bbb4ad8d2027783" #留空
voteCount_1 = "2" #与公钥数组一一对应的不同票数的数组，数组总值低于钱包内存在的ont数量
voteCount_2 = "2" #与公钥数组一一对应的不同票数的数组，数组总值高于钱包内存在的ont数量
voteCount_3 = "2" #比公钥数组数量少的票数数组
voteCount_4 = "2" #乱码
voteCount_5 = "2" #留空
####################################################

# test cases
class TestVoteForPeer(ParametrizedTestCase):
    def test_48_VoteForPeer(self):
        logger.open("48_VoteForPeer.log", "48_VoteForPeer")
        (result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_49_VoteForPeer(self):
        logger.open("49_VoteForPeer.log", "49_VoteForPeer")
        (result, response) = invoke_function_vote("voteForPeer",walletAddress_2,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_50_VoteForPeer(self):
        logger.open("50_VoteForPeer.log", "50_VoteForPeer")
        (result, response) = invoke_function_vote("voteForPeer",walletAddress_3,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    def test_51_VoteForPeer(self):
        logger.open("51_VoteForPeer.log", "51_VoteForPeer")
        (result, response) = invoke_function_vote("voteForPeer",walletAddress_4,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_52_VoteForPeer(self):
        logger.open("52_VoteForPeer.log", "52_VoteForPeer")
        (result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_53_VoteForPeer(self):
        logger.open("53_VoteForPeer.log", "53_VoteForPeer")
        (result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_2,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_54_VoteForPeer(self):
        logger.open("54_VoteForPeer.log", "54_VoteForPeer")
        (result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_3,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_55_VoteForPeer(self):
        logger.open("55_VoteForPeer.log", "55_VoteForPeer")
        (result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_4,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_56_VoteForPeer(self):
        logger.open("56_VoteForPeer.log", "56_VoteForPeer")
        (result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_5,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_57_VoteForPeer(self):
        logger.open("57_VoteForPeer.log", "57_VoteForPeer")
        (result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_6,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_58_VoteForPeer(self):
        logger.open("58_VoteForPeer.log", "58_VoteForPeer")
        (result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_59_VoteForPeer(self):
        logger.open("59_VoteForPeer.log", "59_VoteForPeer")
        (result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_2)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_60_VoteForPeer(self):
        logger.open("60_VoteForPeer.log", "60_VoteForPeer")
        (result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_3)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_61_VoteForPeer(self):
        logger.open("61_VoteForPeer.log", "61_VoteForPeer")
        (result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_4)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_62_VoteForPeer(self):
        logger.open("62_VoteForPeer.log", "62_VoteForPeer")
        (result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_5)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_63_VoteForPeer(self):
        logger.open("63_VoteForPeer.log", "63_VoteForPeer")
        (result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_6,voteCount_5)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()