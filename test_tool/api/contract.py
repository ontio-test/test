# -*- coding:utf-8 -*-
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys
import getopt
import subprocess
import time
import re

sys.path.append('..')
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.taskrunner import TaskRunner
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.common import Common
from node import NodeApi

nodeapi = NodeApi()

class ContractApi:
    def deploy_contract_full(self, neo_code_path, name = "name", desc = "this is desc", price = 0):
        try:
            if not neo_code_path or neo_code_path == "":
                return None

            deploy_contract_addr = None
            deploy_contract_txhash = None
            
            logger.print("[ DEPLOY ] ")
            cmd = Config.TOOLS_PATH + "/deploy_contract.sh " + neo_code_path + " \"" + name + "\" \"" + desc + "\" \"" + str(price) +  "\" > tmp"
            logger.print(cmd)
            p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
            begintime = time.time()
            secondpass = 0
            timeout = 3
            while p.poll() is None:
                secondpass = time.time() - begintime
                if secondpass > timeout:
                    p.terminate()
                    logger.error("Error: execute " + cmd + " time out!")
                time.sleep(0.1)
            p.stdout.close()

            tmpfile = open("tmp", "r+")  # 打开文件
            contents = tmpfile.readlines()
            for line in contents:
                #for log
                logger.print(line.strip('\n'))

            for line in contents:
                regroup = re.search(r'Contract Address:(([0-9]|[a-z]|[A-Z])*)', line)
                if regroup:
                    deploy_contract_addr = regroup.group(1)

                regroup = re.search(r'TxHash:(([0-9]|[a-z]|[A-Z])*)', line)
                if regroup:
                    deploy_contract_txhash = regroup.group(1)

                if deploy_contract_addr and deploy_contract_txhash:
                    break
            tmpfile.close()
            return (deploy_contract_addr, deploy_contract_txhash)
        except Exception as e:
            print(e)
            return (None, None)

    #部署合约
    #返回值： 部署的合约地址
    def deploy_contract(self, neo_code_path, name = "name", desc = "this is desc", price = 0):
        (deploy_contract_addr, deploy_contract_txhash) = self.deploy_contract_full(neo_code_path, name, desc, price)
        nodeapi.wait_gen_block()
        return deploy_contract_addr

    def sign_transction(self, task, judge = True, process_log = True):
        if task.node_index() != None:
            logger.info("sign transction with other node: " + str(task.node_index()))
            task.set_type("st")
            request = task.request()
            task.set_request({
                                "method": "siginvoketx",
                                "jsonrpc": "2.0",
                                "id": 0,
                            })
            task.request()["params"] = request

            (result, response) = TaskRunner.run_single_task(task, False, process_log)
            if result:
                response = response["result"]
            return (result, response)
        else:
            task.set_type("cli")
            (result, response) = TaskRunner.run_single_task(task, False, process_log)
            return (result, response)

    def call_signed_contract(self, signed_tx, pre = True, node_index = None):
        sendrawtxtask = Task(Config.BASEAPI_PATH + "/rpc/sendrawtransaction.json")
        if pre:
            sendrawtxtask.request()["params"] = [signed_tx, 1]
        else:
            sendrawtxtask.request()["params"] = [signed_tx]

        if node_index != None:
            sendrawtxtask.data()["NODE_INDEX"] = node_index
            
        (result, response) = TaskRunner.run_single_task(sendrawtxtask, True, False)

        sendrawtxtask.data()["RESPONSE"] = response

        if not response is None and ("result" in response and "Result" in response["result"]) and not isinstance(response["result"]["Result"], list):
            response["result"]["Result String"] = HexToByte(response["result"]["Result"]).decode('iso-8859-1')

        logger.print("[ CALL CONTRACT ] " + json.dumps(sendrawtxtask.data(), indent = 4))

        return (result, response)

    #运行合约
    #task: 需要执行的task
    #judge: 是否需要比较结果
    #pre: 是否需要预执行
    # 返回值: (result: True or False, response: 网络请求， 如果result为False, 返回的是字符串)
    def call_contract(self, task, judge = True, pre = True, twice = False, sleep = 5):
        try:
            logger.print("\n")
            logger.print("[-------------------------------]")
            logger.print("[ RUN      ] "+ "contract" + "." + task.name())
            
            taskdata = task.data()
            node_index = None
            deploy_first = False
            deploy_code_path = None
            deploy_contract_addr = None
            for key in taskdata:
                if key.upper() == "DEPLOY":
                    deploy_first = taskdata[key]
                if key.upper() == "CODE_PATH":
                    deploy_code_path = taskdata[key]
                if key.upper() == "NODE_INDEX":
                    node_index = int(taskdata[key])

            if deploy_first:
                deploy_contract_addr = self.deploy_contract(deploy_code_path)
            #step 1: signed tx
            expect_response = None
            expect_signresponse = None
            if "RESPONSE" in taskdata:
                expect_response = taskdata["RESPONSE"]

            if "SIGN_RESPONSE" in taskdata:
                expect_signresponse = taskdata["SIGN_RESPONSE"]

            if deploy_contract_addr:
                taskdata["REQUEST"]["Params"]["address"] = deploy_contract_addr.strip()

            (result, response) = self.sign_transction(task, True, False)

            task.data()["RESPONSE"] = response
            logger.print("[ SIGNED TX ] " + json.dumps(taskdata, indent = 4))

            #step 2: call contract
            if expect_signresponse != None:             
                result = Common.cmp(expect_signresponse, response)
                if result and "error_code" in response and int(response["error_code"]) != 0:
                    return (result, response) 

                if not result:
                    raise Error("not except sign result")


            signed_tx = None
            if not response is None and "result" in response and not response["result"] is None and "signed_tx" in response["result"]:
                signed_tx = response["result"]["signed_tx"]

            if signed_tx == None or signed_tx == '':
                raise Error("no signed tx")

            if twice:
                (result, response) = self.call_signed_contract(signed_tx, True, node_index)
                (result1, response2) = self.call_signed_contract(signed_tx, False, node_index)
                if response and response2 and "result" in response2:
                    response["txhash"] = response2["result"]
            else:
                (result, response) = self.call_signed_contract(signed_tx, pre, node_index)
        
            if response is None or "error" not in response:# or str(response["error"]) != '0':
                raise Error("call contract error")

            if judge and expect_response:
                result = Common.cmp(expect_response, response)
                if not result:
                    raise Error("not except result")

            response["signed_tx"] = signed_tx
            if deploy_contract_addr:
                response["address"] = taskdata["REQUEST"]["Params"]["address"]
            
            time.sleep(sleep)
            return (result, response)

        except Error as err:
            return (False, err.msg)

    def sign_multi_transction(self, task, judge = True, process_log = True):
        if task.node_index() != None:
            logger.info("sign transction with other node: " + str(task.node_index()))
            task.set_type("st")
            request = task.request()
            task.set_request({
              "method": "siginvoketx",
              "jsonrpc": "2.0",
              "id": 0,
            })
            task.request()["params"] = request
            (result, response) = TaskRunner.run_single_task(task, False, process_log)
            if result:
                response = response["result"]
            return (result, response)
        else:
            task.set_type("cli")
            (result, response) = TaskRunner.run_single_task(task, False, process_log)
            return (result, response)

    def call_multisig_contract(self, task, m, pubkeyArray, sleep = 5):
        taskdata = task.data()

        (result, response) = self.sign_transction(task)#Task(name="multi", ijson=request))
        if not result:
            logger.error("call_multisig_contract.sign_transction error!")
            return (result, response)
        signed_tx = response["result"]["signed_tx"]
        
        #print(request1)
        execNum=0
        signed_raw=signed_tx
        for pubkey in pubkeyArray:
            request1 = {
                "REQUEST": {
                    "qid":"1",
                    "method":"sigmutilrawtx",
                    "params":{
                        "raw_tx":signed_raw,
                        "m":m,
                        "pub_keys":pubkeyArray
                    }
                },
                "RESPONSE": {"error_code" : 0}
            }
            for node_index in range(len(Config.NODES)):
                if Config.NODES[node_index]["pubkey"] == pubkey:
                    request1["NODE_INDEX"] = node_index 
                    (result, response) = self.sign_multi_transction(Task(name="multi", ijson=request1))
                    if not result:
                        logger.error("call_multisig_contract.sign_multi_transction error![1]")
                        return (result, response)
                    if "error_code" not in response or response["error_code"] != 0:
                        logger.error("call_multisig_contract.sign_multi_transction error![2]")
                        return (False, response)
                    signed_raw = response["result"]["signed_tx"]
                    logger.info("multi sign tx:" + str(execNum)+pubkey)
                    execNum=execNum+1
                    break
                    
            if execNum >= m:
                (result,response)=self.call_signed_contract(signed_raw, True)
                self.call_signed_contract(signed_raw, False)
                time.sleep(sleep)
                return (result,response)
                
        return (False, {"error_info":"multi times lesss than except!only "+str(execNum)})

    def init_admin(self, contract_address, admin_address, node_index = None):
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
                            "value": "init"
                        },
                        {
                            "type": "array",
                            "value": [
    							{
    								"type" : "string",
    								"value" : ""
    							}
                            ]
                        },
    					{
                            "type": "array",
                            "value": [
    							{
    								"type" : "string",
    								"value" : ""
    							}
                            ]
                        }
                    ]
                }
            },
            "RESPONSE":{"error" : 0}
        }

        if node_index != None:
            request["NODE_INDEX"] = node_index
        else:
            node_index = Config.ontid_map[admin_address]
            request["NODE_INDEX"] = node_index		
    	
        return self.call_contract(Task(name="init_admin", ijson=request), twice = True)

    def invoke_function(self, contract_address, function_str, callerOntID, public_key="1", argvs = [{"type": "string","value": ""}], node_index = None, sleep = 5):
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
                            "value": function_str
                        },
                        {
                            "type": "array",
                            "value": [
                                {
                                    "type": "bytearray",
                                    "value": callerOntID
                                },
                                {
                                    "type": "int",
                                    "value": public_key
                                }
                            ]
                        },
    					{
                            "type": "array",
                            "value": argvs
                        }
                    ]
                }
            },
            "RESPONSE":{"error" : 0}
        }

        if node_index != None:
            request["NODE_INDEX"] = node_index
        else:
            node_index = Config.ontid_map[callerOntID]
            request["NODE_INDEX"] = node_index
    		
        return self.call_contract(Task(name="invoke_function", ijson=request), twice = True, sleep = sleep)

    def invoke_function_test(self, contract_address, function_str, argvs = [{"type": "string","value": ""}], node_index = None):
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
                            "value": function_str
                        },
                        {
                            "type": "array",
                            "value": argvs
                        }
                    ]
                }
            },
            "RESPONSE":{"error" : 0}
        }
            
        return self.call_contract(Task(name="invoke_function_test", ijson=request), twice = True)