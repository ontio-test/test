import os
import json
import time

import utils.connect
from utils.config import Config
from utils.common import Common
from utils.logger import LoggerInstance as logger
from utils.error import TestError

class TaskRunner:
	#执行单个webapi
	# task: 需要执行的task
	# judge: 是否需要结果判断
	# process_log： 是否需要记录运行log
	# 返回值: (result: True or False, response: 网络请求)
	@staticmethod
	def run_single_task(task, judge = True, process_log = True):
		try:
			connecttype = task.type()
			name = task.name()
			start_time = time.time()

			if process_log:
				logger.print("[-------------------------------]")
				logger.print("[ RUN      ] "+ connecttype + "." + name)
			cfg_content = task.data()
			cfg_request = cfg_content["REQUEST"]
			cfg_response = cfg_content["RESPONSE"]
			if process_log:
				logger.print("[ PARAMS   ]" + json.dumps(cfg_content, indent = 4))

			#(result, response) = self.multithread_run(logger, cfg_request, cfg_response)
			node_index = task.node_index()
			node_ip = None
			print(node_index)
			if node_index != None:
				node_ip = Config.NODES[int(node_index)]["ip"]
				print("run on other service: " + str(node_index) + "  " + node_ip)
				
			response = utils.connect.con(connecttype, node_ip, cfg_request)
			if process_log:
				logger.print("[ RESULT   ]" + json.dumps(response, indent = 4))

			end_time = time.time()
			time_consumed = (end_time - start_time) * 1000
			
			result = True
			if judge:
				result = Common.cmp(cfg_response, response)
				if process_log:
					if result:
						logger.print("[ OK       ] " + connecttype + "."+ name +" (%d ms)" % (time_consumed))
					else:
						logger.print("[ Failed   ] " + connecttype + "."+ name +" (%d ms)"% (time_consumed))
					logger.print("[-------------------------------]")
					logger.print("")

			return (result, response)

		except TestError as e:
			print(e.msg)
			return (False, None)
		except Exception as e:
			print(e)
			return (False, None)
		

	#运行两个task
	#假设 task1生成reponse1， task2得到reponse2， compare_src_key为 key1|key2, compare_dist_key为 key3|key4
	#最终会比较reponse1["key1"]["key2"]和reponse2["key3"]["key4"]
	#result: 比较结果 True or False
	@staticmethod
	def run_pair_task(task1, task2, compare_src_key = None, compare_dist_key = None):
		result = True

		(result1, response1) = TaskRunner.run_single_task(task1)
		if not result1:
			return result1

		(result2, response2) = TaskRunner.run_single_task(task2)
		if not result2:
			return result2

		compare_src_data = response1
		if compare_src_key:
			compare_src_keys = compare_src_key.split('/')
			for key in compare_src_keys:
				if compare_src_data:
					compare_src_data = compare_src_data[key]
				else:
					break

			####split dist key
			compare_dist_data = response2
			if compare_dist_key:
				compare_dist_keys = compare_dist_key.split('/')
				for key in compare_dist_keys:
					if compare_dist_data:
						compare_dist_data = compare_dist_data[key]
					else:
						break
			result = Common.cmp(compare_src_data, compare_dist_data)
		else:
			result = True

		return result