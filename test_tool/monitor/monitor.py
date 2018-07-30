import time
import os
import unittest
import sys
import json
import fileinput

sys.path.append('..')
sys.path.append('../..')

from utils.logger import LoggerInstance as logger
from utils.config import Config

from api.apimanager import API

TRY_RECOVER_TIMES = 2
CHECK_LOOP = 50
FAILED_RADIO = 40 # 40%

class TestMonitor:
	#分析环境，未知错误的检查
	def __init__(self):
		self.faild_step_count = 0
		self.total_step_count = 0
		self.case_count = 0
		self.retry_cases = []
		self.retry_logger_path = []
		self.initmap = {}
		self.alltestcase = []
		self.unittestrunner = None

	def reset(self):
		self.faild_step_count = 0
		self.total_step_count = 0
		self.case_count = 0
		self.retry_cases = []
		self.retry_logger_path = []
		

	def need_retry(self):
		print("case_count:", self.case_count, " faild_step_count:", self.faild_step_count, " total_step_count:", self.total_step_count)
		if self.total_step_count <= 10:
			return False

		if (self.case_count >= CHECK_LOOP) and (self.faild_step_count * 100 / self.total_step_count) >= FAILED_RADIO:
			print("case_count:", self.case_count, " radio:", self.faild_step_count * 100 / self.total_step_count)
			return True
		else:
			print("case_count:", self.case_count, " radio:", self.faild_step_count * 100 / self.total_step_count)
			return False


	#恢复测试环境
	def recover_env(self):
		print("recover env...")
		#restart node
		API.node().stop_all_nodes()
		API.node().start_nodes(range(len(Config.NODES)), clear_chain = True, clear_log = True)

		#restart sigserver
		for node_index in range(len(Config.NODES)):
			API.node().stop_sigsvr(node_index)
			API.node().start_sigsvr(Config.NODE_PATH + "/wallet.dat", node_index)

		return True

	def retry(self):
		self.recover_env()
		testcases = self.retry_cases.copy()
		self.reset()
		self.initmap = {}
		for case in testcases:
			self.run_case(case)

	def analysis_case(self, case, logpath):
		if not os.path.exists(logpath):
			print("no log gennerator...")
			return False

		f = open(logpath, 'r')
		org_failed_count = self.faild_step_count
		JSONBody = ""
		catch_connet_error = False
		end_line = ""
		for line in f.readlines():
			line = line.strip()
			end_line = line
			if line.find("ERROR: Connect Error") >= 0:
				print("catch connect error...")
				catch_connet_error = True

			if line.find('[ CALL CONTRACT ] {') >= 0 or line.find("[ SIGNED TX ] {") >= 0:
				JSONBody = "{"
			elif JSONBody != "":
				JSONBody = JSONBody + line[len("1970-00-00 00:00:00:"):]
				#print(JSONBody)
			try:
				JSONObj = json.loads(JSONBody)
				if JSONObj:
					if "RESPONSE" in JSONObj:
						RESPONSE = JSONObj["RESPONSE"]
						if "result" in RESPONSE and "State" in RESPONSE["result"]:
							#for contract pre called.
							if RESPONSE["result"]["State"] != 1:
								print("catch faild [1]")
								self.faild_step_count = self.faild_step_count + 1
						elif "error" in RESPONSE:
							if RESPONSE["error"] != 0:
								print("catch faild [2]")
								self.faild_step_count = self.faild_step_count + 1
						elif "error_code" in RESPONSE:
							if RESPONSE["error_code"] != 0:
								print("catch faild [3]")
								self.faild_step_count = self.faild_step_count + 1
						elif "Error" in RESPONSE:
							if RESPONSE["Error"] == "Connection Error":
								print("catch connection error [4]")
								catch_connet_error = True
					else:
						self.faild_step_count = self.faild_step_count + 1

					self.total_step_count = self.total_step_count + 1
			except Exception as e:
				#print(e.args)
				pass
		f.close()

		self.case_count = self.case_count + 1
		if org_failed_count != self.faild_step_count:
			if case not in self.retry_cases:
				self.retry_cases.append(case)
				self.retry_logger_path.append(logpath)

		if end_line.find("[ OK       ]") < 0 and catch_connet_error:
			print("sure connect error...")
			return False

		return True

	def run_case(self, case):
		testmethodname = case._testMethodName
		testcaseclass = case.__class__
		if testmethodname == "test_init":
			return True
		if (testcaseclass in self.initmap) and (self.initmap[testcaseclass] == True):
			print("already ran init..")
		else:
			for initcase in self.alltestcase:
				if initcase.__class__ == testcaseclass and initcase._testMethodName == "test_init":
					print("run init" + str(initcase.__class__) + "." + initcase._testMethodName)
					testsuit = unittest.TestSuite()
					testsuit.addTest(initcase)
					self.unittestrunner.run(testsuit)
					self.initmap[testcaseclass] = True

		print("run " + str(case.__class__) + "." + case._testMethodName)
		testsuit = unittest.TestSuite()
		testsuit.addTest(case)
		self.unittestrunner.run(testsuit)
		return self.analysis_case(case, logger.logPath())

	def set_retry_block(self):
		for path in self.retry_logger_path:
			with open(path, 'a+') as f:
				f.write('[ BLOCK ]')

			collectionlogpath = os.path.dirname(path) + "/collection_log.csv"
			for line in fileinput.input(collectionlogpath, backup='.bak', inplace=1):
				if os.path.basename(path) in line.rstrip():
					line.rstrip().replace('pass', 'block')
					line.rstrip().replace('fail', 'block')

	def exec(self, runner, testcases, monitor = True):
		self.alltestcase = testcases.copy()
		self.unittestrunner = runner
		testcaseremain = testcases.copy()

		for case in testcaseremain:
			try:
				if not monitor:
					self.run_case(case)
					continue
				else:
					if self.run_case(case):
						if self.case_count >= CHECK_LOOP:
							if not self.need_retry():
								self.reset()
					else:
						print("retry single case...")
						self.recover_env()
						self.initmap = {}
						if not self.run_case(case):
							self.set_retry_block()

					if self.need_retry():
						print("need retry...[1]")
						retry_ret = False
						for i in range(TRY_RECOVER_TIMES):
							self.retry()
							retry_ret = self.need_retry()
							if retry_ret == True:
								break
						if retry_ret == False:
							print("need retry...[2]")
							self.set_retry_block()
			except Exception as e:
				print(e.args)