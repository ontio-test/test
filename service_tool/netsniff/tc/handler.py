# -*- coding: utf-8 -*-
import json
import traceback
import tornado.web
from common import log, exec_cmd, get_netcard

class TCHandler(tornado.web.RequestHandler):
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
            elif m == "add":
                result['result'] = self.tcadd(p)
            elif m == "set":
                result['result'] = self.tcset(p)
            elif m == "del":
                device = self.safe_get_argument(p, "device", "eth0")
                result['result'] = self.tcdel(device)
            elif m == "show":
                device = self.safe_get_argument(p, "device", "eth0")
                result['result'] = self.tcshow(device)
        except Exception as e:
            exstr = traceback.format_exc()
            log(exstr)
            result = {"status": "fail", "exception": str(e)}
        return self.write(json.dumps(result))

    def tcadd(self, para):
        cmd = "tcset "
        if "device" not in para:
            return
        for key in para:
            if para[key]:
                cmd += "--%s %s " % (str(key), str(para[key]))
        cmd += "--add"
        return exec_cmd(cmd)

    def tcset(self, para):
        cmd = "tcset "
        if "device" not in para:
            return
        for key in para:
            if para[key]:
                cmd += "--%s %s " % (str(key), str(para[key]))
        cmd += "--overwrite"
        return exec_cmd(cmd)

    def tcdel(self, device):
        cmd = "tcdel --device %s --all" % (device)
        return exec_cmd(cmd)

    def tcshow(self, device):
        cmd = "tcshow --device %s" % (device)
        return exec_cmd(cmd)

