import leveldb
import hashlib
import socket
import urllib

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher
from config import Configure

def get_db_md5(db_name):
  db = leveldb.LevelDB(db_name)
  md5 = hashlib.md5()
  iter = db.RangeIter()
  
  for (key, value) in iter:
    md5.update(key)
    md5.update(value)
  
  return md5.hexdigest()

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


@dispatcher.add_method
def get_states_md5(**kwargs):
	"""
	Get md5 value of leveldb named states
	"""
	return get_db_md5(Configure.LEVELDB_PATH_STATES)

@dispatcher.add_method
def get_block_md5(**kwargs):
	"""
	Get md5 value of leveldb named block
	"""
	return get_db_md5(Configure.LEVELDB_PATH_BLOCK)

@dispatcher.add_method
def get_ledgerevent_md5(**kwargs):
	"""
	Get md5 value of leveldb named ledgerevent
	"""
	return get_db_md5(Configure.LEVELDB_PATH_LEDGEREVENT)


@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["get_states_md5"] = get_states_md5
    dispatcher["get_block_md5"] = get_block_md5
    dispatcher["get_ledgerevent_md5"] = get_ledgerevent_md5
    

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple(get_host_ip(), config.PORT, application)
