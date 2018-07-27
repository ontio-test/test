# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

sys.path.append('..')
sys.path.append('../..')
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
test_path = os.path.dirname(os.path.realpath(__file__))

#from utils.selfig import selfig

from utils.hexstring import *
from utils.error import Error
from utils.config import Config

from api.apimanager import API

class test_config():
	
	deploy_neo_1=test_path + "/resource/auth.neo"
	deploy_neo_2=test_path + "/resource/auth_2.neo"
	deploy_neo_3=test_path + "/resource/auth_3.neo"
	deploy_neo_4=test_path + "/resource/auth_4.neo"
	deploy_neo_5=test_path + "/resource/auth_10.neo"
	deploy_neo_6=test_path + "/resource/auth_11.neo"
	deploy_neo_7=test_path + "/resource/auth_12.neo"
	deploy_neo_8=test_path + "/resource/auth_138_A.neo"
	deploy_neo_9=test_path + "/resource/auth_138_B.neo"
	deploy_neo_10=test_path + "/resource/auth_139_A.neo"
	
	contract_addr = ""
	contract_addr_1 = ""
	contract_addr_2 = ""
	contract_addr_3 = ""
	contract_addr_10 = ""
	contract_addr_11 = ""
	contract_addr_12 = ""
	contract_addr_138_1 = ""
	contract_addr_138_2 = ""
	contract_addr_139 = ""
	
	CONTRACT_ADDRESS_CORRECT = ""               # correct
	CONTRACT_ADDRESS_INCORRECT_1 = ""          # wrong ontid
	CONTRACT_ADDRESS_INCORRECT_2 = ""          # null ontid
	CONTRACT_ADDRESS_INCORRECT_3 = ""          # init twice
	CONTRACT_ADDRESS_INCORRECT_4 = ""    # not real contract
	CONTRACT_ADDRESS_INCORRECT_5 = ""             # messy code
	CONTRACT_ADDRESS_INCORRECT_6 = ""                      # null
	CONTRACT_ADDRESS_INCORRECT_10 = ""        # verifytoken contract with wrong address
	CONTRACT_ADDRESS_INCORRECT_11 = ""        # verifytoken contract with messy code address
	CONTRACT_ADDRESS_INCORRECT_12 = ""        # verifytoken contract with wrong address

	CONTRACT_ADDRESS_138 = ""              # appcall contract with correct address
	CONTRACT_ADDRESS_139 = ""                # appcall contract with messy code address

	ontID_A = ByteToHex(bytes(Config.NODES[0]['ontid'], encoding = "utf8"))       # contract ontid
	ontID_B = ByteToHex(bytes(Config.NODES[2]['ontid'], encoding = "utf8"))     # the first ontid
	ontID_C = ByteToHex(b"did:ont:123")                    # messy code
	ontID_D = ""                
	ontID_E = ByteToHex(bytes(Config.NODES[3]['ontid'], encoding = "utf8"))                           # null

	ROLE_CORRECT = Config.roleA_hex                                              # roleA
	ROLE_INCORRECT_1 = ""                                                        # null
	ROLE_INCORRECT_2 = "7e21402324255e262a2820295f2b"                            # role "~!@#$%^&*( )_+"
	ROLE_INCORRECT_3 = "31313131313131"                                          # role not exist

	FUNCTION_A = "A"                                                             # function A
	FUNCTION_B = "B"                                                             # function B
	FUNCTION_C = "InvokeTransfer"                                                # function InvokeTransfer
	FUNCTION_D = "xxx"                                                           # function not exist

	KEY_NO_1 = "10"                                                              # wrong keyno
	KEY_NO_2 = "abc"                                                             # wrong keyno
	KEY_NO_3 = ""                                                                # null

	PERIOD_CORRECT = "20"                                                        # correct period
	PERIOD_INCORRECT_1 = "0"                                                     # period 0
	PERIOD_INCORRECT_2 = "-1"                                                    # wrong period -1
	PERIOD_INCORRECT_3 = "2.04"                                                  # wrong period 2.04
	PERIOD_INCORRECT_4 = "abc"                                                   # wrong period abc
	PERIOD_INCORRECT_5 = ""                                                      # null

	LEVEL_CORRECT = "1"                                                          # correct level 1
	LEVEL_INCORRECT_1 = "2"                                                      # wrong level 2
	LEVEL_INCORRECT_2 = "0"                                                      # wrong level 0
	LEVEL_INCORRECT_3 = "abc"                                                    # wrong level abc
	LEVEL_INCORRECT_4 = ""                                                       # null