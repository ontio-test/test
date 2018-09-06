# -*- coding:utf-8 -*-

import ddt
import unittest
import sys, getopt
import time
import traceback

sys.path.append('..')
sys.path.append('../..')

# from utils.selfig import selfig
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.config import Config

from api.apimanager import API

from test_auth.test_api import *
from test_auth.test_config import test_config


####################################################
# test cases
class test_auth_1(ParametrizedTestCase):

    def setUp(self):
        logger.open("test_auth/" + self._testMethodName + ".log", self._testMethodName)

        time.sleep(2)
        print("stop all")
        API.node().stop_all_nodes()
        print("start all")
        API.node().start_nodes([0, 1, 2, 3, 4, 5, 6, 7, 8], Config.DEFAULT_NODE_ARGS, True, True)

        for i in range(9):
            API.native().regid_with_publickey(i, sleep=0)

        API.native().init_ont_ong()

        (test_config.contract_addr, test_config.contract_tx_hash) = API.contract().deploy_contract_full(
            test_config.deploy_neo_1)
        (test_config.contract_addr_1, test_config.contract_tx_hash_1) = API.contract().deploy_contract_full(
            test_config.deploy_neo_2)
        (test_config.contract_addr_2, test_config.contract_tx_hash_2) = API.contract().deploy_contract_full(
            test_config.deploy_neo_3)
        (test_config.contract_addr_3, test_config.contract_tx_hash_3) = API.contract().deploy_contract_full(
            test_config.deploy_neo_4)
        (test_config.contract_addr_10, test_config.contract_tx_hash_10) = API.contract().deploy_contract_full(
            test_config.deploy_neo_5)
        (test_config.contract_addr_11, test_config.contract_tx_hash_11) = API.contract().deploy_contract_full(
            test_config.deploy_neo_6)
        (test_config.contract_addr_12, test_config.contract_tx_hash_12) = API.contract().deploy_contract_full(
            test_config.deploy_neo_7)
        (test_config.contract_addr_138_1, test_config.contract_tx_hash_138_1) = API.contract().deploy_contract_full(
            test_config.deploy_neo_8)
        (test_config.contract_addr_138_2, test_config.contract_tx_hash_138_2) = API.contract().deploy_contract_full(
            test_config.deploy_neo_9)
        (test_config.contract_addr_139, test_config.contract_tx_hash_139) = API.contract().deploy_contract_full(
            test_config.deploy_neo_10)
        # (test_config.contract_addr_140, test_config.contract_tx_hash_140) = API.contract().deploy_contract_full(test_config.deploy_neo_11)

        test_config.CONTRACT_ADDRESS_CORRECT = test_config.contract_addr
        test_config.CONTRACT_ADDRESS_CORRECT = test_config.contract_addr  # correct
        test_config.CONTRACT_ADDRESS_INCORRECT_1 = test_config.contract_addr_1  # wrong ontid
        test_config.CONTRACT_ADDRESS_INCORRECT_2 = test_config.contract_addr_2  # null ontid
        test_config.CONTRACT_ADDRESS_INCORRECT_3 = test_config.contract_addr_3  # init twice
        test_config.CONTRACT_ADDRESS_INCORRECT_4 = test_config.contract_addr + "11"  # not real contract
        test_config.CONTRACT_ADDRESS_INCORRECT_5 = "45445566"  # messy code
        test_config.CONTRACT_ADDRESS_INCORRECT_6 = ""  # null
        test_config.CONTRACT_ADDRESS_INCORRECT_10 = test_config.contract_addr_10  # verifytoken contract with wrong address
        test_config.CONTRACT_ADDRESS_INCORRECT_11 = test_config.contract_addr_11  # verifytoken contract with messy code address
        test_config.CONTRACT_ADDRESS_INCORRECT_12 = test_config.contract_addr_12  # verifytoken contract with wrong address

        test_config.CONTRACT_ADDRESS_138 = test_config.contract_addr_138_1  # appcall contract with correct address
        test_config.CONTRACT_ADDRESS_139 = test_config.contract_addr_139  # appcall contract with messy code address

        API.node().wait_gen_block()

    def tearDown(self):
        logger.close(self.result())

    def test_base_001_initContractAdmin(self):
        try:

            (process, response) = init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_002_initContractAdmin(self):
        try:

            (process, response) = init_admin(test_config.CONTRACT_ADDRESS_INCORRECT_1, test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")

        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_003_initContractAdmin(self):
        try:

            (process, response) = init_admin(test_config.CONTRACT_ADDRESS_INCORRECT_2, test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_004_initContractAdmin(self):
        try:
            (process, response) = init_admin(test_config.CONTRACT_ADDRESS_INCORRECT_3, test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_base_005_verifyToken(self):
        try:
            (process, response) = init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A,
                                                  test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "41", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_006_verifyToken(self):
        try:
            (process, response) = init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A,
                                                  test_config.ontID_B)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_007_verifyToken(self):
        try:

            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A,
                                                  test_config.ontID_C)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_008_verifyToken(self):
        try:

            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A,
                                                  test_config.ontID_D)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_009_verifyToken(self):
        try:
            (process, response) = init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A,
                                                  test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "41", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_010_verifyToken(self):
        try:

            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_INCORRECT_10, test_config.FUNCTION_A,
                                                  test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_011_verifyToken(self):
        try:

            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_INCORRECT_11, test_config.FUNCTION_A,
                                                  test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_012_verifyToken(self):
        try:

            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_INCORRECT_12, test_config.FUNCTION_A,
                                                  test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_013_verifyToken(self):
        try:
            (process, response) = init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A,
                                                  test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "41", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_014_verifyToken(self):
        try:

            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, "C", test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_015_verifyToken(self):
        try:

            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_B,
                                                  test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_016_verifyToken(self):
        try:

            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, "", test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_base_017_transfer(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().transfer_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_B)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_018_transfer(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().transfer_admin(test_config.CONTRACT_ADDRESS_INCORRECT_1,
                                                              test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_019_transfer(self):
        try:
            (process, response) = API.native().transfer_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_020_transfer(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().transfer_admin(test_config.CONTRACT_ADDRESS_INCORRECT_5,
                                                              test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(traceback.print_exc())

    def test_abnormal_021_transfer(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().transfer_admin(test_config.CONTRACT_ADDRESS_INCORRECT_6,
                                                              test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_022_transfer(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().transfer_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_023_transfer(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().transfer_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_24_transfer(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().transfer_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_C)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_025_transfer(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().transfer_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_D)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_026_transfer(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().transfer_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_027_transfer(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().transfer_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              public_key=test_config.KEY_NO_1)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_028_transfer(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().transfer_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              public_key=test_config.KEY_NO_2)
            if isinstance(response, dict) and response.get("result", False):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_029_transfer(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().transfer_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              public_key=test_config.KEY_NO_3)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_base_030_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_031_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_INCORRECT_4,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_032_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_INCORRECT_5,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_033_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_INCORRECT_6,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_034_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_035_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().transfer_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_B)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_036_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_B, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A], node_index=0)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_037_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_C, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A], node_index=0)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            traceback.print_exc()
            logger.print(e.args[0])

    def test_abnormal_038_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_D, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A], node_index=0)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_039_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_040_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_041_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_INCORRECT_1,
                                                                  [test_config.FUNCTION_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_042_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_INCORRECT_2,
                                                                  [test_config.FUNCTION_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_043_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_044_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_B, test_config.FUNCTION_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_045_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A, test_config.FUNCTION_B,
                                                                   test_config.FUNCTION_C])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_046_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_047_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_INCORRECT_2,
                                                                  [test_config.FUNCTION_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_048_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_D])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_049_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A, test_config.FUNCTION_D])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_050_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_051_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A],
                                                                  public_key=test_config.KEY_NO_1)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_052_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A],
                                                                  public_key=test_config.KEY_NO_2)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_053_assignFuncsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A],
                                                                  public_key=test_config.KEY_NO_3)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_base_054_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_055_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_INCORRECT_4,
                                                              test_config.ontID_A, test_config.ROLE_CORRECT,
                                                              [test_config.ontID_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_056_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_INCORRECT_5,
                                                              test_config.ontID_A, test_config.ROLE_CORRECT,
                                                              [test_config.ontID_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_057_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_INCORRECT_6,
                                                              test_config.ontID_A, test_config.ROLE_CORRECT,
                                                              [test_config.ontID_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_058_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_059_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().transfer_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_B)
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_060_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_B,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A],
                                                              node_index=0)
            process = (response["result"]["Result"] == "00")
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_061_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A], node_index=0)
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_C,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A],
                                                              node_index=0)
            process = (response["result"]["Result"] == "00")
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_062_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A], node_index=0)
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_D,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A],
                                                              node_index=0)
            process = (response["result"]["Result"] == "00")
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_063_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_064_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_INCORRECT_3, [test_config.ontID_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_065_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_INCORRECT_1, [test_config.ontID_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_066_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT,
                                                              [test_config.ontID_A, test_config.ontID_B])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_067_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT,
                                                              [test_config.ontID_A, test_config.ontID_B,
                                                               test_config.ontID_C])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_068_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_D])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_069_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_070_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A],
                                                              public_key=test_config.KEY_NO_1)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_071_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A],
                                                              public_key=test_config.KEY_NO_2)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_072_assignOntIDsToRole(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A],
                                                              public_key=test_config.KEY_NO_3)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_base_073_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_074_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_INCORRECT_4,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT, node_index=0)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_075_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_INCORRECT_5,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_076_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_INCORRECT_6,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT, node_index=0)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_077_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT, node_index=0)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_078_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT)
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_B, test_config.ontID_E,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT, node_index=2)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_079_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_B, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT, node_index=0)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_080_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_C, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT, node_index=0)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_081_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_082_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT, node_index=0)
            API.node().wait_gen_block()
            time.sleep(10)
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT, node_index=0)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_083_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_A,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_084_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_C,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_085_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_D,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_086_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_087_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_INCORRECT_3,
                                                                  test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_088_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_INCORRECT_1,
                                                                  test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_089_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_090_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT,
                                                                  test_config.PERIOD_INCORRECT_1,
                                                                  test_config.LEVEL_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_091_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT,
                                                                  test_config.PERIOD_INCORRECT_2,
                                                                  test_config.LEVEL_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_092_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT,
                                                                  test_config.PERIOD_INCORRECT_3,
                                                                  test_config.LEVEL_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_093_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT,
                                                                  test_config.PERIOD_INCORRECT_4,
                                                                  test_config.LEVEL_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_094_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT,
                                                                  test_config.PERIOD_INCORRECT_5,
                                                                  test_config.LEVEL_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_095_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_096_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_INCORRECT_1)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_097_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_INCORRECT_2)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_098_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_INCORRECT_3)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_099_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_INCORRECT_4)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_100_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_101_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT,
                                                                  public_key=test_config.KEY_NO_1)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_102_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT,
                                                                  public_key=test_config.KEY_NO_2)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_103_delegate(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT,
                                                                  public_key=test_config.KEY_NO_3)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_base_104_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_105_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_INCORRECT_4,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_106_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_INCORRECT_5,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_107_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_INCORRECT_6,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_108_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_109_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_B, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, node_index=0)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_110_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_E, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_E,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_E, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_111_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_C, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, node_index=0)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_112_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_D, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, node_index=0)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_113_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_114_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_A,
                                                                  test_config.ROLE_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_115_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_A,
                                                                  test_config.ROLE_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_116_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_A,
                                                                  test_config.ROLE_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_117_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_C,
                                                                  test_config.ROLE_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_118_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_D,
                                                                  test_config.ROLE_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_119_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_120_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_INCORRECT_3)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_121_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_INCORRECT_2)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_122_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_INCORRECT_1)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_normal_134_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_135_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT,
                                                                  public_key=test_config.KEY_NO_1)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_136_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT,
                                                                  public_key=test_config.KEY_NO_2)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_137_withdraw(self):
        try:
            init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = API.native().delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT,
                                                                  test_config.LEVEL_CORRECT)
            (process, response) = API.native().withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ontID_B,
                                                                  test_config.ROLE_CORRECT,
                                                                  public_key=test_config.KEY_NO_3)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_base_138_appcall(self):
        try:
            # init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_138, "contractA_Func_A",
                                                  test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "01", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_139_appcall(self):
        try:
            # init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_139, "contractA_Func_A",
                                                  test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "323232", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_base_146_verifyToken(self):
        try:
            (process, response) = init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
            (process, response) = API.native().bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT,
                                                                  test_config.ontID_A, test_config.ROLE_CORRECT,
                                                                  [test_config.FUNCTION_A])
            (process, response) = API.native().bind_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A,
                                                              test_config.ROLE_CORRECT, [test_config.ontID_A])
            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A,
                                                  test_config.ontID_A)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "41", "")
            else:
                self.ASSERT(False, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_147_verifyToken(self):
        try:

            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A,
                                                  test_config.ontID_A, public_key=test_config.KEY_NO_1)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_148_verifyToken(self):
        try:

            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A,
                                                  test_config.ontID_A, public_key=test_config.KEY_NO_2)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])

    def test_abnormal_149_verifyToken(self):
        try:

            (process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A,
                                                  test_config.ontID_A, public_key=test_config.KEY_NO_3)
            if isinstance(response, dict) and response.get("result", False) and isinstance(response.get("result", False), dict):
                self.ASSERT(response["result"]["Result"] == "00", "")
            else:
                self.ASSERT(True, "")
        except Exception as e:
            logger.print(e.args[0])


####################################################
if __name__ == '__main__':
    unittest.main()
