# -*- coding: utf-8 -*-

import requests
import json
import os
from utils.config import Config
from utils.baseapi import BaseApi

class RPC(BaseApi):
    def __init__(self):
        BaseApi.TYPE = "rpc"
        BaseApi.CONFIG_PATH = "tasks/rpc"

    def connnet(self, request):
        response = requests.post(Config.RPC_URL, data=json.dumps(request), headers=Config.RPC_HEADERS)
        return response.json()