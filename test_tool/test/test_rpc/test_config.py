# -*- coding: utf-8 -*-
import sys
sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from api.apimanager import API



class test_config():
	m_getstorage_contract_key = "1234" # ByteToHex(b'key1')
	m_getstorage_contract_value = ByteToHex(b'value1')

	getsmartcodeevent_height = 5

	getbalance_address_true = Config.NODES[0]["address"]
	getbalance_address_false = "ccccccccccccccc"

	m_contractaddr_right = ""
	m_txhash_right = ""		

	m_txhash_wrong = "is a wrong tx hash"

	m_block_hash_right = ""

	m_block_hash_error = "this is a wrong block hash"

	m_block_height_right = 1

	m_block_height_wrong = 9999

	m_block_height_overflow = 99999999

	m_signed_txhash_right = ""
	m_signed_txhash_wrong = "" #两个self
			
	m_getstorage_contract_addr = ""
	m_getstorage_contract_addr_wrong = ""

