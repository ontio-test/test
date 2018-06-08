# -*- coding: utf-8 -*-
import os
import time
import psutil
import signal
import threading
from subprocess import Popen, PIPE
from os import kill


def log(text):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print("[%s] %s" % (timestamp, text))

def exec_cmd(cmd):
    log(cmd)
    r = os.popen(cmd)  
    text = r.read()  
    r.close()  
    return text

def get_netcard():  
    netcard_info = []
    info = psutil.net_if_addrs()
    for k,v in info.items():
        for item in v:
            if item[0] == 2 and not item[1]=='127.0.0.1':
                netcard_info.append((k,item[1]))
    return netcard_info

def timestamp(time_epoch):
    mseconds = time_epoch - int(time_epoch)
    timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_epoch))
    mstr = "%.3f" % (mseconds)
    timestr = timestr + mstr[1:]
    return timestr

class LoopCmd(threading.Thread):
    def __init__(self, cmd, callback):
        threading.Thread.__init__(self)
        self.p = Popen(cmd, shell=True, stdout=PIPE)
        self.callback = callback
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            line = self.p.stdout.readline()
            try:
                line = str(line, encoding="utf-8").strip()
            except:
                line = str(line).strip()
            if line:
                self.callback(line)
            time.sleep(0.01)
        kill(self.p.pid, signal.SIGTERM)
        self.p = None

    def stop(self):
        self.running = False

def test(line):
    output.append(line)

if __name__ == "__main__":
    output = []
    loopcmd = LoopCmd("tshark -i eth0 -f 'tcp' -T fields -e frame.time_epoch -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -l", test)
    loopcmd.start()
    time.sleep(10)
    loopcmd.stop()
    print(str(output))
