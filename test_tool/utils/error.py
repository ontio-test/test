# -*- coding: utf-8 -*-
from utils.config import Config
from utils.logger import LoggerInstance as logger

class Error(Exception):
	def __init__(self, msg):
		self.msg = msg

class TestError(Error):
	def __init__(self, code):
		self.code = code
		self.msg = "UNKNOW ERROR"
		if code in Config.ERR_CODE:
			self.msg = Config.ERR_CODE[code]

		logger.error(self.msg)