# -*- coding:utf-8 -*-
import re
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import shutil
import sys
import getopt
import time
import requests
import subprocess
import tempfile

import utils.base
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.commonapi import *
from utils.rpcapi import *
from utils.multi_sig import *
from utils.init_ong_ont import *

NODE_PATH = "/home/ubuntu/ontology/node"

TO_ADDRESS = Config.NODES[0]["address"]
CONTRACT_ADDRESS = "./neo_1_194.cs"


rpcapi = RPCApi()

logger = LoggerInstance

def get_avm(contract_path, type = "CSharp"):
    URL = "http://139.219.97.24:8080/api/v1.0/compile"
    with open(contract_path, "r") as f:
            code = f.read()
    try:
        data = {"code":code, "type":type}
        r = requests.post(URL, data=json.dumps(data))
    except:
        raise Error("Unable to load " + URL)

    response_json = r.json()
    if response_json["errcode"] == 0 and response_json["avm"]:
        return response_json["avm"]
    else:
        return None

def transfer_neo(contract_address, pay_address, get_address, amount, node_index=0):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": contract_address,
                "version": 1,
                "params": [
                    {
                        "type": "string",
                        "value": "transfer"
                    },

                    {
                        "type": "array",
                        "value":  [
                            {
                                "type": "bytearray",

                                "value": script_hash_bl_reserver(base58_to_address(pay_address))
                            },
                            {
                                "type": "bytearray",
                                "value": script_hash_bl_reserver(base58_to_address(get_address))
                            },
                            {
                                "type": "int",
                                "value": amount
                            }
                        ]
                    }
                ]
            }
        },
        "RESPONSE": {"error": 0},
        "NODE_INDEX": node_index
    }
    return call_contract(Task(name="transfer", ijson=request), twice=True)


def my_multi_contract(task, m, pubkeyArray, all_wallet_address):
    node_index = 0
    logger.print("restarting sig server")
    stop_sigsvr(node_index)
    start_sigsvr(all_wallet_address[0], node_index)
    time.sleep(2)
    # Task(name="multi", ijson=request))
    (result, response) = sign_transction(task)
    signed_tx = response["result"]["signed_tx"]

    # print(request1)
    execNum = 0
    signed_raw = signed_tx
    for pubkey in pubkeyArray:
        request1 = {
            "REQUEST": {
                "qid": "1",
                "method": "sigmutilrawtx",
                "params": {
                    "raw_tx": signed_raw,
                    "m": m,
                    "pub_keys": pubkeyArray
                }
            },
            "RESPONSE": {},
            "NODE_INDEX": node_index
        }

        wallet_address = all_wallet_address[pubkeyArray.index(pubkey)]
        stop_sigsvr(node_index)
        start_sigsvr(wallet_address, node_index)
        time.sleep(2)

        (result, response) = sign_multi_transction(
            Task(name="multi", ijson=request1))
        signed_raw = response["result"]["signed_tx"]
        print("multi sign tx:" + str(execNum)+pubkey)
        execNum = execNum+1
    print("exenum:", execNum)
    if execNum == m:
        (result, response) = call_signed_contract(signed_raw, True)
        call_signed_contract(signed_raw, False)
        return (result, response)

    return (False, {"error_info": "multi times lesss than except!only "+str(execNum)})


def get_balance_ont(address):
    (result, response) = rpcapi.getbalance(address)
    return int(response["result"]["ont"])

def get_balance_ong(address):
    (result, response) = rpcapi.getbalance(address)
    return int(response["result"]["ong"])


def init(node_index):
    wallets_path = NODE_PATH + "/wallets"
    list_dir = os.listdir(wallets_path)
    amount = "1"

    stop_sigsvr(node_index)
    start_sigsvr(NODE_PATH + "/wallet.dat", node_index)

    try:
        for wallet in list_dir:
            wallet_path = os.path.join(wallets_path, wallet)

            print("initing.....")
            time.sleep(2)

            with open(wallet_path, "r") as f:
                js_dict = json.load(f)
                address = js_dict["accounts"][0]["address"]

                # before transfer get balance
                balance1 = get_balance_ont(address)

                (result, response) = native_transfer_ont(
                    Config.NODES[0]["address"], address, amount, node_index)
                time.sleep(3)

                # after transfer get balance
                balance2 = get_balance_ont(address)

                print("transfer to address:", address)
                logger.print("balance before transfer:"+str(balance1))
                logger.print("balance after transfer:"+str(balance2))

                if balance2 - balance1 != int(amount):
                    raise Error("transfer to address [" + address + "] failed")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, response)


def multi_wallet_sig(node_index):
    wallets_path = "/home/ubuntu/ontology/node/wallets"
    list_dir = os.listdir(wallets_path)
    amount = "1"

    try:
        for wallet in list_dir:
            wallet_path = os.path.join(wallets_path, wallet)
            stop_sigsvr(node_index)
            start_sigsvr(wallet_path, node_index)

            print("restarting sigserver...")
            time.sleep(2)

            with open(wallet_path, "r") as f:
                js_dict = json.load(f)
                address = js_dict["accounts"][0]["address"]

                print("transfer to address:", address, wallet_path)
                # before transfer get balance
                balance1 = get_balance_ont(address)

                (result, response) = native_transfer_ont(
                    address, Config.NODES[0]["address"], amount, node_index)
                time.sleep(3)

                # after transfer get balance
                balance2 = get_balance_ont(address)

                logger.print("balance before transfer:"+str(balance1))
                logger.print("balance after transfer:"+str(balance2))

                if balance1 - balance2 != int(amount):
                    raise Error("transfer to address [" + address + "] failed")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, response)


def get_all_pubkey():
    wallets_path = "/home/ubuntu/ontology/node/wallets"
    list_dir = os.listdir(wallets_path)
    all_address = []
    all_wallet_path = []

    for wallet in list_dir:
        wallet_path = os.path.join(wallets_path, wallet)

        with open(wallet_path, "r") as f:
            js_dict = json.load(f)
            address = js_dict["accounts"][0]["publicKey"]
            all_address.append(address)
            all_wallet_path.append(wallet_path)

    return (all_address, all_wallet_path)


def get_multi_sig_address(_index):
    node_path = "/home/ubuntu/ontology/node/ontology "
    if _index == 0:
        all_address = ",".join(get_all_pubkey()[0][0: 16])
        cmd = node_path + "account multisigaddr  -m 16 --pubkey " + all_address + " > tmp"
    elif _index == 1:
        all_address = ",".join(get_all_pubkey()[0][16: 32])
        cmd = node_path + "account multisigaddr  -m 16 --pubkey " + all_address + " > tmp"
    elif _index == 2:
        all_address = ",".join(get_all_pubkey()[0])  # [32: 35])
        cmd = node_path + "account multisigaddr  -m 3 --pubkey " + all_address + " > tmp"

    print(cmd)

    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT,
                         stdout=subprocess.PIPE, shell=True)
    time.sleep(2)
    tmpfile = open("tmp", "r+")  # 打开文件
    contents = tmpfile.readlines()
    for line in contents:
        if "MultiSigAddress" in line:
            regroup = re.search(
                r'MultiSigAddress:(([0-9]|[a-z]|[A-Z])*)', line)
            multi_address = regroup.group(1)
            print(multi_address)
            return multi_address

    return None


