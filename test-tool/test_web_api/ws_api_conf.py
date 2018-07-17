# -*- coding: utf-8 -*-
import sys
sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.commonapi import *
from utils.contractapi import *
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.rpcapi import RPCApi

rpcApi = RPCApi()

def get_signed_data():
    request = {
        "REQUEST": {
        "Qid":"t",
        "Method":"signativeinvoketx",
        "Params":{
                "gas_price":0,
                "gas_limit":1000000000,
                "address":"0100000000000000000000000000000000000000",
                "method":"name",
                "version":0,
                "params":[]
            }
        },
        "RESPONSE": {
        }
    }
    return sign_transction(Task(name="get_signed_data", ijson=request))[1]["result"]["signed_tx"]

class Conf():
    (contract_addr, contract_tx_hash) = deploy_contract_full(Config.UTILS_PATH + "/test.neo")

    block_height = int(rpcApi.getblockcount()[1]["result"]) - 1
    block_hash = rpcApi.getblockhash(block_height - 1)[1]["result"]
    signed_data = get_signed_data()

    HEIGHT_CORRECT = block_height - 1
    HEIGHT_BORDER = 0
    HEIGHT_INCORRECT_1 = -1
    HEIGHT_INCORRECT_2 = block_height + 1000
    HEIGHT_INCORRECT_3 = "abc"

    BLOCK_HASH_CORRECT = block_hash
    BLOCK_HASH_INCORRECT_1 = "" # NULL
    BLOCK_HASH_INCORRECT_2 = block_hash[:-2] # HASH NOT EXISTENT
    BLOCK_HASH_INCORRECT_3 = block_hash + "1111"
    BLOCK_HASH_INCORRECT_4 = 1234

    TX_HASH_CORRECT = contract_tx_hash
    TX_HASH_INCORRECT_1 = "" # NULL
    TX_HASH_INCORRECT_2 = contract_tx_hash[:-2] # TX HASH NOT EXISTENT
    TX_HASH_INCORRECT_3 = contract_tx_hash + "1111"
    TX_HASH_INCORRECT_4 = 1234
    TX_HASH_INCORRECT_5 = "616ed453ff654ccc9b6048d3fc62b16aff8424a68be7cc21a9c9f4e9982b89db" # tx FAILED ??

    RAW_TRANSACTION_DATA_CORRECT = signed_data
    RAW_TRANSACTION_DATA_INCORRECT_1 = "" # NULL
    RAW_TRANSACTION_DATA_INCORRECT_2 = "11111111" + signed_data + "1111111111" # INCORRECT SERIALIZE
    RAW_TRANSACTION_DATA_INCORRECT_3 = 1234

    ACCOUNT_ADDRESS_CORRECT = Config.NODES[0]['address']
    ACCOUNT_ADDRESS_INCORRECT_1 = "" # NULL
    ACCOUNT_ADDRESS_INCORRECT_2 = Config.NODES[0]['address'] + "11" # NOT EXISTENT
    ACCOUNT_ADDRESS_INCORRECT_3 = "abc"
    ACCOUNT_ADDRESS_INCORRECT_4 = 1234

    CONTRACT_ADDRESS_CORRECT = contract_addr
    CONTRACT_ADDRESS_INCORRECT_1 = "" # NULL
    CONTRACT_ADDRESS_INCORRECT_2 = contract_addr + "11" # NOT EXISTENT
    CONTRACT_ADDRESS_INCORRECT_3 = "abc"
    CONTRACT_ADDRESS_INCORRECT_4 = 1234

    KEY_CORRECT = ""
    KEY_INCORRECT_1 = "" # NULL
    KEY_INCORRECT_2 = "" # NOT EXISTENT
    KEY_INCORRECT_3 = "abc"
    KEY_INCORRECT_4 = 1234 
