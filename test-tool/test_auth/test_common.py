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
from test_api import *
    
def set_premise(neo_path):
    result = False
    contract_address = None
    
    contract_address = deploy_contract(neo_path)

    (result, response) = init_admin(contract_address, Common.ontID_Admin)
    if not result:
        raise(Error("init_admin error"))
    (result, response) = bind_role_function(contract_address, Common.ontID_Admin, Common.roleA_hex, ["A", "C"])
    if not result:
        raise(Error("bind_role_function error [1]"))
    (result, response) = bind_role_function(contract_address, Common.ontID_Admin, Common.roleB_hex , ["B", "C"])
    if not result:
        raise(Error("bind_role_function error [2]"))
    if not result:
        raise(Error("set_premise error"))
        
    return contract_address

def set_premise_a(neo_path_a, neo_path_b):

    result = False
    contract_address = None
    adminOntID = ByteToHex(b"TA6CtF4hZwqAmXdc6opa4B79fRS17YJjX5")
    roleA_hex = ByteToHex(b"roleA")
    roleB_hex = ByteToHex(b"roleB")

    ontID_A = ByteToHex(b"did:ont:TA7TSQ5aJcA8sU5MpqJNyTG1r13AQYLYpR")
    ontID_B = ByteToHex(b"did:ont:TA82XAPQXtVzncQMczcY9SVytjb2VuTQy4") 
    ontID_C = ByteToHex(b"did:ont:TA6CtF4hZwqAmXdc6opa4B79fRS17YJjX5")

    # 初始化合约B管理员为A用户,
    contract_address_B = deploy_contract(neo_path_b)

        # 部署智能合约A
    contract_address_A = deploy_contract(neo_path_a)

    (result, response) = init_admin(contract_address_B, ontID_A)
    if not result:
        raise(Error("init_admin error"))

    # 用户A创建角色A
    (result, response) = bind_role_function(contract_address_B, ontID_A , roleA_hex, ["contractB_Func_A"])
    if not result:
        raise(Error("bind_role_function error [1]"))

    # setp 1 用户A绑定角色A
    (result, response) = bind_user_role(contract_address_B, ontID_A, roleA_hex, [ontID_A])
    if not result:
        raise(Error("bind_user_role error"))
    
    if result:
        return (contract_address_A, contract_address_B, roleA_hex, roleB_hex, ontID_A, ontID_B, ontID_C)
    else:
        raise(Error("set_premise error"))

def set_premise_b(neo_path):
    contract_address = None
    adminOntID = ByteToHex(b"TA6CtF4hZwqAmXdc6opa4B79fRS17YJjX5")
    roleA_hex = ByteToHex(b"roleA")
    roleB_hex = ByteToHex(b"roleB")

    ontID_A = ByteToHex(b"did:ont:TA7TSQ5aJcA8sU5MpqJNyTG1r13AQYLYpR")
    ontID_B = ByteToHex(b"did:ont:TA82XAPQXtVzncQMczcY9SVytjb2VuTQy4") 
    ontID_C = ByteToHex(b"did:ont:TA6CtF4hZwqAmXdc6opa4B79fRS17YJjX5")


    contract_address = deploy_contract(neo_path)

    (result, response) = init_admin(contract_address, ontID_A)
    if not result:
        raise(Error("init_admin error"))

    (result, response) = bind_role_function(contract_address, ontID_A, roleA_hex, ["A"])
    if not result:
        raise(Error("bind_role_function error [1]"))

        # setp 1 用户A绑定角色A
    (result, response) = bind_user_role(contract_address_B, ontID_A, roleA_hex, [ontID_A])
    if not result:
        raise(Error("bind_user_role error"))

    if result:
        return (contract_address, adminOntID, roleA_hex, roleB_hex, ontID_A, ontID_B, ontID_C)
    else:
        raise(Error("set_premise error"))

            