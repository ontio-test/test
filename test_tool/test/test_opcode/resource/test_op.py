from boa.interop.Neo.Runtime import Log, Notify
from boa.interop.System.ExecutionEngine import GetScriptContainer, GetExecutingScriptHash
from boa.interop.Neo.Transaction import *
from boa.interop.Neo.Blockchain import GetHeight, GetHeader
from boa.interop.Neo.Action import RegisterAction
from boa.interop.Neo.Runtime import GetTrigger, CheckWitness
from boa.interop.Neo.TriggerType import Application, Verification
from boa.interop.Neo.Output import GetScriptHash, GetValue, GetAssetId
from boa.interop.Neo.Storage import GetContext, Get, Put, Delete
from boa.interop.Neo.Header import GetTimestamp, GetNextConsensus

def Main(operation, args):
    
    if operation == 'add':
        return Add(1, 1)
    
    if operation == 'sub':
        return Sub(1, 0)
    
    if operation == 'Push0':
        return Push0()
    
    if operation == 'PushBytes1':
        return PushBytes1()
    
    if operation == 'PushBytes75':
        return PushBytes75()
    
    if operation == 'Pushdata1':
        return Pushdata1()
    
    if operation == 'PushM1':
        return PushM1()
    
    if operation == 'PushN':
        return PushN(1)
    
    if operation == 'Nop':
        return Nop()
    
    if operation == 'Jmpif':
        return Jmpif(1, 2)
    
    if operation == 'Jmpifnot':
        return Jmpifnot(1, 2)
    
    if operation == 'Call':
        return Call()
    
    if operation == 'Syscall':
        return Syscall()
    
    if operation == 'Toaltstack':
        return Toaltstack()
    
    if operation == 'Fromaltstack':
        return Fromaltstack()
    
    if operation == 'Roll':
        return Roll()
    
    if operation == 'Drop':
        return Drop()
    
    if operation == 'Dup':
        return Dup()
    
    if operation == 'Inc':
        return Inc(1)
    
    if operation == 'Dec':
        return Dec(1)
    
    if operation == 'Negate':
        return Negate(1)
    
    if operation == 'Abs':
        return Abs(1)
    
    if operation == 'Not':
        return Not(1)
    
    if operation == 'Nz':
        return Nz(1)
    
    if operation == 'Mul':
        return Mul(1, 1)
    
    if operation == 'Div':
        return Div(1, 1)
    
    if operation == 'Mod':
        return Mod(1, 1)
    
    if operation == 'Shl':
        return Shl(1, 1)
    
    if operation == 'Shr':
        return Shr(1, 1)
    
    if operation == 'BoolAnd':
        return BoolAnd(1, 1)
    
    if operation == 'BoolOr':
        return BoolOr(1, 1)
    
    if operation == 'NumeQual':
        return NumeQual(1, 1)
    
    if operation == 'NumNotEqual':
        return NumNotEqual(1, 2)
    
    if operation == 'Lt':
        return Lt(1, 1)
    
    if operation == 'Gt':
        return Gt(1, 1)
    
    if operation == 'Lte':
        return Lte(1, 1)
    
    if operation == 'Gte':
        return Gte(1, 1)
    
    if operation == 'Min':
        return Min(1, 1)
    
    if operation == 'Max':
        return Max(1, 1)
    
    if operation == 'Within':
        return Within(1, 1, 1)
    
    if operation == 'And':
        return And(1, 1)
    
    if operation == 'Or':
        return Or(1, 1)
    
    if operation == 'Xor':
        return Xor(0, 1)
    
    if operation == 'Invert':
        return Invert(1)
    
    if operation == 'CAT':
        return CAT()
    
    if operation == 'Left':
        return Left()
    
    if operation == 'SIZE':
        return SIZE()
    
    if operation == 'ARRAYSIZE':
        return ARRAYSIZE()
    
    if operation == 'PACK':
        return PACK()
    
    if operation == 'PICKITEM':
        return PICKITEM()
    
    if operation == 'SETITEM':
        return SETITEM()
    
    if operation == 'NEWARRAY':
        return NEWARRAY()
    
    if operation == 'NEWSTRUCT':
        return NEWSTRUCT()
    
    if operation == 'APPEND':
        return APPEND()
    
    if operation == 'REVERSE':
        return REVERSE()
    
    if operation == 'SHA1':
        return SHA1()
    
    if operation == 'SHA256':
        return SHA256()
    
    if operation == 'HASH160':
        return HASH160()
    
    if operation == 'HASH256':
        return HASH256()
    
    return False


