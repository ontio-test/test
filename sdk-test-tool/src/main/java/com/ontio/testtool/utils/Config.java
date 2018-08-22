package com.ontio.testtool.utils;

import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.ontio.testtool.OntTest;

public class Config {
	static JSONObject jobj = null;
	
	static public String RPC_PORT = json().getString("RPC_PORT");
	static public String RESTFUL_PORT = json().getString("RESTFUL_PORT");
	static public String WS_PORT = json().getString("WS_PORT");
	static public String CLI_PORT = json().getString("CLI_PORT");
	static public String TEST_SERVICE_PORT = json().getString("TEST_SERVICE_PORT");	
	static public JSONArray NODES = json().getJSONArray("NODES");
	static public String DEFAULT_NODE_ARGS = json().getString("DEFAULT_NODE_ARGS");
	static public String PWD = json().getString("PWD");
	static public String RESOURCE_PATH = "resources";
	static public boolean TEST_MODE = json().getBoolean("TEST_MODE");
	static public String nodeIp(int index) {
		if (index >= Config.NODES.size()) {
			Logger.getInstance().error("get node ip: index out of range (" + index + ")");
			return "";
		} 
		
		return Config.NODES.getJSONObject(index).getString("ip");
	}
	static public String nodeWallet(int index) {
		if (index >= Config.NODES.size()) {
			Logger.getInstance().error("get node wallet: index out of range (" + index + ")");
			return "";
		}
		
		return Config.RESOURCE_PATH + "/wallets/" + Config.NODES.getJSONObject(index).getString("wallet") + ".tmp";
	}
	
	static public String rpcUrl(int index) {
		return "http://" + nodeIp(index) + ":" + RPC_PORT + "/jsonrpc";
	}
	
	static public String restfulUrl(int index) {
		return "http://" + nodeIp(index) + ":" + RESTFUL_PORT;
	}
	
	static public String wsUrl(int index) {
		return "ws://" + nodeIp(index) + ":" + WS_PORT;
	}
	
	static public String cliUrl(int index) {
		return "http://" + nodeIp(index) + ":" + CLI_PORT + "/cli";
	}
	
	static public String testServiceUrl(int index) {
		return "http://" + nodeIp(index) + ":" + TEST_SERVICE_PORT + "/jsonrpc";
	}
	
	static public JSONObject json() {
		if (jobj == null) {
			jobj = OntTest.common().loadJson("test_config.json");
		}
		return jobj;
	}
}
