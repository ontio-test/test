# -*- coding:utf-8 -*-
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.commonapi import *
from utils.restfulapi import *
from utils.parametrizedtestcase import ParametrizedTestCase

DEFAULT_NODE_ARGS = "--ws --rest --loglevel=0 --clirpc --networkid=299"

####################################################
#test cases
class Test(ParametrizedTestCase):
    def clear_nodes(self):
        stop_nodes([0, 1, 2, 3, 4, 5, 6])
        start_nodes([0, 1, 2, 3, 4, 5, 6], DEFAULT_NODE_ARGS, True, True)
        time.sleep(10)

    def test_01_get_gen_blk_time(self):
        logger.open("01_get_gen_blk_time.log", "01_get_gen_blk_time")
        (result, response) = RestfulApi().getgenerateblocktime()
        logger.close(result)
    
    # 无区块
    def test_02_get_gen_blk_time(self):
        logger.open("02_get_gen_blk_time.log", "02_get_gen_blk_time")
        (result, response) = RestfulApi().getgenerateblocktime()
        logger.close(result)
        
    def test_03_get_conn_count(self):
        logger.open("03_get_conn_count.log", "03_get_conn_count")
        (result, response) = RestfulApi().getconnectioncount()
        logger.close(result)

    # 无节点
    def test_04_get_conn_count(self):
        logger.open("04_get_conn_count.log", "04_get_conn_count")
        (result, response) = RestfulApi().getconnectioncount()
        logger.close(result)
        
    def test_05_get_conn_count(self):
        logger.open("05_get_conn_count.log", "05_get_conn_count")
        task = Task(Config.BASEAPI_PATH + "/restful/get_conn_count.json")
        task.set_type("restful")
        taskrequest = task.request()
        taskrequest["api"] = "/api/v1/node/connection"
        task.set_request(taskrequest)
        (result, response) = run_single_task(task)
        logger.close(result)
        
    def test_06_get_conn_count(self):
        logger.open("06_get_conn_count.log", "06_get_conn_count")
        task = Task(Config.BASEAPI_PATH + "/restful/get_conn_count.json")
        task.set_type("restful")
        taskrequest = task.request()
        taskrequest["api"] = "/api/v1/node/"
        task.set_request(taskrequest)
        (result, response) = run_single_task(task)
        logger.close(result)

    def test_07_get_blk_txs_by_height(self,height=1):
        logger.open("07_get_blk_txs_by_height.log", "07_get_blk_txs_by_height")
        (result, response) = RestfulApi().getblocktxsbyheight(height)
        logger.close(result)
        
    def test_08_get_blk_txs_by_height(self,height=0):
        logger.open("08_get_blk_txs_by_height.log", "08_get_blk_txs_by_height")
        (result, response) = RestfulApi().getblocktxsbyheight(height)
        logger.close(result)
        
    # 无区块
    def test_09_get_blk_txs_by_height(self,height=0):
        self.clear_nodes()
        logger.open("09_get_blk_txs_by_height.log", "09_get_blk_txs_by_height")
        (result, response) = RestfulApi().getblocktxsbyheight(height)
    
    def test_10_get_blk_txs_by_height(self,height=6000):
        logger.open("10_get_blk_txs_by_height.log", "10_get_blk_txs_by_height")
        (result, response) = RestfulApi().getblocktxsbyheight(height)
        logger.close(result)

    def test_11_get_blk_txs_by_height(self,height=65537):
        logger.open("11_get_blk_txs_by_height.log", "11_get_blk_txs_by_height")
        (result, response) = RestfulApi().getblocktxsbyheight(height)
        logger.close(result)
        
    def test_12_get_blk_txs_by_height(self,height="abc"):
        logger.open("12_get_blk_txs_by_height.log", "12_get_blk_txs_by_height")
        (result, response) = RestfulApi().getblocktxsbyheight(height)
        logger.close(result)

    def test_13_get_blk_txs_by_height(self,height=-1):
        logger.open("13_get_blk_txs_by_height.log", "13_get_blk_txs_by_height")
        (result, response) = RestfulApi().getblocktxsbyheight(height)
        logger.close(result)

    def test_14_get_blk_txs_by_height(self,height=""):
        logger.open("14_get_blk_txs_by_height.log", "14_get_blk_txs_by_height")
        (result, response) = RestfulApi().getblocktxsbyheight(height)
        logger.close(result)

    def test_15_get_blk_by_height(self,height=1):
        logger.open("15_get_blk_by_height.log", "15_get_blk_by_height")
        (result, response) = RestfulApi().getblockbyheight(height)
        logger.close(result)

    def test_16_get_blk_by_height(self,height=0):
        logger.open("16_get_blk_by_height.log", "16_get_blk_by_height")
        (result, response) = RestfulApi().getblockbyheight(height)
        logger.close(result)
        
    # 无区块
    def test_17_get_blk_by_height(self,height=0):
        self.clear_nodes()
        logger.open("17_get_blk_by_height.log", "17_get_blk_by_height")
        (result, response) = RestfulApi().getblockbyheight(height)
        logger.close(result)

    def test_18_get_blk_by_height(self,height=6000):
        logger.open("18_get_blk_by_height.log", "18_get_blk_by_height")
        (result, response) = RestfulApi().getblockbyheight(height)
        logger.close(result)

    def test_19_get_blk_by_height(self,height=65536):
        logger.open("19_get_blk_by_height.log", "19_get_blk_by_height")
        (result, response) = RestfulApi().getblockbyheight(height)
        logger.close(result)

    def test_20_get_blk_by_height(self,height="abc"):
        logger.open("20_get_blk_by_height.log", "20_get_blk_by_height")
        (result, response) = RestfulApi().getblockbyheight(height)
        logger.close(result)

    def test_21_get_blk_by_height(self,height=-1):
        logger.open("21_get_blk_by_height.log", "21_get_blk_by_height")
        (result, response) = RestfulApi().getblockbyheight(height)
        logger.close(result)

    def test_22_get_blk_by_height(self,height=""):
        logger.open("22_get_blk_by_height.log", "22_get_blk_by_height")
        (result, response) = RestfulApi().getblockbyheight(height)
        logger.close(result)

    def test_23_get_blk_by_hash(self,_hash="14b1e88110c3c9685cd65e4b2c3a7b1deae47620af2183fa541f82790171ecb4",raw=1):    
        logger.open("23_get_blk_by_hash.log", "23_get_blk_by_hash")
        (result, response) = RestfulApi().getblockbyhash(_hash,raw)    
        logger.close(result)

    def test_24_get_blk_by_hash(self,_hash="3e23cf222a47739d4141255da617cd42925a12638ac19cadcc85501f9079722d",raw=1):    
        logger.open("24_get_blk_by_hash.log", "24_get_blk_by_hash")
        (result, response) = RestfulApi().getblockbyhash(_hash,raw)  
        logger.close(result)

    def test_25_get_blk_height(self):    
        logger.open("25_get_blk_height.log", "25_get_blk_height")
        (result, response) = RestfulApi().getblockheight()    
        logger.close(result)

    # 无区块
    def test_26_get_blk_height(self):
        self.clear_nodes()  
        logger.open("26_get_blk_height.log", "26_get_blk_height")
        (result, response) = RestfulApi().getblockheight()    
        logger.close(result)

    def test_27_get_blk_height(self):
        logger.open("27_get_blk_height.log", "27_get_blk_height")
        task = Task(Config.BASEAPI_PATH + "/restful/get_blk_height.json")
        task.set_type("restful")
        taskrequest = task.request()
        taskrequest["api"] = "/api/v1/block/test"
        task.set_request(taskrequest)
        (result, response) = run_single_task(task)
        logger.close(result)

    def test_28_get_blk_height(self):
        logger.open("28_get_blk_height.log", "28_get_blk_height")
        task = Task(Config.BASEAPI_PATH + "/restful/get_blk_height.json")
        task.set_type("restful")
        taskrequest = task.request()
        taskrequest["api"] = "/api/v1/block/"
        task.set_request(taskrequest)
        (result, response) = run_single_task(task)
        logger.close(result)

    def test_29_get_blk_hash(self,height=1):
        logger.open("29_get_blk_hash.log", "29_get_blk_hash")
        (result, response) = RestfulApi().getblockhashbyheight(height)    
        logger.close(result)

    def test_30_get_blk_hash(self,height=0):
        logger.open("30_get_blk_hash.log", "30_get_blk_hash")
        (result, response) = RestfulApi().getblockhashbyheight(height) 
        logger.close(result)

    # 无区块
    def test_31_get_blk_hash(self,height=0):
        self.clear_nodes()  
        logger.open("31_get_blk_hash.log", "31_get_blk_hash")
        (result, response) = RestfulApi().getblockhashbyheight(height)    
        logger.close(result)

    def test_32_get_blk_hash(self,height=6000):
        logger.open("32_get_blk_hash.log", "32_get_blk_hash")
        (result, response) = RestfulApi().getblockhashbyheight(height)    
        logger.close(result)

    def test_33_get_blk_hash(self,height=65536):
        logger.open("33_get_blk_hash.log", "33_get_blk_hash")
        (result, response) = RestfulApi().getblockhashbyheight(height)    
        logger.close(result)

    def test_34_get_blk_hash(self,height="abc"):
        logger.open("34_get_blk_hash.log", "34_get_blk_hash")
        (result, response) = RestfulApi().getblockhashbyheight(height)    
        logger.close(result)

    def test_35_get_blk_hash(self,height="abc"):
        logger.open("35_get_blk_hash.log", "35_get_blk_hash")
        (result, response) = RestfulApi().getblockhashbyheight(height) 
        logger.close(result)

    def test_36_get_blk_hash(self,height=""):
        logger.open("36_get_blk_hash.log", "36_get_blk_hash")
        (result, response) = RestfulApi().getblockhashbyheight(height)   
        logger.close(result)

    def test_37_get_tx(self,_hash="18f2be1fb70ad2b335cb94729773a181f8f6f828c048ae8ea9fe0337bf63f683"):
        logger.open("37_get_tx.log", "37_get_tx")
        (result, response) = RestfulApi().gettransactionbytxhash(_hash) 
        logger.close(result)
        
    def test_38_get_tx(self,_hash="18f2be1fb70ad2b335cb94729773a181f8f6f828c048ae8ea9fe0337bf63f684"):
        logger.open("38_get_tx.log", "38_get_tx")
        (result, response) = RestfulApi().gettransactionbytxhash(_hash) 
        logger.close(result)    

    def test_39_post_raw_tx(self,rawtxdata="80000001195876cb34364dc38b730077156c6bc3a7fc570044a66fbfeeea56f71327e8ab0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500c65eaf440000000f9a23e06f74cf86b8827a9108ec2e0f89ad956c9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc50092e14b5e00000030aab52ad93f6ce17ca07fa88fc191828c58cb71014140915467ecd359684b2dc358024ca750609591aa731a0b309c7fb3cab5cd0836ad3992aa0a24da431f43b68883ea5651d548feb6bd3c8e16376e6e426f91f84c58232103322f35c7819267e721335948d385fae5be66e7ba8c748ac15467dcca0693692dac", action = "sendrawtransaction", version = "1.0.0"):
        logger.open("39_post_raw_tx.log", "39_post_raw_tx")
        (result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
        logger.close(result)

    def test_40_post_raw_tx(self,rawtxdata="80000001195876cb34364dc38b730077156c6bc3a7fc570044a66fbfeeea56f71327e8ab0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500c65eaf440000000f9a23e06f74cf86b8827a9108ec2e0f89ad956c9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc50092e14b5e00000030aab52ad93f6ce17ca07fa88fc191828c58cb71014140915467ecd359684b2dc358024ca750609591aa731a0b309c7fb3cab5cd0836ad3992aa0a24da431f43b68883ea5651d548feb6bd3c8e16376e6e426f91f84c58232103322f35c7819267e721335948d385fae5be66e7ba8c748ac15467dcca0693692dac", action = "sendrawtransaction", version = "1.0.0"):
        logger.open("40_post_raw_tx.log", "40_post_raw_tx")
        (result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
        logger.close(result)

    def test_41_post_raw_tx(self,rawtxdata="80000001195876cb34364dc38b730077156c6bc3a7fc570044a66fbfeeea56f71327e8ab0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500c65eaf440000000f9a23e06f74cf86b8827a9108ec2e0f89ad956c9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc50092e14b5e00000030aab52ad93f6ce17ca07fa88fc191828c58cb71014140915467ecd359684b2dc358024ca750609591aa731a0b309c7fb3cab5cd0836ad3992aa0a24da431f43b68883ea5651d548feb6bd3c8e16376e6e426f91f84c58232103322f35c7819267e721335948d385fae5be66e7ba8c748ac15467dcca0693692dac", action = "sendrawtransaction", version = "1.0.0"):
        logger.open("41_post_raw_tx.log", "41_post_raw_tx")
        (result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
        logger.close(result)

    def test_42_post_raw_tx(self,rawtxdata="80000001195876cb34364dc38b730077156c6bc3a7fc570044a66fbfeeea56f71327e8ab0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500c65eaf440000000f9a23e06f74cf86b8827a9108ec2e0f89ad956c9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc50092e14b5e00000030aab52ad93f6ce17ca07fa88fc191828c58cb71014140915467ecd359684b2dc358024ca750609591aa731a0b309c7fb3cab5cd0836ad3992aa0a24da431f43b68883ea5651d548feb6bd3c8e16376e6e426f91f84c58232103322f35c7819267e721335948d385fae5be66e7ba8c748ac15467dcca0693692dac", action = "sendrawtransaction", version = "1.0.0"):
        logger.open("42_post_raw_tx.log", "42_post_raw_tx")
        (result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
        logger.close(result)

    def test_43_post_raw_tx(self,rawtxdata="80000001195876cb34364dc38b730077156c6bc3a7fc570044a66fbfeeea56f71327e8ab0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500c65eaf440000000f9a23e06f74cf86b8827a9108ec2e0f89ad956c9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc50092e14b5e00000030aab52ad93f6ce17ca07fa88fc191828c58cb71014140915467ecd359684b2dc358024ca750609591aa731a0b309c7fb3cab5cd0836ad3992aa0a24da431f43b68883ea5651d548feb6bd3c8e16376e6e426f91f84c58232103322f35c7819267e721335948d385fae5be66e7ba8c748ac15467dcca0693692dac", action = "sendrawtransaction", version = "1.0.0"):
        logger.open("43_post_raw_tx.log", "43_post_raw_tx")
        (result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
        logger.close(result)   

    def test_44_post_raw_tx(self,rawtxdata="80000001195876cb34364dc38b730077156c6bc3a7fc570044a66fbfeeea56f71327e8ab0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500c65eaf440000000f9a23e06f74cf86b8827a9108ec2e0f89ad956c9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc50092e14b5e00000030aab52ad93f6ce17ca07fa88fc191828c58cb71014140915467ecd359684b2dc358024ca750609591aa731a0b309c7fb3cab5cd0836ad3992aa0a24da431f43b68883ea5651d548feb6bd3c8e16376e6e426f91f84c58232103322f35c7819267e721335948d385fae5be66e7ba8c748ac15467dcca0693692dac", action = "sendrawtransaction", version = "1.0.0"):
        logger.open("44_post_raw_tx.log", "44_post_raw_tx")
        (result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
        logger.close(result)

    def test_45_post_raw_tx(self,rawtxdata="80000001195876cb34364dc38b730077156c6bc3a7fc570044a66fbfeeea56f71327e8ab0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500c65eaf440000000f9a23e06f74cf86b8827a9108ec2e0f89ad956c9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc50092e14b5e00000030aab52ad93f6ce17ca07fa88fc191828c58cb71014140915467ecd359684b2dc358024ca750609591aa731a0b309c7fb3cab5cd0836ad3992aa0a24da431f43b68883ea5651d548feb6bd3c8e16376e6e426f91f84c58232103322f35c7819267e721335948d385fae5be66e7ba8c748ac15467dcca0693692dac", action = "sendrawtransaction", version = "1.0.0"):
        logger.open("45_post_raw_tx.log", "45_post_raw_tx")
        (result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
        logger.close(result)

    def test_46_post_raw_tx(self,rawtxdata="80000001195876cb34364dc38b730077156c6bc3a7fc570044a66fbfeeea56f71327e8ab0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500c65eaf440000000f9a23e06f74cf86b8827a9108ec2e0f89ad956c9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc50092e14b5e00000030aab52ad93f6ce17ca07fa88fc191828c58cb71014140915467ecd359684b2dc358024ca750609591aa731a0b309c7fb3cab5cd0836ad3992aa0a24da431f43b68883ea5651d548feb6bd3c8e16376e6e426f91f84c58232103322f35c7819267e721335948d385fae5be66e7ba8c748ac15467dcca0693692dac", action = "sendrawtransaction", version = "1.0.0"):
        logger.open("46_post_raw_tx.log", "46_post_raw_tx")
        (result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
        logger.close(result)

    def test_47_post_raw_tx(self,rawtxdata="80000001195876cb34364dc38b730077156c6bc3a7fc570044a66fbfeeea56f71327e8ab0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500c65eaf440000000f9a23e06f74cf86b8827a9108ec2e0f89ad956c9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc50092e14b5e00000030aab52ad93f6ce17ca07fa88fc191828c58cb71014140915467ecd359684b2dc358024ca750609591aa731a0b309c7fb3cab5cd0836ad3992aa0a24da431f43b68883ea5651d548feb6bd3c8e16376e6e426f91f84c58232103322f35c7819267e721335948d385fae5be66e7ba8c748ac15467dcca0693692dac", action = "sendrawtransaction", version = "1.0.0"):
        logger.open("47_post_raw_tx.log", "47_post_raw_tx")
        (result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
        logger.close(result)

    def test_48_post_raw_tx(self,rawtxdata="80000001195876cb34364dc38b730077156c6bc3a7fc570044a66fbfeeea56f71327e8ab0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500c65eaf440000000f9a23e06f74cf86b8827a9108ec2e0f89ad956c9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc50092e14b5e00000030aab52ad93f6ce17ca07fa88fc191828c58cb71014140915467ecd359684b2dc358024ca750609591aa731a0b309c7fb3cab5cd0836ad3992aa0a24da431f43b68883ea5651d548feb6bd3c8e16376e6e426f91f84c58232103322f35c7819267e721335948d385fae5be66e7ba8c748ac15467dcca0693692dac", action = "sendrawtransaction", version = "1.0.0"):
        logger.open("48_post_raw_tx.log", "48_post_raw_tx")
        (result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
        logger.close(result)

    def test_49_post_raw_tx(self,rawtxdata="80000001195876cb34364dc38b730077156c6bc3a7fc570044a66fbfeeea56f71327e8ab0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500c65eaf440000000f9a23e06f74cf86b8827a9108ec2e0f89ad956c9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc50092e14b5e00000030aab52ad93f6ce17ca07fa88fc191828c58cb71014140915467ecd359684b2dc358024ca750609591aa731a0b309c7fb3cab5cd0836ad3992aa0a24da431f43b68883ea5651d548feb6bd3c8e16376e6e426f91f84c58232103322f35c7819267e721335948d385fae5be66e7ba8c748ac15467dcca0693692dac", action = "sendrawtransaction", version = "1.0.0"):
        logger.open("49_post_raw_tx.log", "49_post_raw_tx")
        (result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
        logger.close(result)

    def test_50_post_raw_tx(self,rawtxdata="80000001195876cb34364dc38b730077156c6bc3a7fc570044a66fbfeeea56f71327e8ab0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500c65eaf440000000f9a23e06f74cf86b8827a9108ec2e0f89ad956c9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc50092e14b5e00000030aab52ad93f6ce17ca07fa88fc191828c58cb71014140915467ecd359684b2dc358024ca750609591aa731a0b309c7fb3cab5cd0836ad3992aa0a24da431f43b68883ea5651d548feb6bd3c8e16376e6e426f91f84c58232103322f35c7819267e721335948d385fae5be66e7ba8c748ac15467dcca0693692dac", action = "sendrawtransaction", version = "1.0.0"):
        logger.open("50_post_raw_tx.log", "50_post_raw_tx")
        (result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
        logger.close(result)

    def test_51_post_raw_tx(self,rawtxdata="80000001195876cb34364dc38b730077156c6bc3a7fc570044a66fbfeeea56f71327e8ab0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500c65eaf440000000f9a23e06f74cf86b8827a9108ec2e0f89ad956c9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc50092e14b5e00000030aab52ad93f6ce17ca07fa88fc191828c58cb71014140915467ecd359684b2dc358024ca750609591aa731a0b309c7fb3cab5cd0836ad3992aa0a24da431f43b68883ea5651d548feb6bd3c8e16376e6e426f91f84c58232103322f35c7819267e721335948d385fae5be66e7ba8c748ac15467dcca0693692dac", action = "sendrawtransaction", version = "1.0.0"):
        logger.open("51_post_raw_tx.log", "51_post_raw_tx")
        (result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
        logger.close(result)

    def test_52_post_raw_tx(self,rawtxdata="80000001195876cb34364dc38b730077156c6bc3a7fc570044a66fbfeeea56f71327e8ab0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500c65eaf440000000f9a23e06f74cf86b8827a9108ec2e0f89ad956c9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc50092e14b5e00000030aab52ad93f6ce17ca07fa88fc191828c58cb71014140915467ecd359684b2dc358024ca750609591aa731a0b309c7fb3cab5cd0836ad3992aa0a24da431f43b68883ea5651d548feb6bd3c8e16376e6e426f91f84c58232103322f35c7819267e721335948d385fae5be66e7ba8c748ac15467dcca0693692dac", action = "sendrawtransaction", version = "1.0.0"):
        logger.open("52_post_raw_tx.log", "52_post_raw_tx")
        (result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
        logger.close(result)

    def test_53_post_raw_tx(self,rawtxdata="80000001195876cb34364dc38b730077156c6bc3a7fc570044a66fbfeeea56f71327e8ab0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500c65eaf440000000f9a23e06f74cf86b8827a9108ec2e0f89ad956c9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc50092e14b5e00000030aab52ad93f6ce17ca07fa88fc191828c58cb71014140915467ecd359684b2dc358024ca750609591aa731a0b309c7fb3cab5cd0836ad3992aa0a24da431f43b68883ea5651d548feb6bd3c8e16376e6e426f91f84c58232103322f35c7819267e721335948d385fae5be66e7ba8c748ac15467dcca0693692dac", action = "sendrawtransaction", version = "1.0.0"):
        logger.open("53_post_raw_tx.log", "53_post_raw_tx")
        (result, response) = RestfulApi().postrawtx(rawtxdata,action,version) 
        logger.close(result)

    def test_54_get_storage(self,script_hash="ff00000000000000000000000000000000000001", key="0144587c1094f6929ed7362d6328cffff4fb4da2"):
        logger.open("54_get_storage.log", "54_get_storage")
        (result, response) = RestfulApi().getstorage(script_hash, key) 
        logger.close(result)

    def test_55_get_storage(self,script_hash="ff00000000000000000000000000000000000001", key="0144587c1094f6929ed7362d6328cffff4fb4da2"):
        logger.open("55_get_storage.log", "55_get_storage")
        (result, response) = RestfulApi().getstorage(script_hash, key) 
        logger.close(result)

    def test_56_get_storage(self,script_hash="ff00000000000000000000000000000000000001", key="0144587c1094f6929ed7362d6328cffff4fb4da2"):
        logger.open("56_get_storage.log", "56_get_storage")
        (result, response) = RestfulApi().getstorage(script_hash, key) 
        logger.close(result)

    def test_57_get_storage(self,script_hash="ff00000000000000000000000000000000000001", key="0144587c1094f6929ed7362d6328cffff4fb4da2"):
        logger.open("57_get_storage.log", "57_get_storage")
        (result, response) = RestfulApi().getstorage(script_hash, key) 
        logger.close(result)

    def test_58_get_storage(self,script_hash="ff00000000000000000000000000000000000001", key="0144587c1094f6929ed7362d6328cffff4fb4da2"):
        logger.open("58_get_storage.log", "58_get_storage")
        (result, response) = RestfulApi().getstorage(script_hash, key) 
        logger.close(result)

    def test_59_get_storage(self,script_hash="ff00000000000000000000000000000000000001", key="0144587c1094f6929ed7362d6328cffff4fb4da2"):
        logger.open("59_get_storage.log", "59_get_storage")
        (result, response) = RestfulApi().getstorage(script_hash, key) 
        logger.close(result)

    def test_60_get_storage(self,script_hash="ff00000000000000000000000000000000000001", key="0144587c1094f6929ed7362d6328cffff4fb4da2"):
        logger.open("60_get_storage.log", "60_get_storage")
        (result, response) = RestfulApi().getstorage(script_hash, key) 
        logger.close(result)

    def test_61_get_storage(self,script_hash="ff00000000000000000000000000000000000001", key="0144587c1094f6929ed7362d6328cffff4fb4da2"):
        logger.open("61_get_storage.log", "61_get_storage")
        (result, response) = RestfulApi().getstorage(script_hash, key) 
        logger.close(result)

    def test_62_get_balance(self,attr="TA5uYzLU2vBvvfCMxyV2sdzc9kPqJzGZWq"):
        logger.open("62_get_balance.log", "62_get_balance")
        (result, response) = RestfulApi().getbalance(attr) 
        logger.close(result)

    def test_63_get_balance(self,attr="TA5uYzLU2vBvvfCMxyV2sdzc9kPqJzGZWq"):
        logger.open("63_get_balance.log", "63_get_balance")
        (result, response) = RestfulApi().getbalance(attr) 
        logger.close(result)

    def test_64_get_balance(self,attr="TA5uYzLU2vBvvfCMxyV2sdzc9kPqJzGZWq"):
        logger.open("64_get_balance.log", "64_get_balance")
        (result, response) = RestfulApi().getbalance(attr) 
        logger.close(result)

    def test_65_get_balance(self,attr="TA5uYzLU2vBvvfCMxyV2sdzc9kPqJzGZWq"):
        logger.open("65_get_balance.log", "65_get_balance")
        (result, response) = RestfulApi().getbalance(attr) 
        logger.close(result)

    def test_66_get_balance(self,attr="TA5uYzLU2vBvvfCMxyV2sdzc9kPqJzGZWq"):
        logger.open("66_get_balance.log", "66_get_balance")
        (result, response) = RestfulApi().getbalance(attr) 
        logger.close(result)

    def test_67_get_balance(self,attr="TA5uYzLU2vBvvfCMxyV2sdzc9kPqJzGZWq"):
        logger.open("67_get_balance.log", "67_get_balance")
        (result, response) = RestfulApi().getbalance(attr)
        logger.close(result)
        
    # 无区块
    def test_68_get_contract_state(self,script_hash="fff49c809d302a2956e9dc0012619a452d4b846c"):
        self.clear_nodes()
        logger.open("68_get_contract_state.log", "68_get_contract_state")
        (result, response) = RestfulApi().getcontract(script_hash) 
        logger.close(result)

    def test_69_get_contract_state(self,script_hash="fff49c809d302a2956e9dc0012619a452d4b846c"):
        logger.open("69_get_contract_state.log", "69_get_contract_state")
        (result, response) = RestfulApi().getcontract(script_hash) 
        logger.close(result)

    def test_70_get_contract_state(self,script_hash="fff49c809d302a2956e9dc0012619a452d4b846c"):
        logger.open("70_get_contract_state.log", "70_get_contract_state")
        (result, response) = RestfulApi().getcontract(script_hash) 
        logger.close(result)

    def test_71_get_smtcode_evt_txs(self,height=900):
        logger.open("71_get_smtcode_evt_txs.log", "71_get_smtcode_evt_txs")
        (result, response) = RestfulApi().getsmartcodeeventbyheight(height) 
        logger.close(result)

    def test_72_get_smtcode_evt_txs(self,height=0):
        logger.open("72_get_smtcode_evt_txs.log", "72_get_smtcode_evt_txs")
        (result, response) = RestfulApi().getsmartcodeeventbyheight(height) 
        logger.close(result)

    # 无区块
    def test_73_get_smtcode_evt_txs(self,height=0):
        logger.open("73_get_smtcode_evt_txs.log", "73_get_smtcode_evt_txs")
        (result, response) = RestfulApi().getsmartcodeeventbyheight(height) 
        logger.close(result)

    def test_74_get_smtcode_evt_txs(self,height=999):
        logger.open("74_get_smtcode_evt_txs.log", "74_get_smtcode_evt_txs")
        (result, response) = RestfulApi().getsmartcodeeventbyheight(height) 
        logger.close(result)

    def test_75_get_smtcode_evt_txs(self,height=65537):
        logger.open("75_get_smtcode_evt_txs.log", "75_get_smtcode_evt_txs")
        (result, response) = RestfulApi().getsmartcodeeventbyheight(height) 
        logger.close(result)

    def test_76_get_smtcode_evt_txs(self,height="abc"):
        logger.open("76_get_smtcode_evt_txs.log", "76_get_smtcode_evt_txs")
        (result, response) = RestfulApi().getsmartcodeeventbyheight(height) 
        logger.close(result)

    def test_77_get_smtcode_evt_txs(self,height=-1):
        logger.open("77_get_smtcode_evt_txs.log", "77_get_smtcode_evt_txs")
        (result, response) = RestfulApi().getsmartcodeeventbyheight(height) 
        logger.close(result)

    def test_78_get_smtcode_evt_txs(self,height=""):
        logger.open("78_get_smtcode_evt_txs.log", "78_get_smtcode_evt_txs")
        (result, response) = RestfulApi().getsmartcodeeventbyheight(height) 
        logger.close(result)

    def test_79_get_smtcode_evts(self,hash="b8a4f77e19fcae04faa576fbc71fa5a9775166d4485ce13f1ba5ff30ce264c52"):
        logger.open("79_get_smtcode_evts.log", "79_get_smtcode_evts")
        (result, response) = RestfulApi().getsmartcodeeventbyhash(hash) 
        logger.close(result)

    def test_80_get_smtcode_evts(self,hash="3e23cf222a47739d4141255da617cd42925a12638ac19cadcc85501f907972c8"):
        logger.open("80_get_smtcode_evts.log", "80_get_smtcode_evts")
        (result, response) = RestfulApi().getsmartcodeeventbyhash(hash) 
        logger.close(result)

    def test_81_get_smtcode_evts(self,hash="3e23cf222a47739d4141255da617cd42925a12638ac19cadcc85501f907972c8"):
        logger.open("81_get_smtcode_evts.log", "81_get_smtcode_evts")
        (result, response) = RestfulApi().getsmartcodeeventbyhash(hash) 
        logger.close(result)

    def test_82_get_blk_hgt_by_txhash(self,hash="5263f32ec015f9a4af5d2ab6e0c8a58512d4c263d67fad82bee5f25922aaf1d1"):
        logger.open("82_get_blk_hgt_by_txhash.log", "82_get_blk_hgt_by_txhash")
        (result, response) = RestfulApi().getblockheightbytxhash(hash)
        logger.close(result)
        
    def test_83_get_blk_hgt_by_txhash(self,hash="3e23cf222a47739d4141255da617cd42925a12638ac19cadcc85501f907972c8"):
        logger.open("83_get_blk_hgt_by_txhash.log", "83_get_blk_hgt_by_txhash")
        (result, response) = RestfulApi().getblockheightbytxhash(hash)
        logger.close(result)

    def test_84_get_blk_hgt_by_txhash(self,hash="3e23cf222a47739d4141255da617cd42925a12638ac19cadcc85501f907972c8"):
        logger.open("84_get_blk_hgt_by_txhash.log", "84_get_blk_hgt_by_txhash")
        (result, response) = RestfulApi().getblockheightbytxhash(hash) 
        logger.close(result)

    def test_85_get_merkle_proof(self,hash="3e23cf222a47739d4141255da617cd42925a12638ac19cadcc85501f907972c8"):
        logger.open("85_get_merkle_proof.log", "85_get_merkle_proof")
        (result, response) = RestfulApi().getmerkleproofbytxhash(hash) 
        logger.close(result)

    def test_86_get_merkle_proof(self,hash="3e23cf222a47739d4141255da617cd42925a12638ac19cadcc85501f907972c1"):
        logger.open("86_get_merkle_proof.log", "86_get_merkle_proof")
        (result, response) = RestfulApi().getmerkleproofbytxhash(hash) 
        logger.close(result)

    def test_87_get_merkle_proof(self,hash=""):
        logger.open("87_get_merkle_proof.log", "87_get_merkle_proof")
        (result, response) = RestfulApi().getmerkleproofbytxhash(hash) 
        logger.close(result)

    def test_88_get_merkle_proof(self,hash="10"):
        logger.open("88_get_merkle_proof.log", "88_get_merkle_proof")
        (result, response) = RestfulApi().getmerkleproofbytxhash(hash) 
        logger.close(result)
        
####################################################
if __name__ == '__main__':
    unittest.main()  
