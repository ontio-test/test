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
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.rpcapi import RPCApi
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.init_ong_ont import *
from utils.commonapi import *

from test_api import *
rpcapiTest=RPCApi()
logger = LoggerInstance
node_index=5
nodePath="/home/ubuntu/ontology/node"
contract_address=deploy_contract("ong_neo.json")
pay_address=Config.NODES[node_index]["address"]
get_address=Config.NODES[2]["address"]
amount="10"
sender=Config.NODES[2]["address"]
sender_node=2
senderType=False

##############################
from1= pay_address  #from_正确的from值_正常
from2= "1111111111111111111111111111"  #from_错误的from值（参数不正确）_异常
from3= ""  #from_留空_异常
to1= get_address  #to_正确的to值_正常
to2= from2  #to_错误的to值_异常
to3= ""  #to_留空_异常
amount1= "10"  #amount_正确的数量10_正常
amount2= "0"  #amount_正确的数量0_正常
amount3= "-1"  #amount_错误的数量（-1）_异常
amount4= "2000000000000"  #amount_错误的数量（from账户不存在这么多数量的ont）_异常
amount5= "abc"  #amount_错误的数量（abc）_异常
amount6= ""  #amount_错误的数量（留空）_异常
from4= from2  #from_错误的from值_异常
sender1= to1 #sender_正确的sender值（被授权的账户地址)_正常
sender1_node=2
sender1Type=senderType
sender2= contract_address  #sender_正确的sender值（被授权的智能合约地址)_正常
sender2_node=2
sender2Type=True
sender3= from1  #sender_正确的sender值（from账户地址)_正常
sender3_node=2
sender3Type=False
sender4= "ANdtbPPwfMv79eMev9z7aAZRM6bUuQQ3rf"  #sender_错误的sender值（未被授权的账户地址)_异常
sender4_node=2
sender4Type=False
sender5= deploy_contract("ongErr.json")  #sender_错误的sender值（未被授权的智能合约地址)_异常
sender5_node=2
sender5Type=True
sender6= "abc"  #sender_错误的sender值（abc）_异常
sender6Type=False
sender6_node=2
sender7= ""  #sender_留空_异常
sender7_node=2
sender7Type=False
from5= from1  #from_正确的from值（账户存在）_正常
from6= "ASK6GGsZfPf8WfSYhWUhw7SaZxnZ111111"  #from_错误的from值（账户不存在）_异常
to4= to1  #to_正确的to值（账户存在）_正常
to5= from6  #to_错误的to值（账户不存在）_异常
amount7= "10"  #amount_正确的数量10_异常
address1= from1  #address_正确的address值_正常
address2= from2  #address_错误的address值_异常
address3= ""  #address_留空_异常
from7= from1  #from_正确的from值_异常
sender8= to1  #sender_正确的sender值（被授权的账户地址)_异常
sender8_node=5
sender8Type=False
address4= from1  #address_正确的address值_异常





