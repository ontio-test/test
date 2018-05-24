import time
import os

class LogWriter():
	def __init__(self, filepath):
		self.prefix = self.get_prefix_path()
		self.logfile = open(self.prefix + "/" + filepath + ".log", "w")  # 打开文件

	def get_prefix_path(self):
		pathstr = "logs/" + time.strftime('%Y-%m-%d',time.localtime(time.time()))
		if not os.path.exists(pathstr):
			os.makedirs(pathstr)
		if not os.path.exists(pathstr + "/rpc"):
			os.makedirs(pathstr + "/rpc")
		if not os.path.exists(pathstr + "/restful"):
			os.makedirs(pathstr + "/restful") 
		if not os.path.exists(pathstr + "/websocket"):
			os.makedirs(pathstr + "/websocket")

		return pathstr

	#write
	def w(self, str):
		print(str)
		self.logfile.write(str + "\n")

	def close(self):
		self.logfile.close()

