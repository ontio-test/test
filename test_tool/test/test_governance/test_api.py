# -*- coding:utf-8 -*-
import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from test_governance.test_config import test_config

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