def multi_sig_transfer(pay_address, get_address, amount, node_index, sig_times, MultiSigAddress, all_wallet_address):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0100000000000000000000000000000000000000",
                "method": "transfer",
                "version": 1,
                "params": [
                    [
                        [
                            pay_address,
                            get_address,
                            amount
                        ]
                    ]
                ]
            }
        },
        "RESPONSE": {},
        "NODE_INDEX": node_index
    }

    return my_multi_contract(Task(name="transfer", ijson=request), sig_times, MultiSigAddress, all_wallet_address)


def test_41_():
    MultiSigAddress = get_multi_sig_address(0)
    all_address = get_all_pubkey()[0]
    wallet_address = get_all_pubkey()[1]
    amount1 = "100"
    amount2 = "50"
    to_address = TO_ADDRESS
    sig_times1 = 16
    sig_times2 = 15
    node_index = 0

    try:
        balance1 = get_balance_ont(MultiSigAddress)
        stop_sigsvr(node_index)
        start_sigsvr(NODE_PATH + "/wallet.dat", node_index)
        time.sleep(2)
        native_transfer_ont(
            Config.NODES[0]["address"], MultiSigAddress, amount1, 0)
        time.sleep(3)
        balance2 = get_balance_ont(MultiSigAddress)

        logger.print("balance2 : "+str(balance2))

        if balance2 - balance1 != int(amount1):
            raise Error("transfer to address [" + MultiSigAddress + "] failed")

        (result, response) = multi_sig_transfer(MultiSigAddress, to_address,
                                                amount2, 0, sig_times1, all_address[0:16], wallet_address[0:16])
        time.sleep(10)
        balance3 = get_balance_ont(MultiSigAddress)
        if balance2 - balance3 != int(amount2):
            raise Error("transfer to address [" + to_address + "] failed")

        (result, response) = multi_sig_transfer(MultiSigAddress, to_address,
                                                amount2, 0, sig_times2, all_address[0:16], wallet_address[0:16])
        time.sleep(10)
        balance4 = get_balance_ont(MultiSigAddress)
        if balance4 - balance3 == int(amount2):
            raise Error("transfer to address [" + to_address + "] failed")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, response)


def test_61_():
    MultiSigAddress = get_multi_sig_address(1)
    all_address = get_all_pubkey()[0]
    wallet_address = get_all_pubkey()[1]
    amount1 = "100"
    amount2 = "50"
    to_address = TO_ADDRESS
    sig_times1 = 16
    sig_times2 = 15
    node_index = 0

    try:
        balance1 = get_balance_ont(MultiSigAddress)
        stop_sigsvr(node_index)
        start_sigsvr(NODE_PATH + "/wallet.dat", node_index)
        time.sleep(2)
        native_transfer_ont(
            Config.NODES[0]["address"], MultiSigAddress, amount1, 0)
        time.sleep(5)
        balance2 = get_balance_ont(MultiSigAddress)

        if balance2 - balance1 != int(amount1):
            raise Error("transfer to address [" + MultiSigAddress + "] failed")

        (result, response) = multi_sig_transfer(MultiSigAddress, to_address,
                                                amount2, 0, sig_times1, all_address[16:32], wallet_address[16:32])
        time.sleep(10)
        balance3 = get_balance_ont(MultiSigAddress)
        if balance2 - balance3 != int(amount2):
            raise Error("transfer to address [" + to_address + "] failed")

        (result, response) = multi_sig_transfer(MultiSigAddress, to_address,
                                                amount2, 0, sig_times2, all_address[16:32], wallet_address[16:32])
        time.sleep(10)
        balance4 = get_balance_ont(MultiSigAddress)
        if balance4 - balance3 == int(amount2):
            raise Error("transfer to address [" + to_address + "] failed")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, response)


def test_62_():
    MultiSigAddress = get_multi_sig_address(2)
    all_address = get_all_pubkey()[0]
    wallet_address = get_all_pubkey()[1]
    amount1 = "100"
    amount2 = "50"
    to_address = TO_ADDRESS
    sig_times1 = 3
    sig_times2 = 2
    node_index = 0

    try:
        balance1 = get_balance_ont(MultiSigAddress)
        stop_sigsvr(node_index)
        start_sigsvr(NODE_PATH + "/wallet.dat", node_index)
        time.sleep(2)
        native_transfer_ont(
            Config.NODES[0]["address"], MultiSigAddress, amount1, 0)
        time.sleep(5)
        balance2 = get_balance_ont(MultiSigAddress)

        if balance2 - balance1 != int(amount1):
            raise Error("transfer to address [" + MultiSigAddress + "] failed")

        (result, response) = multi_sig_transfer(MultiSigAddress,
                                                to_address, amount2, 0, sig_times1, all_address, wallet_address)
        time.sleep(10)
        balance3 = get_balance_ont(MultiSigAddress)
        if balance2 - balance3 != int(amount2):
            raise Error("transfer to address [" + to_address + "] failed")

        (result, response) = multi_sig_transfer(MultiSigAddress,
                                                to_address, amount2, 0, sig_times2, all_address, wallet_address)
        time.sleep(10)
        balance4 = get_balance_ont(MultiSigAddress)
        if balance4 - balance3 == int(amount2):
            raise Error("transfer to address [" + to_address + "] failed")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, response)


def test_42_(node_index):
    wallets_path = "/home/ubuntu/ontology/node/wallets"
    list_dir = os.listdir(wallets_path)
    amount = "1"

    try:
        for wallet in list_dir:
            wallet_path = os.path.join(wallets_path, wallet)
            stop_sigsvr(node_index)
            start_sigsvr(wallet_path, node_index)

            print("restarting sigserver...")
            time.sleep(2)

            with open(wallet_path, "r") as f:
                js_dict = json.load(f)
                address = js_dict["accounts"][0]["address"]

                print("transfer to address:", address, wallet_path)
                # before transfer get balance
                balance1 = get_balance_ont(address)

                (result, response) = native_transfer_ont(
                    address, Config.NODES[0]["address"], amount, node_index)
                time.sleep(10)

                # after transfer get balance
                balance2 = get_balance_ont(address)

                logger.print("balance before transfer:"+str(balance1))
                logger.print("balance after transfer:"+str(balance2))

                if balance1 - balance2 != int(amount):
                    raise Error("transfer to address [" + address + "] failed")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, response)


def test_43_(node_index):
    wallets_path = "/home/ubuntu/ontology/node/wallets"
    list_dir = os.listdir(wallets_path)
    amount = "1"

    contract_address = deploy_contract("ont_neo.json")

    try:
        for wallet in list_dir:
            wallet_path = os.path.join(wallets_path, wallet)
            stop_sigsvr(node_index)
            start_sigsvr(wallet_path, node_index)

            print("restarting sigserver...")
            time.sleep(2)

            with open(wallet_path, "r") as f:
                js_dict = json.load(f)
                address = js_dict["accounts"][0]["address"]

                print("transfer to address:", address, wallet_path)
                # before transfer get balance
                balance1 = get_balance_ont(address)

                (result, response) = transfer_neo(contract_address,
                                                  address, Config.NODES[0]["address"], amount)
                time.sleep(3)

                # after transfer get balance
                balance2 = get_balance_ont(address)

                logger.print("balance before transfer:"+str(balance1))
                logger.print("balance after transfer:"+str(balance2))

                if balance1 - balance2 != int(amount):
                    raise Error("transfer to address [" + address + "] failed")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, response)


