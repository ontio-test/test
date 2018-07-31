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
sys.path.append('../..')
testpath = os.path.dirname(os.path.realpath(__file__))

from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.config import Config

from test_opcode.test_api import test_api
from api.apimanager import API

# test cases
class TestOpCode(ParametrizedTestCase):
    def test_init(self):
        API.node().stop_all_nodes()
        API.node().start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True)
        time.sleep(10)
        (self.contract_address, _) = API.contract().deploy_contract_full(testpath+"/resource/test_op.avm", "name", "desc", 0)
        API.node().wait_gen_block()

        self.param_1 = "1"
        self.param_2 = "1"

    def setUp(self):
        logger.open("test_opcode/" + self._testMethodName+".log",self._testMethodName)

    def tearDown(self):
        logger.close(self.result())

    def test_01_base_add(self):
        try:
            (process, response) = invoke_function_opCode(self.contract_address,"add",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_02_normal_sub(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"sub",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_03_normal_Push0(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Push0",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_04_normal_PushBytes1(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"PushBytes1",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_05_normal_Pushdata1(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Pushdata1",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_06_normal_PushM1(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"PushM1",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_07_normal_Nop(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"07_Nop",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_08_normal_Jmpif(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Jmpif",self.param_1,self.param_2)
        if not result:
            raise Error("invoke_function error")
        logger.close(result)
    
    def test_09_normal_Jmpifnot(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Jmpifnot",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_10_normal_Call(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Call",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_11_normal_Syscall(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Syscall",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_12_normal_Toaltstack(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Toaltstack",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_13_normal_Fromaltstack(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Fromaltstack",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_14_normal_Roll(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Roll",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_15_normal_Drop(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Drop",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_16_normal_Dup(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Dup",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_17_normal_Inc(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Inc",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_18_normal_Dec(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Dec",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
    
    def test_19_normal_Negate(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Negate",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_20_normal_Abs(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Abs",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_21_normal_Syscall(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Syscall",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_22_normal_Toaltstack(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Toaltstack",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_23_normal_Fromaltstack(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Fromaltstack",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_24_normal_Roll(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Roll",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_25_normal_Drop(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Drop",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_26_normal_Dup(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Dup",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_27_normal_Inc(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Inc",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_28_normal_Dec(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Dec",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
    
    def test_29_normal_Negate(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Negate",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_30_normal_Abs(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Abs",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_31_normal_Not(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Not",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_32_normal_Nz(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Nz",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_33_normal_Mul(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Mul",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_34_normal_Div(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Div",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_35_normal_Mod(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Mod",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_36_normal_Shl(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Shl",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_37_normal_Shr(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Shr",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_38_normal_BoolAnd(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"BoolAnd",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
    
    def test_39_normal_BoolOr(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"BoolOr",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
    def test_40_normal_NumeQual(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"NumeQual",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_41_normal_NumNotEqual(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"NumNotEqual",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_42_normal_Lt(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Lt",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_43_normal_Gt(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Gt",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_44_normal_Lte(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Lte",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_45_normal_Gte(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Gte",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_46_normal_Min(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Min",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_47_normal_Max(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Max",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_48_normal_Within(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Within",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
    
    def test_49_normal_And(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"And",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_50_normal_Or(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Or",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
    
    def test_51_normal_Xor(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Xor",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_52_normal_Invert(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Invert",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_53_normal_CAT(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"CAT",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
    def test_54_normal_Left(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"Left",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_55_normal_SIZE(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"SIZE",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_56_normal_ARRAYSIZE(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"ARRAYSIZE",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_57_normal_PACK(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"PACK",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_58_normal_PICKITEM(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"PICKITEM",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_59_normal_SETITEM(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"SETITEM",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
    
    def test_60_normal_NEWARRAY(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"NEWARRAY",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_61_normal_NEWSTRUCT(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"NEWSTRUCT",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
    
    def test_62_APPEND(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"APPEND",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_63_normal_REVERSE(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"REVERSE",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_64_normal_SHA1(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"SHA1",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_65_normal_SHA256(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"SHA256",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_66_normal_HASH160(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"HASH160",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
    
    def test_67_normal_HASH256(self):
        try:
            (result, response) = invoke_function_opCode(self.contract_address,"HASH256",self.param_1,self.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
####################################################
if __name__ == '__main__':
    unittest.main()