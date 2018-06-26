# -*- coding: utf-8 -*-
import gc
import json
import time
import traceback
import tornado.web
from common import log, exec_cmd, get_netcard, timestamp, LoopCmd

class SniffHandler(tornado.web.RequestHandler):
    index = 0
    packet = []
    capture = None
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    
    def safe_get_argument(self, params, name, default):
        if name in params:
            return str(params[name])
        else:
            return default

    def post(self, url=None):
        if url is not None:
            log("post:" + url)
        try:
            argument = json.loads(self.request.body)
        except:
            return self.get(url)
        m = argument['m']
        if isinstance(argument['p'], dict):
            p = argument['p']
        else:
            p = json.loads(argument['p'])
        return self.process(m, p)

    def get(self, url=None):
        if url is not None:
            log("get:" + url)
        m = self.get_argument("m")
        p = json.loads(self.get_argument("p", "{}"))
        return self.process(m, p)
        
    def process(self, m, p):
        log("method:"+json.dumps(m))
        log("para:"+json.dumps(p))
        result = {"status":"success"}
        try:
            if m == "netcardinfo":
                result['result'] = get_netcard()
            elif m == "sniff":
                interface = self.safe_get_argument(p, "interface", "eth0")
                capfilter = self.safe_get_argument(p, "capfilter", "")
                count = self.safe_get_argument(p, "count", "")
                timeout = self.safe_get_argument(p, "timeout", "")
                result['result'] = self.sniff(interface, capfilter, timeout, count)
            elif m == "startsniff":
                interface = self.safe_get_argument(p, "interface", "eth0")
                capfilter = self.safe_get_argument(p, "capfilter", "")
                self.start_sniff(interface, capfilter)
            elif m == "stopsniff":
                result['result'] = self.stop_sniff()
            elif m == "grabpacket":
                result['result'] = self.grab_packet()
        except Exception as e:
            exstr = traceback.format_exc()
            log(exstr)
            result = {"status": "fail", "exception": str(e)}
        return self.write(json.dumps(result))

    def sniff(self, interface, capfilter="", timeout="", count=""):
        cmd = "tshark -i %s -T fields -e frame.time_epoch -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport -e frame.protocols -l" % (interface)
        if capfilter:
            cmd += ' -f "%s"' % (capfilter)
        if timeout:
            cmd += " -a duration:%s" % (timeout)
        if count:
            cmd += " -c %s" % (count)
        if not timeout and not count:
            cmd += " -c 1"
        output = exec_cmd(cmd)
        result = self.parse_result(output.split("\n"))
        return result

    def parse_result(self, lines):
        result = []
        #去掉首尾两行非包信息
        lines = lines[1:-1]
        for line in lines:
            time_epoch, src_ip, dst_ip, tcp_src_port, tcp_dst_port, udp_src_port, udp_dst_port, protocol = line.split("\t")
            result.append(
                          {
                           "time":timestamp(float(time_epoch)),
                           "src_ip":src_ip,
                           "dst_ip":dst_ip,
                           "tcp_src_port":tcp_src_port,
                           "tcp_dst_port":tcp_dst_port,
                           "udp_src_port":udp_src_port,
                           "udp_dst_port":udp_dst_port,
                           "protocol":protocol,
                           }
                          )
        return result

    def sniff_callback(self, line):
        try:
            time_epoch, src_ip, dst_ip, tcp_src_port, tcp_dst_port, udp_src_port, udp_dst_port, protocol = line.split("\t")
            SniffHandler.packet.append(
                                       {
                                       "time":timestamp(float(time_epoch)),
                                       "src_ip":src_ip,
                                       "dst_ip":dst_ip,
                                       "tcp_src_port":tcp_src_port,
                                       "tcp_dst_port":tcp_dst_port,
                                       "udp_src_port":udp_src_port,
                                       "udp_dst_port":udp_dst_port,
                                       "protocol":protocol,
                                       }
                                       )
        except:
            pass

    def start_sniff(self, interface, capfilter=""):
        cmd = "tshark -i %s -T fields -e frame.time_epoch -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport -e frame.protocols -l -a duration:60" % (interface)
        if capfilter:
            cmd += ' -f "%s"' % (capfilter)
        print(cmd)
        SniffHandler.capture = LoopCmd(cmd, self.sniff_callback)
        SniffHandler.packet = []
        SniffHandler.index = 0
        SniffHandler.capture.start()

    def stop_sniff(self):
        result = []
        if SniffHandler.capture:
            result = SniffHandler.packet[:]
            SniffHandler.capture.stop()
            SniffHandler.capture = None
            SniffHandler.packet = []
            SniffHandler.index = 0
        return result

    def grab_packet(self):
        count = 0
        while len(SniffHandler.packet) <= SniffHandler.index:
            time.sleep(0.1)
            count += 1
            if count > 50:
                return None
        SniffHandler.index += 1
        return SniffHandler.packet[SniffHandler.index-1]