def test_37_(node_index):
    MultiSigAddress = get_multi_sig_address(2)
    amount1 = "100"
    amount2 = "50"
    to_address = TO_ADDRESS
    sig_times1 = 3
    sig_times2 = 2
    node_index = 0
    all_address = get_all_pubkey()[0]
    wallet_address = get_all_pubkey()[1]
    print(wallet_address[0:3])

    try:
        balance1 = get_balance_ont(MultiSigAddress)
        stop_sigsvr(node_index)
        start_sigsvr(NODE_PATH + "/wallet.dat", node_index)
        time.sleep(2)
        native_transfer_ont(
            Config.NODES[0]["address"], MultiSigAddress, amount1, 0)
        time.sleep(5)
        balance2 = get_balance_ont(MultiSigAddress)

        if balance2 - balance1 != int(amount1):
            raise Error("transfer to address [" + MultiSigAddress + "] failed")

        (result, response) = multi_sig_transfer(MultiSigAddress, to_address,
                                                amount2, 0, sig_times1, all_address[0:3], wallet_address[0:3])
        time.sleep(10)
        balance3 = get_balance_ont(MultiSigAddress)
        if balance2 - balance3 != int(amount2):
            raise Error("transfer to address [" + to_address + "] failed")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, response)

def native_transfer_ont(pay_address,get_address,amount, node_index = None,errorcode=0, gas_price=0):
	request = {
		"REQUEST": {
			"Qid": "t",
			"Method": "signativeinvoketx",
			"Params": {
				"gas_price": 0,
				"gas_limit": 1000000000,
				"address": "0100000000000000000000000000000000000000",
				"method": "transfer",
				"version": 1,
				"params": [
                    [
                        [
                            pay_address,
                            get_address,
                            amount
                        ]
                    ]
				]
			}
		},
		"RESPONSE":{"error" : errorcode},
		"NODE_INDEX":node_index
	}
	return call_contract(Task(name="transfer", ijson=request), twice = True)

def test_40_():
    try:
        (result, response) = native_transfer_ont(Config.NODES[0]["address"], Config.NODES[1]["address"], "1000", 0)
    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, response)

def test_44_():
    try:
        block_count1 = rpcapi.getblockcount()
        stop_node(3)
        time.sleep(10)
        block_count2 = rpcapi.getblockcount()
        if block_count1 == block_count2:
            raise Error("block count is not changing")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_18_():
    try:
        (result, response) = native_transfer_ont(Config.NODES[0]["address"], Config.NODES[1]["address"], "10", 0)
        rpcapi.getsmartcodeevent(response["txhash"])
    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)


def test_45_():
    try:
        # stop node 3
        block_count1 = rpcapi.getblockcount()
        stop_node(3)
        time.sleep(10)
        block_count2 = rpcapi.getblockcount()
        if block_count1 == block_count2:
            raise Error("block count is not changing")

        # stop node 2
        block_count1 = rpcapi.getblockcount()
        stop_node(2)
        time.sleep(10)
        block_count2 = rpcapi.getblockcount()
        if block_count1 != block_count2:
            raise Error("block count is changing")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_46_():
    try:
        # stop node 3
        block_count1 = rpcapi.getblockcount()
        stop_node(1)
        time.sleep(10)
        block_count2 = rpcapi.getblockcount()
        if block_count1 == block_count2:
            raise Error("block count is not changing")

        time.sleep(300)

        # stop node 2
        block_count1 = rpcapi.getblockcount()
        stop_node(2)
        time.sleep(10)
        block_count2 = rpcapi.getblockcount()
        if block_count1 != block_count2:
            raise Error("block count is changing")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_47_():
    try:
        block_count1 = rpcapi.getblockcount()
        stop_node(1)
        time.sleep(10)
        block_count2 = rpcapi.getblockcount()
        if block_count1 == block_count2:
            raise Error("block count is not changing")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_48_():
    try:
        # stop node 3
        block_count1 = rpcapi.getblockcount()
        stop_node(1)
        time.sleep(10)
        block_count2 = rpcapi.getblockcount()
        if block_count1 == block_count2:
            raise Error("block count is not changing")

        # stop node 2
        block_count1 = rpcapi.getblockcount()
        stop_node(2)
        time.sleep(10)
        block_count2 = rpcapi.getblockcount()
        if block_count1 == block_count2:
            raise Error("block count is not changing")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_49_():
    wallet_address1 = "/home/ubuntu/ontology/node/wallet.dat"
    wallet_address2 = "/home/ubuntu/ontology/node/wallet_bp.dat"
    node_index = 0
    try:
        if os.path.exists(wallet_address1):
            # back up pre-wallet
            shutil.move(wallet_address1, wallet_address2)
        time.sleep(2)

        new_wallet()

        wallet_json = get_wallet(wallet_address1)

        # restart node with new wallet
        stop_node(node_index)
        start_node(node_index)

        time.sleep(5)

        balance1 = get_balance_ont(Config.NODES[0]["address"])
        contents = shell_transfer(wallet_json["accounts"][0]["address"], Config.NODES[1]["address"], "10")
        balance2 = get_balance_ont(Config.NODES[0]["address"])

        if balance1 != balance2:
            raise Error("balance is not right")

        for line in contents:
            regroup = re.search(r'TxHash:(([0-9]|[a-z]|[A-Z])*)', line)
            if regroup:
                tx_hash = regroup.group(1)
  
        if not tx_hash:
            raise Error("tx_hash not found")
        logger.print("\ntxhash:"+tx_hash)

        time.sleep(6)
        state = get_tx_state(tx_hash)

        if state == 0:
            result = True
        else:
            result = False

        # move back
        shutil.move(wallet_address2, wallet_address1)

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_50_():
    wallet_address1 = "/home/ubuntu/ontology/node/wallet.dat"
    wallet_address2 = "/home/ubuntu/ontology/node/wallet_bp.dat"
    node_index = 0
    try:
        
        if os.path.exists(wallet_address1):
            # back up pre-wallet
            shutil.move(wallet_address1, wallet_address2)
        time.sleep(2)

        new_wallet()

        wallet_json = get_wallet(wallet_address1)

        # restart node with new wallet
        stop_node(node_index)
        start_node(node_index)
        time.sleep(5)

        balance1 = get_balance_ont(Config.NODES[0]["address"])
        contents = shell_transfer(wallet_json["accounts"][0]["address"], Config.NODES[1]["address"], "0", 1)
        balance2 = get_balance_ont(Config.NODES[0]["address"])

        if balance1 != balance2:
            raise Error("balance is not right")

        for line in contents:
            regroup = re.search(r'TxHash:(([0-9]|[a-z]|[A-Z])*)', line)
            if regroup:
                tx_hash = regroup.group(1)
  
        if not tx_hash:
            raise Error("tx_hash not found")
        logger.print("\ntxhash:"+tx_hash)

        time.sleep(6)
        state = get_tx_state(tx_hash)

        if state == 0:
            result = True
        else:
            result = False

        # move back
        shutil.move(wallet_address2, wallet_address1)
        
    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)


