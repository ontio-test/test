# -*- coding: utf-8 -*-

import os
import json

from utils.config import Config

class Task:
	def __init__(self, path = "", name = "", ijson = None):
		self._type = "rpc"
		self._path = path
		self._name = name
		self._taskjson = ijson
		self._nodeindex = None

		if self._path is not "":
			self._taskjson = self.load_cfg(self._path)
			self._name = os.path.basename(self._path).replace('.json', '')

		if self._taskjson:
			for key in self._taskjson:
				if key.upper() == "TYPE":
					self._type = self._taskjson[key]
				if key.upper() == "NODE_INDEX":
					self._nodeindex = self._taskjson[key]

		self._data = self._taskjson

	def path(self):
		return self._path

	def log_path(self):
		return self._path.replace('tasks/', '').replace(".json", ".log")

	def dir(self):
		return self._path.replace(os.path.basename(self._path), '')

	def set_type(self, itype):
		self._type = itype

	def type(self):
		return self._type

	def name(self):
		return self._name

	def data(self):
		return self._data

	def to_json(self):
		return self._taskjson

	def request(self):
		return self._data["REQUEST"]

	def set_request(self, request):
		self._data["REQUEST"] = request

	def node_index(self):
		for key in self._taskjson:
			if key.upper() == "NODE_INDEX":
				return self._taskjson[key]
		return None

	def load_cfg(self, cfg):
		if ".json" not in cfg:
			cfg = cfg + ".json"
		cfg_file = open(cfg, "rb")
		cfg_json = json.loads(cfg_file.read().decode("utf-8"))
		cfg_file.close()
		return cfg_json


class TaskData:
	def __init__(self, path):
		self.PATH = "tasks/" + path

	def tasks(self, recursive = True):
		ret = []
		if recursive:
			for root, dirs, files in os.walk(self.PATH):
				for file in files:
					fullpath = root + "/" + file
					if os.path.isfile(fullpath) and os.path.splitext(fullpath)[1] == ".json":
						ret.append(Task(fullpath))
		else:
			for filename in os.listdir(self.PATH):
				fullpath = os.path.join(self.PATH, filename)
				if os.path.isfile(fullpath) and os.path.splitext(fullpath)[1] == ".json":
					ret.append(Task(fullpath))
			
		return ret