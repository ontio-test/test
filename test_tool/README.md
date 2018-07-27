1.目录结构
	|-utils	测试基本工具
	|
	|-test_neo_api   		测试neo合约工程
	|	|
	|	logs				log目录
	|	|
	|	tasks				测试case目录
	|	|
	|	config.json   		配置测试节点地址
	|	|
	|	test_contract.py  	测试执行器
	|
	|-test_neo_native_api   测试neo合约调用native工程
	|	|	
	|	logs
	|	|
	|	tasks
	|	|
	|	config.json
	|	|
	|	test_neo_native.py 
	|
	|-test_web_api			测试webapi工程
	|	|
	|	logs
	|	|
	|	tasks
	|	|
	|	config.json
	|	|
	|	test_webapi.py

2.环境搭建
	pip3 install websocket-client
	pip3 install requests
	
3.执行test_web_api步骤
	> cd test_web_api
	> python3 test_webapi.py