# -*- coding:utf-8 -*-
import re
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys
import getopt
import time
import requests
import subprocess

sys.path.append('..')

import utils.base
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from test_api import *

def set_premise(neo_path):
    result = False
    contract_address = None
    adminOntID = ByteToHex(b"TA6CtF4hZwqAmXdc6opa4B79fRS17YJjX5")
    roleA_hex = ByteToHex(b"roleA")
    roleB_hex = ByteToHex(b"roleB")

    ontID_A = ByteToHex(b"did:ont:TA7TSQ5aJcA8sU5MpqJNyTG1r13AQYLYpR")
    ontID_B = ByteToHex(b"did:ont:TA82XAPQXtVzncQMczcY9SVytjb2VuTQy4") 
    ontID_C = ByteToHex(b"did:ont:TA6CtF4hZwqAmXdc6opa4B79fRS17YJjX5")

    contract_address = deploy_contract(neo_path)
    (result, response) = init_admin(contract_address, adminOntID)
    if not result:
        raise("init_admin error")
    
    (result, response) = bind_role_function(contract_address, adminOntID, roleA_hex, ["A", "C"])
    if not result:
        raise("bind_role_function error [1]")
    
    (result, response) = bind_role_function(contract_address, adminOntID, roleB_hex , ["B", "C"])
    if not result:
        raise("bind_role_function error [2]")
    if result:
        return (contract_address, adminOntID, roleA_hex, roleB_hex, ontID_A, ontID_B, ontID_C)
    else:
        raise("set_premise error")

            