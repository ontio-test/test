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
from utils.hexstring import *
def attributeChange(attribute):
	result=[]
	for test in attribute:
		result.append(ByteToHex(test.encode("utf-8")))
	print(result)
	return result
node_now = 5
node_6=6
node_now_ontid="did:ont:AdVERGmipcx4rGcHJPNwFtQEinEomPbSdu"
node_now_pubkey = Config.NODES[node_now]["pubkey"]
addKey_018="0339e720d8bcb918c21871c245030a9bf711c48e9ed765aa732868c4a21b55f379"
public_key1= node_now_pubkey  #用户公钥_ByteArray_正确的公�?
public_key2= "abcdefghijklmn123542465456747"  #用户公钥_ByteArray_乱码
public_key3= ""  #用户公钥_ByteArray_留空
public_key4= node_now_pubkey  #用户公钥_ByteArray_用户已注册公�?
public_key5 = Config.NODES[node_6]["pubkey"]  #用户公钥_ByteArray_其他用户公钥，绑定menualOntId
##default#######
public_key=node_now_pubkey
ontId=node_now_ontid
byteOntId=ByteToHex(b"did:ont:AdVERGmipcx4rGcHJPNwFtQEinEomPbSdu")
node_index=5
pubkey_re_address=node_now_pubkey
new_publickey="025e2166e920de74fdf66da721d8c5b818a3c68296b95e636d5ba946a9fd37057c"#永远不会被注册成功的pubkey
remove_publickey="025e2166e920de74fdf66da721d8c5b818a3c68296b95e636d5ba946a9fd37057c"#永远不会被删除成功的pubkey
recoveryaddress=recoveryAddress(1,[public_key,public_key5])#绑定ontid的恢复地址
recoveryaddress_Array=[1,[public_key,public_key5]]
old_recovery_address=recoveryAddress(1,[public_key,public_key5])#绑定ontid的恢复地址
old_recovery_address_Array=[1,[public_key,public_key5]]
new_recovery_address=recoveryAddress(1,[public_key,new_publickey])#永远不会被绑定的ontid的恢复地址
new_recovery_address_Array=[1,[public_key,new_publickey]]
newontId="did:ont:AY7SgwZoQjnSC4EkAgeM2RGV2br5Wn25ws"#永远不会被注册成功的id
attribute_array=[[ByteToHex(b"testkey"),ByteToHex(b"string"),ByteToHex(b"testvalue")]]#属性组
attributes_array=[[ByteToHex(b"testkey"),ByteToHex(b"string"),ByteToHex(b"testvalue")]]#属性组
attributePath=ByteToHex(b"testkey")#与attribute对应的路�?
keyNum="1"
#################################
menualOntId="did:ont:AaidkUh6SksUZnguxdAiJKDRcbAsgmhm6c"#注册成功
menualOntId2="did:ont:AQx2TtVmDbpzfkzmJ3AHnAUT5jRgUpEm9s"#注册失败
menualPubKey1="02513a0658a4a8785ac44440c3a4cbd3eaf58b536b71b083e61e696ba3bdb5b90e"#9用，绑定public_key到ontid，会被删�?
menualPubKey2="0250fbd7d4e3871c2de455f51b8c25d66dc87055c2cbb1862c4a31e74878601ad5"#20用，绑定public_key到ontid
menualPubKey3="02a9a24d5be6c2233ad2bfd023966f8d05eb2826eba266984879b0f983b5eee218"#绑定public_key到ontid
removeKey_32="0363c6ce912e3a83b1be7b2d79655a2bf04399fe410fd9e88833a01ad533a16630"#32专用,pubkey
removeKey_35="1201034540e784ed78660fcf83fbc3187cefeb46659ff449875b67e8abff4b"#35专用，pubkey
addRecovery_38="did:ont:AYxhtBRRdDR1tAmiB5ZT29URfExYFJZ9Dc"#38专用，ontid
addRecovery_42="did:ont:AbHGZGdvjP5gS4dXwgEUesV4i5dJXVdXuJ"#42专用，ontid
addRecovery_46="did:ont:ARWHr68nCrgbvcv8YSGgPjzksHRHH43ABu"#46专用，ontid
regIDWithAttributes_61="did:ont:AWduUTRB47jhaC4RA5a75jDVotfh7Xpr9v"#61专用，ontid
regIDWithAttributes_65="did:ont:AZCFDenGDsSb8jabs5yJHKtBJHgw3aWdYr"#65专用，ontid
regIDWithAttributes_66="did:ont:AYNjFNDF4Nrh8kpuwGK6vnCm6qXjXrYPr8"#66专用，ontid
regIDWithAttributes_71="did:ont:AXyNvwCt4a4RiK8jHKq4WPVRbRfPnXvSMD"#71专用，ontid
addAttributes_74=[attributeChange(["addAttributes_74","string","addAttributes_74value"])]#74专用，attributes
addAttributes_84=[attributeChange(["addAttributes_84","string","addAttributes_84value"])]#84专用，attributes
keyNo1= "1"  #公钥序号_int_正确的序�?
keyNo2= "555"  #公钥序号_int_不存在的序号
keyNo3= "0"  #公钥序号_int_0
keyNo4= "abcdefghijklmn123542465456747"  #公钥序号_int_乱码
recoveryAddress1= recoveryAddress(1,[public_key,public_key5])  #恢复地址_Address_恢复地址（之前需没有设定恢复地址�?
recoveryAddress1_Array=[1,[public_key,public_key5]]
recoveryAddress2= recoveryAddress(1,[public_key,menualPubKey1])  #恢复地址_Address_恢复地址（之前需设定完毕恢复地址�?
recoveryAddress2_Array=[1,[public_key,menualPubKey1]]
recoveryAddress3= "abcdefghijklmn123542465456747"  #恢复地址_Address_乱码
recoveryAddress4= ""  #恢复地址_Address_留空
attribute1= [attributeChange(["attribute1","string","attribute1value"])]  #属性_AttributeArray_正常的一组属性配�?
attribute2= [attributeChange(["attribute2_1","string","attribute2_1value"]),attributeChange(["attribute2_2","int","2"]),attributeChange(["attribute2_3","bytearray",node_now_pubkey])]  #属性_AttributeArray_正常多组属性配�?
attribute3= [attributeChange(["attribute1","string"])]  #属性_AttributeArray_一组属性中有参数缺失的配置
attribute4= [attributeChange(["attribute1","123333","attribute1value"])]  #属性_AttributeArray_一组属性中有参数有问题的配�?
attribute5= ""  #属性_AttributeArray_留空
attribute6= "abcdefghijklmn123542465456747"  #属性_AttributeArray_乱码
new_recoveryAddress1= recoveryAddress(1,[public_key,menualPubKey1])  #新的恢复地址_Address_恢复地址（与之前不同�?
new_recoveryAddress1_Array=[1,[public_key,menualPubKey1]]
new_recoveryAddress2= recoveryAddress(1,[public_key,public_key5])  #新的恢复地址_Address_恢复地址（与之前相同�?
new_recoveryAddress2_Array= [1,[public_key,public_key5]]  #新的恢复地址_Address_恢复地址（与之前相同�?
new_recoveryAddress3= "abcdefghijklmn123542465456747"  #新的恢复地址_Address_乱码
new_recoveryAddress4= ""  #新的恢复地址_Address_留空
userOntId1= node_now_ontid  #用户Id_ByteArray_did:ont:账户地址(正确的id) 
userOntId2= "did:ont:2222222222222222222222222222222222"  #用户Id_ByteArray_did:ont:乱码(错误的id) 
userOntId3= "AXbevnGZBypZrcQwQfdYZxXj5zcFTtiMEA"  #用户Id_ByteArray_账户地址(错误的id) 
userOntId4= "abcdefghijklmn123542465456747"  #用户Id_ByteArray_乱码(错误的id) 
userOntId5= ""  #用户Id_ByteArray_留空
userOntId6= node_now_ontid #用户Id_ByteArray_did:ont:账户地址(已注册id) 
userOntId7= "did:ont:AM8A3i3S1Tdmcx8iSH9dY9PptYy8Y2psgb"  #用户Id_ByteArray_did:ont:账户地址(未注册id) ,从来没有注册成功�?
userOntId8= node_now_ontid  #用户id_string_did:ont:账户地址(已注册id) 
userOntId9= "did:ont:AQx2TtVmDbpzfkzmJ3AHnAUT5jRgUpEm9s"  #用户id_string_did:ont:账户地址(未注册id) 
userOntId10= "abcdefghijklmn123542465456747"  #用户id_string_乱码(错误的id) 
userOntId11= ""  #用户id_string_留空

