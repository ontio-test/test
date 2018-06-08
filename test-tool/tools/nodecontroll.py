# -*- coding: utf-8 -*-
import sys, getopt

sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.commonapi import *

#init doc
__doc__ = "[1] -h --help\n[2] -a --action\n[3] -n --node\n[4] -v --value\n[5] -v1 --value1\n[6] -v2 --value2"
#end doc


DEFAULT_NODE_ARGS = "--ws --rest --loglevel=0"

class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg

def main(argv = None):
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(sys.argv[1:], "ha:v:v1:v2:n:", ["help", "action=", "value=", "value1=", "value2=", "node="])
		except getopt.error as msg:
			raise Usage(msg)

		_action = ""
		_value = ""
		_value1 = ""
		_value2 = ""
		_nodes = []
		#opts = [('-t', 'restful'), ('-n', 'get_blk_by_hash.json')]
		for op, value in opts:
			if op in ("-a", "--action"):
				_action = value
			if op in ("-v", "--value"):
				_value = value
			if op in ("-v1", "--value1"):
				_value1 = value
			if op in ("-v2", "--value2"):
				_value2 = value
			if op in ("-n", "--node"):
				_nodes = str(value).split(",")
			if op in ("-h", "--help"):
				print(__doc__)
				return 0

		if len(_nodes) <= 0:
			raise(Usage("please set -n which is node index..."))

		for _node in _nodes:
			print(_action + ": " + str(_node))
			if _node:
				_node = int(_node)
				if _node >= 0:
					if _action == "start":
						start_node(_node, DEFAULT_NODE_ARGS)
					elif _action == "stop":
						stop_node(_node)
					elif _action == "replace_config":
						cfg_json = None
						if _value:
							cfg_file = open(_value, "rb")
							cfg_json = json.loads(cfg_file.read().decode("utf-8"))
							cfg_file.close()
						replace_config(_node, cfg_json)
					elif _action == "restart":
						start_node(_node, DEFAULT_NODE_ARGS, True, True)
					else:
						raise(Usage("no action: " + str(_action)))
				else:
					raise(Usage("error node: " + str(_node)))
			else:
				raise(Usage("error node: " + str(_node)))

	except Usage as err:
		print(err.msg)
		print("for help use --help")
		return 2

if __name__ == "__main__":
	sys.exit(main())
