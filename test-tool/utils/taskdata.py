# -*- coding: utf-8 -*-

import os
import json

from utils.config import Config

class Task:
	def __init__(self, name, ijson):
		self._path = ""
		self._type = "rpc"
		if "type" in self._taskjson:
			self._type = self._taskjson["type"]
		self._name = name
		self._taskjson = ijson
		self._data = ijson

	def __init__(self, path = ""):
		self._path = path
		self._type = "rpc"
		if self._path:
			self._taskjson = self.load_cfg(self._path)
			self._name = os.path.basename(self._path).replace('.json', '')

		if self._taskjson:
			if "type" in self._taskjson:
				self._type = self._taskjson["type"]
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