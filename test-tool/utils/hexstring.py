# -*- coding: utf-8 -*-
import struct
import binascii

def FileToHex(path):
    with open(path, "rb") as f:
        value = f.read()
    
    return binascii.b2a_hex(value).decode('utf-8')

def ByteToHex(bytes_value):    
    return binascii.b2a_hex(bytes_value).decode('utf-8')

def HexToByte(hexStr):
    """
    Convert a string hex byte values into a byte string. The Hex Byte values may
    or may not be space separated.
    """
    if hexStr == None or len(hexStr) == 0 :
        return bytearray(0)
    if len(hexStr) % 2 == 1:
        raise RuntimeError('IllegalArgumentException')
    result = bytearray(int(len(hexStr)/2))
    for i in range(len(result)):
        result[i] = int(hexStr[i * 2: i * 2 + 2],16)
    return result
    
    # b = toHexString("./asset.wasm")
    # print (b)

    # a = HexToByte(b)
    # for i in a:
    #     print("%x" % i)