def test_51_():
    wallet_address1 = "/home/ubuntu/ontology/node/wallet.dat"
    wallet_address2 = "/home/ubuntu/ontology/node/wallet_bp.dat"
    node_index = 0
    amount1 = 10000
    amount2 = 100000
    try:
        
        if os.path.exists(wallet_address1):
            # back up pre-wallet
            shutil.move(wallet_address1, wallet_address2)
        time.sleep(2)

        new_wallet()

        wallet_json = get_wallet(wallet_address1)

        balance1 = get_balance_ont(Config.NODES[0]["address"])
        native_transfer_ont(Config.NODES[0]["address"], wallet_json["accounts"][0]["address"], str(amount1), 0)
        time.sleep(6)
        balance2 = get_balance_ont(Config.NODES[0]["address"])
        if balance1 - balance2 != amount1:
            raise Error("balance is not right")

        # restart node with new wallet
        stop_node(node_index)
        start_node(node_index)
        time.sleep(5)

        balance1 = get_balance_ont(Config.NODES[0]["address"])
        contents = shell_transfer(wallet_json["accounts"][0]["address"], Config.NODES[0]["address"], str(amount2))
        balance2 = get_balance_ont(Config.NODES[0]["address"])

        if balance1 != balance2:
            raise Error("balance is not right")

        for line in contents:
            regroup = re.search(r'TxHash:(([0-9]|[a-z]|[A-Z])*)', line)
            if regroup:
                tx_hash = regroup.group(1)
  
        if not tx_hash:
            raise Error("tx_hash not found")
        logger.print("\ntxhash:"+tx_hash)

        time.sleep(10)
        state = get_tx_state(tx_hash)

        if state == 0:
            result = True
        else:
            result = False

        # move back
        shutil.move(wallet_address2, wallet_address1)
        
    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_52_():
    wallet_address1 = "/home/ubuntu/ontology/node/wallet.dat"
    wallet_address2 = "/home/ubuntu/ontology/node/wallet_bp.dat"
    node_index = 0
    amount1 = 10000
    amount2 = 10
    result = True
    try:
        
        if os.path.exists(wallet_address1):
            # back up pre-wallet
            shutil.move(wallet_address1, wallet_address2)
        time.sleep(2)

        new_wallet()

        wallet_json = get_wallet(wallet_address1)

        balance1 = get_balance_ont(wallet_json["accounts"][0]["address"])
        native_transfer_ont(Config.NODES[0]["address"], wallet_json["accounts"][0]["address"], str(amount1), 0)
        time.sleep(10)
        balance2 = get_balance_ont(wallet_json["accounts"][0]["address"])
        if balance2 - balance1 != amount1:
            raise Error("balance is not right")

        # restart node with new wallet
        stop_node(node_index)
        start_node(node_index)
        time.sleep(5)

        balance1 = get_balance_ont(wallet_json["accounts"][0]["address"])
        contents = shell_transfer(wallet_json["accounts"][0]["address"], Config.NODES[0]["address"], str(amount2), 1)
        time.sleep(10)
        balance2 = get_balance_ont(wallet_json["accounts"][0]["address"])

        if balance1 != balance2:
            raise Error("balance is not right")

        # move back
        shutil.move(wallet_address2, wallet_address1)
        
    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_53_():
    wallet_address1 = "/home/ubuntu/ontology/node/wallet.dat"
    wallet_address2 = "/home/ubuntu/ontology/node/wallet_bp.dat"
    node_index = 0
    amount1 = 10000
    amount2 = 10
    result = True
    try:
        
        if os.path.exists(wallet_address1):
            # back up pre-wallet
            shutil.move(wallet_address1, wallet_address2)
        time.sleep(2)

        new_wallet()

        wallet_json = get_wallet(wallet_address1)

        balance1 = get_balance_ont(wallet_json["accounts"][0]["address"])
        native_transfer_ont(Config.NODES[0]["address"], wallet_json["accounts"][0]["address"], str(amount1), 0)
        time.sleep(15)
        balance2 = get_balance_ont(wallet_json["accounts"][0]["address"])
        if balance2 - balance1 != amount1:
            raise Error("balance is not right")

        # restart node with new wallet
        stop_node(node_index)
        start_node(node_index)
        time.sleep(5)

        balance1 = get_balance_ont(wallet_json["accounts"][0]["address"])
        contents = shell_transfer(wallet_json["accounts"][0]["address"], Config.NODES[0]["address"], str(amount2))
        time.sleep(15)
        balance2 = get_balance_ont(wallet_json["accounts"][0]["address"])

        if balance1 - balance2 != amount2:
            raise Error("balance is not right")

        # move back
        shutil.move(wallet_address2, wallet_address1)
        
    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_54_():
    wallet_address1 = "/home/ubuntu/ontology/node/wallet.dat"
    wallet_address2 = "/home/ubuntu/ontology/node/wallet_bp.dat"
    node_index = 0
    amount1 = 10000
    result = True
    try:
        
        if os.path.exists(wallet_address1):
            # back up pre-wallet
            shutil.move(wallet_address1, wallet_address2)
        time.sleep(2)

        new_wallet()

        wallet_json = get_wallet(wallet_address1)

        # restart node with new wallet
        stop_node(node_index)
        start_node(node_index)
        time.sleep(5)

        contents = shell_transfer(Config.NODES[1]["address"], Config.NODES[0]["address"], str(amount1))

        # move back
        shutil.move(wallet_address2, wallet_address1)
        
    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def native_transfer_ont_gasprice(pay_address, get_address, amount, node_index=0, gas_price=1):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": gas_price,
                "gas_limit": 1000000000,
                "address": "0100000000000000000000000000000000000000",
                "method": "transfer",
                "version": 1,
                "params": [
                    [
                        [
                            pay_address,
                            get_address,
                            amount
                        ]
                    ]
                ]
            }
        },
        "RESPONSE": {"error": 0},
        "NODE_INDEX": node_index
    }
    return call_contract(Task(name="transfer", ijson=request), twice=True)




def test_21_():
    try:
        block_count1 = rpcapi.getblockcount()[1]["result"]
        logger.print("block count1 "+str(block_count1))
        for i in range(1, 1000):
            native_transfer_ont_gasprice(
                Config.NODES[0]["address"], Config.NODES[2]["address"], "1", 0, int(i/10))
            block_count2 = rpcapi.getblockcount()[1]["result"]
            rpcapi.getblock(block_count2-1, None)
        time.sleep(2)
        block_count2 = rpcapi.getblockcount()[1]["result"]
        logger.print("block count2 "+str(block_count2))

        rpcapi.getblock(block_count2-1, None)
    except Exception as e:
        logger.print(e.msg)
        result = False

    return True


def test_55_():
    amount = "1"
    try:
        balance1 = get_balance_ont(Config.NODES[1]["address"])
        (result, response) = native_transfer_ont_gasprice(
            Config.NODES[1]["address"], Config.NODES[2]["address"], amount, 1, 10)
        time.sleep(5)

        balance2 = get_balance_ont(Config.NODES[1]["address"])

        logger.print("balance1:" + str(balance1))
        logger.print("balance2:" + str(balance2))

        if balance1 - balance2 != int(amount):
            raise Error("transfer failed")
    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, response)

def test_56_():
    result = True
    amount = 1
    try:    
    
        balance1 = get_balance_ont(Config.NODES[0]["address"])
        for i in range(10):
            native_transfer_ont_gasprice(Config.NODES[0]["address"], Config.NODES[1]["address"], str(amount), 0, gas_price=1000)
        time.sleep(15)
        balance2 = get_balance_ont(Config.NODES[0]["address"])

        if balance1 - balance2 != amount:
            raise Error("transfer failed")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)


def test_60_():
    amount = "297690825"
    try:
        balance1 = get_balance_ont(Config.NODES[0]["address"])
        (result, response) = native_transfer_ont_gasprice(
            Config.NODES[0]["address"], Config.NODES[2]["address"], amount, 0, 10)
        (result, response) = native_transfer_ont_gasprice(
            Config.NODES[0]["address"], Config.NODES[2]["address"], amount, 0, 100)
        time.sleep(5)

        balance2 = get_balance_ont(Config.NODES[0]["address"])

        logger.print("balance1:" + str(balance1))
        logger.print("balance2:" + str(balance2))

        if balance2 - balance1 != int(amount):
            raise Error("transfer failed")
    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, response)

