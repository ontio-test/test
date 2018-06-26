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
voteList_1 = "120203b82882103c4de05f386897e29caa869274dbd5a670bc1a9b4bbb4ad8d2027783" #取消过投票的节点公钥数组
voteList_2 = "120203b82882103c4de05f386897e29caa869274dbd5a670bc1a9b4bbb4ad8d2027783" #未取消过投票的节点公钥数组
voteList_3 = "120203b82882103c4de05f386897e29caa869274dbd5a670bc1a9b4bbb4ad8d2027783" #未投过票的节点公钥数组
voteList_4 = "120203b82882103c4de05f386897e29caa869274dbd5a670bc1a9b4bbb4ad8d2027783" #乱码
voteList_5 = "120203b82882103c4de05f386897e29caa869274dbd5a670bc1a9b4bbb4ad8d2027783" #留空
voteCount_1 = "2" #与公钥数组一一对应的不同票数的数组，数组总值低于钱包内存在的ont数量
voteCount_2 = "2" #与公钥数组一一对应的不同票数的数组，数组总值高于钱包内存在的ont数量
voteCount_3 = "2" #比公钥数组数量少的票数数组
voteCount_4 = "2" #乱码
voteCount_5 = "2" #留空
####################################################

# test cases
class Testwithdraw(ParametrizedTestCase):
    def test_79_withdraw(self):
        logger.open("79_withdraw.log", "79_withdraw")
        (result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_80_withdraw(self):
        logger.open("80_withdraw.log", "80_withdraw")
        (result, response) = invoke_function_vote("withdraw",walletAddress_2,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_81_withdraw(self):
        logger.open("81_withdraw.log", "81_withdraw")
        (result, response) = invoke_function_vote("withdraw",walletAddress_3,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    def test_82_withdraw(self):
        logger.open("82_withdraw.log", "82_withdraw")
        (result, response) = invoke_function_vote("withdraw",walletAddress_4,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_83_withdraw(self):
        logger.open("83_withdraw.log", "83_withdraw")
        (result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_84_withdraw(self):
        logger.open("84_withdraw.log", "84_withdraw")
        (result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_2,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_85_withdraw(self):
        logger.open("85_withdraw.log", "85_withdraw")
        (result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_3,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_86_withdraw(self):
        logger.open("86_withdraw.log", "86_withdraw")
        (result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_4,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)

    def test_87_withdraw(self):
        logger.open("87_withdraw.log", "87_withdraw")
        (result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_5,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_88_withdraw(self):
        logger.open("88_withdraw.log", "88_withdraw")
        (result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_1,voteCount_1)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_89_withdraw(self):
        logger.open("89_withdraw.log", "89_withdraw")
        (result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_1,voteCount_2)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_90_withdraw(self):
        logger.open("90_withdraw.log", "90_withdraw")
        (result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_1,voteCount_3)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_91_withdraw(self):
        logger.open("91_withdraw.log", "91_withdraw")
        (result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_1,voteCount_4)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_92_withdraw(self):
        logger.open("92_withdraw.log", "92_withdraw")
        (result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_1,voteCount_5)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_93_withdraw(self):
        logger.open("93_withdraw.log", "93_withdraw")
        (result, response) = invoke_function_vote("withdraw",walletAddress_1,voteList_5,voteCount_5)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()