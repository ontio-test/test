package com.ontio.testtool.controller;

import java.io.IOException;
import java.net.MalformedURLException;
import java.util.ArrayList;
import java.util.List;

import com.alibaba.fastjson.JSONObject;
import com.github.ontio.network.exception.RpcException;
import com.ontio.testtool.utils.Config;
import com.ontio.testtool.utils.RpcClient;

public class OntNodeController {
	private List<RpcClient> rpcs = new ArrayList<RpcClient>();
	public OntNodeController() {
		for(int i = 0; i < Config.NODES.size(); i++) {
			JSONObject node = (JSONObject) Config.NODES.getJSONObject(i);
			String ip = node.getString("ip");
			try {
				RpcClient rpc = new RpcClient("http://" + ip + ":"+  Config.TEST_SERVICE_PORT + "/jsonrpc");
				rpcs.add(rpc);
			} catch (MalformedURLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
	
	boolean _start(int nodeindex, String ontology, String config, String args, boolean clean_chain, boolean clean_log) {
		System.out.println("start node " + nodeindex + " " + Config.DEFAULT_NODE_ARGS);
		RpcClient rpc = rpcs.get(nodeindex);
		JSONObject params = new JSONObject();
		params.put("clear_chain", clean_chain);
		params.put("clear_log", clean_log);
		params.put("name", ontology);
		params.put("node_args", args);
		params.put("config", config);
		
		try {
			rpc.call("start_node", params);
		} catch (RpcException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}
		return true;
	}
	
	/**
	 */
	public boolean stopAll() {
		int[] nodeindexs = new int[Config.NODES.size()];
		for(int i = 0; i < Config.NODES.size(); i++) {
			nodeindexs[i] = i;
		}
		
		return stop(nodeindexs);
	}
	
	public boolean stop(int nodeindex) {
		System.out.println("stop node " + nodeindex + " " + Config.DEFAULT_NODE_ARGS);
		RpcClient rpc = rpcs.get(nodeindex);
		try {
			rpc.call("stop_node", null);
			return true;
		} catch (RpcException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}
	}
	public boolean stop(int[] nodeindexs) {
		boolean ret = true;
		for(int i = 0; i < nodeindexs.length; i++) {
			boolean ret1 = stop(nodeindexs[i]);
			if (!ret1) {
				ret = false;
			}
		}
	
		return ret;
	}
	/**
	 */
	public boolean startAll() {
		return startAll("ontology", "config.json", Config.DEFAULT_NODE_ARGS);
	}
	public boolean startAll(String program, String config, String nodeargs) {
		int[] nodeindexs = new int[Config.NODES.size()];
		for(int i = 0; i < Config.NODES.size(); i++) {
			nodeindexs[i] = i;
		}
		
		return start(nodeindexs, program, config, nodeargs);	
	}
	
	
	public boolean start(int[] nodeindexs, String program, String config, String nodeargs) {
		boolean ret = true;
		for(int i = 0; i < nodeindexs.length; i++) {
			boolean ret1 = _start(nodeindexs[i], program, config, nodeargs, false, false);
			if (!ret1) {
				ret = ret1;
			}
		}
		return ret;
	}
	/**
	 */
	public boolean restartAll() {
		return restartAll("ontology", "config.json", Config.DEFAULT_NODE_ARGS);
	}
	public boolean restartAll(String program, String config, String nodeargs) {
		stopAll();
		
		int[] nodeindexs = new int[Config.NODES.size()];
		for(int i = 0; i < Config.NODES.size(); i++) {
			nodeindexs[i] = i;
		}
		
		return restart(nodeindexs, program, config, nodeargs);		
	}
	
	public boolean restart(int[] nodeindexs, String program, String config, String nodeargs) {
		stop(nodeindexs);
		boolean ret = true;
		for(int i = 0; i < nodeindexs.length; i++) {
			boolean ret1 = _start(nodeindexs[i], program, config, nodeargs, true, true);
			if (!ret1) {
				ret = ret1;
			}
        }

		return ret;
	}
	
	public boolean restart(int nodeindex, String program, String config, String nodeargs) {
		stop(nodeindex);
		System.out.println("restart node " + nodeindex + " " + Config.DEFAULT_NODE_ARGS);
		return _start(nodeindex, program, config, nodeargs, true, true);
	}
	/**
	 */
	public boolean replaceConfigAll(String path) {return true;}
	public boolean replaceConfig(int[] nodeindexs, String path) {return true;}
	/**
	 */
	public boolean replaceConfigAll(JSONObject cfg) {return true;}
	public boolean replaceConfig(int[] nodeindexs, JSONObject cfg) {return true;}
	
	
	public boolean checkNodeSync(int[] nodeindexs) {
		boolean isSame = true;
		String lastMd5 = "";
		for(int i = 0; i < nodeindexs.length; i++) {
			int nodeindex = nodeindexs[i];
			String md5 = getStatesMd5(nodeindex);
			if (i != 0 && lastMd5 != md5) {
				isSame = false;
			}
			
			lastMd5 = md5;
		}
		
		return isSame;
	}
	
	/**
	 */
	public String getStatesMd5(int nodeindex) {
		String ret = "";
		System.out.println("getStatesMd5 " + nodeindex + " ");
		RpcClient rpc = rpcs.get(nodeindex);
		try {
			return (String)rpc.call("get_states_md5", null);
		} catch (RpcException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			ret = "";
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			ret = "";
		}
		
		return ret;
	}

	/**
	 */
	public String getBlockMd5(int nodeindex) {
		String ret = "";
		System.out.println("getBlockMd5 " + nodeindex + " ");
		RpcClient rpc = rpcs.get(nodeindex);
		try {
			return (String)rpc.call("get_block_md5", null);
		} catch (RpcException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			ret = "";
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			ret = "";
		}
		
		return ret;
	}
	/**
	 */
	public String getLedgereventMd5(int nodeindex) {
		String ret = "";
		System.out.println("getBlockMd5 " + nodeindex + " ");
		RpcClient rpc = rpcs.get(nodeindex);
		try {
			return (String)rpc.call("get_ledgerevent_md5", null);
		} catch (RpcException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			ret = "";
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			ret = "";
		}
		
		return ret;
	}
	/**
	 */
	public String exec(int nodeindex, String cmd) {return "";}

}
