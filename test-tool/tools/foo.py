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

regIDWithPublicKey(0)
regIDWithPublicKey(1)
regIDWithPublicKey(2)
regIDWithPublicKey(3)
regIDWithPublicKey(4)
regIDWithPublicKey(5)
regIDWithPublicKey(6)

print(json.dumps(transfer_ont(0, 0, 100000)))
time.sleep(5)
print(json.dumps(withdrawong(0)))
time.sleep(1)
print(json.dumps(transfer_ont(1, 1, 100000)))
time.sleep(5)
print(json.dumps(withdrawong(1)))
time.sleep(1)
print(json.dumps(transfer_ont(2, 2, 100000)))
time.sleep(5)
print(json.dumps(withdrawong(2)))
time.sleep(1)
print(json.dumps(transfer_ont(3, 3, 100000)))
time.sleep(5)
print(json.dumps(withdrawong(3)))
time.sleep(1)
print(json.dumps(transfer_ont(4, 4, 100000)))
time.sleep(5)
print(json.dumps(withdrawong(4)))
time.sleep(1)
print(json.dumps(transfer_ont(5, 5, 100000)))
time.sleep(5)
print(json.dumps(withdrawong(5)))
time.sleep(1)
print(json.dumps(transfer_ont(6, 6, 100000)))
time.sleep(5)
print(json.dumps(withdrawong(6)))
