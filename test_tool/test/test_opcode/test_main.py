# -*- coding:utf-8 -*-
import unittest
import os
import sys
import time


sys.path.append('..')
sys.path.append('../..')
testpath = os.path.dirname(os.path.realpath(__file__))

from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.config import Config


from test_opcode.test_api import *
from test_opcode.test_config import test_config

from api.apimanager import API

# test cases
class test_opcode_1(ParametrizedTestCase):
    def test_init(self):

        API.node().stop_all_nodes()
        API.node().start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True)
        time.sleep(10)

        (test_config.contract_address, _) = API.contract().deploy_contract_full(testpath+"/resource/test_op.avm", "name", "desc", 0)
        API.node().wait_gen_block()


    def setUp(self):
        logger.open("test_opcode/" + self._testMethodName+".log",self._testMethodName)

    def tearDown(self):
        logger.close(self.result())

    def test_normal_001_Push0(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Push0",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_003_PushBytes1(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"PushBytes1",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_005_Pushdata1(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Pushdata1",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_008_PushM1(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"PushM1",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_028_Jmpif(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Jmpif",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_029_Jmpifnot(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Jmpifnot",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_030_Call(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Call",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_033_Syscall(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Syscall",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    

    def test_normal_035_Toaltstack(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Toaltstack",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_036_Fromaltstack(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Fromaltstack",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_041_Drop(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Drop",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_042_Dup(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Dup",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
    
    def test_normal_046_Roll(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Roll",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_084_Within(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Within",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_050_CAT(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"CAT",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_056_And(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"And",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_base_067_add(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"add",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_068_sub(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"sub",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
    

    def test_normal_060_Inc(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Inc",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_061_Dec(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Dec",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_063_Negate(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Negate",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_064_Abs(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Abs",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    

    def test_normal_065_Not(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Not",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_066_Nz(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Nz",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_069_Mul(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Mul",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_070_Div(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Div",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_071_Mod(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Mod",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_072_Shl(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Shl",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_073_Shr(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Shr",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_074_BoolAnd(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"BoolAnd",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_075_BoolOr(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"BoolOr",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
    def test_normal_076_NumeQual(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"NumeQual",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_077_NumNotEqual(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"NumNotEqual",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_078_Lt(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Lt",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_079_Gt(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Gt",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_080_Lte(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Lte",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_081_Gte(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Gte",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_082_Min(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Min",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_083_Max(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Max",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    
    
    

    def test_normal_057_Or(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Or",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_058_Xor(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Xor",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_054_SIZE(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"SIZE",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_055_Invert(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Invert",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])



    

    def test_normal_085_ARRAYSIZE(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"ARRAYSIZE",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_086_PACK(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"PACK",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_088_PICKITEM(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"PICKITEM",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_089_SETITEM(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"SETITEM",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_090_NEWARRAY(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"NEWARRAY",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_091_NEWSTRUCT(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"NEWSTRUCT",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_092_APPEND(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"APPEND",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_093_REVERSE(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"REVERSE",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_096_SHA1(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"SHA1",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_097_SHA256(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"SHA256",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_098_HASH160(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"HASH160",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_099_HASH256(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"HASH256",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
####################################################
if __name__ == '__main__':
    unittest.main()