# -*- coding:utf-8 -*-
import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from test_governance.test_config import test_config
from api.apimanager import API
from utils.common import Common
from utils.hexstring import *

class test_api():

    @staticmethod
    def get_config():
        wallet_A_address   = test_config.wallet_A_address
        wallet_B_address   = test_config.wallet_B_address
        vote_price 		   = test_config.vote_price
        node_B_puiblic_key = test_config.node_B_puiblic_key
        blocks_per_round   = test_config.blocks_per_round
        punish_ratio       = test_config.punish_ratio
        return (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio)
    
    @staticmethod
    def nodeCountCheck(InResponse,nodeCount):
        (result1, response1)=API.rpc().getstorage("0700000000000000000000000000000000000000",ByteToHex(b"governanceView"))
        if not result1:
            return (False,{"error_info":"getstorage governanceView error !"})
        viewvalue=""
        viewvalue=response1["result"][0:8]
        print(viewvalue)
        (result1, response1)=API.rpc().getstorage("0700000000000000000000000000000000000000",ByteToHex(b"peerPool")+viewvalue)
        if not result1:
            return (False,{"error_info":"getstorage peerPool error ! viewValue:"+viewvalue})
        resCheck = Common.bl_reserver(response1["result"][0:2])
        print(resCheck)
        resInt= bytes.fromhex(resCheck)
        print(resInt.hex())
        if isinstance(InResponse,dict):
            InResponse["nodeCountNow"]=int(resInt.hex(), 16)
        else:
            InResponse={"response":InResponse,"nodeCountNow":int(resInt.hex(), 16)}

        if (nodeCount==int(resInt.hex(), 16)):
            return (True,InResponse)
        else:
            return (False,InResponse)
