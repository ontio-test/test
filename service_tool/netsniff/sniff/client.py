# -*- coding: utf-8 -*-
"""The Console Log Client implementation"""
import sys
sys.path.append('./')
sys.path.append('../')
import json
from requests import post
from common import log, exec_cmd

class SniffClient:
    """
    Console Log Client
    """

    def __init__(self, host='localhost', port='10001'):
        self.url = "http://" + host + ":" + port + "/cscservice/sniff"

    def sniff_api(self, method, paras):
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
        result = self.sniff_api(method, paras)
        if result['status'] == "success":
            return result['result']
        else:
            return ""

    def sniff(self, interface, capfilter="", timeout="", count=""):
        method = "sniff"
        paras = {"interface":interface,
                 "capfilter":capfilter,
                 "timeout":timeout,
                 "count":count
                 }
        result = self.sniff_api(method, paras)
        if result['status'] == "success":
            return result['result']
        else:
            return []

    def start_sniff(self, interface, capfilter=""):
        method = "startsniff"
        paras = {"interface":interface,
                 "capfilter":capfilter
                 }
        self.sniff_api(method, paras)

    def stop_sniff(self):
        method = "stopsniff"
        paras = {}
        result = self.sniff_api(method, paras)
        if result['status'] == "success":
            return result['result']
        else:
            return []

    def grab_packet(self):
        method = "grabpacket"
        paras = {}
        result = self.sniff_api(method, paras)
        if result['status'] == "success":
            return result['result']
        else:
            return None

if __name__ == "__main__":
    target_ip = "10.0.0.46"
    sc = SniffClient(target_ip, "10001")
    log(sc.get_netcard_info())
    
    result = sc.sniff("eth0", timeout = 5)
    log(json.dumps(result))
    result = sc.sniff("eth0", count = 5)
    log(json.dumps(result))
    sc.start_sniff("eth0", "icmp")
    exec_cmd("ping "+target_ip+" -c 5")
    packet = sc.grab_packet()
    while packet:
        log(json.dumps(packet))
        packet = sc.grab_packet()
    result = sc.stop_sniff()
    log(result)

    