pubkey_reAddress1= node_now_pubkey  #用户公钥或恢复地址_ByteArray_用户已注册公�?
pubkey_reAddress2= Config.NODES[node_6]["pubkey"]  #用户公钥或恢复地址_ByteArray_其他用户公钥，绑定menualOntId
pubkey_reAddress3= recoveryAddress(1,[public_key,public_key5])  #用户公钥或恢复地址_ByteArray_恢复地址（之前需设定完毕恢复地址�?
pubkey_reAddress3_Array=[1,[public_key,public_key5]]
pubkey_reAddress4= "abcdefghijklmn123542465456747"  #用户公钥或恢复地址_ByteArray_乱码
pubkey_reAddress5= ""  #用户公钥或恢复地址_ByteArray_留空
pubkey_reAddress6= "02513a0658a4a8785ac44440c3a4cbd3eaf58b536b71b083e61e696ba3bdb5b90e"  #用户公钥或恢复地址_ByteArray_即将被删除的公钥
del_pubkey1= "035a0f0774789de2abf2b0429a1584ed79cd925df25e7657d7060104318af4a6f3"  #欲删除的公钥_ByteArray_正确的公钥（已在该id注册），需要新�?
del_pubkey2= Config.NODES[node_6]["pubkey"]  #欲删除的公钥_ByteArray_正确的公钥（已在其他id注册），绑定menualOntId
del_pubkey3= "020806cfb047114862137e925f723dea6ea43edc2842c7eb277df3590facf2430c"  #欲删除的公钥_ByteArray_正确的公钥（未注册），需要新�?
del_pubkey4= "abcdefghijklmn123542465456747"  #欲删除的公钥_ByteArray_乱码
del_pubkey5= ""  #欲删除的公钥_ByteArray_留空
delAttriPath1= ByteToHex(b"testkey")  #欲删除属性的路径_ByteArray_正常要删除的属性路�?
delAttriPath2= ByteToHex(b"abcdzaxscdvf")  #欲删除属性的路径_ByteArray_错误的属性路�?
delAttriPath3= ByteToHex(b"")   #欲删除属性的路径_ByteArray_留空
delAttriPath4= ByteToHex(b"abcdefghijklmn123542465456747")  #欲删除属性的路径_ByteArray_乱码
new_publickey1= "03f0ea102bcef92e6ff4029e0d1c6afe6bbe254816b89ec9085e2675a39bf5a697"  #欲添加的新公钥_ByteArray_正确的公钥（未注册）�?3用，绑定ontid
new_publickey2= node_now_pubkey  #欲添加的新公钥_ByteArray_正确的公钥（已在该id注册�?
new_publickey3= "02d4706a689fb743c0c2a31892e624cf8b24acc020179552f1e66d0bec99b7855b"  #欲添加的新公钥_ByteArray_正确的公钥（已在其他id注册），绑定menualOntId
new_publickey4= "abcdefghijklmn123542465456747"  #欲添加的新公钥_ByteArray_乱码
new_publickey5= ""  #欲添加的新公钥_ByteArray_留空
old_recoverAddress1= recoveryAddress(1,[public_key,public_key5])  #原先的恢复地址_Address_正常的恢复地址
old_recoverAddress1_Array=[1,[public_key,public_key5]]
old_recoverAddress2= "abcdefghijklmn123542465456747"  #原先的恢复地址_Address_乱码
old_recoverAddress3= ""  #原先的恢复地址_Address_留空

####################################################
