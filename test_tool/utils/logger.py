# -*- coding: utf-8 -*-
import time
import os
from utils.config import Config

class Logger():
	def __init__(self):
		self.prefix = Config.LOG_PATH + "/" + time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
		self.prefixFul = self.prefix;
		self.init = False
		#self.prefix = "logs/" + time.strftime('%Y-%m-%d',time.localtime(time.time()))
		self.logfile = None
		self.logpath = ""
		self.collectionfile = None

	def __del__(self):
		if self.init:
			pass

	def setPath(self, path):
		self.prefixFul = self.prefix + "/" + path

	def logPath(self):
		return self.logpath

	def open(self, filepath, title = None):
		self.logpath = self.prefixFul + "/" + filepath
		logdir = self.prefixFul + "/" + os.path.dirname(filepath)
		if not os.path.exists(logdir):
			os.makedirs(logdir)

		if not self.init:
			self.init = True

		self.logfile = open(self.logpath, "w")  # 打开文件
		self.logtitle = title if title else os.path.splitext(filepath)[0]
	#write
	def print(self, str):
		strtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

		strlist = str.split("\n")
		str = ""
		for line in strlist:
			str = str + strtime + ": " + line + "\n"
		
		print(str, end='')
		if self.logfile:
			self.logfile.write(str)

	def error(self, str):
		strtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		str = "[ ERROR ]  " + str

		strlist = str.split("\n")
		str = ""
		for line in strlist:
			str = str + strtime + ": " + line + "\n"

		print(str, end='')
		if self.logfile:
			self.logfile.write(str)

	def info(self, str):
		strtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		str = "[ INFO ]  " + str

		strlist = str.split("\n")
		str = ""
		for line in strlist:
			str = str + strtime + ": " + line + "\n"

		print(str, end='')
		if self.logfile:
			self.logfile.write(str)

	def close(self, result = None, msg = None):
		if not result is None:
			if result == "pass":
				self.print("[ OK       ] ")
				self.append_record(self.logtitle, "pass", self.logpath.replace(self.prefix + "/", ""))
			elif result == "fail":
				self.print("[ Failed   ] ")
				self.append_record(self.logtitle, "fail", self.logpath.replace(self.prefix + "/", ""))
			else:
				self.print("[ Block    ] ")
				self.append_record(self.logtitle, "block", self.logpath.replace(self.prefix + "/", ""))
		if self.logfile:
			self.logfile.close()
			self.logfile = None

	def append_record(self, name, status, logpath, retrytimes = 0):
		filename = "collection_log"
		try:
			newfile = False
			if not os.path.exists(os.path.dirname(self.logpath) + "/" + filename + ".csv"):
				newfile = True
			self.collectionfile = open(os.path.dirname(self.logpath) + "/" + filename + ".csv", "a+")  # 打开文件
			
			if newfile:
				self.collectionfile.write("NAME,STATUS,LOG PATH\n")
			self.collectionfile.write(name + "," + status + "," + logpath + "\n")
			self.collectionfile.close()
		except Exception as e:
			print("append_record:", e)
			#append_record(name, status, logpath, retrytimes = retrytimes + 1)

LoggerInstance = Logger()