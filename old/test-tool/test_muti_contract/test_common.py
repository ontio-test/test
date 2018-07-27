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

def set_premise(neo_path):
    result = False
    contract_address = None
    
    contract_address = deploy_contract(neo_path)

    (result, response) = init_admin(contract_address, Config.ontID_A)
    if not result:
        raise(Error("init_admin error"))
    (result, response) = bind_role_function(contract_address, Config.ontID_A, Config.roleA_hex, ["A", "C"])
    if not result:
        raise(Error("bind_role_function error [1]"))
    (result, response) = bind_role_function(contract_address, Config.ontID_A, Config.roleB_hex , ["B", "C"])
    if not result:
        raise(Error("bind_role_function error [2]"))
    if not result:
        raise(Error("set_premise error"))
        
    return contract_address

def set_premise_a(neo_path_a, neo_path_b):

    result = False
    contract_address = None

    # 初始化合约B管理员为A用户,
    contract_address_B = deploy_contract(neo_path_b)

    # 部署智能合约A
    contract_address_A = deploy_contract(neo_path_a)

    (result, response) = init_admin(contract_address_B, Config.ontID_A)
    if not result:
        raise(Error("init_admin error"))

    # 用户A创建角色A
    (result, response) = bind_role_function(contract_address_B, Config.ontID_A , Config.roleA_hex, ["contractB_Func_A"])
    if not result:
        raise(Error("bind_role_function error [1]"))

    # setp 1 用户A绑定角色A
    (result, response) = bind_user_role(contract_address_B, Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
    if not result:
        raise(Error("bind_user_role error"))
    
    if result:
        return (contract_address_A, contract_address_B)
    else:
        raise(Error("set_premise error"))

def set_premise_b(neo_path):
    result = False
    contract_address = deploy_contract(neo_path)

    (result, response) = init_admin(contract_address, Config.ontID_A)
    if not result:
        raise(Error("init_admin error"))

    (result, response) = bind_role_function(contract_address, Config.ontID_A, Config.roleA_hex, ["transfer", "approve", "transferFrom", "allowance", "balanceOf"])
    if not result:
        raise(Error("bind_role_function error [1]"))

    # setp 1 用户A绑定角色A
    (result, response) = bind_user_role(contract_address, Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
    if not result:
        raise(Error("bind_user_role error"))

    if result:
        return contract_address
    else:
        raise(Error("set_premise error"))
        
def set_premise_c(neo_path_a, neo_path_b):
    result = False
    contract_address = None

    # 部署智能合约B,
    contract_address_B = deploy_contract(neo_path_b)

    # 部署智能合约A
    contract_address_A = deploy_contract(neo_path_a)

    (result, response) = init_admin(contract_address_A, Config.ontID_A)
    if not result:
        raise(Error("init_admin error"))

    (result, response) = init_admin(contract_address_B, Config.ontID_B)
    if not result:
        raise(Error("init_admin error"))

    # 用户A创建角色A
    (result, response) = bind_role_function(contract_address_A, Config.ontID_A, Config.roleA_hex, ["A", "A2"])
    if not result:
        raise(Error("bind_role_function error [1]"))

    # setp 1 用户A绑定角色A
    (result, response) = bind_user_role(contract_address_A, Config.ontID_A, Config.roleA_hex, [Config.ontID_A])
    if not result:
        raise(Error("bind_user_role error"))
    
    # 用户B创建角色B
    (result, response) = bind_role_function(contract_address_B, Config.ontID_B , Config.roleB_hex, ["B"])
    if not result:
        raise(Error("bind_role_function error [1]"))

    # setp 1 用户B绑定角色A
    (result, response) = bind_user_role(contract_address_B, Config.ontID_B, Config.roleB_hex, [Config.ontID_B])
    if not result:
        raise(Error("bind_user_role error"))
        
    if result:
        return (contract_address_A, contract_address_B)
    else:
        raise(Error("set_premise error"))


            