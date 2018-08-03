# -*- coding:utf-8 -*-
import re
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt
import time
import requests
import subprocess

import utils.connect
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase

class Common:
	#比较两边数据是否一致
	@staticmethod
	def cmp(expect_data, cmp_data):
		if isinstance(expect_data, dict):
			# 若为dict格式
			if not cmp_data or not isinstance(cmp_data, dict):
				return False
			for key in expect_data:
				cmp_key = key
				if cmp_key not in cmp_data:
					if cmp_key.capitalize() not in cmp_data:
						return False
					else:
						cmp_key = cmp_key.capitalize()
				if not Common.cmp(expect_data[key], cmp_data[cmp_key]):
					return False
			return True
		elif isinstance(expect_data, list):
			# 若为list格式
			if not cmp_data or not isinstance(cmp_data, list):
				return False

			if len(expect_data) > len(cmp_data):
				return False
			for src_list, dst_list in zip(sorted(expect_data), sorted(cmp_data)):
				if not Common.cmp(src_list, dst_list):
					return False
			return True
		else:
			if str(expect_data) != str(cmp_data):
				return False
			else:
				return True

	#暂停测试，需手动输入才能返回
	# msg:暂停原因
	# 返回值: 手动输入的值
	@staticmethod
	def pause(msg):
		print("[ PAUSE     ] " + msg)
		command = ""
		try:
			command = sys.stdin.readline().strip('\n')
		except Exception as e:
			print(e)
		return command

	@staticmethod
	def bl_reserver(input):
		if input == None:
			return ""
		if len(input) % 2 != 0:
			return input
			
		rstrs = input[::-1]
		output = ""
		for i in range(0, len(input), 2):
			output = output + rstrs[i + 1]
			output = output + rstrs[i]
		return output

	@staticmethod
	def base58_to_address(input):
		if input == None:
			return ""
		address = ""
		cmd = Config.TOOLS_PATH + "/base58ToAddress -base58 \"" + input + "\" > address.tmp"
		os.system(cmd)
		print(cmd)
		tmpfile = open("address.tmp", "r+")  # 打开文件
		contents = tmpfile.readlines()
		for line in contents:
			#for log
			logger.print(line.strip('\n'))

		for line in contents:
			regroup = re.search(r'address: (([0-9]|[a-z]|[A-Z])*)', line)
			if regroup:
				address = regroup.group(1)
		tmpfile.close()
		return address

	@staticmethod
	def address_to_base58(input):
		if input == None:
			return ""
		input = Common.bl_reserver(input)

		base58 = ""
		cmd = Config.TOOLS_PATH + "/addressToBase58 \"" + input + "\" > base58.tmp"
		os.system(cmd)
		print(cmd)
		tmpfile = open("base58.tmp", "r+")  # 打开文件
		contents = tmpfile.readlines()
		for line in contents:
			#for log
			logger.print(line.strip('\n'))

		for line in contents:
			#regroup = re.search(r'address: (([0-9]|[a-z]|[A-Z])*)', line)
			#if regroup:
			base58 = line.strip()
		tmpfile.close()
		return base58

	@staticmethod
	def bl_address(input):
		return Common.bl_reserver(Common.base58_to_address(input))

	#check_node_state([0,1,2,3,4,5,6])
