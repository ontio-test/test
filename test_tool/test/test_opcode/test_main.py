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
class TestOpCode(ParametrizedTestCase):
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

    def test_base_001_add(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"add",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_002_sub(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"sub",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_003_Push0(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Push0",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_004_PushBytes1(self):
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

    def test_normal_006_PushM1(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"PushM1",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_007_Nop(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"07_Nop",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_008_Jmpif(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Jmpif",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_009_Jmpifnot(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Jmpifnot",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_010_Call(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Call",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_011_Syscall(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Syscall",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_012_Toaltstack(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Toaltstack",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_013_Fromaltstack(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Fromaltstack",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_014_Roll(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Roll",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_015_Drop(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Drop",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_016_Dup(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Dup",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_017_Inc(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Inc",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_018_Dec(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Dec",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_019_Negate(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Negate",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_020_Abs(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Abs",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_021_Syscall(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Syscall",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_022_Toaltstack(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Toaltstack",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_023_Fromaltstack(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Fromaltstack",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_024_Roll(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Roll",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_025_Drop(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Drop",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_026_Dup(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Dup",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_027_Inc(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Inc",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_028_Dec(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Dec",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_029_Negate(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Negate",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_030_Abs(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Abs",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_031_Not(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Not",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_032_Nz(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Nz",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_033_Mul(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Mul",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_034_Div(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Div",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_035_Mod(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Mod",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_036_Shl(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Shl",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_037_Shr(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Shr",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_038_BoolAnd(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"BoolAnd",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_039_BoolOr(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"BoolOr",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
    def test_normal_040_NumeQual(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"NumeQual",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_041_NumNotEqual(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"NumNotEqual",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_042_Lt(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Lt",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_043_Gt(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Gt",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_044_Lte(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Lte",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_045_Gte(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Gte",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_046_Min(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Min",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_047_Max(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Max",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_048_Within(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Within",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_049_And(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"And",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_050_Or(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Or",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_051_Xor(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Xor",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_052_Invert(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Invert",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_053_CAT(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"CAT",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
    def test_normal_054_Left(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"Left",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_055_SIZE(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"SIZE",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_056_ARRAYSIZE(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"ARRAYSIZE",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_057_PACK(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"PACK",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_058_PICKITEM(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"PICKITEM",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_059_SETITEM(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"SETITEM",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_060_NEWARRAY(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"NEWARRAY",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_061_NEWSTRUCT(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"NEWSTRUCT",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_062_APPEND(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"APPEND",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_063_REVERSE(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"REVERSE",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_064_SHA1(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"SHA1",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_065_SHA256(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"SHA256",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_066_HASH160(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"HASH160",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_067_HASH256(self):
        try:
            (process, response) = invoke_function_opCode(test_config.contract_address,"HASH256",test_config.param_1,test_config.param_2)
            self.ASSERT(process, "")
        except Exception as e:
            logger.print(e.args[0])
####################################################
if __name__ == '__main__':
    unittest.main()