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


from utils.config import Config
#from utils.taskdata import TaskData, Task
#from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
#from utils.api.rpcapi import RPCApi
#from utils.parametrizedtestcase import ParametrizedTestCase
#from utils.api.init_ong_ont import *
#from utils.api.commonapi import *
from api.apimanager import API	
#from test_ont_native.test_api import *

class test_config():
	try:
		node_index=API.node().get_current_node()
		#node_index=5
		nodePath=Config.NODE_PATH
		contract_address=""
		pay_address=Config.NODES[node_index]["address"]
		get_address=Config.NODES[2]["address"]
		amount="10"
		sender=Config.NODES[2]["address"]
		sender_node=2
		senderType=False
		test_path=os.path.dirname(os.path.realpath(__file__))
		neo1filename= test_path+"/resource/ong_neo.json"
		neo2filename= test_path+"/resource/ongErr.json"
		from1= pay_address  #from_正确的from值_正常
		from2= "1111111111111111111111111111"  #from_错误的from值（参数不正确）_异常
		from3= ""  #from_留空_异常
		to1= get_address  #to_正确的to值_正常
		to2= from2  #to_错误的to值_异常
		to3= ""  #to_留空_异常
		

			
		amount1= "10"  #amount_正确的数�?0_正常
		amount2= "0"  #amount_正确的数�?_正常
		amount3= "-1"  #amount_错误的数量（-1）_异常
		amount4= "20000000000000000"  #amount_错误的数量（from账户不存在这么多数量的ont）_异常
		amount5= "abc"  #amount_错误的数量（abc）_异常
		amount6= ""  #amount_错误的数量（留空）_异常
		from4= from2  #from_错误的from值_异常
		sender1= to1 #sender_正确的sender值（被授权的账户地址)_正常
		sender1_node=2
		sender1Type=senderType
		sender2= ""  #sender_正确的sender值（被授权的智能合约地址)_正常
		sender2_node=2
		sender2Type=True
		sender3= from1  #sender_正确的sender值（from账户地址)_正常
		sender3_node=2
		sender3Type=False
		sender4= "ANdtbPPwfMv79eMev9z7aAZRM6bUuQQ3rf"  #sender_错误的sender值（未被授权的账户地址)_异常
		sender4_node=2
		sender4Type=False
		sender5= ""  #sender_错误的sender值（未被授权的智能合约地址)_异常
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
		amount7= "10"  #amount_正确的数�?0_异常
		address1= from1  #address_正确的address值_正常
		address2= from2  #address_错误的address值_异常
		address3= ""  #address_留空_异常
		from7= from1  #from_正确的from值_异常
		sender8= to1  #sender_正确的sender值（被授权的账户地址)_异常
		sender8_node=5
		sender8Type=False
		address4= from1  #address_正确的address值_异常
	except Exception as e:
		print(e)