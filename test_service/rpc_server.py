# -*- coding: utf-8 -*-
import leveldb
import hashlib
import pyjsonrpc
import socket

from config import Configure

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

class RequestHandler(pyjsonrpc.HttpRequestHandler):
    
    def get_db_md5(self, db_name):
        db = leveldb.LevelDB(db_name)
        md5 = hashlib.md5()
        iter = db.RangeIter()

        for (key, value) in iter:
            md5.update(key)
            md5.update(value)

        return md5.hexdigest()


    @pyjsonrpc.rpcmethod
    def get_states_md5(self):
        """
        Get md5 value of leveldb named states
        """
        return self.get_db_md5(Configure.LEVELDB_PATH_STATES)

    @pyjsonrpc.rpcmethod
    def get_block_md5(self):
        """
        Get md5 value of leveldb named block
        """
        return self.get_db_md5(Configure.LEVELDB_PATH_BLOCK)

    @pyjsonrpc.rpcmethod
    def get_ledgerevent_md5(self):
        """
        Get md5 value of leveldb named ledgerevent
        """
        return self.get_db_md5(Configure.LEVELDB_PATH_LEDGEREVENT)

local_ipaddress = get_host_ip()

# Threading HTTP-Server
http_server = pyjsonrpc.ThreadingHttpServer(
    server_address = (local_ipaddress, Configure.PORT),
    RequestHandlerClass = RequestHandler
)
print "Starting HTTP server ..."
print "URL: http://"+local_ipaddress+":"+str(Configure.PORT)
http_server.serve_forever()

