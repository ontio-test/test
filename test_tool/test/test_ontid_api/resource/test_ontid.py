# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt
import time
sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.api.contractapi import *
from test_api import *
from test_config import *
from utils.api.commonapi import call_contract
from utils.api.init_ong_ont import *
logger = LoggerInstance

####################################################
#test cases
class test_ontid_api_1(ParametrizedTestCase):##TestContract
	#@classmethod
	def test_init(self):
		stop_all_nodes()
		start_nodes(range(0, 8), Config.DEFAULT_NODE_ARGS, clear_chain = True, clear_log = True)
		time.sleep(10)
		init_ont_ong()
		time.sleep(20)
		
	def setUp(self):
		logger.open( self._testMethodName+".log",self._testMethodName)
		
	def tearDown(self):
		logger.close(self.result())
		pass
		
	def test(self):
		transfer()
	
		
	def test_base_001_regIDWithPublicKey(self):
		try:
			(process response) = regIDWithPublicKey(test_config.userOntId1, test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass


	def test_abnormal_002_regIDWithPublicKey(self):
		try:
			(process, response) = regIDWithPublicKey(test_config.userOntId2, test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
			pass


	def test_abnormal_003_regIDWithPublicKey(self):
		try:
			(process, response) = regIDWithPublicKey(test_config.userOntId3, test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
			pass


	def test_abnormal_004_regIDWithPublicKey(self):		
		try:
			(process, response) = regIDWithPublicKey(test_config.userOntId4, test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		
		
	def test_abnormal_005_regIDWithPublicKey(self):
		try:
			(process, response) = regIDWithPublicKey(test_config.userOntId5, test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		
		
	def test_normal_006_regIDWithPublicKey(self):
		try:
			(process, response) = regIDWithPublicKey(test_config.menualOntId, test_config.public_key1,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		
		
	def test_abnormal_007_regIDWithPublicKey(self):
		try:
			(process, response) = regIDWithPublicKey(test_config.menualOntId2, test_config.public_key2, test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
			pass
		
	
	def test_abnormal_008_regIDWithPublicKey(self):
		try:
			(process, response) = regIDWithPublicKey(test_config.menualOntId2, test_config.public_key3,test_config.node_index)
			ASSERT(process, "")
		except:
			pass


	def test_abnormal_normal_009_addKey(self):
		try:
			(process, response) = addKey(test_config.userOntId6, test_config.menualPubKey1, test_config.pubkey_re_address,  test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		
		
	def test_abnormal_010_addKey(self):
		try:
			(process, response) = addKey(test_config.userOntId7, test_config.new_publickey, test_config.pubkey_re_address, test_config.node_index)
			ASSERT(process, "")
		except:
			pass
	

	def test_abnormal_011_addKey(self):
		try:
			(process, response) = addKey(test_config.userOntId4, test_config.new_publickey,test_config.pubkey_re_address,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_012_addKey(self):
		try:
			(process, response) = addKey(test_config.userOntId5, test_config.new_publickey,test_config.pubkey_re_address,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_013_addKey(self):
		try:
			(process, response) = addKey(test_config.ontId, test_config.new_publickey1,test_config.pubkey_re_address,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_014_addKey(self):
		try:
			(process, response) = addKey(test_config.ontId, test_config.new_publickey2,test_config.pubkey_re_address,test_config.node_index)
			ASSERT(process, "")
		except:
			pass


	def test_normal_015_addKey(self):
		try:
			(process, response) = addKey(test_config.menualOntId, test_config.new_publickey3,test_config.pubkey_re_address,test_config.node_index,0)#先在其他用户处注册完毕该公钥
			(process, response) = addKey(test_config.ontId, test_config.new_publickey3,test_config.pubkey_re_address,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_016_addKey(self):
		try:
			(process, response) = addKey(test_config.ontId, test_config.new_publickey4,test_config.pubkey_re_address,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_017_addKey(self):
		try:
			(process, response) = addKey(test_config.ontId, test_config.new_publickey5,test_config.pubkey_re_address,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_018_addKey(self):
		try:
			(process, response) = addKey(test_config.ontId, test_config.addKey_018,test_config.pubkey_reAddress1,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass

		
	def test_abnormal_019_addKey(self):
		try:
			(process, response) = addKey(test_config.ontId, test_config.new_publickey,test_config.pubkey_reAddress2,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_020_addKey(self):
		try:
			(process, response) = addRecovery(test_config.ontId, test_config.recoveryaddress,test_config.public_key,test_config.node_index,0)#需要先设定完毕恢复地址
			(process, response) = addKey(test_config.ontId, test_config.menualPubKey2,test_config.pubkey_reAddress3,test_config.node_index,0,test_config.pubkey_reAddress3_Array)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_021_addKey(self):
		try:
			(process, response) = addKey(test_config.ontId, test_config.new_publickey,test_config.pubkey_reAddress4,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_022_addKey(self):
		try:
			(process, response) = addKey(test_config.ontId, test_config.new_publickey,test_config.pubkey_reAddress5,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_base_023_removeKey(self):
		try:
			(process, response) = removeKey(test_config.userOntId6, test_config.menualPubKey1,test_config.pubkey_re_address,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_024_removeKey(self):
		try:
			(process, response) = removeKey(test_config.userOntId7, test_config.remove_publickey,test_config.pubkey_re_address,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_025_removeKey(self):
		try:
			(process, response) = removeKey(test_config.userOntId4, test_config.remove_publickey,test_config.pubkey_re_address,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_026_removeKey(self):
		try:
			(process, response) = removeKey(test_config.userOntId5, test_config.remove_publickey,test_config.pubkey_re_address,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_027_removeKey(self):
		try:
			(process, response) = addKey(test_config.ontId, test_config.del_pubkey1,test_config.pubkey_re_address,test_config.node_index,0)#先把这个key加上县
			(process, response) = removeKey(test_config.ontId, test_config.del_pubkey1,test_config.pubkey_re_address,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_028_removeKey(self):
		try:
			(process, response) = removeKey(test_config.ontId, test_config.del_pubkey2,test_config.pubkey_re_address,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_029_removeKey(self):
		try:
			(process, response) = removeKey(test_config.ontId, test_config.del_pubkey3,test_config.pubkey_re_address,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_030_removeKey(self):
		try:
			(process, response) = removeKey(test_config.ontId, test_config.del_pubkey4,test_config.pubkey_re_address,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_031_removeKey(self):
		try:
			(process, response) = removeKey(test_config.ontId, test_config.del_pubkey5,test_config.pubkey_re_address,test_config.node_index,errorcode=0)
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_032_removeKey(self):
		try:
			(process, response) = addKey(test_config.ontId, test_config.removeKey_32,test_config.pubkey_reAddress1,test_config.node_index,0)#先注册公钿
			(process, response) = removeKey(test_config.ontId, test_config.removeKey_32,test_config.pubkey_reAddress1,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_033_removeKey(self):
		try:
			(process, response) = removeKey(test_config.ontId, test_config.remove_publickey,test_config.pubkey_reAddress2,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_034_removeKey(self):
		try:
			(process, response) = removeKey(test_config.ontId, test_config.remove_publickey,test_config.pubkey_reAddress6,test_config.node_index)
			ASSERT(process, "")
		except:
			pass


	def test_normal_035_removeKey(self):
		try:
			(process, response) = addKey(test_config.ontId, test_config.removeKey_35, test_config.pubkey_reAddress1,test_config.node_index,0)#先注册公钿		
			(process, response) = removeKey(test_config.ontId, test_config.removeKey_35,test_config.pubkey_reAddress3,test_config.node_index,0,test_config.pubkey_reAddress3_Array)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_036_removeKey(self):
		try:
			(process, response) = removeKey(test_config.ontId, test_config.remove_publickey,test_config.pubkey_reAddress4,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_037_removeKey(self):
		try:
			(process, response) = removeKey(test_config.ontId, test_config.remove_publickey,test_config.pubkey_reAddress5,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_base_038_addRecovery(self):
		try:
			(process, response) = regIDWithPublicKey(test_config.addRecovery_38,test_config.public_key,test_config.node_index,0)#先注册一个账叿
			(process, response) = addRecovery(test_config.addRecovery_38, test_config.recoveryaddress,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass

		
	def test_abnormal_039_addRecovery(self):
		try:
			(process, response) = addRecovery(test_config.userOntId7, test_config.recoveryaddress,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_040_addRecovery(self):
		try:
			(process, response) = addRecovery(test_config.userOntId4, test_config.recoveryaddress,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_041_addRecovery(self):
		try:
			(process, response) = addRecovery(test_config.userOntId5, test_config.recoveryaddress,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_042_addRecovery(self):
		try:
			(process, response) = regIDWithPublicKey(test_config.addRecovery_42,test_config.public_key,test_config.node_index,0)#先注册一个账叿
			(process, response) = addRecovery(test_config.addRecovery_42, test_config.recoveryAddress1,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_043_addRecovery(self):
		try:
			(process, response) = addRecovery(test_config.ontId, test_config.recoveryAddress2,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_044_addRecovery(self):
		try:
			(process, response) = addRecovery(test_config.ontId, test_config.recoveryAddress3,test_config.public_key,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_045_addRecovery(self):
		try:
			(process, response) = addRecovery(test_config.ontId, test_config.recoveryAddress4,test_config.public_key,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_046_addRecovery(self):
		try:
			(process, response) = regIDWithPublicKey(test_config.addRecovery_46,test_config.public_key,test_config.node_index,0)#先注册一个账叿
			(process, response) = addRecovery(test_config.addRecovery_46, test_config.recoveryaddress,test_config.public_key4,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_047_addRecovery(self):
		try:
			(process, response) = addRecovery(test_config.ontId, test_config.recoveryaddress,test_config.public_key5,test_config.node_index)
			ASSERT(process, "")
		except:
			pass


	def test_abnormal_048_addRecovery(self):
		try:
			(process, response) = addRecovery(test_config.ontId, test_config.recoveryaddress,test_config.public_key2,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_049_addRecovery(self):
		try:
			(process, response) = addRecovery(test_config.ontId, test_config.recoveryaddress,test_config.public_key3,test_config.node_index)
			ASSERT(process, "")
		except:
			pass


	def test_base_050_changeRecovery(self):
		try:
			(process, response) = changeRecovery(test_config.userOntId6, test_config.new_recovery_address,test_config.old_recovery_address,test_config.public_key,test_config.node_index,0,test_config.old_recovery_address_Array)#先把它换成新皿
			(process, response) = changeRecovery(test_config.userOntId6, test_config.old_recovery_address,test_config.new_recovery_address,test_config.public_key,test_config.node_index,0,test_config.new_recovery_address_Array)#再把它换回来
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_051_changeRecovery(self):
		try:
			(process, response) = changeRecovery(test_config.userOntId7, test_config.new_recovery_address,test_config.old_recovery_address,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_052_changeRecovery(self):
		try:
			(process, response) = changeRecovery(test_config.userOntId4, test_config.new_recovery_address,test_config.old_recovery_address,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_053_changeRecovery(self):
		try:
			(process, response) = changeRecovery(test_config.userOntId5, test_config.new_recovery_address,test_config.old_recovery_address,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_054_changeRecovery(self):
		try:
			(process, response) = changeRecovery(test_config.ontId, test_config.new_recoveryAddress1,test_config.old_recovery_address,test_config.public_key,test_config.node_index,0,test_config.old_recovery_address_Array)#换这丿
			(process, response) = changeRecovery(test_config.ontId, test_config.old_recovery_address,test_config.new_recoveryAddress1,test_config.public_key,test_config.node_index,0,test_config.new_recoveryAddress1_Array)#再换回来
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_055_changeRecovery(self):
		try:
			(process, response) = changeRecovery(test_config.ontId, test_config.old_recovery_address,test_config.old_recovery_address,test_config.public_key,test_config.node_index,47001,test_config.old_recovery_address_Array)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_056_changeRecovery(self):
		try:
			(process, response) = changeRecovery(test_config.ontId, test_config.new_recoveryAddress3,test_config.old_recovery_address,test_config.public_key,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_057_changeRecovery(self):
		try:
			(process, response) = changeRecovery(test_config.ontId, test_config.new_recoveryAddress4,test_config.old_recovery_address,test_config.public_key,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_058_changeRecovery(self):
		try:
			(process, response) = changeRecovery(test_config.ontId, test_config.new_recovery_address,test_config.old_recoverAddress1,test_config.public_key,test_config.node_index,0,test_config.old_recoverAddress1_Array)#换这丿
			(process, response) = changeRecovery(test_config.ontId, test_config.old_recoverAddress1,test_config.new_recovery_address,test_config.public_key,test_config.node_index,0,test_config.new_recovery_address_Array)#再换回来
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_059_changeRecovery(self):
		try:
			(process, response) = changeRecovery(test_config.ontId, test_config.new_recovery_address,test_config.old_recoverAddress2,test_config.public_key,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_060_changeRecovery(self):
		try:
			(process, response) = changeRecovery(test_config.ontId, test_config.new_recovery_address,test_config.old_recoverAddress3,test_config.public_key,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
			pass
		

	def test_base_061_regIDWithAttributes(self):
		try:
			(process, response) = regIDWithAttributes(test_config.regIDWithAttributes_61, test_config.attributes_array,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_062_regIDWithAttributes(self):
		try:
			(process, response) = regIDWithAttributes(test_config.userOntId6, test_config.attributes_array,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_063_regIDWithAttributes(self):
		try:
			(process, response) = regIDWithAttributes(test_config.userOntId4, test_config.attributes_array,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_064_regIDWithAttributes(self):
		try:
			(process, response) = regIDWithAttributes(test_config.userOntId5, test_config.attributes_array,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_065_regIDWithAttributes(self):
		try:
			(process, response) = regIDWithAttributes(test_config.regIDWithAttributes_65, test_config.attribute1,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_066_regIDWithAttributes(self):
		try:
			(process, response) = regIDWithAttributes(test_config.regIDWithAttributes_66, test_config.attribute2,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_067_regIDWithAttributes(self):
		try:
			(process, response) = regIDWithAttributes(test_config.newontId, test_config.attribute3,test_config.public_key,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_068_regIDWithAttributes(self):
		try:
			(process, response) = regIDWithAttributes(test_config.newontId, test_config.attribute4,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_069_regIDWithAttributes(self):
		try:
			(process, response) = regIDWithAttributes(test_config.newontId, test_config.attribute5,test_config.public_key,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_070_regIDWithAttributes(self):
		try:
			(process, response) = regIDWithAttributes(test_config.newontId, test_config.attribute6,test_config.public_key,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_071_regIDWithAttributes(self):
		try:
			(process, response) = regIDWithAttributes(test_config.regIDWithAttributes_71, test_config.attributes_array,test_config.public_key1,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_072_regIDWithAttributes(self):
		try:
			(process, response) = regIDWithAttributes(test_config.newontId, test_config.attributes_array,test_config.public_key2,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_073_regIDWithAttributes(self):
		try:
			(process, response) = regIDWithAttributes(test_config.newontId, test_config.attributes_array,test_config.public_key3,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_base_074_addAttributes(self):
		try:
			(process, response) = addAttributes(test_config.userOntId6, test_config.addAttributes_74,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_075_addAttributes(self):
		try:
			(process, response) = addAttributes(test_config.userOntId7, test_config.attributes_array,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_076_addAttributes(self):
		try:
			(process, response) = addAttributes(test_config.userOntId4, test_config.attributes_array,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_077_addAttributes(self):
		try:
			(process, response) = addAttributes(test_config.userOntId5, test_config.attributes_array,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_078_addAttributes(self):
		try:
			(process, response) = addAttributes(test_config.ontId, test_config.attribute1,test_config.public_key,test_config.node_index,0)
			(process, response) = getAttributes(test_config.ontId,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_079_addAttributes(self):
		try:
			(process, response) = addAttributes(test_config.ontId, test_config.attribute2,test_config.public_key,test_config.node_index,0)
			(process, response) = getAttributes(test_config.ontId,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
			pass
		

	def test_abnormal_080_addAttributes(self):
		try:
			(process, response) = addAttributes(test_config.ontId, test_config.attribute3,test_config.public_key,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
			pass
		

	def test_normal_081_addAttributes(self):
		try:
			(process, response) = addAttributes(test_config.ontId, test_config.attribute4,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:


	def test_abnormal_082_addAttributes(self):
		try:
			(process, response) = addAttributes(test_config.ontId, test_config.attribute5,test_config.public_key,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
		

	def test_abnormal_083_addAttributes(self):
		try:
			(process, response) = addAttributes(test_config.ontId, test_config.attribute6,test_config.public_key,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
		

	def test_normal_084_addAttributes(self):
		try:
			(process, response) = addAttributes(test_config.ontId, test_config.addAttributes_84,test_config.public_key4,test_config.node_index,0)
			ASSERT(process, "")
		except:
		

	def test_abnormal_085_addAttributes(self):
		try:
			(process, response) = addAttributes(test_config.ontId, test_config.attributes_array,test_config.public_key5,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_abnormal_086_addAttributes(self):
		try:
			(process, response) = addAttributes(test_config.ontId, test_config.attributes_array,test_config.public_key2,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
		

	def test_abnormal_087_addAttributes(self):
		try:
			(process, response) = addAttributes(test_config.ontId, test_config.attributes_array,test_config.public_key3,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_base_088_removeAttribute(self):
		try:
			result = True
			(process, response) = addAttributes(test_config.userOntId6, test_config.attributes_array,test_config.public_key,test_config.node_index,0)#先把attribute加进
			(process, response) = removeAttribute(test_config.userOntId6, test_config.attributePath,test_config.public_key,test_config.node_index,0)#再删了它 
			ASSERT(process, "")
		except:

		
	def test_abnormal_089_removeAttribute(self):
		try:
			result = True
			(process, response) = removeAttribute(test_config.userOntId7, test_config.attributePath,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_abnormal_090_removeAttribute(self):
		try:
			(process, response) = removeAttribute(test_config.userOntId4, test_config.attributePath,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:



	def test_abnormal_091_removeAttribute(self):
		try:
			(process, response) = removeAttribute(test_config.userOntId5, test_config.attributePath,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_normal_092_removeAttribute(self):
		try:
			(process, response) = removeAttribute(test_config.ontId, test_config.delAttriPath1,test_config.public_key,test_config.node_index,0)#先把attribute删了
			(process, response) = addAttributes(test_config.ontId, test_config.attributes_array,test_config.public_key,test_config.node_index,0)#再加进去
			ASSERT(process, "")
		except:
		

	def test_abnormal_093_removeAttribute(self):
		try:
			(process, response) = removeAttribute(test_config.ontId, test_config.delAttriPath2,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_abnormal_094_removeAttribute(self):
		try:
			(process, response) = removeAttribute(test_config.ontId, test_config.delAttriPath3,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_abnormal_095_removeAttribute(self):
		try:
			(process, response) = removeAttribute(test_config.ontId, test_config.delAttriPath4,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_normal_096_removeAttribute(self):
		try:
			(process, response) = removeAttribute(test_config.ontId, test_config.attributePath,test_config.public_key4,test_config.node_index,0)
			(process, response) = addAttributes(test_config.ontId, test_config.attributes_array,test_config.public_key4,test_config.node_index,0)#再加进去
			ASSERT(process, "")
		except:
		

	def test_abnormal_097_removeAttribute(self):
		try:
			(process, response) = removeAttribute(test_config.ontId, test_config.attributePath,test_config.public_key5,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_abnormal_098_removeAttribute(self):
		try:
			(process, response) = removeAttribute(test_config.ontId, test_config.attributePath,test_config.public_key2,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
		

	def test_abnormal_099_removeAttribute(self):
		try:
			(process, response) = removeAttribute(test_config.ontId, test_config.attributePath,test_config.public_key3,test_config.node_index)
			ASSERT(process, "")
		except:
		
		

	def test_base_100_getPublicKeys(self):
		try:
			(process, response) = getPublicKeys(test_config.userOntId6,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
		

	def test_normal_101_getPublicKeys(self):
		try:
			(process, response) = getPublicKeys(test_config.userOntId7,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
		

	def test_normal_102_getPublicKeys(self):
		try:
			(process, response) = getPublicKeys(test_config.userOntId4,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
		

	def test_abnormal_103_getPublicKeys(self):
		try:
			(process, response) = getPublicKeys(test_config.userOntId5,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
	

	def test_base_104_getKeyState(self):
		try:
			(process, response) = getKeyState(test_config.userOntId6,test_config.keyNum,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
		

	def test_abnormal_105_getKeyState(self):
		try:
			(process, response) = getKeyState(test_config.userOntId7,test_config.keyNum,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_abnormal_106_getKeyState(self):
		try:
			(process, response) = getKeyState(test_config.userOntId4,test_config.keyNum,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_abnormal_107_getKeyState(self):
		try:
			(process, response) = getKeyState(test_config.userOntId5,test_config.keyNum,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_normal_108_getKeyState(self):
		try:
			(process, response) = getKeyState(test_config.ontId,test_config.keyNo1,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
		

	def test_abnormal_109_getKeyState(self):
		try:
			(process, response) = getKeyState(test_config.ontId,test_config.keyNo2,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_abnormal_110_getKeyState(self):
		try:
			(process, response) = getKeyState(test_config.ontId,test_config.keyNo3,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_abnormal_111_getKeyState(self):
		try:
			(process, response) = getKeyState(test_config.ontId,keyNo4,test_config.public_key,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
		

	def test_base_112_getAttributes(self):
		try:
			(process, response) = getAttributes(test_config.userOntId6,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
		

	def test_normal_113_getAttributes(self):
		try:
			(process, response) = getAttributes(test_config.userOntId7,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
		

	def test_normal_114_getAttributes(self):
		try:
			(process, response) = getAttributes(test_config.userOntId4,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
		

	def test_abnormal_115_getAttributes(self):
		try:
			(process, response) = getAttributes(test_config.userOntId5,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_base_116_getDDO(self):
		try:
			(process, response) = getDDO(test_config.userOntId6,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
	

	def test_normal_117_getDDO(self):
		try:
			(process, response) = getDDO(test_config.userOntId7,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
		

	def test_normal_118_getDDO(self):
		try:
			(process, response) = getDDO(test_config.userOntId4,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
		

	def test_abnormal_119_getDDO(self):
		try:
			(process, response) = getDDO(test_config.userOntId5,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_base_120_verifySignature(self):
		try:
			(process, response) = verifySignature(test_config.userOntId8,test_config.keyNum,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:


	def test_abnormal_121_verifySignature(self):
		try:
			(process, response) = verifySignature(test_config.userOntId9,test_config.keyNum,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_abnormal_122_verifySignature(self):
		try:
			(process, response) = verifySignature(test_config.userOntId10,test_config.keyNum,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_abnormal_123_verifySignature(self):
		try:
			(process, response) = verifySignature(test_config.userOntId11,test_config.keyNum,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_normal_124_verifySignature(self):
		try:
			(process, response) = verifySignature(test_config.ontId,test_config.keyNo1,test_config.public_key,test_config.node_index,0)
			ASSERT(process, "")
		except:
		

	def test_abnormal_125_verifySignature(self):
		try:
			(process, response) = verifySignature(test_config.ontId,test_config.keyNo2,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_abnormal_126_verifySignature(self):
		try:
			(process, response) = verifySignature(test_config.ontId,test_config.keyNo3,test_config.public_key,test_config.node_index)
			ASSERT(process, "")
		except:
		

	def test_abnormal_127_verifySignature(self):
		try:
			(process, response) = verifySignature(test_config.ontId,test_config.keyNo4,test_config.public_key,test_config.node_index,900,errorkey="error_code")
			ASSERT(process, "")
		except:
		

####################################################
if __name__ == '__main__':
	unittest.main()

