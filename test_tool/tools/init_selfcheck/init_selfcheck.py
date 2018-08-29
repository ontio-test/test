# -*- coding:utf-8 -*-
import os
import sys
import logging
import paramiko
import hashlib
import json
import time

sys.path.append('..')
sys.path.append('../..')

#from utils.selfig import selfig
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.config import Config
from api.apimanager import API

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handle = logging.FileHandler("init_selfcheck.log", mode="w")
handle.setLevel(level=logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handle.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(level=logging.INFO)
console.setFormatter(formatter)

logger.addHandler(handle)
logger.addHandler(console)

def sftp_transfer(_from, _to, _node_index, _op="get"):
    # on local host
    if _node_index == 0:
        cmd = "cp -rf " + _from + " " + _to
        os.system(cmd)
        return 

    private_key = paramiko.RSAKey.from_private_key_file("../../resource/id_rsa", "367wxd")

    transport = paramiko.Transport((Config.NODES[_node_index]["ip"] , 22))

    transport.connect(username="ubuntu", pkey=private_key)

    sftp = paramiko.SFTPClient.from_transport(transport)

    if _op == "put":
        sftp.put(_from, _to)
    elif _op == "get":
        sftp.get(_from, _to)
    else:
        logger.error("operation not supported")

    transport.close()

def sftp_transfer_dir(_from, _to, _node_index, _op="get"):
    # on local host
    if _node_index == 0:
        cmd = "cp -rf " + _from + " " + _to
        os.system(cmd)
        return 

    private_key = paramiko.RSAKey.from_private_key_file("../../resource/id_rsa", "367wxd")

    transport = paramiko.Transport((Config.NODES[_node_index]["ip"] , 22))

    transport.connect(username="ubuntu", pkey=private_key)

    sftp = paramiko.SFTPClient.from_transport(transport)
    
    try:
        sftp.mkdir(_to)
    except:
        pass

    for item in os.listdir(_from):
        if _op == "put":
            sftp.put(os.path.join(_from, item), os.path.join(_to, item))
        elif _op == "get":
            sftp.get(os.path.join(_from, item), os.path.join(_to, item))
        else:
            logger.error("operation not supported")

    transport.close()


def calc_md5_for_file(_file):
    md5 = hashlib.md5()
    with open(_file, "rb") as f:
        md5.update(f.read())
    return md5.hexdigest()

def calc_md5_for_files(_folder):
    md5 = []
    files = os.listdir(_folder)
    files.sort()
    for _file in files:
        md5.append(str(calc_md5_for_file(os.path.join(_folder, _file))))
    return md5

def calc_md5_for_folder(folder):
  md5 = hashlib.md5()
  files = os.listdir(folder)
  files.sort()
  for _file in files:
    md5.update(str(calc_md5_for_file(os.path.join(folder, _file))).encode())
  return md5.hexdigest()

def get_connected_nodes():
    return int(API.rpc().getconnectioncount()[1]["result"])


class InitConfig():
    def __init__(self):
        self.initconfig = {}
    
    def get_init_config(self):
        with open("config.json") as f:
            cf = json.load(f)

        self.initconfig["ontology_source_path"] = cf["resource"]["root"] + cf["resource"]["ontology_source_name"]
        self.initconfig["wallet_source_path"] = cf["resource"]["root"] + cf["resource"]["wallet_source_name"]
        self.initconfig["onto_config_source_path"] = cf["resource"]["root"] + cf["resource"]["onto_config_source_name"]
        self.initconfig["test_config_source_path"] = cf["resource"]["root"] + cf["resource"]["test_config_source_name"]
        self.initconfig["sigsvr_source_path"] = cf["resource"]["root"] + cf["resource"]["sigsvr_source_name"]
        self.initconfig["abi_source_path"] = cf["resource"]["root"] + cf["resource"]["abi_source_name"]
        self.initconfig["test_service_source_path"] = cf["resource"]["root"] + cf["resource"]["test_service_source_name"]
        self.initconfig["ontology_dbft_1_source_name"] = cf["resource"]["root"] + cf["resource"]["ontology_dbft_1_source_name"]
        self.initconfig["ontology_dbft_2_source_name"] = cf["resource"]["root"] + cf["resource"]["ontology_dbft_2_source_name"]
        self.initconfig["ontology_dbft_3_source_name"] = cf["resource"]["root"] + cf["resource"]["ontology_dbft_3_source_name"]

        self.initconfig["node_path"] = cf["node"]["root"] + cf["node"]["onto_name"]
        self.initconfig["wallet_path"] = cf["node"]["root"] + cf["node"]["wallet_name"]
        self.initconfig["onto_config_path"] = cf["node"]["root"] + cf["node"]["onto_config_name"]
        self.initconfig["sigsvr_path"] = cf["node"]["root"] + cf["node"]["sigsvr_name"]
        self.initconfig["abi_path"] = cf["node"]["root"] + cf["node"]["abi_name"]
        self.initconfig["ntology_dbft_1_path"] = cf["node"]["root"] + cf["node"]["ontology_dbft_1_name"]
        self.initconfig["ntology_dbft_2_path"] = cf["node"]["root"] + cf["node"]["ontology_dbft_2_name"]
        self.initconfig["ntology_dbft_3_path"] = cf["node"]["root"] + cf["node"]["ontology_dbft_3_name"]

        self.initconfig["test_service_path"] = cf["test_service_path"]
        self.initconfig["test_config_path"] = cf["test_config_path"]
        self.initconfig["default_node_args"] = cf["default_node_args"]



class SelfCheck():
    def __init__(self, initconfig):
        self.nodecounts = len(Config.NODES)
        self.default_node_args = initconfig["default_node_args"]

        self.ontology_source_path = initconfig["ontology_source_path"]
        self.wallet_source_path = initconfig["wallet_source_path"]
        self.onto_config_source_path = initconfig["onto_config_source_path"]
        self.test_config_source_path = initconfig["test_config_source_path"]
        self.sigsvr_source_path = initconfig["sigsvr_source_path"]
        self.abi_source_path = initconfig["abi_source_path"]
        self.test_service_source_path = initconfig["test_service_source_path"]
        self.ontology_dft_1_source_path = initconfig["ontology_dbft_1_source_name"]
        self.ontology_dft_2_source_path = initconfig["ontology_dbft_2_source_name"]
        self.ontology_dft_3_source_path = initconfig["ontology_dbft_3_source_name"]

        self.node_path = initconfig["node_path"]
        self.wallet_path = initconfig["wallet_path"]
        self.onto_config_path = initconfig["onto_config_path"]
        self.test_config_path = initconfig["test_config_path"]
        self.sigsvr_path = initconfig["sigsvr_path"]
        self.abi_path = initconfig["abi_path"]
        self.test_service_path = initconfig["test_service_path"]
        self.ontology_dft_1_path = initconfig["ntology_dbft_1_path"]
        self.ontology_dft_2_path = initconfig["ntology_dbft_2_path"]
        self.ontology_dft_3_path = initconfig["ntology_dbft_3_path"]

        self.ontology_correct_md5 = str(calc_md5_for_file(self.ontology_source_path))
        self.wallet_correct_md5 = calc_md5_for_files(self.wallet_source_path)
        self.onto_config_md5 = str(calc_md5_for_file(self.onto_config_source_path))
        self.test_config_md5 = str(calc_md5_for_file(self.test_config_source_path))
        self.sigsvr_md5 = str(calc_md5_for_file(self.sigsvr_source_path))
        self.abi_md5 = str(calc_md5_for_folder(self.abi_source_path))
        self.test_service_md5 = str(calc_md5_for_file(self.test_service_source_path))


    def stop_nodes(self):
        logger.info("stop all nodes ontology and sigsvr")
        API.node().stop_all_nodes()
        API.node().stop_sigsvrs(list(range(len(Config.NODES))))
        for i in range(len(Config.NODES)):
            API.node().exec_cmd("killall sigsvr", i)
            API.node().exec_cmd("killall sigsvr-linux", i)

    def start_nodes(self):
        logger.info("start all nodes ontology and sigsvr")
        API.node().start_nodes(list(range(len(Config.NODES))), start_params=self.default_node_args, clear_chain = True, clear_log = True)
        API.node().start_sigsvrs(self.wallet_path, list(range(len(Config.NODES))))
        logger.info("waiting for 10 seconds......")
        time.sleep(10)

    def check_ontology(self):
        logger.info("----------------------------------")
        logger.info("start checking all nodes ontology\n")

        for i in range(self.nodecounts):
            logger.info("checking node " + str(i+1) + " ontology......")
            response = API.node().get_version_ontology(i)
            if "doesnot exists" in response["result"] or (response["result"]["md5"] != self.ontology_correct_md5):
                logger.error("node " + str(i+1) + " ontology version error or not exists")
                logger.info("start transfer ontology from node 1 to node " + str(i+1))
                sftp_transfer(self.ontology_source_path, self.node_path, i, "put")
                logger.info("transfer ontology OK ")
            
            API.node().check_xmode_ontology(i)

            logger.info("checking node " + str(i+1) + " ontology OK\n")

        logger.info("checking all nodes ontology OK")
        logger.info("----------------------------------\n\n")

    def check_ontology_dft(self):
        logger.info("----------------------------------")
        logger.info("start checking all nodes ontology_dft\n")

        for i in range(self.nodecounts):
            logger.info("checking node " + str(i+1) + " ontology_dft......")
            sftp_transfer(self.ontology_dft_1_source_path, self.ontology_dft_1_path, i, "put")
            sftp_transfer(self.ontology_dft_2_source_path, self.ontology_dft_2_path, i, "put")
            sftp_transfer(self.ontology_dft_3_source_path, self.ontology_dft_3_path, i, "put")
            
            logger.info("checking node " + str(i+1) + " ontology_dft OK\n")

        logger.info("checking all nodes ontology_dft OK")
        logger.info("----------------------------------\n\n")

    def check_wallet(self):
        logger.info("----------------------------------")
        logger.info("start checking all nodes wallets\n")

        for i in range(self.nodecounts):
            logger.info("checking node " + str(i+1) + " wallet......")
            response = API.node().get_version_wallet(i)
            if "doesnot exists" in response["result"] or (response["result"] != self.wallet_correct_md5[i]):
                logger.error("node " + str(i+1) + " wallet version error or not exists")
                logger.info("start transfer wallet from node 1 to node " + str(i+1))
                wallet_index = "0" + str(i) if i < 10 else str(i)
                sftp_transfer(self.wallet_source_path+"/wallet"+wallet_index+".dat", self.wallet_path, i, "put")
                logger.info("transfer wallet OK ")

            logger.info("checking node " + str(i+1) + " wallet OK\n")

        logger.info("checking all nodes wallets OK")
        logger.info("----------------------------------\n\n")
        
    def check_onto_config(self):
        logger.info("----------------------------------")
        logger.info("start checking all nodes ontology config\n")

        for i in range(self.nodecounts):
            logger.info("checking node " + str(i+1) + " ontology config......")
            response = API.node().get_version_onto_config(i)
            if "doesnot exists" in response["result"] or (response["result"] != self.onto_config_md5):
                logger.error("node " + str(i+1) + " ontology config version error or not exists")
                logger.info("start transfer ontology config from node 1 to node " + str(i+1))
                sftp_transfer(self.onto_config_source_path, self.onto_config_path, i, "put")
                logger.info("transfer ontology config OK ")

            logger.info("checking node " + str(i+1) + " ontology config OK\n")

        logger.info("checking all nodes ontology config OK")
        logger.info("----------------------------------\n\n")

    def check_test_config(self):
        logger.info("----------------------------------")
        logger.info("start checking all nodes test config\n")

        for i in range(self.nodecounts):
            logger.info("checking node " + str(i+1) + " test config......")
            response = API.node().get_version_test_config(i)
            if "doesnot exists" in response["result"] or (response["result"] != self.test_config_md5):
                logger.error("node " + str(i+1) + " test config version error or not exists")
                logger.info("start transfer test config from node 1 to node " + str(i+1))
                sftp_transfer(self.test_config_source_path, self.test_config_path, i, "put")
                logger.info("transfer test config OK ")

            logger.info("checking node " + str(i+1) + " test config OK\n")

        logger.info("checking all nodes test config OK")
        logger.info("----------------------------------\n\n")


    def check_sigsvr(self):
        logger.info("----------------------------------")
        logger.info("start checking all nodes sigsvr\n")

        for i in range(self.nodecounts):
            logger.info("checking node " + str(i+1) + " sigsvr......")
            response = API.node().get_version_sigsvr(i)
            if "doesnot exists" in response["result"] or (response["result"]["md5"] != self.sigsvr_md5):
                logger.error("node " + str(i+1) + " sigsvr version error or not exists")
                logger.info("start transfer sigsvr from node 1 to node " + str(i+1))
                sftp_transfer(self.sigsvr_source_path, self.sigsvr_path, i, "put")
                logger.info("transfer sigsvr OK ")
            
            API.node().check_xmode_sigsvr(i)

            logger.info("checking node " + str(i+1) + " sigsvr OK\n")

        logger.info("checking all nodes sigsvr OK")
        logger.info("----------------------------------\n\n")

    def check_abi(self):
        logger.info("----------------------------------")
        logger.info("start checking all nodes abi\n")

        for i in range(self.nodecounts):
            logger.info("checking node " + str(i+1) + " abi......")
            response = API.node().get_version_abi(i)
            if "doesnot exists" in response["result"] or (response["result"] != self.abi_md5):
                logger.error("node " + str(i+1) + " abi version error or not exists")
                logger.info("start transfer abi from node 1 to node " + str(i+1))
                sftp_transfer_dir(self.abi_source_path, self.abi_path, i, "put")
                logger.info("transfer abi OK ")

            logger.info("checking node " + str(i+1) + " abi OK\n")

        logger.info("checking all nodes abi OK")
        logger.info("----------------------------------\n\n")

    def check_tools(self):
        logger.info("----------------------------------")
        logger.info("start checking all nodes tools\n")

        for i in range(self.nodecounts):
            logger.info("checking node " + str(i+1) + " tools......")
            
            response = API.node().check_xmode_tools(i)
            if isinstance(response["result"], str) and "doesnot exists" in response["result"]:
                logger.error(response["result"])

            logger.info("checking node " + str(i+1) + " tools OK\n")

        logger.info("checking all nodes tools OK")
        logger.info("----------------------------------\n\n")

    def check_test_service(self):
        logger.info("----------------------------------")
        logger.info("start checking all nodes test service\n")

        for i in range(self.nodecounts):
            logger.info("checking node " + str(i+1) + " test service......")
            response = API.node().get_version_test_service(i)
            if "doesnot exists" in response["result"] or (response["result"] != self.test_service_md5):
                logger.error("node " + str(i+1) + " test service version error or not exists")
                logger.info("start transfer test service from node 1 to node " + str(i+1))
                sftp_transfer(self.test_service_source_path, self.test_service_path, i, "put")
                logger.info("transfer test service OK ")
                API.node().stop_test_service(i)

            logger.info("checking node " + str(i+1) + " test service OK\n")

        logger.info("checking all nodes test service OK")
        logger.info("----------------------------------\n\n")

    def check_self_wallets(self):
        logger.info("----------------------------------")
        logger.info("start checking self wallets\n")

        # check wallet amount
        files = os.listdir(self.wallet_source_path)
        files.sort()
        if len(files) != len(Config.NODES):
            logger.error("wallets number incorrect, wallets : [%d] config : [%d]" % (len(files), len(Config.NODES)))
        
        address = []
        pubkey = []
        with open(self.onto_config_source_path) as f:
            config_json = json.load(f)

        for _file in files:
            with open(os.path.join(self.wallet_source_path, _file)) as f:
                wallet_json = json.load(f)

            address.append(wallet_json["accounts"][0]["address"])
            pubkey.append(wallet_json["accounts"][0]["publicKey"])

        for nd in config_json["VBFT"]["peers"]:
            if not nd["address"] in address:
                logger.error("wallet address %s not in onto config" % nd["address"])
            if not nd["peerPubkey"] in pubkey:
                logger.error("wallet pubkey %s not in onto config" % nd["peerPubkey"])  

        logger.info("checking self wallets OK")
        logger.info("----------------------------------\n\n")

    def check_connected_nodes(self):
        logger.info("----------------------------------")
        logger.info("start checking connected node count\n")

        connected_node_count = get_connected_nodes()
        if connected_node_count != len(Config.NODES) - 1:
            logger.error("connected node counts : %d, config node counts : %d" % (connected_node_count, len(Config.NODES) - 1))

        logger.info("checking connected node count OK")
        logger.info("----------------------------------\n\n")

    def check_all(self):
        # stop all nodes
        self.stop_nodes()

        # check ontology exec mode and md5 value  
        self.check_ontology()

        # check ontology dbft 
        self.check_ontology_dft()

        # check abi md5 value
        self.check_abi()

        # check test service md5 value
        self.check_test_service()
        time.sleep(10)

        # check wallets and config in resource
        self.check_self_wallets()

        # check onto config
        self.check_onto_config()

        # check check node wallets
        self.check_wallet()

        # check sigsvr exec mode and md5 value
        self.check_sigsvr()

        # start all nodes
        self.start_nodes()

        # check connected node count
        self.check_connected_nodes()
        
        # self.check_test_config()  
        # self.check_tools()


if __name__ == "__main__":
    # get config
    initconfig = InitConfig()
    initconfig.get_init_config()

    #API.node().start_sigsvrs(initconfig.initconfig["wallet_path"], list(range(len(Config.NODES))))
    # start self check
    selfcheck = SelfCheck(initconfig.initconfig)
    selfcheck.check_all()


    
