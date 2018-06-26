# -*- coding:utf-8 -*-
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys
import getopt

sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.commonapi import *
from utils.parametrizedtestcase import ParametrizedTestCase
from test_conf import testConfig


def get_config():
    wallet_A_address   = testConfig.wallet_A_address
    wallet_B_address   = testConfig.wallet_B_address
    vote_price 		   = testConfig.vote_price
    node_B_puiblic_key = testConfig.node_B_puiblic_key
    blocks_per_round   = testConfig.blocks_per_round
    punish_ratio       = testConfig.punish_ratio
    return (wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio)


def vote_for_peer(wallet_address, nodes_to_vote, ballot_to_vote):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "voteForPeer",
                "version": 0,
                "params": [
                    wallet_address,
                    nodes_to_vote,
                    ballot_to_vote
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request), twice = True)

def vote_for_peer_index(wallet_address, nodes_to_vote, ballot_to_vote):
    request = {
        "NODE_INDEX":0,
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "voteForPeer",
                "version": 0,
                "params": [
                    wallet_address,
                    nodes_to_vote,
                    ballot_to_vote
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request), twice = True)

def unvote_for_peer(wallet_address, nodes_to_vote, ballot_to_vote):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "unVoteForPeer",
                "version": 0,
                "params": [
                    wallet_address,
                    nodes_to_vote,
                    ballot_to_vote
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request), twice = True)

def unvote_for_peer_index(wallet_address, nodes_to_vote, ballot_to_vote):
    request = {
        "NODE_INDEX":0,
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "unVoteForPeer",
                "version": 0,
                "params": [
                    wallet_address,
                    nodes_to_vote,
                    ballot_to_vote
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request), twice = True)


def withdraw_ont(wallet_address, nodes_to_vote, ballot_to_vote):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "withdraw",
                "version": 0,
                "params": [
                    wallet_address,
                    nodes_to_vote,
                    ballot_to_vote
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request), twice = True)

def withdraw_ont_index(wallet_address, nodes_to_vote, ballot_to_vote):
    request = {
        "NODE_INDEX":0,
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "withdraw",
                "version": 0,
                "params": [
                    wallet_address,
                    nodes_to_vote,
                    ballot_to_vote
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request), twice = True)

def quit_node(node_public_key, wallet_address):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 10000,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "quitNode",
                "version": 0,
                "params": [
                    node_public_key,
                    wallet_address
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request))

def quit_node_index(node_public_key, wallet_address):
    request = {
        "NODE_INDEX":7,
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 10000,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "quitNode",
                "version": 0,
                "params": [
                    node_public_key,
                    wallet_address
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request))

def black_node(node_public_key):
    request = {
        "NODE_INDEX":5,
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 10000,
                "gas_limit": 1000000000,
                "address": "0700000000000000000000000000000000000000",
                "method": "blackNode",
                "version": 0,
                "params": [
                    node_public_key
                ]
            }
        },
        "RESPONSE": {}
    }

    return call_contract(Task(name="test_1", ijson=request), twice = True)

def getbalance_ont(wallet_address):
    getbalance = Task("../utils/baseapi/rpc/getbalance.json")
    getbalance.data()["REQUEST"]["params"] = [wallet_address]
    (result, response) = run_single_task(getbalance, True, False)
    return int(response["result"]["ont"])

def getblockcount():
    getbalance = Task("../utils/baseapi/rpc/getblockcount.json")
    (result, response) = run_single_task(getbalance, True, False)
    return int(response["result"])

def getMaxBlockChangeView():
    getbalance = Task("../utils/baseapi/rpc/getstorage.json")
    contract_address = "0200000000000000000000000000000000000000"
    key = "79626674436f6e666967"
    getbalance.data()["REQUEST"]["params"] = [contract_address, key]
    (result, response) = run_single_task(getbalance, True, False)
    return int(response["result"]["ont"])