def invoke_function_add(contract_address, node_index = None):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": contract_address,
                "version": 0,
                "params": [
                    {
                        "type": "string",
                        "value": "Add"
                    },
                    {
                        "type": "array",
                        "value": [
                            {
                                "type": "int",
                                "value": "1"
                            },
                            {
                                "type":"int",
                                "value":"1"
                            }
                        ]
                    }
                ]
            }
        },
        "RESPONSE": {}
    }
    
    return call_contract(Task(name="init_admin", ijson=request), twice = True)

def get_tx_state(tx_hash):
    cmd = Config.NODE_ADDRESS + " info status " + tx_hash + " > "+ Config.ROOT_PATH + "/test_m/tmp"
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, shell=True)
    print(cmd)
    state = None
    begintime = time.time()
    secondpass = 0
    timeout = 2
    
    while p.poll() is None:
        secondpass = time.time() - begintime
        if secondpass > timeout:
            p.terminate()
            print("Error: execute " + cmd + " time out!")
        time.sleep(0.1)
    
    with open("tmp", "r+") as tmpfile:# 打开文件
        contents = tmpfile.readlines()

    for line in contents:
        #for log
        logger.print(line.strip('\n'))
    
    for line in contents:
        regroup = re.search(r'"State": (([0-9])*)', line)
        if regroup:
            state = regroup.group(1)
    return int(state) if state else None


def exec_cmd(cmd, show_output=True):
    contents = None

    print(cmd)
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, shell=True)
    begintime = time.time()
    secondpass = 0
    timeout = 2
    while p.poll() is None:
        secondpass = time.time() - begintime
        if secondpass > timeout:
            p.terminate()
            print("Error: execute " + cmd + " time out!")
        time.sleep(0.1)

    if show_output:
        with open("tmp", "r+") as tmpfile:# 打开文件
            contents = tmpfile.readlines()

        for line in contents:
            #for log
            logger.print(line.strip('\n'))
    return contents

