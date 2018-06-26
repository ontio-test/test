# -*- coding: utf-8 -*-
"""The Console Log Client implementation"""
import sys
sys.path.append('./')
sys.path.append('../')
import json
import time
from requests import post
from common import exec_cmd
from common import log

class TCClient:
    """
    Console Log Client
    """

    def __init__(self, host='localhost', port='10001'):
        self.url = "http://" + host + ":" + port + "/cscservice/tc"

    def tc_api(self, method, paras):
        data = {"m":method, "p":paras}
        response = post(self.url, json=data)
        if response.status_code == 200:
            response.encoding = "utf-8"
            return json.loads(response.text)
        else:
            return {"status": "fail"}

    def get_netcard_info(self):
        method = "netcardinfo"
        paras = {}
        result = self.tc_api(method, paras)
        if result['status'] == "success":
            return result['result']
        else:
            return ""

    def tc_add(self, device, dst_network="", dst_port="", src_network="", src_port="", exclude_dst_network="", exclude_dst_port="", exclude_src_network="", exclude_src_port="", rate="", delay="", delay_distro="", loss="", corruption="", duplicate="", reordering="", direction=""):
        method = "add"
        paras = {"device":device,
                 "dst-network":dst_network,
                 "dst-port":dst_port,
                 "src-network":src_network,
                 "src-port":src_port,
                 "exclude-dst-network":exclude_dst_network,
                 "exclude-dst-port":exclude_dst_port,
                 "exclude-src-network":exclude_src_network,
                 "exclude-src-port":exclude_src_port,
                 "rate":rate,
                 "delay":delay,
                 "delay_distro":delay_distro,
                 "loss":loss,
                 "corruption":corruption,
                 "duplicate":duplicate,
                 "reordering":reordering,
                 "direction":direction
                 }
        result = self.tc_api(method, paras)
        if result['status'] == "success":
            return result['result']
        else:
            return ""

    def tc_set(self, device, dst_network="", dst_port="", src_network="", src_port="", exclude_dst_network="", exclude_dst_port="", exclude_src_network="", exclude_src_port="", rate="", delay="", delay_distro="", loss="", corruption="", duplicate="", reordering="", direction=""):
        method = "set"
        paras = {"device":device,
                 "dst-network":dst_network,
                 "dst-port":dst_port,
                 "src-network":src_network,
                 "src-port":src_port,
                 "exclude-dst-network":exclude_dst_network,
                 "exclude-dst-port":exclude_dst_port,
                 "exclude-src-network":exclude_src_network,
                 "exclude-src-port":exclude_src_port,
                 "rate":rate,
                 "delay":delay,
                 "delay_distro":delay_distro,
                 "loss":loss,
                 "corruption":corruption,
                 "duplicate":duplicate,
                 "reordering":reordering,
                 "direction":direction
                 }
        result = self.tc_api(method, paras)
        if result['status'] == "success":
            return result['result']
        else:
            return ""
        
    def tc_del(self, device):
        method = "del"
        paras = {"device":device}
        result = self.tc_api(method, paras)
        if result['status'] == "success":
            return result['result']
        else:
            return ""

    def tc_show(self, device):
        method = "show"
        paras = {"device":device}
        result = self.tc_api(method, paras)
        if result['status'] == "success":
            return result['result']
        else:
            return ""
        
if __name__ == "__main__":
    target_ip = "10.0.0.89"
    local_ip = "10.0.0.61"
    tcc = TCClient(target_ip, "10001")
    log(tcc.get_netcard_info())
    
    tcc.tc_set("eth0", dst_network=local_ip, delay="100ms")
    log(tcc.tc_show("eth0"))
    log(exec_cmd("ping "+target_ip+" -c 5"))
    tcc.tc_set("eth0", src_network=local_ip, delay="100ms", direction="incoming")
    log(tcc.tc_show("eth0"))
    log(exec_cmd("ping "+target_ip+" -c 5"))
    tcc.tc_set("eth0", dst_network=local_ip, loss="20")
    log(tcc.tc_show("eth0"))
    time.sleep(5)
    log(exec_cmd("ping "+target_ip+" -c 10"))
    tcc.tc_del("eth0")
    log(tcc.tc_show("eth0"))
