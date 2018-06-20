# -*- coding: utf-8 -*-
import sys, getopt
import time
sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.commonapi import *
from utils.contractapi import *
from utils.logger import LoggerInstance
import base58

#regIDWithPublicKey(0)
#regIDWithPublicKey(1)
#regIDWithPublicKey(2)
#regIDWithPublicKey(3)
#regIDWithPublicKey(4)
#regIDWithPublicKey(5)
#regIDWithPublicKey(6)
#print(ByteToHex(base58.b58decode(b'AepFgMk9A4m3kTJYs9fhqMMQrKfL9VR7nx')))
print(json.dumps(transfer_ont(3, Config.SERVICES[3]["address"], Config.SERVICES[4]["address"], 1000000), indent = 4))
time.sleep(5)
print(json.dumps(withdrawong(3)))