def test_01_():
    node_index = 0
    avm_file_path = Config.ROOT_PATH + "/test_m/tmp.avm"
    tx_hash = None

    try:
        avm = get_avm(CONTRACT_ADDRESS).strip("b'")
        logger.print(avm)

        with open(avm_file_path, "w") as f:
            f.write(avm)
            f.flush()
        time.sleep(2)

        contract_address = deploy_contract(avm_file_path)

        logger.print("transfering ont...")
        transfer_ont(node_index, node_index, 100)
        logger.print("withdrawing ong...")
        withdrawong(node_index)

        get_balance_ont(Config.NODES[node_index]["address"])

        cmd = "cd ~/ontology/node\n"
        cmd += "echo 123456|" + Config.NODE_ADDRESS + " contract invoke --address "+ contract_address + " --params string:Add,[int:1,int:1] > " + Config.ROOT_PATH + "/test_m/tmp"
        contents = exec_cmd(cmd)
        
        for line in contents:
            regroup = re.search(r'TxHash:(([0-9]|[a-z]|[A-Z])*)', line)
            if regroup:
                tx_hash = regroup.group(1)
  
        if not tx_hash:
            raise Error("tx_hash not found")
        logger.print("\ntxhash:"+tx_hash)

        time.sleep(2)
        state = get_tx_state(tx_hash)

        if state == 1:
            result = True
        else:
            result = False

        # (result, response) = invoke_function_add(contract_address)

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_02_():
    node_index = 0
    avm_file_path = Config.ROOT_PATH + "/test_m/tmp.avm"
    tx_hash = None

    try:
        # start node
        '''
        stop_node(node_index)
        start_node(node_index)
        time.sleep(300) # waiting for sync
        '''

        gas_price1 = get_balance_ong(Config.NODES[node_index]["address"])
        logger.print (str(gas_price1))

        # deploy 
        avm = get_avm(CONTRACT_ADDRESS).strip("b'")
        logger.print(avm)

        with open(avm_file_path, "w") as f:
            f.write(avm)
            f.flush()
        time.sleep(2)

        contract_address = deploy_contract(avm_file_path)

        # invoke -p
        cmd = "cd ~/ontology/node\n"
        cmd += "echo 123456|" + Config.NODE_ADDRESS + " contract invoke --address "+ contract_address + " --params string:Add,[int:1,int:1] -p> " + Config.ROOT_PATH + "/test_m/tmp"
        contents = exec_cmd(cmd)
        
        for line in contents:
            regroup = re.search(r'Return:(([0-9]|[a-z]|[A-Z])*)', line)
            if regroup:
                return_value = regroup.group(1)
  
        if not return_value:
            raise Error("return_value not found")
        logger.print("\nreturn:"+return_value)

    
        # invoke
        cmd = "cd ~/ontology/node\n"
        cmd += "echo 123456|" + Config.NODE_ADDRESS + " contract invoke --address "+ contract_address + " --params string:Add,[int:1,int:1] --gasprice 1 > " + Config.ROOT_PATH + "/test_m/tmp"
        contents = exec_cmd(cmd)

        for line in contents:
            regroup = re.search(r'TxHash:(([0-9]|[a-z]|[A-Z])*)', line)
            if regroup:
                tx_hash = regroup.group(1)
  
        if not tx_hash:
            raise Error("tx_hash not found")
        logger.print("\ntxhash:"+tx_hash)

        time.sleep(2)
        state = get_tx_state(tx_hash)

        if state == 1:
            result = True
        else:
            raise Error("tx state is not 1")
        
        gas_price2 = get_balance_ong(Config.NODES[node_index]["address"])
        logger.print (str(gas_price2))

        logger.print ("gas price:"+str(gas_price1 - gas_price2))

        if gas_price1 - gas_price2 < 20000:
            raise Error("gas price is not 20000")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_20_():
    result = True
    try:
        cmd = "cd ~/ontology/node\n"
        cmd += 'echo "123456" |' + Config.NODE_ADDRESS + ' account list > ' + Config.ROOT_PATH + '/test_m/tmp'
        exec_cmd(cmd)

        for i in range(0, 10):
            cmd = "cd ~/ontology/node\n"
            cmd += Config.NODE_ADDRESS + ' account add -d > ' + Config.ROOT_PATH + '/test_m/tmp'
            # exec_cmd(cmd)#, show_output=False)
            print(cmd)
            p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True)
            p.stdin.write(b'123456\n')
            time.sleep(1)
            p.stdin.write(b'123456\n')  

            begintime = time.time()
            secondpass = 0
            timeout = 2
            while p.poll() is None:
                secondpass = time.time() - begintime
                if secondpass > timeout:
                    p.terminate()
                    print("Error: execute " + cmd + " time out!")
                time.sleep(0.1)

            with open("tmp", "r+") as tmpfile:# 打开文件
                contents = tmpfile.readlines()

            for line in contents:
                #for log
                logger.print(line.strip('\n'))

        cmd = "cd ~/ontology/node\n"
        cmd += 'echo "123456" |' + Config.NODE_ADDRESS + ' account list > ' + Config.ROOT_PATH + '/test_m/tmp'
        exec_cmd(cmd)

        
    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_23_():
    result = False
    avm_file_path = Config.ROOT_PATH + "/test_m/tmp.avm"
    tx_hash = None
    try:
        
        time.sleep(2)
        print("stop all")
        stop_nodes([0,1,2,3,4,5,6,7,8])
        print("start all")
        start_nodes([0,1,2,3,4,5,6,7,8], Config.DEFAULT_NODE_ARGS, True, True)
        time.sleep(10)

        init_ont_ong()
        time.sleep(5)

        time.sleep(2)
        print("stop all")
        stop_nodes([0,1,2,3,4,5,6,7,8])
        print("start all")
        start_nodes([0,1,2,3,4,5,6,7,8], Config.DEFAULT_NODE_ARGS+" --gasprice 1000")
        time.sleep(10)
        
        # deploy 
        avm = get_avm(CONTRACT_ADDRESS).strip("b'")
        logger.print(avm)

        with open(avm_file_path, "w") as f:
            f.write(avm)
            f.flush()
        time.sleep(2)

        contract_address = deploy_contract(avm_file_path, price=1000)

        # invoke -p
        cmd = "cd ~/ontology/node\n"
        cmd += "echo 123456|" + Config.NODE_ADDRESS + " contract invoke --address "+ contract_address + " --params string:Add,[int:1,int:1] > " + Config.ROOT_PATH + "/test_m/tmp"
        contents = exec_cmd(cmd)

        for line in contents:
            regroup = re.search(r'TxHash:(([0-9]|[a-z]|[A-Z])*)', line)
            if regroup:
                tx_hash = regroup.group(1)
  
        if not tx_hash:
            raise Error("tx_hash not found")
        logger.print("\ntxhash:"+tx_hash)

        time.sleep(2)
        state = get_tx_state(tx_hash)

        if not state:
            result = True
        else:
            raise Error("invoke contract error")


    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_24_():
    result = False
    avm_file_path = Config.ROOT_PATH + "/test_m/tmp.avm"
    tx_hash = None
    try:
        '''
        time.sleep(2)
        print("stop all")
        stop_nodes([0,1,2,3,4,5,6])
        print("start all")
        start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
        time.sleep(10)

        init_ont_ong()
        time.sleep(5)
        for i in range(0, 7):
            time.sleep(2)
            print("stop node : ", str(i))
            stop_node(i)
            print("start node : ", str(i))
            start_node(i, Config.DEFAULT_NODE_ARGS+" --gasprice " + str((i+1) * 100))
        
        time.sleep(2)
        '''
        # deploy 
        avm = get_avm(CONTRACT_ADDRESS).strip("b'")
        logger.print(avm)

        with open(avm_file_path, "w") as f:
            f.write(avm)
            f.flush()
        time.sleep(2)

        contract_address = deploy_contract(avm_file_path, price=1000)

        # invoke -p
        cmd = "cd ~/ontology/node\n"
        cmd += "echo 123456|" + Config.NODE_ADDRESS + " contract invoke --address "+ contract_address + " --params string:Add,[int:1,int:1] --gasprice 301 > " + Config.ROOT_PATH + "/test_m/tmp"
        contents = exec_cmd(cmd)

        for line in contents:
            regroup = re.search(r'TxHash:(([0-9]|[a-z]|[A-Z])*)', line)
            if regroup:
                tx_hash = regroup.group(1)
  
        if not tx_hash:
            raise Error("tx_hash not found")
        logger.print("\ntxhash:"+tx_hash)

        time.sleep(2)
        state = get_tx_state(tx_hash)

        if not state:
            result = True
        else:
            raise Error("invoke contract error")


    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_25_():
    result = False
    avm_file_path = Config.ROOT_PATH + "/test_m/tmp.avm"
    tx_hash = None
    try:
        '''
        time.sleep(2)
        print("stop all")
        stop_nodes([0,1,2,3,4,5,6])
        print("start all")
        start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
        time.sleep(10)

        init_ont_ong()
        time.sleep(5)
        for i in range(0, 7):
            time.sleep(2)
            print("stop node : ", str(i))
            stop_node(i)
            print("start node : ", str(i))
            start_node(i, Config.DEFAULT_NODE_ARGS+" --gasprice " + str((i+1) * 100))
        
        time.sleep(2)
        '''
        # deploy 
        avm = get_avm(CONTRACT_ADDRESS).strip("b'")
        logger.print(avm)

        with open(avm_file_path, "w") as f:
            f.write(avm)
            f.flush()
        time.sleep(2)

        contract_address = deploy_contract(avm_file_path, price=1000)

        # invoke -p
        cmd = "cd ~/ontology/node\n"
        cmd += "echo 123456|" + Config.NODE_ADDRESS + " contract invoke --address "+ contract_address + " --params string:Add,[int:1,int:1] --gasprice 501 > " + Config.ROOT_PATH + "/test_m/tmp"
        contents = exec_cmd(cmd)

        for line in contents:
            regroup = re.search(r'TxHash:(([0-9]|[a-z]|[A-Z])*)', line)
            if regroup:
                tx_hash = regroup.group(1)
  
        if not tx_hash:
            raise Error("tx_hash not found")
        logger.print("\ntxhash:"+tx_hash)

        time.sleep(5)
        state = get_tx_state(tx_hash)

        if state == 1:
            result = True
        else:
            raise Error("tx state is not 1")


    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_26_():
    result = False
    avm_file_path = Config.ROOT_PATH + "/test_m/tmp.avm"
    tx_hash = None
    try:
        
        time.sleep(2)
        print("stop all")
        stop_nodes([0,1,2,3,4,5,6])
        print("start all")
        start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
        time.sleep(10)

        init_ont_ong()
        time.sleep(5)
        for i in range(0, 7):
            time.sleep(2)
            print("stop node : ", str(i))
            stop_node(i)
            print("start node : ", str(i))
            start_node(i, Config.DEFAULT_NODE_ARGS+" --gasprice " + str((i+1) * 100))
        
        time.sleep(2)
        
        # deploy 
        avm = get_avm(CONTRACT_ADDRESS).strip("b'")
        logger.print(avm)

        with open(avm_file_path, "w") as f:
            f.write(avm)
            f.flush()
        time.sleep(2)

        contract_address = deploy_contract(avm_file_path, price=1000)

        # invoke -p
        cmd = "cd ~/ontology/node\n"
        cmd += "echo 123456|" + Config.NODE_ADDRESS + " contract invoke --address "+ contract_address + " --params string:Add,[int:1,int:1] --gasprice 800 > " + Config.ROOT_PATH + "/test_m/tmp"
        contents = exec_cmd(cmd)

        for line in contents:
            regroup = re.search(r'TxHash:(([0-9]|[a-z]|[A-Z])*)', line)
            if regroup:
                tx_hash = regroup.group(1)
  
        if not tx_hash:
            raise Error("tx_hash not found")
        logger.print("\ntxhash:"+tx_hash)

        time.sleep(5)
        state = get_tx_state(tx_hash)

        if state == 1:
            result = True
        else:
            raise Error("tx state is not 1")


    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def set_gasprice_B(gasprice_B, node_counts = 0):
    cmd = Config.ROOT_PATH + "/test_m/main setglobalparam --globalgasprice " + str(gasprice_B) + " --ip " + Config.NODES[0]["ip"]
    print(cmd)
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, shell=True)
    begintime = time.time()
    secondpass = 0
    timeout = 40
    while p.poll() is None:
        secondpass = time.time() - begintime
        if secondpass > timeout:
            p.terminate()
            print("Error: execute " + cmd + " time out!")
        time.sleep(0.1)

    time.sleep(15)

    return 

