# -*- coding: utf-8 -*-
import sys
import tornado.ioloop
import tornado.web
from tornado import websocket
from tc.handler import TCHandler
from sniff.handler import SniffHandler
from common import log

APP = None
CONNECTSET = set()

class NoCasheFileHandler(tornado.web.StaticFileHandler):  
    def set_extra_headers(self, path):
        self.set_header("Cache-control", "no-cache")

class WSHandler(websocket.WebSocketHandler):
    def open(self):
        global CONNECTSET
        CONNECTSET.add(self)

    def on_message(self, message):
        log("get:" + message)

    def on_close(self):
        log("disconnect:" + self.request.remote_ip)
        CONNECTSET.remove(self)

def noticeResult(notice):
    log("send:" + str(notice))
    for client in CONNECTSET:
        client.write_message(notice)

def make_app():
    global APP
    APP = tornado.web.Application([
        (r"/ws", WSHandler),
        (r"/cscservice/tc", TCHandler),
        (r"/cscservice/sniff", SniffHandler),
        (r"/cscservice/static/(.*)", NoCasheFileHandler, {"path": "static"})
    ])

def startServer(port):
    APP.listen(int(port))
    log("Server is running on " + str(port))
    tornado.ioloop.IOLoop.instance().start()

def stopServer():
    tornado.ioloop.IOLoop.instance().stop()

def main(port):
    make_app()
    startServer(port)

if __name__ == "__main__":
    port = 10001
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    main(port)

