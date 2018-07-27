# -*- coding: utf-8 -*-

import leveldb
import hashlib
import socket
import urllib
import json
import requests
import os
import setproctitle
import stat
import subprocess
import time

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher
from config import Configure as config

setproctitle.setproctitle("test_service")


def calc_md5_for_file(_file):
  md5 = hashlib.md5()
  with open(_file, "rb") as f:
    md5.update(f.read())
  return md5.hexdigest()

def calc_md5_for_folder(folder):
  md5 = hashlib.md5()
  files = os.listdir(folder)
  files.sort()
  for _file in files:
    print (os.path.join(folder, _file))
    md5.update(str(calc_md5_for_file(os.path.join(folder, _file))).encode())
  return md5.hexdigest()

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
  os.popen("killall -9 ontology-bft_1")
  os.popen("killall -9 ontology-bft_2")
  os.popen("killall -9 ontology-bft_3")
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
  price = kwargs["price"]

  cmd = "cd " + config.NODE_PATH + "\n";
  cmd = cmd + "echo 123456|" + config.NODE_PATH + "/ontology asset transfer --asset=ont --from=\"" + str(_from) + "\" " + "--to=\"" + str(to) + "\"" + " --amount=\"" + str(amount) + "\""
  if price > 0:
    cmd = cmd + " --gasprice=" + str(price)
  cmd = cmd + " > .tmp"
  print(cmd)
  os.system(cmd)

  tmpfile = open(config.NODE_PATH + "/.tmp", "r+")  # 打开文件
  contents = tmpfile.readlines()
  return contents

@dispatcher.add_method
def transfer_ong(**kwargs):
  if os.path.exists(".tmp"):
    os.remove(".tmp")

  _from = kwargs["from"]
  to = kwargs["to"]
  amount = kwargs["amount"]
  price = kwargs["price"]

  cmd = "cd " + config.NODE_PATH + "\n";
  cmd = cmd + "echo 123456|" + config.NODE_PATH + "/ontology asset transfer --asset=ong  --from=\"" + str(_from) + "\" " + "--to=\"" + str(to) + "\"" + " --amount=\"" + str(amount) + "\""
  if price > 0:
    cmd = cmd + " --gasprice=" + str(price)
  cmd = cmd + " > .tmp"
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
  program_name = "ontology"
  config_file = "config.json"
  if "clear_chain" in kwargs:
    clear_chain = kwargs["clear_chain"]
  if "clear_log" in kwargs:
    clear_log = kwargs["clear_log"]

  if "name" in kwargs:
    program_name = kwargs["name"]

  if "config" in kwargs:
    config_file = kwargs["config"]

  if "node_args" in kwargs:
    node_args = kwargs["node_args"]

  if clear_chain:
    os.system("rm -rf " + config.NODE_PATH + "/Chain")
  if clear_log:
    os.system("rm -rf " + config.NODE_PATH + "/Log")

  if node_args:
    cmd = "cd " + config.NODE_PATH + "\n";
    cmd = cmd + "echo 123456|" + config.NODE_PATH + "/" + program_name + " -w=\"" + config.NODE_PATH + "/wallet.dat\" --config=\"" + config.NODE_PATH + "/" + config_file + "\" " + node_args + " &"
    print(cmd)
    os.system(cmd)
  else:
    cmd = "cd " + config.NODE_PATH + "\n";
    cmd = cmd + "echo 123456|" + config.NODE_PATH + "/" + program_name + " -w=\"" + config.NODE_PATH + "/wallet.dat\" --config=\"" + config.NODE_PATH + "/" + config_file +  "\" " + " &"
    print(cmd)
    os.system(cmd)

  return True

@dispatcher.add_method
def exec_cmd(**kwargs):
  cmd = ""
  if "cmd" in kwargs:
    cmd = kwargs["cmd"]
  os.system(cmd)
  return True

@dispatcher.add_method
def stop_sigsvr(**kwargs):
  os.popen("killall -9 sigsvr-linux")
  return True

@dispatcher.add_method
def start_sigsvr(**kwargs):
  program_name = "sigsvr-linux"
  if "wallet" in kwargs:
    wallet = kwargs["wallet"]
  cmd = "cd " + config.NODE_PATH + "\n"
  cmd = cmd + "echo 123456|" + config.NODE_PATH + "/" + program_name + " -w=\"" + wallet + "\" &"
  print(cmd)
  os.system(cmd)
  return True

@dispatcher.add_method
def heart_beat(**kwargs):
  return "I'm OK."

