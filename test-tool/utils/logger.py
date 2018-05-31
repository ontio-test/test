# -*- coding: utf-8 -*-
import time
import os

class Logger():
	def __init__(self):
		#pathstr = "logs/" + time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
		pathstr = "logs/" + time.strftime('%Y-%m-%d',time.localtime(time.time()))
		if not os.path.exists(pathstr):
			os.makedirs(pathstr)
		#for subpath in ["rpc", "restful", "ws", "cli", "contract"]:
		#	if not os.path.exists(pathstr + "/" + subpath):
		#		os.makedirs(pathstr + "/" + subpath)
		
		self.prefix = pathstr
		self.collectionfile = open(pathstr + "/collection_log.csv", "w")  # 打开文件
		self.collectionfile.write("NAME,STATUS,LOG PATH\n")

	def __del__(self):
		self.collectionfile.close()

	def open(self, filepath):
		logdir = self.prefix + "/" + os.path.dirname(filepath)
		if not os.path.exists(logdir):
			os.makedirs(logdir)

		self.logpath = self.prefix + "/" + filepath
		self.logfile = open(self.logpath, "w")  # 打开文件

	#write
	def print(self, str):
		print(str)
		self.logfile.write(str + "\n")

	def close(self, name = None, result = None):
		if not result is None:
			if result:
				self.print("[ OK       ] ")
				self.append_record(name, "pass", self.logpath)
			else:
				self.print("[ Failed   ] ")
				self.append_record(name, "fail", self.logpath)
		self.logfile.close()

	def append_record(self, name, status, logpath):
		self.collectionfile.write(name + "," + status + "," + logpath + "\n")


LoggerInstance = Logger()