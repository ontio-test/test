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
from utils.rpcapi import *

from test_api import *

logger = LoggerInstance
rpcapiTest=RPCApi()

# test cases
class TestMultiWallet(ParametrizedTestCase):

    def test_01(self):
        logger.open("test_01.log", "test_01")
        #init(0)
        (result, response) = test_01_()
        logger.close(result)

    def test_02(self):
        logger.open("test_02.log", "test_02")
        #init(0)
        (result, response) = test_02_()
        logger.close(result)

    def test_18(self):
        logger.open("test_18.log", "test_18")
        #init(0)
        (result, response) = test_18_()
        logger.close(result)

    def test_20(self):
        logger.open("test_20.log", "test_20")
        #init(0)
        (result, response) = test_20_()
        logger.close(result)

    def test_21(self):
        logger.open("test_21.log", "test_21")
        #init(0)
        result = test_21_()
        logger.close(result)

    def test_23(self):
        logger.open("test_23.log", "test_23")
        #init(0)
        (result, response) = test_23_()
        logger.close(result)

    def test_24(self):
        logger.open("test_24.log", "test_24")
        #init(0)
        (result, response) = test_24_()
        logger.close(result)

    def test_25(self):
        logger.open("test_25.log", "test_25")
        #init(0)
        (result, response) = test_25_()
        logger.close(result)

    def test_26(self):
        logger.open("test_26.log", "test_26")
        #init(0)
        (result, response) = test_26_()
        logger.close(result)

    def test_27(self):
        logger.open("test_27.log", "test_27")
        #init(0)
        (result, response) = test_27_()
        logger.close(result)

    def test_28(self):
        logger.open("test_28.log", "test_28")
        #init(0)
        (result, response) = test_28_()
        logger.close(result)

    def test_29(self):
        logger.open("test_29.log", "test_29")
        #init(0)
        (result, response) = test_29_()
        logger.close(result)

    def test_30(self):
        logger.open("test_30.log", "test_30")
        #init(0)
        (result, response) = test_30_()
        logger.close(result)


    def test_31(self):
        logger.open("test_31.log", "test_31")
        #init(0)
        (result, response) = test_31_()
        logger.close(result)

    def test_32(self):
        logger.open("test_32.log", "test_32")
        #init(0)
        (result, response) = test_32_()
        logger.close(result)

    def test_33(self):
        logger.open("test_33.log", "test_33")
        #init(0)
        (result, response) = test_33_()

    def test_34(self):
        logger.open("test_34.log", "test_34")
        #init(0)
        (result, response) = test_34_()

    def test_35(self):
        logger.open("test_35.log", "test_35")
        #init(0)
        (result, response) = test_35_()

    def test_36(self):
        logger.open("test_36.log", "test_36")
        #init(0)
        (result, response) = test_37_(0)
        logger.close(result)

    def test_37(self):
        logger.open("test_37.log", "test_37")
        #init(0)
        (result, response) = test_37_(0)
        logger.close(result)

    def test_40(self):
        logger.open("test_40.log", "test_40")
        #init(0)
        (result, response) = test_40_()
        logger.close(result)

    def test_41(self):
        logger.open("test_41.log", "test_41")
        (result, response) = test_41_()
        logger.close(not result)

    def test_42(self):
        logger.open("test_42.log", "test_42")
        init(0)
        (result, response) = test_42_(0)
        logger.close(result)

    def test_43(self):
        logger.open("test_43.log", "test_43")
        #init(0)
        (result, response) = test_43_(0)
        logger.close(result)

    def test_44(self):
        logger.open("test_44.log", "test_44")
        #init(0)
        (result, response) = test_44_()
        logger.close(result)
    
    def test_45(self):
        logger.open("test_45.log", "test_45")
        #init(0)
        (result, response) = test_45_()
        logger.close(result)

    def test_46(self):
        logger.open("test_46.log", "test_46")
        #init(0)
        (result, response) = test_46_()
        logger.close(result)

    def test_47(self):
        logger.open("test_47.log", "test_47")
        #init(0)
        (result, response) = test_47_()
        logger.close(result)

    def test_48(self):
        logger.open("test_48.log", "test_48")
        #init(0)
        (result, response) = test_48_()
        logger.close(result)

    def test_49(self):
        logger.open("test_49.log", "test_49")
        (result, response) = test_49_()
        logger.close(result)

    def test_50(self):
        logger.open("test_50.log", "test_50")
        (result, response) = test_50_()
        logger.close(result)

    def test_51(self):
        logger.open("test_51.log", "test_51")
        (result, response) = test_51_()
        logger.close(result)

    def test_52(self):
        logger.open("test_52.log", "test_52")
        (result, response) = test_52_()
        logger.close(result)

    def test_53(self):
        logger.open("test_53.log", "test_53")
        (result, response) = test_53_()
        logger.close(result)

    def test_54(self):
        logger.open("test_54.log", "test_54")
        (result, response) = test_54_()
        logger.close(result)

    def test_55(self):
        logger.open("test_55.log", "test_55")
        #init(0)
        (result, response) = test_55_()
        logger.close(result)

    def test_56(self):
        logger.open("test_56.log", "test_56")
        #init(0)
        (result, response) = test_56_()
        logger.close(result)

    def test_65(self):
        logger.open("test_40.log", "test_40")

        init(0)
        (result, response) = multi_wallet_sig(0)

        logger.close(result)

    

    
    

    def test_60(self):
        logger.open("test_60.log", "test_60")
        #init(0)
        (result, response) = test_60_()
        logger.close(result)

    def test_61(self):
        logger.open("test_61.log", "test_61")
        (result, response) = test_61_()
        logger.close(not result)

    def test_62(self):
        logger.open("test_62.log", "test_62")
        (result, response) = test_62_()
        logger.close(not result)


if __name__ == '__main__':
    unittest.main()