@dispatcher.add_method
def check_xmode_ontology(**kwargs):
  ontology_path = config.NODE_PATH + "/ontology"
  if not os.path.exists(ontology_path):
    return ontology_path + " doesnot exists."
  
  if not os.access(ontology_path, os.X_OK):
    # chmod 777
    os.chmod(ontology_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
  
  return True

@dispatcher.add_method
def check_xmode_sigsvr(**kwargs):
  sigsvr_path = None
  for sigsvr in ["sigsvr", "sigsvr-linux"]:
    sigsvr_path = config.NODE_PATH + "/" + sigsvr
    if os.path.exists(sigsvr_path):
      break
    else:
      sigsvr_path = None

  if not sigsvr_path:
    return "sigsvr doesnot exists."
  
  if not os.access(sigsvr_path, os.X_OK):
    # chmod 777
    os.chmod(sigsvr_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
  
  return True

@dispatcher.add_method
def check_xmode_tools(**kwargs):
  tools_path = None
  for tools in ["base58ToAddress"]:
    tools_path = config.TEST_PATH + "/tools/" + tools
    if not os.path.exists(tools_path):
      return tools_path + " doesnot exists."
  
    if not os.access(tools_path, os.X_OK):
      # chmod 777
      os.chmod(tools_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

  return True

@dispatcher.add_method
def get_version_ontology(**kwargs):
  result = {}
  ontology_path = config.NODE_PATH + "/ontology"

  if not os.path.exists(ontology_path):
    return ontology_path + " doesnot exists."

  #get version
  cmd = "cd ~/ontology/node\n"
  cmd += ontology_path + " --version" 
  print(cmd)
  p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
  time.sleep(1)
  version = p.stdout.read()
  p.stdout.close()
  p.terminate()

  # get md5
  md5 = calc_md5_for_file(ontology_path)

  result["version"] = str(version).strip("'b\\n")
  result["md5"] = str(md5)

  return result

@dispatcher.add_method
def get_version_wallet(**kwargs):
  wallet_path = config.NODE_PATH + "/wallet.dat"
  if not os.path.exists(wallet_path):
    return wallet_path + " doesnot exists."

  # get md5
  md5 = calc_md5_for_file(wallet_path)

  return md5

@dispatcher.add_method
def get_version_onto_config(**kwargs):
  onto_config_path = config.NODE_PATH + "/config.json"
  if not os.path.exists(onto_config_path):
    return onto_config_path + " doesnot exists."

  # get md5
  md5 = calc_md5_for_file(onto_config_path)

  return md5

@dispatcher.add_method
def get_version_test_config(**kwargs):
  test_config_path = config.TEST_PATH + "/config.json"
  if not os.path.exists(test_config_path):
    return test_config_path + " doesnot exists."

  # get md5
  md5 = calc_md5_for_file(test_config_path)

  return md5

@dispatcher.add_method
def get_version_sigsvr(**kwargs):
  sigsvr_path = None
  result = {}

  for sigsvr in ["sigsvr", "sigsvr-linux"]:
    sigsvr_path = config.NODE_PATH + "/" + sigsvr
    if os.path.exists(sigsvr_path):
      break
    else:
      sigsvr_path = None

  if not sigsvr_path:
    return "sigsvr doesnot exists."

  #get version
  cmd = "cd ~/ontology/node\n"
  cmd += sigsvr_path + " --version" 
  print(cmd)
  p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
  time.sleep(1)
  version = p.stdout.read()
  p.stdout.close()
  p.terminate()

  # get md5
  md5 = calc_md5_for_file(sigsvr_path)

  result["version"] = str(version).strip("'b\\n")
  result["md5"] = str(md5)

  return result

@dispatcher.add_method
def get_version_abi(**kwargs):
  abi_path = config.NODE_PATH + "/abi"
  if not os.path.exists(abi_path):
    return abi_path + " doesnot exists."

  # get md5
  md5 = calc_md5_for_folder(abi_path)

  return md5

@dispatcher.add_method
def get_version_test_service(**kwargs):
  test_service_path = "/home/ubuntu/ontology/test_service/rpcserver.py"
  if not os.path.exists(test_service_path):
    return test_service_path + " doesnot exists."

  # get md5
  md5 = calc_md5_for_file(test_service_path)

  return md5

@dispatcher.add_method
def stop_test_service(**kwargs):
  os.popen("killall -9 test_service")
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
    dispatcher["transfer_ong"] = transfer_ong
    dispatcher["withdrawong"] = withdrawong
    dispatcher["exec_cmd"] = exec_cmd
    dispatcher["start_sigsvr"] = start_sigsvr
    dispatcher["stop_sigsvr"] = stop_sigsvr
    dispatcher["heart_beat"] = heart_beat
    dispatcher["check_xmode_ontology"] = check_xmode_ontology
    dispatcher["check_xmode_sigsvr"] = check_xmode_sigsvr
    dispatcher["check_xmode_tools"] = check_xmode_tools
    dispatcher["get_version_ontology"] = get_version_ontology
    dispatcher["get_version_wallet"] = get_version_wallet
    dispatcher["get_version_onto_config"] = get_version_onto_config
    dispatcher["get_version_test_config"] = get_version_test_config
    dispatcher["get_version_sigsvr"] = get_version_sigsvr
    dispatcher["get_version_abi"] = get_version_abi
    dispatcher["get_version_test_service"] = get_version_test_service
    dispatcher["stop_test_service"] = stop_test_service

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    print(request)
    responseobj =json.loads(response.json)
    print(responseobj)
    if "error" not in responseobj:
        responseobj["error"] = 0
    else:
        if "message" in responseobj["error"]:
          responseobj["desc"] = responseobj["error"]["message"]
        if "code" in responseobj["error"]:
          responseobj["error"] = responseobj["error"]["code"]
    print(json.dumps(responseobj))
    return Response(json.dumps(responseobj), mimetype='application/json')

if __name__ == '__main__':
    run_simple(get_host_ip(), config.PORT, application)
