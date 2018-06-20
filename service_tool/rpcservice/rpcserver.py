# -*- coding: utf-8 -*-

import leveldb
import hashlib
import socket
import urllib
import json
import requests
import os
import setproctitle

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher
from config import Configure as config

setproctitle.setproctitle("test_service")

def get_db_md5(db_name):
  print("---------------------------------")
  db = leveldb.LevelDB(db_name)
  md5 = hashlib.md5()
  iter = db.RangeIter()
  
  i = 0
  for (key, value) in iter:
    if key[0] in [0x03, 0x04, 0x05, 0x07, 0x08]:
      md5.update(key)
      md5.update(value)
      print(i)
      print(key[0])
      print(key)
      print(value)
      i = i + 1

  return md5.hexdigest()

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

def con_cli(request):
  try:
    url = "http://127.0.0.1:20000/cli"
    response = requests.post(url, data=json.dumps(request), headers={'content-type': 'application/json'})
    return response.json()
  except Exception as e:
    print(e)
    return json.loads("{\"Desc\": \"Connection Error\", \"Error\": \"Connection Error\"}")


@dispatcher.add_method
def get_states_md5(**kwargs):
	"""
	Get md5 value of leveldb named states
	"""
	return get_db_md5(config.NODE_PATH + "/Chain/states")

@dispatcher.add_method
def get_block_md5(**kwargs):
	"""
	Get md5 value of leveldb named block
	"""
	return get_db_md5(config.NODE_PATH + "/Chain/block")

@dispatcher.add_method
def get_ledgerevent_md5(**kwargs):
	"""
	Get md5 value of leveldb named ledgerevent
	"""
	return get_db_md5(config.NODE_PATH + "/Chain/ledgerevent")

@dispatcher.add_method
def siginvoketx(**kwargs):
  print("recive siginvoketx")
  request = kwargs
  return con_cli(request)

@dispatcher.add_method
def stop_node(**kwargs):
  os.popen("killall -9 ontology")
  return True

@dispatcher.add_method
def replace_node_config(**kwargs):
  file = open(config.NODE_PATH + "/" + "config.json", "w")
  file.write(json.dumps(kwargs,  indent = 4))
  file.close()
  return True

@dispatcher.add_method
def transfer_ont(**kwargs):
  if os.path.exists(".tmp"):
    os.remove(".tmp")

  _from = kwargs["from"]
  to = kwargs["to"]
  amount = kwargs["amount"]

  cmd = "cd " + config.NODE_PATH + "\n";
  cmd = cmd + "echo 123456|" + config.NODE_PATH + "/ontology asset transfer --from=\"" + str(_from) + "\" " + "--to=\"" + str(to) + "\"" + " --amount=\"" + str(amount) + "\" > .tmp"
  print(cmd)
  os.system(cmd)

  tmpfile = open(config.NODE_PATH + "/.tmp", "r+")  # 打开文件
  contents = tmpfile.readlines()
  return contents

@dispatcher.add_method
def withdrawong(**kwargs):
  if os.path.exists(".tmp"):
    os.remove(".tmp")

  cmd = "cd " + config.NODE_PATH + "\n";
  cmd = cmd + "echo 123456|" + config.NODE_PATH + "/ontology asset withdrawong 1 > .tmp"

  print(cmd)
  os.system(cmd)

  tmpfile = open(config.NODE_PATH + "/.tmp", "r+")  # 打开文件
  contents = tmpfile.readlines()

  return contents

@dispatcher.add_method
def start_node(**kwargs):
  os.system("rm -rf " + config.NODE_PATH + "/Chain")
  clear_chain=None
  clear_log=None
  node_args=None
  if "clear_chain" in kwargs:
    clear_chain = kwargs["clear_chain"]
  if "clear_log" in kwargs:
    clear_log = kwargs["clear_log"]
  if "node_args" in kwargs:
    node_args = kwargs["node_args"]

  if clear_chain:
    os.system("rm -rf " + config.NODE_PATH + "/Chain")
  if clear_log:
    os.system("rm -rf " + config.NODE_PATH + "/Log")

  if node_args:
    cmd = "cd " + config.NODE_PATH + "\n";
    cmd = cmd + "echo 123456|" + config.NODE_PATH + "/ontology -w=\"" + config.NODE_PATH + "/wallet.dat\" --config=\"" + config.NODE_PATH + "/config.json\" " + node_args + " &"
    print(cmd)
    os.system(cmd)
  else:
    cmd = "cd " + config.NODE_PATH + "\n";
    cmd = cmd + "echo 123456|" + config.NODE_PATH + "/ontology -w=\"" + config.NODE_PATH + "/wallet.dat\" --config=\"" + config.NODE_PATH + "/config.json\" " + " &"
    print(cmd)
    os.system(cmd)

  return True

@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["get_states_md5"] = get_states_md5
    dispatcher["get_block_md5"] = get_block_md5
    dispatcher["get_ledgerevent_md5"] = get_ledgerevent_md5
    dispatcher["siginvoketx"] = siginvoketx
    dispatcher["start_node"] = start_node
    dispatcher["stop_node"] = stop_node
    dispatcher["replace_node_config"] = replace_node_config
    dispatcher["transfer"] = transfer_ont
    dispatcher["withdrawong"] = withdrawong

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple(get_host_ip(), config.PORT, application)