# PUSH0/PUSHF
def Push0():
    a = 0
    return a

# PUSHBYTES1
def PushBytes1():
    a = 20
    return a

# PUSHBYTES75
def PushBytes75():
    a = '11111111111111111111111111111111111111111111111111111111111111111111111111'
    return a

# PUSHDATA1
def Pushdata1():
    a = "1111111111111111111111111111111111111111111111111111111111111111111111111111"
    return a

# PUSHM1
def PushM1():
    a = -1
    return a

# PUSHN(n is between [1, 16])
def PushN(n):
    a = n
    return a

# NOP
def Nop():
    if True:
        pass
    return 1

# JMPIF
def Jmpif(a, b):
    if a == b:
        pass
    else:
        return 1
    return 1

# JMPIFNOT
def Jmpifnot(a, b):
    if not a == b:
        pass
    else:
        return 1
    return 1

# CALL
def Call():
    return p()

def p():
    return 1

# SYSCALL
def Syscall():
    return 1

# TOALTSTACK
def Toaltstack():
    a = 1
    b = 1
    return a 

# FROMALTSTACK
def Fromaltstack():
    a = 1
    b = 1
    return a 

# ROLL
def Roll():
    a = 1
    b = 2
    del a
    return 1

# DROP
def Drop():
    a = 1
    b = 2
    del a
    return 1

# DUP
def Dup():
    a = 1
    b = 2
    c = 1
    del a
    return 1

# INC
def Inc(a):
    return a + 1
    
# DEC
def Dec(a):
    return a - 1

# NEGATE
def Negate(a):
    return -a

# ABS
def Abs(a):
    return abs(a)

# NOT
def Not(a):
    return not a

# NZ
def Nz(a):
    return a != 0

# ADD
def Add(a, b):
    return a + b
    
# SUB
def Sub(a, b):
    return a - b
    
# MUL
def Mul(a, b):
    return a * b

# DIV
def Div(a, b):
    return a / b
    
# MOD
def Mod(a, b):
    return a % b
    
# SHL
def Shl(X, n):
    return X << n
    
# SHR
def Shr(X, n):
    return X >> n

# BOOLAND
def BoolAnd(a, b):
    return a and b

# BOOLOR
def BoolOr(a, b):
    return a or b
    
# NUMEQUAL
def NumeQual(a, b):
    return a == b
    
# NUMNOTEQUAL
def NumNotEqual(a, b):
    return a != b
    
# LT
def Lt(a, b):
    return a < b

# GT
def Gt(a, b):
    return a > b
    
# LTE
def Lte(a, b):
    return a <= b
    
# GTE    
def Gte(a, b):
    return a >= b
    
# MIN
def Min(a, b):
    return min(a, b)
    
# MAX
def Max(a, b):
    return max(a, b)
  
# WITHIN
def Within(X, a, b):
    return X >= a and X < b


# INVERT
def Invert(a):
    return ~a

# AND
def And(a, b):
    return a & b

# OR
def Or(a, b):
    return a | b

# XOR
def Xor(a, b):
    return a ^ b

# CAT
def CAT():
    a = 'test1'
    b = 'test2'
    return a + b
    
# Left
def Left():
    a = 'test1'
    b = 'test2'
    return a < b
    
# SIZE
def SIZE():
    str = 'aaaaaaa'
    return len(str)

# ARRAYSIZE
def ARRAYSIZE():
    array = [0,1,2,3,4,5]
    return len(array)
    
# PACK
def PACK():
    array = [0,1,2,3,4,5]
    return array
    
# PICKITEM
def PICKITEM():
    array = [0,1,2,3,4,5]
    return array[1]
    
# SETITEM
def SETITEM():
    array = [0,1,2,3,4,5]
    array[1] = 3
    return array[1]

# NEWARRAY
def NEWARRAY():
    array = [0,1,2,3,4,5]
    return array
    
# NEWSTRUCT
def NEWSTRUCT():
    d1 = {'a': '1', 'c': 'd'}
    return d1
    
# APPEND
def APPEND():
    array = [0,1,2,3,4,5]
    array.append(9)
    return array
    
# REVERSE
def REVERSE():
    arr = [1,2,3]
    arr.reverse()
    return arr

# SHA1
def SHA1():
    c='12369'
    return sha1(c)
    
# SHA256
def SHA256():
    c='12369'
    return sha256(c)
    
# HASH160
def HASH160():
    c='12369'
    return hash160(c)
    
# HASH256
def HASH256():
    c='12369'
    return hash256(c)