####################################################
#test cases
class TestContract(ParametrizedTestCase):
	@classmethod
	def setUpClass(self):
		stop_all_nodes()
		start_nodes(range(0, 7), Config.DEFAULT_NODE_ARGS, clear_chain = True, clear_log = True)
		time.sleep(10)
		init_ont_ong()
		time.sleep(10)
		global contract_address
		contract_address=deploy_contract("ont_neo.json")
		global sender5
		sender5= deploy_contract("ontErr.json") 
		#os.system(nodePath+ "/ontology account import -s wallettest.dat -w "+nodePath+"/wallet.dat")
		#deploy_contract
	def test_001_transfer(self):
		logger.open( "1_transfer.log","1_transfer")
		(result, response) = transfer(contract_address,from1,get_address,amount, node_index,0)
		logger.close(result)
		
	def test_002_transfer(self):
		logger.open( "2_transfer.log","2_transfer")
		(result, response) = transfer(contract_address,from2,get_address,amount, node_index)
		logger.close(result)


	def test_003_transfer(self):
		logger.open( "3_transfer.log","3_transfer")
		(result, response) = transfer(contract_address,from3,get_address,amount, node_index)
		logger.close(result)


	def test_004_transfer(self):
		logger.open( "4_transfer.log","4_transfer")
		(result, response) = transfer(contract_address,pay_address,to1,amount, node_index,0)
		logger.close(result)


	def test_005_transfer(self):
		logger.open( "5_transfer.log","5_transfer")
		(result, response) = transfer(contract_address,pay_address,to2,amount, node_index,0)
		logger.close(result)


	def test_006_transfer(self):
		logger.open( "6_transfer.log","6_transfer")
		(result, response) = transfer(contract_address,pay_address,to3,amount, node_index)
		logger.close(result)


	def test_007_transfer(self):
		logger.open( "7_transfer.log","7_transfer")
		(result, response) = transfer(contract_address,pay_address,get_address,amount1, node_index,0)
		logger.close(result)


	def test_008_transfer(self):
		logger.open( "8_transfer.log","8_transfer")
		(result, response) = transfer(contract_address,pay_address,get_address,amount2, node_index,0)
		logger.close(result)


	def test_009_transfer(self):
		logger.open( "9_transfer.log","9_transfer")
		(result, response) = transfer(contract_address,pay_address,get_address,amount3, node_index)
		logger.close(result)


	def test_010_transfer(self):
		logger.open( "10_transfer.log","10_transfer")
		(result, response) = transfer(contract_address,pay_address,get_address,amount4, node_index)
		logger.close(result)


	def test_013_approve(self):
		logger.open( "13_approve.log","13_approve")
		(result, response) = approve(contract_address,from1,get_address, amount,node_index,0)
		logger.close(result)

	def test_014_approve(self):
		logger.open( "14_approve.log","14_approve")
		(result, response) = approve(contract_address,from4,get_address, amount,node_index)
		logger.close(result)


	def test_015_approve(self):
		logger.open( "15_approve.log","15_approve")
		(result, response) = approve(contract_address,pay_address,to1, amount,node_index,0)
		logger.close(result)


	def test_016_approve(self):
		logger.open( "16_approve.log","16_approve")
		(result, response) = approve(contract_address,pay_address,to2, amount,node_index,0)
		logger.close(result)


	def test_017_approve(self):
		logger.open( "17_approve.log","17_approve")
		(result, response) = approve(contract_address,pay_address,get_address, amount1,node_index,0)
		logger.close(result)


	def test_018_approve(self):
		logger.open( "18_approve.log","18_approve")
		(result, response) = approve(contract_address,pay_address,get_address, amount2,node_index,0)
		logger.close(result)


	def test_019_approve(self):
		logger.open( "19_approve.log","19_approve")
		(result, response) = approve(contract_address,pay_address,get_address, amount4,node_index)
		logger.close(result)


	def test_020_approve(self):
		logger.open( "20_approve.log","20_approve")
		(result, response) = approve(contract_address,pay_address,get_address, amount3,node_index)
		logger.close(result)


	def test_023_transferFrom(self):
		logger.open( "23_transferFrom.log","23_transferFrom")
		(result, response) = approve1(contract_address,pay_address,get_address, amount,node_index,0)#先approve
		(result, response) = transferFrom(contract_address,sender1,pay_address,get_address, amount,sender1_node,sender1Type,0)
		logger.close(result)
	def test_024_transferFrom(self):
		logger.open( "24_transferFrom.log","24_transferFrom")
		(result, response) = approve1(contract_address,pay_address,get_address, amount,node_index,0)#先approve
		(result, response) = transferFrom(contract_address,sender2,pay_address,get_address, amount,sender2_node,sender2Type,0)
		logger.close(result)


	def test_025_transferFrom(self):
		logger.open( "25_transferFrom.log","25_transferFrom")
		(result, response) = approve1(contract_address,pay_address,get_address, amount,node_index,0)#先approve
		(result, response) = transferFrom(contract_address,sender3,pay_address,get_address, amount,sender3_node,sender3Type,0)
		logger.close(result)


	def test_026_transferFrom(self):
		logger.open( "26_transferFrom.log","26_transferFrom")
		(result, response) = transferFrom(contract_address,sender4,pay_address,get_address, amount,sender4_node,sender4Type)
		logger.close(result)


	def test_027_transferFrom(self):
		logger.open( "27_transferFrom.log","27_transferFrom")
		(result, response) = transferFrom(contract_address,sender5,pay_address,get_address, amount,sender5_node,sender5Type)
		logger.close(result)


	def test_028_transferFrom(self):
		logger.open( "28_transferFrom.log","28_transferFrom")
		(result, response) = transferFrom(contract_address,sender6,pay_address,get_address, amount,sender6_node,sender6Type)
		logger.close(result)


	def test_029_transferFrom(self):
		logger.open( "29_transferFrom.log","29_transferFrom")
		(result, response) = transferFrom(contract_address,sender7,pay_address,get_address, amount,sender7_node,sender7Type)
		logger.close(result)


	def test_030_transferFrom(self):
		logger.open( "30_transferFrom.log","30_transferFrom")
		(result, response) = approve1(contract_address,from5,get_address, amount,node_index,0)#先approve
		(result, response) = transferFrom(contract_address,sender,from5,get_address, amount,sender_node,senderType,0)
		logger.close(result)


	def test_031_transferFrom(self):
		logger.open( "31_transferFrom.log","31_transferFrom")
		(result, response) = transferFrom(contract_address,sender,from6,get_address, amount,sender_node,senderType)
		logger.close(result)


	def test_032_transferFrom(self):
		logger.open( "32_transferFrom.log","32_transferFrom")
		#(result, response) = approve1(contract_address,from3,get_address, amount,node_index,0)#先approve
		(result, response) = transferFrom(contract_address,sender,from3,get_address, amount,sender_node,senderType)
		logger.close(result)


	def test_033_transferFrom(self):
		logger.open( "33_transferFrom.log","33_transferFrom")
		(result, response) = approve1(contract_address,pay_address,to4, amount,node_index,0)#先approve
		(result, response) = transferFrom(contract_address,sender,pay_address,to4, amount,sender_node,senderType,0)
		logger.close(result)


	def test_034_transferFrom(self):
		logger.open( "34_transferFrom.log","34_transferFrom")
		(result, response) = transferFrom(contract_address,sender,pay_address,to5, amount,sender_node,senderType)
		logger.close(result)


	def test_035_transferFrom(self):
		logger.open( "35_transferFrom.log","35_transferFrom")
		(result, response) = transferFrom(contract_address,sender,pay_address,to3, amount,sender_node,senderType)
		logger.close(result)


	def test_036_transferFrom(self):
		logger.open( "36_transferFrom.log","36_transferFrom")
		(result, response) = approve1(contract_address,pay_address,get_address, amount,node_index,0)
		(result, response) = transferFrom(contract_address,sender,pay_address,get_address, amount1,sender_node,senderType,0)
		logger.close(result)


	def test_037_transferFrom(self):
		logger.open( "37_transferFrom.log","37_transferFrom")
		(result, response) = approve1(contract_address,pay_address,get_address, amount,node_index,0)
		(result, response) = transferFrom(contract_address,sender,pay_address,get_address, amount2,sender_node,senderType,0)
		logger.close(result)


	def test_038_transferFrom(self):
		logger.open( "38_transferFrom.log","38_transferFrom")
		(result, response) = transferFrom(contract_address,sender,pay_address,get_address, amount4,sender_node,senderType)
		logger.close(result)


	def test_039_transferFrom(self):
		logger.open( "39_transferFrom.log","39_transferFrom")
		(result, response) = approve1(contract_address,pay_address,get_address, "0",node_index,0)
		(result, response) = transferFrom(contract_address,sender,pay_address,get_address, amount7,sender_node,senderType)
		logger.close(result)


	def test_040_transferFrom(self):
		logger.open( "40_transferFrom.log","40_transferFrom")
		(result, response) = transferFrom(contract_address,sender,pay_address,get_address, amount3,sender_node,senderType)
		logger.close(result)


	def test_043_name(self):
		logger.open( "043_name.log","043_name")
		(result, response) = name(contract_address,node_index,0)
		logger.close(result)


	def test_044_symbol(self):
		logger.open( "44_symbol.log","44_symbol")
		(result, response) = symbol(contract_address,node_index,0)
		logger.close(result)


	def test_045_decimals(self):
		logger.open( "45_decimals.log","45_decimals")
		(result, response) = decimals(contract_address,node_index,0)
		logger.close(result)


	def test_046_totalSupply(self):
		logger.open( "46_totalSupply.log","46_totalSupply")
		(result, response) = totalSupply(contract_address,node_index,0)
		logger.close(result)


	def test_047_balanceOf(self):
		logger.open( "47_balanceOf.log","47_balanceOf")
		(result, response) = balanceOf(contract_address,address1,node_index,errorcode=0)
		logger.close(result)


	def test_048_balanceOf(self):
		logger.open( "48_balanceOf.log","48_balanceOf")
		(result, response) = balanceOf(contract_address,address2,node_index,errorcode=0)
		logger.close(result)


	def test_049_balanceOf(self):
		logger.open( "49_balanceOf.log","49_balanceOf")
		(result, response) = balanceOf(contract_address,address3,node_index)
		logger.close(result)


	def test_050_allowance(self):
		logger.open( "50_allowance.log","50_allowance")
		(result, response) = approve1(contract_address,from1,get_address, amount,node_index,0)#先approve
		(result, response) = allowance(contract_address,from1,get_address,node_index,0)
		logger.close(result)


	def test_051_allowance(self):
		logger.open( "51_allowance.log","51_allowance")
		(result, response) = allowance(contract_address,from4,get_address,node_index,errorcode=0)
		logger.close(result)


	def test_052_allowance(self):
		logger.open( "52_allowance.log","52_allowance")
		(result, response) = allowance(contract_address,from3,get_address,node_index)
		logger.close(result)


	def test_053_allowance(self):
		logger.open( "53_allowance.log","53_allowance")
		(result, response) = approve1(contract_address,pay_address,to1, amount,node_index,0)#先approve
		(result, response) = allowance(contract_address,pay_address,to1,node_index,0)
		logger.close(result)


	def test_054_allowance(self):
		logger.open( "54_allowance.log","54_allowance")
		(result, response) =allowance(contract_address,pay_address,to2,node_index,errorcode=0)
		logger.close(result)


	def test_055_allowance(self):
		logger.open( "55_allowance.log","55_allowance")
		(result, response) = allowance(contract_address,pay_address,to3,node_index)
		logger.close(result)


	def test_056_transfer(self):
		logger.open( "56_transfer.log","56_transfer")
		(result, response) = transfer1(contract_address,from1,get_address,amount, node_index,0)
		logger.close(result)


	def test_057_transfer(self):
		logger.open( "57_transfer.log","57_transfer")
		(result, response) = transfer1(contract_address,from2,get_address,amount, node_index,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_058_transfer(self):
		logger.open( "58_transfer.log","58_transfer")
		(result, response) = transfer1(contract_address,from3,get_address,amount, node_index,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_059_transfer(self):
		logger.open( "59_transfer.log","59_transfer")
		(result, response) = transfer1(contract_address,pay_address,to1,amount, node_index,0)
		logger.close(result)


	def test_060_transfer(self):
		logger.open( "60_transfer.log","60_transfer")
		(result, response) = transfer1(contract_address,pay_address,to2,amount, node_index,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_061_transfer(self):
		logger.open( "61_transfer.log","61_transfer")
		(result, response) = transfer1(contract_address,pay_address,to3,amount, node_index,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_062_transfer(self):
		logger.open( "62_transfer.log","62_transfer")
		(result, response) = transfer1(contract_address,pay_address,get_address,amount1, node_index,0)
		logger.close(result)


	def test_063_transfer(self):
		logger.open( "63_transfer.log","63_transfer")
		(result, response) = transfer1(contract_address,pay_address,get_address,amount2, node_index,0)
		logger.close(result)


	def test_064_transfer(self):
		logger.open( "64_transfer.log","64_transfer")
		(result, response) = transfer1(contract_address,pay_address,get_address,amount3, node_index)
		logger.close(result)


	def test_065_transfer(self):
		logger.open( "65_transfer.log","65_transfer")
		(result, response) = transfer1(contract_address,pay_address,get_address,amount4, node_index)
		logger.close(result)


	def test_066_transfer(self):
		logger.open( "66_transfer.log","66_transfer")
		(result, response) = transfer1(contract_address,pay_address,get_address,amount5, node_index,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_067_transfer(self):
		logger.open( "67_transfer.log","67_transfer")
		(result, response) = transfer1(contract_address,pay_address,get_address,amount6, node_index,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_068_approve(self):
		logger.open( "68_approve.log","68_approve")
		(result, response) = approve1(contract_address,from1,get_address, amount,node_index,0)
		logger.close(result)


	def test_069_approve(self):
		logger.open( "69_approve.log","69_approve")
		(result, response) = approve1(contract_address,from4,get_address, amount,node_index,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_070_approve(self):
		logger.open( "70_approve.log","70_approve")
		(result, response) = approve1(contract_address,pay_address,to1, amount,node_index,0)
		logger.close(result)


	def test_071_approve(self):
		logger.open( "71_approve.log","71_approve")
		(result, response) = approve1(contract_address,pay_address,to2, amount,node_index,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_072_approve(self):
		logger.open( "72_approve.log","72_approve")
		(result, response) = approve1(contract_address,pay_address,get_address, amount1,node_index,0)
		logger.close(result)


	def test_073_approve(self):
		logger.open( "73_approve.log","73_approve")
		(result, response) = approve1(contract_address,pay_address,get_address, amount2,node_index,0)
		logger.close(result)


	def test_074_approve(self):
		logger.open( "74_approve.log","74_approve")
		(result, response) = approve1(contract_address,pay_address,get_address, amount4,node_index)
		logger.close(result)


	def test_075_approve(self):
		logger.open( "75_approve.log","75_approve")
		(result, response) = approve1(contract_address,pay_address,get_address, amount3,node_index)
		logger.close(result)


	def test_076_approve(self):
		logger.open( "76_approve.log","76_approve")
		(result, response) = approve1(contract_address,pay_address,get_address, amount5,node_index,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_077_approve(self):
		logger.open( "77_approve.log","77_approve")
		(result, response) = approve1(contract_address,pay_address,get_address, amount6,node_index,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_078_transferFrom(self):
		logger.open( "78_transferFrom.log","78_transferFrom")
		(result, response) = approve1(contract_address,pay_address,get_address, amount,node_index,0)
		(result, response) = transferFrom1(contract_address,sender1,pay_address,get_address, amount,sender1_node,sender1Type,0)
		logger.close(result)


	def test_079_transferFrom(self):
		logger.open( "79_transferFrom.log","79_transferFrom")
		(result, response) = approve1(contract_address,pay_address,get_address, amount,node_index,0)

		(result, response) = transferFrom1(contract_address,sender2,pay_address,get_address, amount,sender2_node,sender2Type,0)
		logger.close(result)


	def test_080_transferFrom(self):
		logger.open( "80_transferFrom.log","80_transferFrom")
		(result, response) = approve1(contract_address,pay_address,get_address, amount,node_index,0)

		(result, response) = transferFrom1(contract_address,sender3,pay_address,get_address, amount,sender3_node,sender3Type)
		logger.close(result)


	def test_081_transferFrom(self):
		logger.open( "81_transferFrom.log","81_transferFrom")
		(result, response) = transferFrom1(contract_address,sender4,pay_address,get_address, amount,sender4_node,sender4Type)
		logger.close(result)


	def test_082_transferFrom(self):
		logger.open( "82_transferFrom.log","82_transferFrom")
		(result, response) = transferFrom1(contract_address,sender5,pay_address,get_address, amount,sender5_node,sender5Type)
		logger.close(result)


	def test_083_transferFrom(self):
		logger.open( "83_transferFrom.log","83_transferFrom")
		(result, response) = transferFrom1(contract_address,sender6,pay_address,get_address, amount,sender6_node,sender6Type,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_084_transferFrom(self):
		logger.open( "84_transferFrom.log","84_transferFrom")
		(result, response) = transferFrom1(contract_address,sender7,pay_address,get_address, amount,sender7_node,sender7Type,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_085_transferFrom(self):
		logger.open( "85_transferFrom.log","85_transferFrom")
		(result, response) = approve1(contract_address,from5,get_address, amount,node_index,0)

		(result, response) = transferFrom1(contract_address,sender,from5,get_address, amount,sender_node,senderType,0)
		logger.close(result)


	def test_086_transferFrom(self):
		logger.open( "86_transferFrom.log","86_transferFrom")
		(result, response) = transferFrom1(contract_address,sender,from6,get_address, amount,sender_node,senderType,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_087_transferFrom(self):
		logger.open( "87_transferFrom.log","87_transferFrom")
		(result, response) = transferFrom1(contract_address,sender,from3,get_address, amount,sender_node,senderType,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_088_transferFrom(self):
		logger.open( "88_transferFrom.log","88_transferFrom")
		(result, response) = approve1(contract_address,pay_address,to4, amount,node_index,0)

		(result, response) = transferFrom1(contract_address,sender,pay_address,to4, amount,sender_node,senderType,0)
		logger.close(result)


	def test_089_transferFrom(self):
		logger.open( "89_transferFrom.log","89_transferFrom")
		(result, response) = transferFrom1(contract_address,sender,pay_address,to5, amount,sender_node,senderType,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_090_transferFrom(self):
		logger.open( "90_transferFrom.log","90_transferFrom")
		(result, response) = transferFrom1(contract_address,sender,pay_address,to3, amount,sender_node,senderType,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_091_transferFrom(self):
		logger.open( "91_transferFrom.log","91_transferFrom")

		(result, response) = approve1(contract_address,pay_address,get_address, amount1,node_index,0)
		(result, response) = transferFrom1(contract_address,sender,pay_address,get_address, amount1,sender_node,senderType,0)
		logger.close(result)


	def test_092_transferFrom(self):
		logger.open( "92_transferFrom.log","92_transferFrom")
		(result, response) = approve1(contract_address,pay_address,get_address, amount2,node_index,0)

		(result, response) = transferFrom1(contract_address,sender,pay_address,get_address, amount2,sender_node,senderType,0)
		logger.close(result)


	def test_093_transferFrom(self):
		logger.open( "93_transferFrom.log","93_transferFrom")
		(result, response) = transferFrom1(contract_address,sender,pay_address,get_address, amount4,node_index,senderType)
		logger.close(result)


	def test_094_transferFrom(self):
		logger.open( "94_transferFrom.log","94_transferFrom")
		(result, response) = approve1(contract_address,pay_address,get_address, "0",node_index,0)
		(result, response) = transferFrom1(contract_address,sender,pay_address,get_address, amount7,sender_node,senderType)
		logger.close(result)


	def test_095_transferFrom(self):
		logger.open( "95_transferFrom.log","95_transferFrom")
		(result, response) = transferFrom1(contract_address,sender,pay_address,get_address, amount3,sender_node,senderType)
		logger.close(result)


	def test_096_transferFrom(self):
		logger.open( "96_transferFrom.log","96_transferFrom")
		(result, response) = transferFrom1(contract_address,sender,pay_address,get_address, amount5,sender_node,senderType,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_097_transferFrom(self):
		logger.open( "97_transferFrom.log","97_transferFrom")
		(result, response) = transferFrom1(contract_address,sender,pay_address,get_address, amount6,sender_node,senderType,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_098_name(self):
		logger.open( "98_name.log","98_name")
		(result, response) = name1(contract_address,node_index,0)
		logger.close(result)


	def test_099_symbol(self):
		logger.open( "99_symbol.log","99_symbol")
		(result, response) = symbol1(contract_address,node_index,0)
		logger.close(result)


	def test_100_decimals(self):
		logger.open( "100_decimals.log","100_decimals")
		(result, response) = decimals1(contract_address,node_index,0)
		logger.close(result)


	def test_101_totalSupply(self):
		logger.open( "101_totalSupply.log","101_totalSupply")
		(result, response) = totalSupply1(contract_address,node_index,0)
		logger.close(result)


	def test_102_balanceOf(self):
		logger.open( "102_balanceOf.log","102_balanceOf")
		(result, response) = balanceOf1(contract_address,address1,node_index,errorcode=0)
		logger.close(result)


	def test_103_balanceOf(self):
		logger.open( "103_balanceOf.log","103_balanceOf")
		(result, response) = balanceOf1(contract_address,address2,node_index,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_104_balanceOf(self):
		logger.open( "104_balanceOf.log","104_balanceOf")
		(result, response) = balanceOf1(contract_address,address3,node_index,errorcode=900,errorkey="error_code")
		logger.close(result)

######################################
	def test_105_allowance(self):
		logger.open( "105_allowance.log","105_allowance")
		(result, response) = approve1(contract_address,from1,get_address, amount,node_index,0)

		(result, response) = allowance1(contract_address,from1,get_address,node_index,0)
		logger.close(result)


	def test_106_allowance(self):
		logger.open( "106_allowance.log","106_allowance")
		(result, response) = allowance1(contract_address,from4,get_address,node_index,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_107_allowance(self):
		logger.open( "107_allowance.log","107_allowance")
		(result, response) = allowance1(contract_address,from3,get_address,node_index,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_108_allowance(self):
		logger.open( "108_allowance.log","108_allowance")
		(result, response) = approve1(contract_address,pay_address,to1, amount,node_index,0)

		(result, response) = allowance1(contract_address,pay_address,to1,node_index,0)
		logger.close(result)


	def test_109_allowance(self):
		logger.open( "109_allowance.log","109_allowance")
		(result, response) = allowance1(contract_address,pay_address,to2,node_index,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_110_allowance(self):
		logger.open( "110_allowance.log","110_allowance")
		(result, response) = allowance1(contract_address,pay_address,to3,node_index,errorcode=900,errorkey="error_code")
		logger.close(result)


	def test_111_transfer(self):
		logger.open( "111_transfer.log","111_transfer")
		(result, response) = transfer1(contract_address,from7,get_address,amount, 0)
		logger.close(result)


	def test_112_approve(self):
		logger.open( "112_approve.log","112_approve")
		(result, response) = approve1(contract_address,from7,get_address, amount,0)
		logger.close(result)


	def test_113_transferFrom(self):
		logger.open( "113_transferFrom.log","113_transferFrom")
		(result, response) = transferFrom1(contract_address,sender8,pay_address,get_address, amount,0,sender8Type)
		logger.close(result)


	def test_114_balanceOf(self):
		logger.open( "114_balanceOf.log","114_balanceOf")
		(result, response) = balanceOf1(contract_address,address4,0,errorcode=0)
		logger.close(result)


	def test_115_allowance(self):
		logger.open( "115_allowance.log","115_allowance")
		(result, response) = allowance1(contract_address,pay_address,get_address,0,errorcode=0)
		logger.close(result)
		

####################################################
if __name__ == '__main__':
	unittest.main()