def test_27_():
    result = False
    avm_file_path = Config.ROOT_PATH + "/test_m/tmp.avm"
    tx_hash = None
    try:
        '''
        time.sleep(2)
        print("stop all")
        stop_nodes([0,1,2,3,4,5,6])
        print("start all")
        start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
        time.sleep(10)

        init_ont_ong()
        time.sleep(5)

        time.sleep(2)
        print("stop all")
        stop_nodes([0,1,2,3,4,5,6])
        print("start all")
        start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS+" --gasprice 1000")
        time.sleep(10)
        '''
        set_gasprice_B(800)
        
        # deploy 
        avm = get_avm(CONTRACT_ADDRESS).strip("b'")
        logger.print(avm)

        with open(avm_file_path, "w") as f:
            f.write(avm)
            f.flush()
        time.sleep(2)

        contract_address = deploy_contract(avm_file_path, price=2000)

        # invoke -p
        cmd = "cd ~/ontology/node\n"
        cmd += "echo 123456|" + Config.NODE_ADDRESS + " contract invoke --address "+ contract_address + " --params string:Add,[int:1,int:1] --gasprice 1001 > " + Config.ROOT_PATH + "/test_m/tmp"
        contents = exec_cmd(cmd)

        for line in contents:
            regroup = re.search(r'TxHash:(([0-9]|[a-z]|[A-Z])*)', line)
            if regroup:
                tx_hash = regroup.group(1)
  
        if not tx_hash:
            raise Error("tx_hash not found")
        logger.print("\ntxhash:"+tx_hash)

        time.sleep(5)
        state = get_tx_state(tx_hash)

        if state == 1:
            result = True
        else:
            raise Error("tx state is not 1")


    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_28_():
    result = False
    avm_file_path = Config.ROOT_PATH + "/test_m/tmp.avm"
    tx_hash = None
    try:
        '''
        time.sleep(2)
        print("stop all")
        stop_nodes([0,1,2,3,4,5,6])
        print("start all")
        start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
        time.sleep(10)

        init_ont_ong()
        time.sleep(5)

        time.sleep(2)
        print("stop all")
        stop_nodes([0,1,2,3,4,5,6])
        print("start all")
        start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS+" --gasprice 1000")
        time.sleep(10)
        '''
        set_gasprice_B(800)
        
        # deploy 
        avm = get_avm(CONTRACT_ADDRESS).strip("b'")
        logger.print(avm)

        with open(avm_file_path, "w") as f:
            f.write(avm)
            f.flush()
        time.sleep(2)

        contract_address = deploy_contract(avm_file_path, price=2000)

        # invoke -p
        cmd = "cd ~/ontology/node\n"
        cmd += "echo 123456|" + Config.NODE_ADDRESS + " contract invoke --address "+ contract_address + " --params string:Add,[int:1,int:1] --gasprice 801 > " + Config.ROOT_PATH + "/test_m/tmp"
        contents = exec_cmd(cmd)

        for line in contents:
            regroup = re.search(r'TxHash:(([0-9]|[a-z]|[A-Z])*)', line)
            if regroup:
                tx_hash = regroup.group(1)
  
        if not tx_hash:
            raise Error("tx_hash not found")
        logger.print("\ntxhash:"+tx_hash)

        time.sleep(10)
        state = get_tx_state(tx_hash)

        if not state:
            result = True
        else:
            raise Error("tx state exists")


    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_29_():
    result = False
    avm_file_path = Config.ROOT_PATH + "/test_m/tmp.avm"
    tx_hash = None
    try:
        time.sleep(2)
        print("stop all")
        stop_nodes([0,1,2,3,4,5,6])
        print("start all")
        start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
        time.sleep(10)

        init_ont_ong()
        time.sleep(5)

        time.sleep(2)
        print("stop all")
        stop_nodes([0,1,2,3,4,5,6])
        print("start all")
        start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS+" --gasprice 600")
        time.sleep(10)

        set_gasprice_B(800)
        
        # deploy 
        avm = get_avm(CONTRACT_ADDRESS).strip("b'")
        logger.print(avm)

        with open(avm_file_path, "w") as f:
            f.write(avm)
            f.flush()
        time.sleep(2)

        contract_address = deploy_contract(avm_file_path, price=2000)

        # invoke -p
        cmd = "cd ~/ontology/node\n"
        cmd += "echo 123456|" + Config.NODE_ADDRESS + " contract invoke --address "+ contract_address + " --params string:Add,[int:1,int:1] --gasprice 801 > " + Config.ROOT_PATH + "/test_m/tmp"
        contents = exec_cmd(cmd)

        for line in contents:
            regroup = re.search(r'TxHash:(([0-9]|[a-z]|[A-Z])*)', line)
            if regroup:
                tx_hash = regroup.group(1)
  
        if not tx_hash:
            raise Error("tx_hash not found")
        logger.print("\ntxhash:"+tx_hash)

        time.sleep(5)
        state = get_tx_state(tx_hash)

        if state == 1:
            result = True
        else:
            raise Error("tx state is not 1")


    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_30_():
    result = False
    avm_file_path = Config.ROOT_PATH + "/test_m/tmp.avm"
    tx_hash = None
    try:
        
        time.sleep(2)
        print("stop all")
        stop_nodes([0,1,2,3,4,5,6])
        print("start all")
        start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
        time.sleep(10)

        init_ont_ong()
        time.sleep(5)
        
        time.sleep(2)
        print("stop all")
        stop_nodes([0,1,2,3,4,5,6])
        print("start all")
        start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS+" --gasprice 600")
        time.sleep(10)
        
        set_gasprice_B(800)
        
        # deploy 
        avm = get_avm(CONTRACT_ADDRESS).strip("b'")
        logger.print(avm)

        with open(avm_file_path, "w") as f:
            f.write(avm)
            f.flush()
        time.sleep(2)

        contract_address = deploy_contract(avm_file_path, price=1000)

        # invoke -p
        cmd = "cd ~/ontology/node\n"
        cmd += "echo 123456|" + Config.NODE_ADDRESS + " contract invoke --address "+ contract_address + " --params string:Add,[int:1,int:1] --gasprice 700 > " + Config.ROOT_PATH + "/test_m/tmp"
        contents = exec_cmd(cmd)

        for line in contents:
            regroup = re.search(r'TxHash:(([0-9]|[a-z]|[A-Z])*)', line)
            if regroup:
                tx_hash = regroup.group(1)
  
        if not tx_hash:
            raise Error("tx_hash not found")
        logger.print("\ntxhash:"+tx_hash)

        time.sleep(5)
        state = get_tx_state(tx_hash)

        if not state:
            result = True
        else:
            raise Error("tx state exists")


    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def new_wallet():
    cmd = "cd ~/ontology/node\n"
    cmd += Config.NODE_ADDRESS + ' account add -d > ' + Config.ROOT_PATH + '/test_m/tmp'
    # exec_cmd(cmd)#, show_output=False)
    print(cmd)
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True)
    p.stdin.write(b'123456\n')
    time.sleep(1)
    p.stdin.write(b'123456\n') 
    p.stdin.close()
    time.sleep(1) 
    p.terminate()
    return 

def shell_get_balance(index):
    cmd = "cd ~/ontology/node\n"
    cmd += Config.NODE_ADDRESS + " asset balance " + str(index) + ' > ' + Config.ROOT_PATH + '/test_m/tmp'
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, shell=True)
    begintime = time.time()
    secondpass = 0
    timeout = 2
    while p.poll() is None:
        secondpass = time.time() - begintime
        if secondpass > timeout:
            p.terminate()
            print("Error: execute " + cmd + " time out!")
        time.sleep(0.1)

    with open("tmp", "r+") as tmpfile:# 打开文件
        contents = tmpfile.readlines()

    for line in contents:
        #for log
        logger.print(line.strip('\n'))

    for line in contents:
        regroup = re.search(r'ONT:(([0-9])*)', line)
        if regroup:
            balance = regroup.group(1)

    return int(balance)

