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
from utils.contractapi import *
from utils.commonapi import *
from utils.init_ong_ont import *
from test_api import *
from test_common import *
logger = LoggerInstance

####################################################
# test cases
class TestMutiContract(ParametrizedTestCase):
    def setUp(self):
        
        time.sleep(2)
        print("stop all")
        stop_all_nodes()
        print("start all")
        start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
        time.sleep(10)
        for i in range(0, 7):
            regIDWithPublicKey(i)

        init_ont_ong()
        

    def test_01(self):
        logger.open("TestMutiContract_1.log", "TestMutiContract_1")
        result = False
        try:
            contract_address = set_premise("tasks/1-32/A.neo")
            # setp 1 绑定用户A拥有roleA角色
            (result, response) = bind_user_role(contract_address, Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise(Error("bind_user_role error"))

            # setp 2 用户A访问A函数
            (result, response) = invoke_function(contract_address, "A", Config.ontID_A)
            if not result:
                raise Error("invoke_function error")
            
            result = (response["result"]["Result"] != "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_02(self):
        logger.open("TestMutiContract_2.log", "TestMutiContract_2")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定用户A拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
            
            # setp 2 用户A访问A函数
            (result, response) = invoke_function(contract_address, "C", Config.ontID_A)
            if not result:
                raise Error("invoke_function error")
        
            result = (response["result"]["Result"] != "00")
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_03(self):
        logger.open("TestMutiContract_3.log", "TestMutiContract_3")
        result = False
        try:
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定用户A拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
            
            # setp 2 用户A访问A函数
            (result, response) = invoke_function(contract_address, "B", Config.ontID_A)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] == "00")

        except Exception as e:
            print(e.msg)
        logger.close(result)


    def test_04(self):
        logger.open("TestMutiContract_4.log", "TestMutiContract_4")
        result = False
        try:
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定用户A拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
            # setp 2 绑定用户A拥有roleB角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleB_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
            # setp 3 用户A访问A函数
            (result, response) = invoke_function(contract_address, "B", Config.ontID_A)
            if not result:
                raise Error("invoke_function error")
            
            result = (response["result"]["Result"] != "00")
            
        except Exception as e:
            print(e.msg)
        logger.close(result)
        
    def test_05(self):
        logger.open("TestMutiContract_5.log", "TestMutiContract_5")
        result = False
        try:
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定角色绑定到用户
            (result, response) = bind_user_role(contract_address, Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
            
            (result, response) = bind_user_role(contract_address, Config.ontID_A, Config.roleB_hex, [Config.ontID_B])
            if not result:
                raise("bind_user_role error")
            
            # setp 1 用户B授权用户A拥有角色B的权限
            (result, response) = delegate_user_role(contract_address, Config.ontID_B, Config.ontID_A, Config.roleB_hex, "100", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 2 用户A访问B函数
            (result, response) = invoke_function(contract_address, "B", Config.ontID_A)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] != "00")
            
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_06(self):
        logger.open("TestMutiContract_6.log", "TestMutiContract_6")
        result = False
        try:
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定roleA角色绑定到用户A
            (result, response) = bind_user_role(contract_address, Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
            
            # setp 1 绑定roleB角色绑定到用户B
            (result, response) = bind_user_role(contract_address, Config.ontID_A, Config.roleB_hex, [Config.ontID_B])
            if not result:
                raise("bind_user_role error")
            
            # setp 1 用户B授权用户A拥有角色B的权限 5 秒
            (result, response) = delegate_user_role(contract_address, Config.ontID_B, Config.ontID_A, Config.roleB_hex, "5", "1")
            if not result:
                raise("bind_user_role error")
            
            print("wait.......60s")
            time.sleep(60)            

            # setp 2 用户A访问B函数
            (result, response) = invoke_function(contract_address, "B", Config.ontID_A)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] == "00")
            
        except Exception as e:
            print(e.msg)
        logger.close(result)
        
    def test_07(self):
        logger.open("TestMutiContract_7.log", "TestMutiContract_7")
        result = False
        try:
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定roleA角色绑定到用户A
            (result, response) = bind_user_role(contract_address, Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
            
            # setp 1 绑定roleB角色绑定到用户B
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleB_hex, [Config.ontID_B])
            if not result:
                raise("bind_user_role error")
            
            # setp 1 用户B授权用户A拥有角色B的权限
            (result, response) = delegate_user_role(contract_address, Config.ontID_B, Config.ontID_A, Config.roleB_hex, "5", "1")
            if not result:
                raise("bind_user_role error")
                
            print("wait.......60s")
            time.sleep(60)
            
            # setp 2 用户A访问C函数
            (result, response) = invoke_function(contract_address, "C", Config.ontID_A)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] != "00")
            
        except Exception as e:
            print(e.msg)
        
        logger.close(result)

    def test_08(self):
        logger.open("TestMutiContract_8.log", "TestMutiContract_8")
        result = False
        try:
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定用户A拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
            
            # setp 2 绑定用户B拥有roleB角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleB_hex, [Config.ontID_B])
            if not result:
                raise("bind_user_role error")
    
            # setp 3 用户B授权用户A拥有角色B的权限
            (result, response) = delegate_user_role(contract_address, Config.ontID_B, Config.ontID_A, Config.roleB_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 4 收回授权用户A拥有的roleB角色
            (result, response) = withdraw_user_role(contract_address, Config.ontID_B, Config.ontID_A, Config.roleB_hex)
            if not result:
                raise("bind_user_role error")
                        
            # setp 5 用户A访问B函数
            (result, response) = invoke_function(contract_address, "B", Config.ontID_A)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] == "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_09(self):
        logger.open("TestMutiContract_9.log", "TestMutiContract_9")
        result = False
        try:
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定用户A拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
            
            # setp 1 绑定用户B拥有roleB角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleB_hex, [Config.ontID_B])
            if not result:
                raise("bind_user_role error")
            
            # setp 1 用户B授权用户A拥有角色B的权限
            (result, response) = delegate_user_role(contract_address, Config.ontID_B, Config.ontID_A, Config.roleB_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 1 收回授权用户A拥有的roleB角色
            (result, response) = withdraw_user_role(contract_address, Config.ontID_B, Config.ontID_A, Config.roleB_hex)
            if not result:
                raise("bind_user_role error")
            
            # setp 2 用户A访问B函数
            (result, response) = invoke_function(contract_address, "C", Config.ontID_A)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] != "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
   
    def test_10(self):
        logger.open("TestMutiContract_10.log", "TestMutiContract_10")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定roleA角色绑定到用户A
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
            
            # setp 1 用户A授权用户A拥有roleA的权限
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex, "5", "1")
            
            result = (response["result"]["Result"] == "00")
        except Exception as e:
            print(e.msg)
        logger.close(result)
    '''   
    def test_11(self):
        logger.open("TestMutiContract_11.log", "TestMutiContract_11")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定roleA角色绑定到用户A
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
            
            # setp 1 用户A授权用户A拥有roleA的权限
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex, "5", "1")
            if not result:
                raise("bind_user_role error")
            
            print("wait 60s.....")
            time.sleep(60)

            # setp 2 用户A访问C函数
            (result, response) = invoke_function(contract_address, "B", Config.ontID_A)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] == "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_12(self):
        logger.open("TestMutiContract_12.log", "TestMutiContract_12")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定roleA角色绑定到用户A
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
            
            # setp 1 用户A授权用户A拥有roleA的权限
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex, "5", "1")
            if not result:
                raise("bind_user_role error")
            
            print("wait 60s.....")
            time.sleep(60)

            # setp 2 用户A访问C函数
            (result, response) = invoke_function(contract_address, "A", Config.ontID_A)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] != "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
        
    def test_13(self):
        logger.open("TestMutiContract_13.log", "TestMutiContract_13")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定roleA角色绑定到用户A
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
            
            # setp 2 授权用户A拥有roleA角色，level1
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 3 收回授权用户A拥有的roleA角色
            (result, response) = withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex)
            if not result:
                raise("bind_user_role error")
            
            # setp 4 用户A访问A函数
            (result, response) = invoke_function(contract_address, "A", Config.ontID_A)
            if not result:
                raise Error("invoke_function error")

            result = (response["result"]["Result"] != "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_14(self):
        logger.open("TestMutiContract_14.log", "TestMutiContract_14")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定roleA角色绑定到用户A
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
            
            # setp 2 授权用户A拥有roleA角色，level1
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 3 收回授权用户A拥有的roleA角色
            (result, response) = withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex)
            if not result:
                raise("bind_user_role error")
            
            # setp 4 用户A访问C函数
            (result, response) = invoke_function(contract_address, "C", Config.ontID_A)
            if not result:
                raise Error("invoke_function error")

            result = (response["result"]["Result"] != "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_15(self):
        logger.open("TestMutiContract_15.log", "TestMutiContract_15")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定roleA角色绑定到用户A
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
            
            # setp 2 授权用户A拥有roleA角色，level1
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 3 收回授权用户A拥有的roleA角色
            (result, response) = withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_A, Config.roleA_hex)
            if not result:
                raise("bind_user_role error")
            
            # setp 4 用户A访问C函数
            (result, response) = invoke_function(contract_address, "B", Config.ontID_A)
            if not result:
                raise Error("invoke_function error")

            result = (response["result"]["Result"] == "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
    '''
    def test_16(self):
        logger.open("TestMutiContract_16.log", "TestMutiContract_16")
        result = False
        try:
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定roleA角色绑定到用户A,B
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
            if not result:
                raise("bind_user_role error")
            
            # setp 2 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
               
            result = (response["result"]["Result"] == "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
    '''    
    def test_17(self):
        logger.open("TestMutiContract_17.log", "TestMutiContract_17")
        result = False
        try:
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定roleA角色绑定到用户A,B
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
            if not result:
                raise("bind_user_role error")
            
            # setp 2 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 3 用户A收回用户B拥有的roleA角色，level1的授权
            (result, response) = withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex)
            if not result:
                raise("bind_user_role error")
            
            # setp 4 用户B访问A函数
            (result, response) = invoke_function(contract_address, "B", Config.ontID_B)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] == "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_18(self):
        logger.open("TestMutiContract_18.log", "TestMutiContract_18")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")
            
            # setp 1 绑定roleA角色绑定到用户A, B
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
            if not result:
                raise("bind_user_role error")
            
            # setp 2 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "5", "1")
            if not result:
                raise("bind_user_role error")
            
            print("wait 60s...")
            time.sleep(60)
            
            # setp 2 用户B访问B函数
            (result, response) = invoke_function(contract_address, "A", Config.ontID_B)
            if not result:
                raise Error("invoke_function error")
            result = (response["result"]["Result"] != "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
        
    def test_19(self):
        logger.open("TestMutiContract_19.log", "TestMutiContract_19")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")
            
            # setp 1 绑定roleA角色绑定到用户A, B
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
            if not result:
                raise("bind_user_role error")
            
            # setp 2 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "5", "1")
            if not result:
                raise("bind_user_role error")
            
            print("wait 60s...")
            time.sleep(60)
            
            # setp 2 用户B访问B函数
            (result, response) = invoke_function(contract_address, "B", Config.ontID_B)
            if not result:
                raise Error("invoke_function error")
            result = (response["result"]["Result"] == "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_20(self):
        logger.open("TestMutiContract_20.log", "TestMutiContract_20")
        result = False
        try:
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 2 绑定用户A拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
                        
            # setp 3 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 4 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10", "1")
            if not result:
                raise("bind_user_role error")
            
            print("wait 60s...")
            time.sleep(60)
            
            # setp 2 用户B访问A函数
            (result, response) = invoke_function(contract_address, "A", Config.ontID_B)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] == "00")
            
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_21(self):
        logger.open("TestMutiContract_21.log", "TestMutiContract_21")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定用户A拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
                        
            # setp 2 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 3 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "100", "1")
            if not result:
                raise("bind_user_role error")
            
            time.sleep(60)
            
            # setp 4 用户B访问A函数
            (result, response) = invoke_function(contract_address, "A", Config.ontID_B)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] != "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_22(self):
        logger.open("TestMutiContract_22.log", "TestMutiContract_22")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定用户A拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
                        
            # setp 2 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "20", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 3 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "30", "1")
            if not result:
                raise("bind_user_role error")
            
            time.sleep(60)
            
            # setp 4 用户B访问A函数
            (result, response) = invoke_function(contract_address, "A", Config.ontID_B)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] == "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
        
    def test_23(self):
        logger.open("TestMutiContract_23.log", "TestMutiContract_23")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定用户A拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
                        
            # setp 2 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "20", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 3 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "30", "1")
            if not result:
                raise("bind_user_role error")
            
            time.sleep(60)
            
            # setp 4 用户B访问A函数
            (result, response) = invoke_function(contract_address, "B", Config.ontID_B)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] == "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_24(self):
        logger.open("TestMutiContract_24.log", "TestMutiContract_24")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定用户A拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
                        
            # setp 2 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 3 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 4 用户A撤回用户B拥有的roleA角色
            (result, response) = withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex)
            if not result:
                raise("bind_user_role error")
            
            # setp 5 用户B不可以访问A函数
            (result, response) = invoke_function(contract_address, "A", Config.ontID_B)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] == "00")

        except Exception as e:
            print(e.msg)
        logger.close(result)
    '''    
    def test_25(self):
        logger.open("TestMutiContract_25.log", "TestMutiContract_25")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定用户A，用户B拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
            if not result:
                raise("bind_user_role error")
                        
            # setp 2 用户A授权用户C拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 3 用户B授权用户C拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_B, Config.ontID_C, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
                
            result = (response["result"]["Result"] == "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
    '''
    def test_26(self):
        logger.open("TestMutiContract_26.log", "TestMutiContract_26")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定用户A，用户B拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
            if not result:
                raise("bind_user_role error")
                        
            # setp 2 用户A授权用户C拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 3 用户B授权用户C拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_B, Config.ontID_C, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
                        
            # setp 4 用户A撤回用户C拥有的roleA角色
            (result, response) = withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex)
            if not result:
                raise("bind_user_role error")
            
            # setp 5 用户C访问A函数
            (result, response) = invoke_function(contract_address, "B", Config.ontID_C)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] == "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_27(self):
        logger.open("TestMutiContract_27.log", "TestMutiContract_27")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定用户A，用户B拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
            if not result:
                raise("bind_user_role error")
                        
            # setp 1 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex, "10", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 1 用户B授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_B, Config.ontID_C, Config.roleA_hex, "100", "1")
            if not result:
                raise("bind_user_role error")
                        
            time.sleep(60)
            
            # setp 2 用户C访问A函数
            (result, response) = invoke_function(contract_address, "A", Config.ontID_C)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] != "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_28(self):
        logger.open("TestMutiContract_28.log", "TestMutiContract_28")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定用户A，用户B拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
            if not result:
                raise("bind_user_role error")
                        
            # setp 1 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex, "10", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 1 用户B授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_B, Config.ontID_C, Config.roleA_hex, "20", "1")
            if not result:
                raise("bind_user_role error")
                        
            time.sleep(60)
            
            # setp 2 用户C访问A函数
            (result, response) = invoke_function(contract_address, "A", Config.ontID_C)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] == "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
        
    def test_29(self):
        logger.open("TestMutiContract_29.log", "TestMutiContract_29")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定用户A，用户B拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
            if not result:
                raise("bind_user_role error")
                        
            # setp 1 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 1 用户B授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_B, Config.ontID_C, Config.roleA_hex, "10", "1")
            if not result:
                raise("bind_user_role error")
                        
            time.sleep(60)
            
            # setp 2 用户C访问A函数
            (result, response) = invoke_function(contract_address, "A", Config.ontID_C)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] != "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
    '''
    def test_30(self):
        logger.open("TestMutiContract_30.log", "TestMutiContract_30")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定用户A，用户B拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
            if not result:
                raise("bind_user_role error")
            
            # setp 1 绑定用户A，用户B拥有roleB角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleB_hex, [Config.ontID_A, Config.ontID_B])
            if not result:
                raise("bind_user_role error")
                        
            # setp 1 用户A授权用户C拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 1 用户B授权用户C拥有roleB角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_B, Config.ontID_C, Config.roleB_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
                        
            # setp 1 用户A撤回用户C拥有的roleA角色
            (result, response) = withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex)
            if not result:
                raise("bind_user_role error")

            # setp 2 用户C访问B函数
            (result, response) = invoke_function(contract_address, "B", Config.ontID_C)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] != "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
        
    def test_31(self):
        logger.open("TestMutiContract_31.log", "TestMutiContract_31")
        result = False
        try:
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定用户A，用户B拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
            if not result:
                raise("bind_user_role error")
            
            # setp 1 绑定用户A，用户B拥有roleB角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleB_hex, [Config.ontID_B])
            if not result:
                raise("bind_user_role error")
                        
            # setp 1 用户A授权用户C拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 1 用户B授权用户C拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_B, Config.ontID_C, Config.roleB_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
                        
            # setp 1 用户A撤回用户C拥有的roleB角色
            (result, response) = withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleB_hex)
            if not result:
                raise("bind_user_role error")
                
            result = (response["result"]["Result"] == "00")

            # # setp 2 用户C访问B函数
            # (result, response) = invoke_function(contract_address, "B")
            # if not result:
            #     raise Error("invoke_function error")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
    '''
    def test_32(self):
        logger.open("TestMutiContract_32.log", "TestMutiContract_32")
        result = False
        try:
            
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定用户A，用户B拥有roleA角色
            (result, response) = bind_user_role(contract_address,Config.ontID_A, Config.roleA_hex, [Config.ontID_A, Config.ontID_B])
            if not result:
                raise("bind_user_role error")
            
            # setp 2 用户A授权用户C拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
            
            # setp 3 用户B授权用户C拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Config.ontID_B, Config.ontID_C, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
                        
            # setp 4 用户A撤回用户C拥有的roleA角色
            (result, response) = withdraw_user_role(contract_address, Config.ontID_A, Config.ontID_C, Config.roleA_hex)
            if not result:
                raise("bind_user_role error")

            # setp 5 用户C访问B函数
            (result, response) = invoke_function(contract_address, "B", Config.ontID_C)
            if not result:
                raise Error("invoke_function error")
            
            result = (response["result"]["Result"] == "00")
    
        except Exception as e:
            print(e.msg)
        logger.close(result)
    '''
    def test_33(self):
        logger.open("TestMutiContract_33.log", "TestMutiContract_33")
        result = False
        try:
            (contract_address_A, contract_address_B) = set_premise_a("tasks/33-37/A.neo", "tasks/33-37/B.neo")

            # A用户去调用A方法
            (result, response) = invoke_function(contract_address_A, "contractA_Func_A",Config.ontID_A)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] != "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_34(self):
        logger.open("TestMutiContract_34.log", "TestMutiContract_34")
        result = False
        try:
            (contract_address_A, contract_address_B) = set_premise_a("tasks/33-37/A.neo", "tasks/33-37/B.neo")

            # B用户去调用A方法
            (result, response) = invoke_function(contract_address_A, "contractA_Func_A", Config.ontID_B)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] == "00")        
        except Exception as e:
            print(e.msg)
        logger.close(result)
        
    def test_35(self):
        logger.open("TestMutiContract_35.log", "TestMutiContract_35")
        result = False
        try:
            (contract_address_A, contract_address_B) = set_premise_a("tasks/33-37/A.neo", "tasks/33-37/B.neo")
            
            # setp 1 用户A授权用户B拥有角色A的权限
            (result, response) = delegate_user_role(contract_address_B, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")

            # B用户去调用A方法
            (result, response) = invoke_function(contract_address_A, "contractA_Func_A", Config.ontID_B)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] != "00")        
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_36(self):
        logger.open("TestMutiContract_36.log", "TestMutiContract_36")
        result = False
        try:
            (contract_address_A, contract_address_B) = set_premise_a("tasks/33-37/A.neo", "tasks/33-37/B.neo")

            # setp 1 用户A授权用户B拥有角色A的权限
            (result, response) = delegate_user_role(contract_address_B, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "5", "1")
            if not result:
                raise("bind_user_role error")

            # ==================================================================
            print("wait 60s...")
            time.sleep(60)

            # B用户去调用A方法
            (result, response) = invoke_function(contract_address_A, "contractA_Func_A", Config.ontID_B)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] == "00")        
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
        
    def test_37(self):
        pass

    def test_38(self):
        logger.open("TestMutiContract_38.log", "TestMutiContract_38")
        result = False
        try:
            (contract_address) = set_premise_b("tasks/38-43_48-59/A.neo")

            # 用户A调用智能合约A中的A方法
            (result, response) = invoke_function(contract_address, "transfer", Config.ontID_A, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_B]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "int",
                                                                                    "value": "10"
                                                                                }])
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] != "00")        
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_39(self):
        logger.open("TestMutiContract_39.log", "TestMutiContract_39")
        result = False
        try:
            contract_address = set_premise_b("tasks/38-43_48-59/A.neo")

            # setp 1 用户A授权用户B拥有角色A的权限
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error") 

            # 用户B调用智能合约A中的A方法
            (result, response) = invoke_function(contract_address, "transfer", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_B]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "int",
                                                                                    "value": "10"
                                                                                }])
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] != "00")        
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_40(self):
        logger.open("TestMutiContract_40.log", "TestMutiContract_40")
        result = False
        try:
            contract_address = set_premise_b("tasks/38-43_48-59/A.neo")

            # setp 1 用户A授权用户B拥有角色A的权限
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")  

            # 用户B调用智能合约A中的A方法
            (result, response) = invoke_function(contract_address, "transfer", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_B]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "int",
                                                                                    "value": "10"
                                                                                }])
                
            result = (not result or response["result"]["Result"] == "00")        
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
        
    def test_41(self):
        logger.open("TestMutiContract_41.log", "TestMutiContract_41")
        result = False
        try:
            contract_address = set_premise_b("tasks/38-43_48-59/A.neo")

            # setp 1 用户A授权用户B拥有角色A的权限
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")

            # 用户B调用智能合约A中的A方法
            (result, response) = invoke_function(contract_address, "approve", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_B]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "int",
                                                                                    "value": "10"
                                                                                }])

            result = (not result or response["result"]["Result"] == "00")        
                
        except Exception as e:
            print(e.msg)
        logger.close(result)
       
    def test_42(self):
        logger.open("TestMutiContract_42.log", "TestMutiContract_42")
        result = False
        try:
            contract_address = set_premise_b("tasks/38-43_48-59/A.neo")
            # setp 1 用户A授权用户B拥有角色A的权限
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
                        
            # ==================================================================
            # time.sleep(5)

            # 用户A授权用户C拥有10 ont
            
            (result, response) = invoke_function(contract_address, "approve", Config.ontID_A, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_C]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "int",
                                                                                    "value": "10"
                                                                                }])
            
            # 用户B调用智能合约A中的A方法
            (result, response) = invoke_function(contract_address, "allowance", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_C]["address"]))
                                                                                }])
            
            if not result:
                raise Error("invoke_function error")

            result = (response["result"]["Result"] != "00" and response["result"]["Result"] != "")          
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
        
    def test_43(self):
        logger.open("TestMutiContract_43.log", "TestMutiContract_43")
        result = False
        try:
            contract_address = set_premise_b("tasks/38-43_48-59/A.neo")

            # setp 1 用户A授权用户B拥有角色A的权限
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")

            # ==================================================================
            # time.sleep(5)

            # 用户B调用智能合约A中的A方法 approve
            (result, response) = invoke_function(contract_address, "approve", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_B]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_C]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "int",
                                                                                    "value": "10"
                                                                                }])
            
            # 用户B调用智能合约A中的A方法 allowance
            (result, response) = invoke_function(contract_address, "allowance", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_B]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_C]["address"]))
                                                                                }])
            if not result:
                raise Error("invoke_function error")

            result = (response["result"]["Result"] != "00" and response["result"]["Result"] != "")        
                
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_44(self):
        logger.open("TestMutiContract_44.log", "TestMutiContract_44")
        result = False
        try:
            (contract_addressA, contract_addressB) = set_premise_c("tasks/44-47/A.neo", "tasks/44-47/B.neo")

            # setp 1 用户A授权用户B拥有角色A的权限
            (result, response) = delegate_user_role(contract_addressA, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")  

            # 用户B调用智能合约A中的A方法
            (result, response) = invoke_function(contract_addressA, "A", Config.ontID_B)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] != "00")        
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_45(self):
        logger.open("TestMutiContract_45.log", "TestMutiContract_45")
        result = False
        try:
            (contract_addressA, contract_addressB) = set_premise_c("tasks/44-47/A.neo", "tasks/44-47/B.neo")

            # 用户A调用智能合约A中的A方法
            (result, response) = invoke_function(contract_addressA, "A", Config.ontID_A)        
                
            result = (not result or response["result"]["Result"] == "00")        
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_46(self):
        logger.open("TestMutiContract_46.log", "TestMutiContract_46")
        result = False
        try:
            (contract_addressA, contract_addressB) = set_premise_c("tasks/44-47/A.neo", "tasks/44-47/B.neo")

            # setp 1 用户B授权用户A拥有角色B的权限
            (result, response) = delegate_user_role(contract_addressB, Config.ontID_B, Config.ontID_A, Config.roleB_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")  

            # 用户B调用智能合约A中的A方法
            (result, response) = invoke_function(contract_addressA, "A", Config.ontID_A)
            if not result:
                raise Error("invoke_function error")
                
            result = (response["result"]["Result"] != "00")        
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_47(self):
        logger.open("TestMutiContract_47.log", "TestMutiContract_47")
        result = False
        try:
            (contract_addressA, contract_addressB) = set_premise_c("tasks/44-47/A.neo", "tasks/44-47/B.neo")

            # setp 1 用户A授权用户B调用方法A的权限
            #(result, response) = delegate_user_role(contract_addressA, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
            #if not result:
            #    raise("bind_user_role error")  

            # 用户B调用智能合约A中的A方法
            (result, response) = invoke_function(contract_addressA, "A2", Config.ontID_B)

            result = (response["result"]["Result"] != "00")        
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
        
    def test_48(self):
        logger.open("TestMutiContract_48.log", "TestMutiContract_48")
        result = False
        try:
            contract_address = set_premise_b("tasks/38-43_48-59/A.neo")

            #用户A授权用户B调用智能合约A方法A的权限，level1
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "1000", "1")
            if not result:
                raise("bind_user_role error")
            
            # 用户A调用智能合约A中的A方法approve用户A给用户C 10 ont
            (result, response) = invoke_function(contract_address, "approve", Config.ontID_A, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_B]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "int",
                                                                                    "value": "10"
                                                                                }])
            if not result:
                raise Error("invoke_function error")            
            

            # 用户B调用智能合约A中的A方法,让用户A使用transferFrom方法获取用户A从用户B的账户上转账来的 10 ONT
            (result, response) = invoke_function(contract_address, "transferFrom", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_B]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "int",
                                                                                    "value": "10"
                                                                                }])

                                                                                
            result = (not result or response["result"]["Result"] == "00")        

        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_49(self):
        logger.open("TestMutiContract_49.log", "TestMutiContract_49")
        result = False
        try:
            contract_address = set_premise_b("tasks/38-43_48-59/A.neo")

            # setp 1 用户A授权用户B拥有角色A的权限
            (result, response) = delegate_user_role(contract_address, Config.ontID_A, Config.ontID_B, Config.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")  

            # 用户B调用智能合约A中的A方法,让用户A使用balanceof方法获取用户A的账户余额
            (result, response) = invoke_function(contract_address, "balanceOf", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                }])

            result = (result and response["result"]["Result"] != "00")    
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
        
    def test_50(self):
        logger.open("TestMutiContract_50.log", "TestMutiContract_50")
        result = False
        try:
            contract_address = deploy_contract("tasks/38-43_48-59/A2.neo")

            # 用户B调用智能合约A中的A方法从用户A的账户中转账10 ont 给用户C
            (result, response) = invoke_function(contract_address, "transfer", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_C]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "int",
                                                                                    "value": "10"
                                                                                }])
            result = (not result or response["result"]["Result"] == "00")    
    
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_51(self):
        logger.open("TestMutiContract_51.log", "TestMutiContract_51")
        result = False
        try:
            contract_address = deploy_contract("tasks/38-43_48-59/A2.neo")

            # 用户B调用智能合约A中的A方法从用户A的账户中approve10 ont 给用户C
            (result, response) = invoke_function(contract_address, "approve", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_C]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "int",
                                                                                    "value": "10"
                                                                                }])
            result = (not result or response["result"]["Result"] == "00")    

        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_52(self):
        logger.open("TestMutiContract_52.log", "TestMutiContract_52")
        result = False
        try:
            contract_address = deploy_contract("tasks/38-43_48-59/A2.neo")

            # 用户A调用智能合约A中的A方法approve用户A给用户C 10 ont
            (result, response) = invoke_function(contract_address, "approve", Config.ontID_A, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_C]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "int",
                                                                                    "value": "10"
                                                                                }])
            if not result:
                raise Error("invoke_function error")            
            

            # 用户B调用智能合约A中的A方法提取用户A给用户C的10 ont
            (result, response) = invoke_function(contract_address, "transferFrom", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_B]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_C]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "int",
                                                                                    "value": "10"
                                                                                }])
            result = (not result or response["result"]["Result"] == "00")    
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_53(self):
        logger.open("TestMutiContract_53.log", "TestMutiContract_53")
        result = False
        try:
            contract_address = deploy_contract("tasks/38-43_48-59/A2.neo")
    
            # 用户B调用智能合约A中的A方法查询用户A的账户ont余额
            (result, response) = invoke_function(contract_address, "balanceOf", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                }])
            result = (result and response["result"]["Result"] != "00")    
        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_54(self):
        logger.open("TestMutiContract_54.log", "TestMutiContract_54")
        result = False
        try:
            contract_address = deploy_contract("tasks/38-43_48-59/A2.neo")

            # 用户B调用智能合约A中的A方法查询用户A给用户C的ont还有多少没有接收
            (result, response) = invoke_function(contract_address, "allowance", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_C]["address"]))
                                                                                }])
            result = (result and response["result"]["Result"] != "00")    

        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_55(self):
        logger.open("TestMutiContract_55.log", "TestMutiContract_55")
        result = False
        try:
            contract_address = deploy_contract("tasks/38-43_48-59/A2.neo")

            # 用户B调用智能合约A中的A方法从用户A的账户中转账10 ONG 给用户C
            (result, response) = invoke_function(contract_address, "transfer_ong", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_C]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "int",
                                                                                    "value": "10"
                                                                                }])
            result = (not result or response["result"]["Result"] == "00")           
            
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_56(self):
        logger.open("TestMutiContract_56.log", "TestMutiContract_56")
        result = False
        try:
            contract_address = deploy_contract("tasks/38-43_48-59/A2.neo")

            # 用户B调用智能合约A中的A方法从用户A的账户中approve10 ong 给用户C
            (result, response) = invoke_function(contract_address, "approve_ong", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_C]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "int",
                                                                                    "value": "10"
                                                                                }])
            result = (not result or response["result"]["Result"] == "00")    

        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_57(self):
        logger.open("TestMutiContract_57.log", "TestMutiContract_57")
        result = False
        try:
            contract_address = deploy_contract("tasks/38-43_48-59/A2.neo")

            # 用户A调用智能合约A中的A方法approve用户A给用户C 10 ong
            (result, response) = invoke_function(contract_address, "approve_ong", Config.ontID_A, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_C]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "int",
                                                                                    "value": "10"
                                                                                }])
            if not result:
                raise Error("invoke_function error")            
            

            # 用户B调用智能合约A中的A方法提取用户A给用户C的10 ong
            (result, response) = invoke_function(contract_address, "transferFrom_ong", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_B]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_C]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "int",
                                                                                    "value": "10"
                                                                                }])
            result = (not result or response["result"]["Result"] == "00")    

        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_58(self):
        logger.open("TestMutiContract_58.log", "TestMutiContract_58")
        result = False
        try:
            contract_address = deploy_contract("tasks/38-43_48-59/A2.neo")
    
            # 用户B调用智能合约A中的A方法查询用户A的账户ont余额
            (result, response) = invoke_function(contract_address, "balanceOf_ong", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                }])
            result = (result and response["result"]["Result"] != "00")    

        
        except Exception as e:
            print(e.msg)
        logger.close(result)

    def test_59(self):
        logger.open("TestMutiContract_59.log", "TestMutiContract_59")
        result = False
        try:
            contract_address = deploy_contract("tasks/38-43_48-59/A2.neo")

            # 用户B调用智能合约A中的A方法查询用户A给用户C的ont还有多少没有接收
            (result, response) = invoke_function(contract_address, "allowance_ong", Config.ontID_B, argvs = [ {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_A]["address"]))
                                                                                },
                                                                                {
                                                                                    "type": "bytearray",
                                                                                    "value": script_hash_bl_reserver(base58_to_address(Config.NODES[Config.node_C]["address"]))
                                                                                }])
            result = (result and response["result"]["Result"] != "00")    

        
        except Exception as e:
            print(e.msg)
        logger.close(result)

####################################################
if __name__ == '__main__':
    unittest.main()
