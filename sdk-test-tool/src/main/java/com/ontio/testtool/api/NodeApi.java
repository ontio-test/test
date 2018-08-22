package com.ontio.testtool.api;

import java.io.IOException;
import java.net.MalformedURLException;
import java.util.ArrayList;
import java.util.List;

import com.alibaba.fastjson.JSONObject;
import com.github.ontio.OntSdk;
import com.github.ontio.account.Account;
import com.github.ontio.common.Address;
import com.github.ontio.core.transaction.Transaction;
import com.github.ontio.network.exception.RpcException;
import com.github.ontio.sdk.manager.WalletMgr;
import com.github.ontio.sdk.wallet.Wallet;
import com.ontio.testtool.OntTest;
import com.ontio.testtool.utils.Common;
import com.ontio.testtool.utils.Config;
import com.ontio.testtool.utils.RpcClient;

public class NodeApi {
	private List<RpcClient> rpcs = new ArrayList<RpcClient>();
	private OntSdk ontSdk = null;
	public NodeApi() {
		ontSdk = OntSdk.getInstance();
		
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
		try {
			int[] nodeindexs = new int[Config.NODES.size()];
			for(int i = 0; i < Config.NODES.size(); i++) {
				nodeindexs[i] = i;
			}
			
			boolean ret = start(nodeindexs, program, config, nodeargs);
			Thread.sleep(10000);
			return ret;
		} catch (Exception e) {
			return false;
		}
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
		try {
			stop(nodeindexs);
			boolean ret = true;
			for(int i = 0; i < nodeindexs.length; i++) {
				boolean ret1 = _start(nodeindexs[i], program, config, nodeargs, true, true);
				if (!ret1) {
					ret = ret1;
				}
	        }

			Thread.sleep(10000);
			return ret;
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();	
			return false;
		}
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

	public boolean initOntOng() {
		try {
			if (Config.TEST_MODE == false) {
				//ontsdk.addMultiSign(tx, M, pubKeys, acct);
		        //create a multi-sig account as a main account
				int M = 5;
				int N = 7;
	            Account[] accounts = new Account[N];
		        for(int i = 0; i < N; i++) {
		        	accounts[i] = OntTest.common().getDefaultAccount(new WalletMgr(Config.nodeWallet(i), ontSdk.defaultSignScheme));
		        }
		        byte[][] pubkeylist = new byte[N][];
		        for(int i = 0; i < N; i++) {
		        	pubkeylist[i] = accounts[i].serializePublicKey();
		        }
		        Address multiAddr = Address.addressFromMultiPubKeys(M, pubkeylist);	        
		        System.out.println("multi: " + multiAddr.toBase58());
	
		        //transfer ont
		        for(int i = 0; i < N; i++) {
			        Transaction tx = ontSdk.nativevm().ont().makeTransfer(multiAddr.toBase58(), accounts[i].getAddressU160().toBase58(), 10000000, accounts[i].getAddressU160().toBase58(), 30000, 0);
			        for (int j = 0; j < M; j++) {
	                    ontSdk.addMultiSign(tx, M, pubkeylist, accounts[j]);
	                }
			        ontSdk.addSign(tx, accounts[i]);	            
		            ontSdk.getConnect().sendRawTransaction(tx.toHexString());
		            OntTest.common().waitTransactionResult(tx.hash().toHexString());
		        }
		        
		        //withdraw ong
		        {
			        Transaction tx = ontSdk.nativevm().ong().makeWithdrawOng(multiAddr.toBase58(), multiAddr.toBase58(), 1000000000000000L, accounts[0].getAddressU160().toBase58(), 30000, 0);
		            for (int j = 0; j < M; j++) {
		                ontSdk.addMultiSign(tx, M, pubkeylist, accounts[j]);
		            }
			        ontSdk.addSign(tx, accounts[0]);	            
		            ontSdk.getConnect().sendRawTransaction(tx.toHexString());
		            OntTest.common().waitTransactionResult(tx.hash().toHexString());
		        }
	            
	            //transfer ong
	            for(int i = 0; i < N; i++) {
			        Transaction tx = ontSdk.nativevm().ong().makeTransfer(multiAddr.toBase58(), accounts[i].getAddressU160().toBase58(), 100000000000000L, accounts[i].getAddressU160().toBase58(), 30000, 0);
			        for (int j = 0; j < M; j++) {
	                    ontSdk.addMultiSign(tx, M, pubkeylist, accounts[j]);
	                }
			        ontSdk.addSign(tx, accounts[i]);	            
		            ontSdk.getConnect().sendRawTransaction(tx.toHexString());
			        System.out.println("smart code: " + ontSdk.getConnect().getSmartCodeEvent(tx.hash().toString()));
			        OntTest.common().waitTransactionResult(tx.hash().toHexString());
		        }
			} else {
				WalletMgr wm = new WalletMgr(Config.nodeWallet(0), ontSdk.defaultSignScheme);
				Wallet w = wm.getWalletFile();
				List<com.github.ontio.sdk.wallet.Account> accountinfos = w.getAccounts();
		        System.out.println("init ont&ong in test mode: " + accountinfos.size());

				com.github.ontio.sdk.wallet.Account defaultaccountInfo = wm.getDefaultAccount();
				Account defaultaccount = wm.getAccount(defaultaccountInfo.address, Config.PWD);
				Transaction tx = ontSdk.nativevm().ont().makeTransfer(defaultaccountInfo.address, defaultaccountInfo.address, 100000000, defaultaccountInfo.address, 30000, 0);
				defaultaccount = wm.getAccount(defaultaccountInfo.address, Config.PWD);
				ontSdk.addSign(tx, defaultaccount);	            
	            ontSdk.getConnect().sendRawTransaction(tx.toHexString());
	            ontSdk.getConnect().sendRawTransactionPreExec(tx.toHexString());
	            OntTest.common().waitTransactionResult(tx.hash().toHexString());

	            tx = ontSdk.nativevm().ong().makeWithdrawOng(defaultaccountInfo.address, defaultaccountInfo.address, 10000000000000000L, defaultaccountInfo.address, 30000, 0);
		        ontSdk.addSign(tx, defaultaccount);
	            ontSdk.getConnect().sendRawTransaction(tx.toHexString());
	            ontSdk.getConnect().sendRawTransactionPreExec(tx.toHexString());
	            OntTest.common().waitTransactionResult(tx.hash().toHexString());

				for(com.github.ontio.sdk.wallet.Account accountInfo : accountinfos) {
					if (accountInfo.isDefault == false) {
				        System.out.println("give " + accountInfo.address + " ont");
						tx = ontSdk.nativevm().ont().makeTransfer(defaultaccountInfo.address, accountInfo.address, 10000000, defaultaccountInfo.address, 30000, 0);
						ontSdk.addSign(tx, defaultaccount);	            
			            ontSdk.getConnect().sendRawTransaction(tx.toHexString());
			            ontSdk.getConnect().sendRawTransactionPreExec(tx.toHexString());
			            OntTest.common().waitTransactionResult(tx.hash().toHexString());

				        System.out.println("give " + accountInfo.address + " ong");
						tx = ontSdk.nativevm().ong().makeTransfer(defaultaccountInfo.address, accountInfo.address, 1000000000000000L, defaultaccountInfo.address, 30000, 0);
				        ontSdk.addSign(tx, defaultaccount);	            
			            ontSdk.getConnect().sendRawTransaction(tx.toHexString());
			            ontSdk.getConnect().sendRawTransactionPreExec(tx.toHexString());
			            OntTest.common().waitTransactionResult(tx.hash().toHexString());
					}
				}
			}
                        
		} catch(Exception e) {
			e.printStackTrace();
			return false;
		}
		
		return true;
	}
}