def shell_transfer(_from, _to, _amount, _gas_price=0):
    cmd = "cd ~/ontology/node\n"
    cmd += "echo 123456 | " + Config.NODE_ADDRESS + " asset transfer --from " + str(_from) + " --to " + str(_to) + " --amount " + str(_amount) + " --gasprice " + str(_gas_price) + ' > ' + Config.ROOT_PATH + '/test_m/tmp'
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, shell=True)
    begintime = time.time()
    secondpass = 0
    timeout = 2
    while p.poll() is None:
        secondpass = time.time() - begintime
        if secondpass > timeout:
            p.terminate()
            print("Error: execute " + cmd + " time out!")
        time.sleep(0.1)

    with open("tmp", "r+") as tmpfile:# 打开文件
        contents = tmpfile.readlines()

    return contents

def change_alg(alg):
    cmd = "cd ~/ontology/node\n"
    cmd += "echo 123456 | " + Config.NODE_ADDRESS + " account set --signature-scheme " + alg + " 1 "
    print(cmd)
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, shell=True)
    begintime = time.time()
    secondpass = 0
    timeout = 2
    while p.poll() is None:
        secondpass = time.time() - begintime
        if secondpass > timeout:
            p.terminate()
            print("Error: execute " + cmd + " time out!")
        time.sleep(0.1)

def new_wallet_a(alg):
    cmd = "cd ~/ontology/node\n"
    cmd += Config.NODE_ADDRESS + ' account add '
    # exec_cmd(cmd)#, show_output=False)
    print(cmd)
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True)
    p.stdin.write(b'2\n' if alg == 2 else b'3\n')
    p.stdin.flush()
    time.sleep(3)
    p.stdin.write(b'123456\n')
    p.stdin.flush()
    time.sleep(3)
    p.stdin.write(b'123456\n')
    p.stdin.flush()
    time.sleep(3) 
    p.stdin.close()
    p.terminate()
    return 


def test_31_():
    result = True

    try:
        '''
        new_wallet()

        stop_node(node_index)
        start_node(node_index, " --testmode --rest --localrpc --gasprice 0 --gaslimit 0 ", True, True)
        
        new_wallet()
        shell_get_balance(1)
        shell_get_balance(2)

        for alg in ["SHA256withECDSA", "SHA224withECDSA", "SHA384withECDSA", "SHA512withECDSA", "SHA3-224withECDSA", "SHA3-256withECDSA", "SHA3-384withECDSA", "SHA3-512withECDSA", "RIPEMD160withECDSA"]:
            print("changing... to alg ", alg)
            time.sleep(2)
            change_alg(alg)

            balance1 = shell_get_balance(1)
            shell_transfer(1, 2, 1)
            time.sleep(8)
            balance2 = shell_get_balance(1)
            
            if balance1 - balance2 != 1:
                raise Error("alg " + alg + " transfer failed")
        '''
        new_wallet_a(2)
        new_wallet_a(3)
        
        # A -> C
        balance1 = shell_get_balance(1)
        shell_transfer(1, 3, 1)
        time.sleep(8)
        balance2 = shell_get_balance(1)
        
        if balance1 - balance2 != 1:
            raise Error("A transfer to C failed")

        # C -> D
        balance1 = shell_get_balance(3)
        shell_transfer(3, 4, 1)
        time.sleep(8)
        balance2 = shell_get_balance(3)
        
        if balance1 - balance2 != 1:
            raise Error("C transfer to D failed")

        # D -> C
        balance1 = shell_get_balance(4)
        shell_transfer(4, 3, 1)
        time.sleep(8)
        balance2 = shell_get_balance(4)
        
        if balance1 - balance2 != 1:
            raise Error("D transfer to C failed")

        
    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_32_():
    result = True

    try:    
        cmd = "cd ~/ontology/node\n"
        cmd += Config.NODE_ADDRESS + " account import --source " + Config.ROOT_PATH + '/test_m/ontWallet.keystore'
        contents = exec_cmd(cmd)
        for line in contents:
            if "successfully" in line:
                result = True
                break
            else:
                raise Error("import from ontWallet.keystore failed")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_33_():
    result = True

    try:    
        cmd = "cd ~/ontology/node\n"
        cmd += Config.NODE_ADDRESS + " account import --source " + Config.ROOT_PATH + '/test_m/ontWallet_1.keystore'
        contents = exec_cmd(cmd)
        for line in contents:
            if "successfully" in line:
                raise Error("import from ontWallet.keystore_1 failed")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def test_34_():
    result = True

    try:    
        cmd = "cd ~/ontology/node\n"
        cmd += Config.NODE_ADDRESS + " account import --source " + Config.ROOT_PATH + '/test_m/ontWallet_2.keystore ' + ' > ' + Config.ROOT_PATH + '/test_m/tmp'
        contents = exec_cmd(cmd)
        for line in contents:
            if "successfully" in line:
                raise Error("import from ontWallet.keystore_1 failed")

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)

def get_wallet(wallet_address):
    with open(wallet_address, "rb") as wallet_file:
	    wallet_json = json.loads(wallet_file.read().decode("utf-8"))

    return wallet_json

def import_from_wif_key(passwd=b"123456\n", _exist=False):
    cmd = "cd ~/ontology/node\n"
    cmd += Config.NODE_ADDRESS + " account import --source " + Config.ROOT_PATH + '/test_m/WIF-key.txt -wif'# + ' > ' + Config.ROOT_PATH + '/test_m/tmp'
    print(cmd)
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True)
    p.stdin.write(passwd)
    p.stdin.flush()
    time.sleep(3)
    if _exist:
        p.stdin.close()
        p.terminate()
        return 
    p.stdin.write(passwd)
    p.stdin.flush()
    time.sleep(3) 
    p.stdin.close()
    p.terminate()
    return 

def test_35_():
    result = True
    wallet_address1 = "/home/ubuntu/ontology/node/wallet.dat"
    wallet_address2 = "/home/ubuntu/ontology/node/wallet_bp.dat"
    address = "AFr9bdZxAZwuy1VGZUeE9rmXBUEykdskyk"

    try:    
        if os.path.exists(wallet_address1):
            # back up pre-wallet
            shutil.move(wallet_address1, wallet_address2)

        #
        import_from_wif_key()
        if not os.path.exists(wallet_address1):
            raise Error("wallet file not exists")

        
        wallet_json = get_wallet(wallet_address1)
        if wallet_json["accounts"][0]["address"] != address:
            raise Error("wallet address 0 is not correct")
        
        #
        import_from_wif_key()
        wallet_json = get_wallet(wallet_address1)
        if wallet_json["accounts"][1]["address"] != address:
            raise Error("wallet address 1 is not correct")
        
        #
        import_from_wif_key(passwd = b"654321\n")
        wallet_json = get_wallet(wallet_address1)
        if wallet_json["accounts"][2]["address"] != address:
            raise Error("wallet address 1 is not correct")
        
        #
        print("removing wallet...")
        os.remove(wallet_address1)
        import_from_wif_key()
        if not os.path.exists(wallet_address1):
            raise Error("wallet file not exists")
        
        #
        print("removing wallet...")
        os.remove(wallet_address1)
        import_from_wif_key(_exist = True)
        if os.path.exists(wallet_address1):
            raise Error("wallet file exists")
        
        # move back
        shutil.move(wallet_address2, wallet_address1)

    except Exception as e:
        logger.print(e.msg)
        result = False

    return (result, None)