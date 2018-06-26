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
from utils.contractapi import *
from test_api import *
from test_ontid_config import *
from utils.commonapi import call_contract

logger = LoggerInstance

####################################################
#test cases
class TestContract(ParametrizedTestCase):
	def start(self, log_path):
		logger.open(log_path)
		
	def finish(self, task_name, log_path, result, msg):
		if result:
			logger.print("[ OK       ] ")
			logger.append_record(task_name, "pass", log_path)
		else:
			logger.print("[ Failed   ] " + msg)
			logger.append_record(task_name, "fail", log_path)
		logger.close()
	def test_001_regIDWithPublicKey(self):
		log_path = "001_regIDWithPublicKey.log"
		task_name = "001_regIDWithPublicKey.log"
		self.start(log_path)
		(result, response) = regIDWithPublicKey(userOntId1, public_key,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_002_regIDWithPublicKey(self):
		log_path = "002_regIDWithPublicKey.log"
		task_name = "002_regIDWithPublicKey.log"
		self.start(log_path)
		(result, response) = regIDWithPublicKey(userOntId2, public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_003_regIDWithPublicKey(self):
		log_path = "003_regIDWithPublicKey.log"
		task_name = "003_regIDWithPublicKey.log"
		self.start(log_path)
		(result, response) = regIDWithPublicKey(userOntId3, public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_004_regIDWithPublicKey(self):
		log_path = "004_regIDWithPublicKey.log"
		task_name = "004_regIDWithPublicKey.log"
		self.start(log_path)
		(result, response) = regIDWithPublicKey(userOntId4, public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_005_regIDWithPublicKey(self):
		log_path = "005_regIDWithPublicKey.log"
		task_name = "005_regIDWithPublicKey.log"
		self.start(log_path)
		(result, response) = regIDWithPublicKey(userOntId5, public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_006_regIDWithPublicKey(self):
		log_path = "006_regIDWithPublicKey.log"
		task_name = "006_regIDWithPublicKey.log"
		self.start(log_path)
		(result, response) = regIDWithPublicKey(menualOntId, public_key1,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_007_regIDWithPublicKey(self):
		log_path = "007_regIDWithPublicKey.log"
		task_name = "007_regIDWithPublicKey.log"
		self.start(log_path)
		(result, response) = regIDWithPublicKey(menualOntId2, public_key2,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


	def test_008_regIDWithPublicKey(self):
		log_path = "008_regIDWithPublicKey.log"
		task_name = "008_regIDWithPublicKey.log"
		self.start(log_path)
		(result, response) = regIDWithPublicKey(menualOntId2, public_key3,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_009_addKey(self):
		log_path = "009_addKey.log"
		task_name = "009_addKey.log"
		self.start(log_path)
		(result, response) = addKey(userOntId6, menualPubKey1,pubkey_re_address,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_010_addKey(self):
		log_path = "010_addKey.log"
		task_name = "010_addKey.log"
		self.start(log_path)
		(result, response) = addKey(userOntId7, new_publickey,pubkey_re_address,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_011_addKey(self):
		log_path = "011_addKey.log"
		task_name = "011_addKey.log"
		self.start(log_path)
		(result, response) = addKey(userOntId4, new_publickey,pubkey_re_address,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_012_addKey(self):
		log_path = "012_addKey.log"
		task_name = "012_addKey.log"
		self.start(log_path)
		(result, response) = addKey(userOntId5, new_publickey,pubkey_re_address,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_013_addKey(self):
		log_path = "013_addKey.log"
		task_name = "013_addKey.log"
		self.start(log_path)
		(result, response) = addKey(ontId, new_publickey1,pubkey_re_address,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_014_addKey(self):
		log_path = "014_addKey.log"
		task_name = "014_addKey.log"
		self.start(log_path)
		(result, response) = addKey(ontId, new_publickey2,pubkey_re_address,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_015_addKey(self):
		log_path = "015_addKey.log"
		task_name = "015_addKey.log"
		self.start(log_path)
		(result, response) = addKey(menualOntId, new_publickey3,pubkey_re_address,node_index,0)#先在其他用户处注册完毕该公钥
		(result, response) = addKey(ontId, new_publickey3,pubkey_re_address,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_016_addKey(self):
		log_path = "016_addKey.log"
		task_name = "016_addKey.log"
		self.start(log_path)
		(result, response) = addKey(ontId, new_publickey4,pubkey_re_address,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


	def test_017_addKey(self):
		log_path = "017_addKey.log"
		task_name = "017_addKey.log"
		self.start(log_path)
		(result, response) = addKey(ontId, new_publickey5,pubkey_re_address,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_018_addKey(self):
		log_path = "018_addKey.log"
		task_name = "018_addKey.log"
		self.start(log_path)
		(result, response) = addKey(ontId, menualPubKey1,pubkey_reAddress1,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_019_addKey(self):
		log_path = "019_addKey.log"
		task_name = "019_addKey.log"
		self.start(log_path)
		(result, response) = addKey(ontId, new_publickey,pubkey_reAddress2,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_020_addKey(self):
		log_path = "020_addKey.log"
		task_name = "020_addKey.log"
		self.start(log_path)
		(result, response) = addRecovery(ontId, recoveryaddress,public_key,node_index,0)#需要先设定完毕恢复地址
		(result, response) = addKey(ontId, menualPubKey2,pubkey_reAddress3,node_index,0,pubkey_reAddress3_Array)
		self.finish(task_name, log_path, result,  "")


	def test_021_addKey(self):
		log_path = "021_addKey.log"
		task_name = "021_addKey.log"
		self.start(log_path)
		(result, response) = addKey(ontId, new_publickey,pubkey_reAddress4,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


	def test_022_addKey(self):
		log_path = "022_addKey.log"
		task_name = "022_addKey.log"
		self.start(log_path)
		(result, response) = addKey(ontId, new_publickey,pubkey_reAddress5,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_023_removeKey(self):
		log_path = "023_removeKey.log"
		task_name = "023_removeKey.log"
		self.start(log_path)
		(result, response) = removeKey(userOntId6, menualPubKey1,pubkey_re_address,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_024_removeKey(self):
		log_path = "024_removeKey.log"
		task_name = "024_removeKey.log"
		self.start(log_path)
		(result, response) = removeKey(userOntId7, remove_publickey,pubkey_re_address,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_025_removeKey(self):
		log_path = "025_removeKey.log"
		task_name = "025_removeKey.log"
		self.start(log_path)
		(result, response) = removeKey(userOntId4, remove_publickey,pubkey_re_address,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_026_removeKey(self):
		log_path = "026_removeKey.log"
		task_name = "026_removeKey.log"
		self.start(log_path)
		(result, response) = removeKey(userOntId5, remove_publickey,pubkey_re_address,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_027_removeKey(self):
		log_path = "027_removeKey.log"
		task_name = "027_removeKey.log"
		self.start(log_path)
		(result, response) = addKey(ontId, del_pubkey1,pubkey_re_address,node_index,0)#先把这个key加上�?
		(result, response) = removeKey(ontId, del_pubkey1,pubkey_re_address,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_028_removeKey(self):
		log_path = "028_removeKey.log"
		task_name = "028_removeKey.log"
		self.start(log_path)
		(result, response) = removeKey(ontId, del_pubkey2,pubkey_re_address,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_029_removeKey(self):
		log_path = "029_removeKey.log"
		task_name = "029_removeKey.log"
		self.start(log_path)
		(result, response) = removeKey(ontId, del_pubkey3,pubkey_re_address,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_030_removeKey(self):
		log_path = "030_removeKey.log"
		task_name = "030_removeKey.log"
		self.start(log_path)
		(result, response) = removeKey(ontId, del_pubkey4,pubkey_re_address,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


	def test_031_removeKey(self):
		log_path = "031_removeKey.log"
		task_name = "031_removeKey.log"
		self.start(log_path)
		(result, response) = removeKey(ontId, del_pubkey5,pubkey_re_address,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_032_removeKey(self):
		log_path = "032_removeKey.log"
		task_name = "032_removeKey.log"
		self.start(log_path)
		(result, response) = addKey(ontId, removeKey_32,pubkey_reAddress1,node_index,0)#先注册公�?
		(result, response) = removeKey(ontId, removeKey_32,pubkey_reAddress1,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_033_removeKey(self):
		log_path = "033_removeKey.log"
		task_name = "033_removeKey.log"
		self.start(log_path)
		(result, response) = removeKey(ontId, remove_publickey,pubkey_reAddress2,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_034_removeKey(self):
		log_path = "034_removeKey.log"
		task_name = "034_removeKey.log"
		self.start(log_path)
		(result, response) = removeKey(ontId, remove_publickey,pubkey_reAddress6,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_035_removeKey(self):
		log_path = "035_removeKey.log"
		task_name = "035_removeKey.log"
		self.start(log_path)
		(result, response) = addKey(ontId, removeKey_35,pubkey_reAddress1,node_index,0)#先注册公�?		
		(result, response) = removeKey(ontId, removeKey_35,pubkey_reAddress3,node_index,0,pubkey_reAddress3_Array)
		self.finish(task_name, log_path, result,  "")


	def test_036_removeKey(self):
		log_path = "036_removeKey.log"
		task_name = "036_removeKey.log"
		self.start(log_path)
		(result, response) = removeKey(ontId, remove_publickey,pubkey_reAddress4,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


	def test_037_removeKey(self):
		log_path = "037_removeKey.log"
		task_name = "037_removeKey.log"
		self.start(log_path)
		(result, response) = removeKey(ontId, remove_publickey,pubkey_reAddress5,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_038_addRecovery(self):
		log_path = "038_addRecovery.log"
		task_name = "038_addRecovery.log"
		self.start(log_path)
		(result, response) = regIDWithPublicKey(addRecovery_38,public_key,node_index,0)#先注册一个账�?
		(result, response) = addRecovery(addRecovery_38, recoveryaddress,public_key,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_039_addRecovery(self):
		log_path = "039_addRecovery.log"
		task_name = "039_addRecovery.log"
		self.start(log_path)
		(result, response) = addRecovery(userOntId7, recoveryaddress,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_040_addRecovery(self):
		log_path = "040_addRecovery.log"
		task_name = "040_addRecovery.log"
		self.start(log_path)
		(result, response) = addRecovery(userOntId4, recoveryaddress,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_041_addRecovery(self):
		log_path = "041_addRecovery.log"
		task_name = "041_addRecovery.log"
		self.start(log_path)
		(result, response) = addRecovery(userOntId5, recoveryaddress,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_042_addRecovery(self):
		log_path = "042_addRecovery.log"
		task_name = "042_addRecovery.log"
		self.start(log_path)
		(result, response) = regIDWithPublicKey(addRecovery_42,public_key,node_index,0)#先注册一个账�?
		(result, response) = addRecovery(addRecovery_42, recoveryAddress1,public_key,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_043_addRecovery(self):
		log_path = "043_addRecovery.log"
		task_name = "043_addRecovery.log"
		self.start(log_path)
		(result, response) = addRecovery(ontId, recoveryAddress2,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_044_addRecovery(self):
		log_path = "044_addRecovery.log"
		task_name = "044_addRecovery.log"
		self.start(log_path)
		(result, response) = addRecovery(ontId, recoveryAddress3,public_key,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


	def test_045_addRecovery(self):
		log_path = "045_addRecovery.log"
		task_name = "045_addRecovery.log"
		self.start(log_path)
		(result, response) = addRecovery(ontId, recoveryAddress4,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_046_addRecovery(self):
		log_path = "046_addRecovery.log"
		task_name = "046_addRecovery.log"
		self.start(log_path)
		(result, response) = regIDWithPublicKey(addRecovery_46,public_key,node_index,0)#先注册一个账�?
		(result, response) = addRecovery(addRecovery_46, recoveryaddress,public_key4,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_047_addRecovery(self):
		log_path = "047_addRecovery.log"
		task_name = "047_addRecovery.log"
		self.start(log_path)
		(result, response) = addRecovery(ontId, recoveryaddress,public_key5,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_048_addRecovery(self):
		log_path = "048_addRecovery.log"
		task_name = "048_addRecovery.log"
		self.start(log_path)
		(result, response) = addRecovery(ontId, recoveryaddress,public_key2,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_049_addRecovery(self):
		log_path = "049_addRecovery.log"
		task_name = "049_addRecovery.log"
		self.start(log_path)
		(result, response) = addRecovery(ontId, recoveryaddress,public_key3,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_050_changeRecovery(self):
		log_path = "050_changeRecovery.log"
		task_name = "050_changeRecovery.log"
		self.start(log_path)
		(result, response) = changeRecovery(userOntId6, new_recovery_address,old_recovery_address,public_key,node_index,0,old_recovery_address_Array)#先把它换成新�?
		(result, response) = changeRecovery(userOntId6, old_recovery_address,new_recovery_address,public_key,node_index,0,new_recovery_address_Array)#再把它换回来
		self.finish(task_name, log_path, result,  "")


	def test_051_changeRecovery(self):
		log_path = "051_changeRecovery.log"
		task_name = "051_changeRecovery.log"
		self.start(log_path)
		(result, response) = changeRecovery(userOntId7, new_recovery_address,old_recovery_address,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_052_changeRecovery(self):
		log_path = "052_changeRecovery.log"
		task_name = "052_changeRecovery.log"
		self.start(log_path)
		(result, response) = changeRecovery(userOntId4, new_recovery_address,old_recovery_address,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_053_changeRecovery(self):
		log_path = "053_changeRecovery.log"
		task_name = "053_changeRecovery.log"
		self.start(log_path)
		(result, response) = changeRecovery(userOntId5, new_recovery_address,old_recovery_address,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_054_changeRecovery(self):
		log_path = "054_changeRecovery.log"
		task_name = "054_changeRecovery.log"
		self.start(log_path)
		(result, response) = changeRecovery(ontId, new_recoveryAddress1,old_recovery_address,public_key,node_index,0,old_recovery_address_Array)#换这�?
		(result, response) = changeRecovery(ontId, old_recovery_address,new_recoveryAddress1,public_key,node_index,0,new_recoveryAddress1_Array)#再换回来
		self.finish(task_name, log_path, result,  "")


	def test_055_changeRecovery(self):
		log_path = "055_changeRecovery.log"
		task_name = "055_changeRecovery.log"
		self.start(log_path)
		(result, response) = changeRecovery(ontId, old_recovery_address,old_recovery_address,public_key,node_index,47001,old_recovery_address_Array)
		self.finish(task_name, log_path, result,  "")


	def test_056_changeRecovery(self):
		log_path = "056_changeRecovery.log"
		task_name = "056_changeRecovery.log"
		self.start(log_path)
		(result, response) = changeRecovery(ontId, new_recoveryAddress3,old_recovery_address,public_key,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


	def test_057_changeRecovery(self):
		log_path = "057_changeRecovery.log"
		task_name = "057_changeRecovery.log"
		self.start(log_path)
		(result, response) = changeRecovery(ontId, new_recoveryAddress4,old_recovery_address,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_058_changeRecovery(self):
		log_path = "058_changeRecovery.log"
		task_name = "058_changeRecovery.log"
		self.start(log_path)
		(result, response) = changeRecovery(ontId, new_recovery_address,old_recoverAddress1,public_key,node_index,0,old_recoverAddress1)#换这�?
		(result, response) = changeRecovery(ontId, old_recoverAddress1,new_recovery_address,public_key,node_index,0,new_recovery_address)#再换回来
		self.finish(task_name, log_path, result,  "")


	def test_059_changeRecovery(self):
		log_path = "059_changeRecovery.log"
		task_name = "059_changeRecovery.log"
		self.start(log_path)
		(result, response) = changeRecovery(ontId, new_recovery_address,old_recoverAddress2,public_key,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


	def test_060_changeRecovery(self):
		log_path = "060_changeRecovery.log"
		task_name = "060_changeRecovery.log"
		self.start(log_path)
		(result, response) = changeRecovery(ontId, new_recovery_address,old_recoverAddress3,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_061_regIDWithAttributes(self):
		log_path = "061_regIDWithAttributes.log"
		task_name = "061_regIDWithAttributes.log"
		self.start(log_path)
		(result, response) = regIDWithAttributes(regIDWithAttributes_61, attributes_array,public_key,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_062_regIDWithAttributes(self):
		log_path = "062_regIDWithAttributes.log"
		task_name = "062_regIDWithAttributes.log"
		self.start(log_path)
		(result, response) = regIDWithAttributes(userOntId6, attributes_array,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_063_regIDWithAttributes(self):
		log_path = "063_regIDWithAttributes.log"
		task_name = "063_regIDWithAttributes.log"
		self.start(log_path)
		(result, response) = regIDWithAttributes(userOntId4, attributes_array,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_064_regIDWithAttributes(self):
		log_path = "064_regIDWithAttributes.log"
		task_name = "064_regIDWithAttributes.log"
		self.start(log_path)
		(result, response) = regIDWithAttributes(userOntId5, attributes_array,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_065_regIDWithAttributes(self):
		log_path = "065_regIDWithAttributes.log"
		task_name = "065_regIDWithAttributes.log"
		self.start(log_path)
		(result, response) = regIDWithAttributes(regIDWithAttributes_65, attribute1,public_key,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_066_regIDWithAttributes(self):
		log_path = "066_regIDWithAttributes.log"
		task_name = "066_regIDWithAttributes.log"
		self.start(log_path)
		(result, response) = regIDWithAttributes(regIDWithAttributes_66, attribute2,public_key,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_067_regIDWithAttributes(self):
		log_path = "067_regIDWithAttributes.log"
		task_name = "067_regIDWithAttributes.log"
		self.start(log_path)
		(result, response) = regIDWithAttributes(newontId, attribute3,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_068_regIDWithAttributes(self):
		log_path = "068_regIDWithAttributes.log"
		task_name = "068_regIDWithAttributes.log"
		self.start(log_path)
		(result, response) = regIDWithAttributes(newontId, attribute4,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_069_regIDWithAttributes(self):
		log_path = "069_regIDWithAttributes.log"
		task_name = "069_regIDWithAttributes.log"
		self.start(log_path)
		(result, response) = regIDWithAttributes(newontId, attribute5,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_070_regIDWithAttributes(self):
		log_path = "070_regIDWithAttributes.log"
		task_name = "070_regIDWithAttributes.log"
		self.start(log_path)
		(result, response) = regIDWithAttributes(newontId, attribute6,public_key,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


	def test_071_regIDWithAttributes(self):
		log_path = "071_regIDWithAttributes.log"
		task_name = "071_regIDWithAttributes.log"
		self.start(log_path)
		(result, response) = regIDWithAttributes(regIDWithAttributes_71, attributes_array,public_key1,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_072_regIDWithAttributes(self):
		log_path = "072_regIDWithAttributes.log"
		task_name = "072_regIDWithAttributes.log"
		self.start(log_path)
		(result, response) = regIDWithAttributes(newontId, attributes_array,public_key2,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


	def test_073_regIDWithAttributes(self):
		log_path = "073_regIDWithAttributes.log"
		task_name = "073_regIDWithAttributes.log"
		self.start(log_path)
		(result, response) = regIDWithAttributes(newontId, attributes_array,public_key3,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_074_addAttributes(self):
		log_path = "074_addAttributes.log"
		task_name = "074_addAttributes.log"
		self.start(log_path)
		(result, response) = addAttributes(userOntId6, addAttributes_74,public_key,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_075_addAttributes(self):
		log_path = "075_addAttributes.log"
		task_name = "075_addAttributes.log"
		self.start(log_path)
		(result, response) = addAttributes(userOntId7, attributes_array,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_076_addAttributes(self):
		log_path = "076_addAttributes.log"
		task_name = "076_addAttributes.log"
		self.start(log_path)
		(result, response) = addAttributes(userOntId4, attributes_array,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_077_addAttributes(self):
		log_path = "077_addAttributes.log"
		task_name = "077_addAttributes.log"
		self.start(log_path)
		(result, response) = addAttributes(userOntId5, attributes_array,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_078_addAttributes(self):
		log_path = "078_addAttributes.log"
		task_name = "078_addAttributes.log"
		self.start(log_path)
		(result, response) = addAttributes(ontId, attribute1,public_key,node_index,0)
		(result, response) = getAttributes(ontId,public_key,node_index,0)

		self.finish(task_name, log_path, result,  "")


	def test_079_addAttributes(self):
		log_path = "079_addAttributes.log"
		task_name = "079_addAttributes.log"
		self.start(log_path)
		(result, response) = addAttributes(ontId, attribute2,public_key,node_index,0)
		(result, response) = getAttributes(ontId,public_key,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_080_addAttributes(self):
		log_path = "080_addAttributes.log"
		task_name = "080_addAttributes.log"
		self.start(log_path)
		(result, response) = addAttributes(ontId, attribute3,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_081_addAttributes(self):
		log_path = "081_addAttributes.log"
		task_name = "081_addAttributes.log"
		self.start(log_path)
		(result, response) = addAttributes(ontId, attribute4,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_082_addAttributes(self):
		log_path = "082_addAttributes.log"
		task_name = "082_addAttributes.log"
		self.start(log_path)
		(result, response) = addAttributes(ontId, attribute5,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_083_addAttributes(self):
		log_path = "083_addAttributes.log"
		task_name = "083_addAttributes.log"
		self.start(log_path)
		(result, response) = addAttributes(ontId, attribute6,public_key,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


	def test_084_addAttributes(self):
		log_path = "084_addAttributes.log"
		task_name = "084_addAttributes.log"
		self.start(log_path)
		(result, response) = addAttributes(ontId, addAttributes_84,public_key4,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_085_addAttributes(self):
		log_path = "085_addAttributes.log"
		task_name = "085_addAttributes.log"
		self.start(log_path)
		(result, response) = addAttributes(ontId, attributes_array,public_key5,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_086_addAttributes(self):
		log_path = "086_addAttributes.log"
		task_name = "086_addAttributes.log"
		self.start(log_path)
		(result, response) = addAttributes(ontId, attributes_array,public_key2,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


	def test_087_addAttributes(self):
		log_path = "087_addAttributes.log"
		task_name = "087_addAttributes.log"
		self.start(log_path)
		(result, response) = addAttributes(ontId, attributes_array,public_key3,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_088_removeAttribute(self):
		log_path = "088_removeAttribute.log"
		task_name = "088_removeAttribute.log"
		self.start(log_path)
		result = True
		(result, response) = addAttributes(userOntId6, attributes_array,public_key,node_index,0)#先把attribute加进
		(result, response) = removeAttribute(userOntId6, attributePath,public_key,node_index,0)#再删了它 
		self.finish(task_name, log_path, result,  "")


	def test_089_removeAttribute(self):
		log_path = "089_removeAttribute.log"
		task_name = "089_removeAttribute.log"
		self.start(log_path)
		(result, response) = removeAttribute(userOntId7, attributePath,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_090_removeAttribute(self):
		log_path = "090_removeAttribute.log"
		task_name = "090_removeAttribute.log"
		self.start(log_path)
		(result, response) = removeAttribute(userOntId4, attributePath,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_091_removeAttribute(self):
		log_path = "091_removeAttribute.log"
		task_name = "091_removeAttribute.log"
		self.start(log_path)
		(result, response) = removeAttribute(userOntId5, attributePath,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_092_removeAttribute(self):
		log_path = "092_removeAttribute.log"
		task_name = "092_removeAttribute.log"
		self.start(log_path)
		(result, response) = removeAttribute(ontId, delAttriPath1,public_key,node_index,0)#先把attribute删了
		(result, response) = addAttributes(ontId, attributes_array,public_key,node_index,0)#再加进去

		self.finish(task_name, log_path, result,  "")


	def test_093_removeAttribute(self):
		log_path = "093_removeAttribute.log"
		task_name = "093_removeAttribute.log"
		self.start(log_path)
		(result, response) = removeAttribute(ontId, delAttriPath2,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_094_removeAttribute(self):
		log_path = "094_removeAttribute.log"
		task_name = "094_removeAttribute.log"
		self.start(log_path)
		(result, response) = removeAttribute(ontId, delAttriPath3,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_095_removeAttribute(self):
		log_path = "095_removeAttribute.log"
		task_name = "095_removeAttribute.log"
		self.start(log_path)
		(result, response) = removeAttribute(ontId, delAttriPath4,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_096_removeAttribute(self):
		log_path = "096_removeAttribute.log"
		task_name = "096_removeAttribute.log"
		self.start(log_path)
		(result, response) = removeAttribute(ontId, attributePath,public_key4,node_index,0)
		(result, response) = addAttributes(ontId, attributes_array,public_key4,node_index,0)#再加进去

		self.finish(task_name, log_path, result,  "")


	def test_097_removeAttribute(self):
		log_path = "097_removeAttribute.log"
		task_name = "097_removeAttribute.log"
		self.start(log_path)
		(result, response) = removeAttribute(ontId, attributePath,public_key5,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_098_removeAttribute(self):
		log_path = "098_removeAttribute.log"
		task_name = "098_removeAttribute.log"
		self.start(log_path)
		(result, response) = removeAttribute(ontId, attributePath,public_key2,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


	def test_099_removeAttribute(self):
		log_path = "099_removeAttribute.log"
		task_name = "099_removeAttribute.log"
		self.start(log_path)
		(result, response) = removeAttribute(ontId, attributePath,public_key3,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_100_getPublicKeys(self):
		log_path = "100_getPublicKeys.log"
		task_name = "100_getPublicKeys.log"
		self.start(log_path)
		(result, response) = getPublicKeys(userOntId6,public_key,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_101_getPublicKeys(self):
		log_path = "101_getPublicKeys.log"
		task_name = "101_getPublicKeys.log"
		self.start(log_path)
		(result, response) = getPublicKeys(userOntId7,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_102_getPublicKeys(self):
		log_path = "102_getPublicKeys.log"
		task_name = "102_getPublicKeys.log"
		self.start(log_path)
		(result, response) = getPublicKeys(userOntId4,public_key,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


	def test_103_getPublicKeys(self):
		log_path = "103_getPublicKeys.log"
		task_name = "103_getPublicKeys.log"
		self.start(log_path)
		(result, response) = getPublicKeys(userOntId5,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_104_getKeyState(self):
		log_path = "104_getKeyState.log"
		task_name = "104_getKeyState.log"
		self.start(log_path)
		(result, response) = getKeyState(userOntId6,keyNum,public_key,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_105_getKeyState(self):
		log_path = "105_getKeyState.log"
		task_name = "105_getKeyState.log"
		self.start(log_path)
		(result, response) = getKeyState(userOntId7,keyNum,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_106_getKeyState(self):
		log_path = "106_getKeyState.log"
		task_name = "106_getKeyState.log"
		self.start(log_path)
		(result, response) = getKeyState(userOntId4,keyNum,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_107_getKeyState(self):
		log_path = "107_getKeyState.log"
		task_name = "107_getKeyState.log"
		self.start(log_path)
		(result, response) = getKeyState(userOntId5,keyNum,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_108_getKeyState(self):
		log_path = "108_getKeyState.log"
		task_name = "108_getKeyState.log"
		self.start(log_path)
		(result, response) = getKeyState(ontId,keyNo1,public_key,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_109_getKeyState(self):
		log_path = "109_getKeyState.log"
		task_name = "109_getKeyState.log"
		self.start(log_path)
		(result, response) = getKeyState(ontId,keyNo2,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_110_getKeyState(self):
		log_path = "110_getKeyState.log"
		task_name = "110_getKeyState.log"
		self.start(log_path)
		(result, response) = getKeyState(ontId,keyNo3,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_111_getKeyState(self):
		log_path = "111_getKeyState.log"
		task_name = "111_getKeyState.log"
		self.start(log_path)
		(result, response) = getKeyState(ontId,keyNo4,public_key,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


	def test_112_getAttributes(self):
		log_path = "112_getAttributes.log"
		task_name = "112_getAttributes.log"
		self.start(log_path)
		(result, response) = getAttributes(userOntId6,public_key,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_113_getAttributes(self):
		log_path = "113_getAttributes.log"
		task_name = "113_getAttributes.log"
		self.start(log_path)
		(result, response) = getAttributes(userOntId7,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_114_getAttributes(self):
		log_path = "114_getAttributes.log"
		task_name = "114_getAttributes.log"
		self.start(log_path)
		(result, response) = getAttributes(userOntId4,public_key,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


	def test_115_getAttributes(self):
		log_path = "115_getAttributes.log"
		task_name = "115_getAttributes.log"
		self.start(log_path)
		(result, response) = getAttributes(userOntId5,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_116_getDDO(self):
		log_path = "116_getDDO.log"
		task_name = "116_getDDO.log"
		self.start(log_path)
		(result, response) = getDDO(userOntId6,public_key,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_117_getDDO(self):
		log_path = "117_getDDO.log"
		task_name = "117_getDDO.log"
		self.start(log_path)
		(result, response) = getDDO(userOntId7,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_118_getDDO(self):
		log_path = "118_getDDO.log"
		task_name = "118_getDDO.log"
		self.start(log_path)
		(result, response) = getDDO(userOntId4,public_key,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


	def test_119_getDDO(self):
		log_path = "119_getDDO.log"
		task_name = "119_getDDO.log"
		self.start(log_path)
		(result, response) = getDDO(userOntId5,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_120_verifySignature(self):
		log_path = "120_verifySignature.log"
		task_name = "120_verifySignature.log"
		self.start(log_path)
		(result, response) = verifySignature(userOntId8,keyNum,public_key,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_121_verifySignature(self):
		log_path = "121_verifySignature.log"
		task_name = "121_verifySignature.log"
		self.start(log_path)
		(result, response) = verifySignature(userOntId9,keyNum,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_122_verifySignature(self):
		log_path = "122_verifySignature.log"
		task_name = "122_verifySignature.log"
		self.start(log_path)
		(result, response) = verifySignature(userOntId10,keyNum,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_123_verifySignature(self):
		log_path = "123_verifySignature.log"
		task_name = "123_verifySignature.log"
		self.start(log_path)
		(result, response) = verifySignature(userOntId11,keyNum,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_124_verifySignature(self):
		log_path = "124_verifySignature.log"
		task_name = "124_verifySignature.log"
		self.start(log_path)
		(result, response) = verifySignature(ontId,keyNo1,public_key,node_index,0)
		self.finish(task_name, log_path, result,  "")


	def test_125_verifySignature(self):
		log_path = "125_verifySignature.log"
		task_name = "125_verifySignature.log"
		self.start(log_path)
		(result, response) = verifySignature(ontId,keyNo2,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_126_verifySignature(self):
		log_path = "126_verifySignature.log"
		task_name = "126_verifySignature.log"
		self.start(log_path)
		(result, response) = verifySignature(ontId,keyNo3,public_key,node_index)
		self.finish(task_name, log_path, result,  "")


	def test_127_verifySignature(self):
		log_path = "127_verifySignature.log"
		task_name = "127_verifySignature.log"
		self.start(log_path)
		(result, response) = verifySignature(ontId,keyNo4,public_key,node_index,900,errorkey="error_code")
		self.finish(task_name, log_path, result,  "")


####################################################
if __name__ == '__main__':
	unittest.main()

