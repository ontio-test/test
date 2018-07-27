# -*- coding: utf-8 -*-
import sys, getopt
import time
sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.api.commonapi import *
from utils.api.contractapi import *
from utils.logger import LoggerInstance
import base58


import hashlib
def recoveryAddress(m,hexArr,checkMultiSig="ae"):
    """
    ripemd160(sha256(m || pk1len+pk1 || ... ||pknlen+ pkn || n || checkMultiSig))
	m=m,hexArr=[pubkey1,pubkey2,pubkey3...pubkeyn],checkMultiSig=0xAE,
    """
	hexAllArr=array()
	for hexnum in hexArr:
		t=len(hexnum)/2
		t_bytes=hex(t)
		hexnum=t_bytes[2:]+hexnum
		print(hexnum)
		
	print(test1)
	hash_str = "51||2102006a6490f7055a694e9dab01e57a1400c106a2d9e93bf8d50bb70af1d5b9a3cd||2102eb607c494cf1efa434c7e284c3fff8f382a0decfc8d6c1b02e2ea5b7e70cf518||52||ae"
	print(hash_str)
	hash_hexstr = hash_str.replace("||","")
	print(hash_hexstr)
	a_bytes = bytes.fromhex(hash_hexstr)
	print(a_bytes)
	aa=a_bytes.hex()
	print(aa)
	hash_256.update(a_bytes)
	#d90df075242df941683f7b9b88a8e3ccce3465dd77778a1c49198e014a6a78b5
	hash_256_value = hash_256.hexdigest()
	test2=bytes.fromhex(hash_256_value)
	obj = hashlib.new('ripemd160',bytes.fromhex(hash_256_value))
	ripemd_160_value = obj.hexdigest()
	print("sha256:", hash_256_value)  # 16杩涘埗  
	print("ripemd160 :",ripemd_160_value)
    return ripemd_160_value

recoveryAddress(1,["2102006a6490f7055a694e9dab01e57a1400c106a2d9e93bf8d50bb70af1d5b9a3cd","2102eb607c494cf1efa434c7e284c3fff8f382a0decfc8d6c1b02e2ea5b7e70cf518"])
