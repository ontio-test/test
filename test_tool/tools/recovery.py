# -*- coding: utf-8 -*-
import sys, getopt
sys.path.append('..')

from utils.hexstring import *

import hashlib
def recoveryAddress(m,hexArr,checkMultiSig="ae"):
    """
    ripemd160(sha256(m || pk1len+pk1 || ... ||pknlen+ pkn || n || checkMultiSig))
	m=m,hexArr=[pubkey1,pubkey2,pubkey3...pubkeyn],checkMultiSig=0xAE,
    """
    hexAllArr=[]
    for hexnum in hexArr:
        if(len(hexnum)%2==1):
          print("error!!!!!!"+hexnum)
          return False
        t=int(len(hexnum)/2)
        print(t)
        t_bytes=hex(t)
        hexnum=t_bytes[2:]+hexnum
        print(hexnum)
        hexAllArr.append(hexnum)
        print(hexAllArr)
    		
    hexAllArr.sort()
    		
    print(hexAllArr)
    hash_str = numSeq(m)
    for tmps in hexAllArr:
      hash_str=hash_str+tmps
    hash_str =hash_str+numSeq(len(hexAllArr))+"ae"
    #"51||2102006a6490f7055a694e9dab01e57a1400c106a2d9e93bf8d50bb70af1d5b9a3cd||2102eb607c494cf1efa434c7e284c3fff8f382a0decfc8d6c1b02e2ea5b7e70cf518||52||ae"
    print(hash_str)
    #hash_hexstr = hash_str.replace("||","")
    #print(hash_hexstr)
    a_bytes = bytes.fromhex(hash_str)
    #print(a_bytes)
    #aa=a_bytes.hex()
    #print(aa)
    hash_256=hashlib.sha256()
    hash_256.update(a_bytes)
    #d90df075242df941683f7b9b88a8e3ccce3465dd77778a1c49198e014a6a78b5
    hash_256_value = hash_256.hexdigest()
    test2=bytes.fromhex(hash_256_value)
    obj = hashlib.new('ripemd160',bytes.fromhex(hash_256_value))
    ripemd_160_value = obj.hexdigest()
    print("sha256:", hash_256_value)  # 16杩涘�? 
    print("ripemd160 :",ripemd_160_value)
    return ripemd_160_value
    
def numSeq(m):
    """
     m change
    """
    if m==0:
      return "00"
    elif m<=16:
      test=eval('0x50')+m
      teststr=hex(test)
      return teststr[2:]
    else:
      print("miao!")
      test=hex(m+1)
      truetest=hex(m)
      test2=test[2:]
      if(len(test2)%2==1):
        test3=test2.zfill(len(test2)+1)
      else:
        test3=test2
      hash_hexstr=truetest[2:].zfill(len(test3))
      print(hash_hexstr)
      a_bytes = bytes.fromhex(hash_hexstr)
      lista=list(a_bytes)
      lista.reverse()
      test222=''
      for a in lista:
        test333=hex(a)
        test333=test333[2:]
        test333=test333.zfill(2)
        test222=test222+test333
      return test222
#recoveryAddress(1,["02006a6490f7055a694e9dab01e57a1400c106a2d9e93bf8d50bb70af1d5b9a3cd","02eb607c494cf1efa434c7e284c3fff8f382a0decfc8d6c1b02e2ea5b7e70cf518"])
