# -*- coding: utf-8 -*-
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

sys.path.append('..')
sys.path.append('../..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from api.apimanager import API

rpcApi = API.rpc()

class test_config():
    m_contractaddr_right = ""
    m_txhash_right = ""
    m_txhash_wrong = "this is a wrong tx hash"
    m_contractaddr_wrong = "this is a wrong address"

    m_block_hash_right = ""
    m_block_hash_error = "this is a wrong block hash"
    
    m_block_height_right = 1
    m_block_height_wrong = 9999
    m_block_height_overflow = 99999999
    
    m_signed_txhash_right = ""
    m_signed_txhash_wrong = "" #两个self
    
    m_getstorage_contract_addr = "03febccf81ac85e3d795bc5cbd4e84e907812aa3"
    m_getstorage_contract_addr_wrong = "5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c"
    m_getstorage_contract_key = ByteToHex(b'key1')
    m_getstorage_contract_value = ByteToHex(b'value1')
    
    getsmartcodeevent_height = 5

    getbalance_address_true = Config.NODES[0]["address"]
    getbalance_address_false = "ccccccccccccccc"
