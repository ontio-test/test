import struct

def toHexString(value):
    hexString = ""
    
    for byte in value : 
        # print byte
        v = struct.unpack('B', byte)[0]
        hexString += str(eval(hex( v >> 4 )))
        hexString += str(eval(hex( v & 0x0f )))
    return hexString


def HexToByte( hexStr ):
    """
    Convert a string hex byte values into a byte string. The Hex Byte values may
    or may not be space separated.
    """
    if hexStr == None or len(hexStr) == 0 :
        return bytearray(0)
    if len(hexStr) % 2 == 1:
        raise RuntimeError('IllegalArgumentException')
    result = bytearray(len(hexStr)/2)
    for i in range(len(result)):
        result.append(int(hexStr[i * 2: i * 2 + 2],16))
    return result
    

if __name__ == '__main__':
    #print toHexString('test')
    print HexToByte("74657374")
