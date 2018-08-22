package com.ontio.testtool.utils;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.alibaba.fastjson.annotation.JSONField;
import com.github.ontio.common.Helper;
import com.github.ontio.core.block.Block;
import com.github.ontio.io.Serializable;
import com.github.ontio.network.exception.ConnectorException;
import com.github.ontio.network.websocket.MsgQueue;
import com.github.ontio.network.websocket.Result;
import com.github.ontio.sdk.manager.WalletMgr;
import com.github.ontio.sdk.wallet.Wallet;
import com.ontio.testtool.OntTest;

class TxStates{
    @JSONField(name="States")
    Object[] states;

    @JSONField(name="ContractAddress")
    String contractAddress;

    public Object[] getStates() {
        return states;
    }

    public void setStates(Object[] states) {
        this.states = states;
    }

    public String getContractAddress() {
        return contractAddress;
    }

    public void setContractAddress(String contractAddress) {
        this.contractAddress = contractAddress;
    }
}

class TxEvent{
    @JSONField(name="GasConsumed")
    int gasConsumed;

    @JSONField(name="TxHash")
    String txHash;

    @JSONField(name="State")
    int state;

    @JSONField(name="Notify")
    TxStates[] notify;

    public int getGasConsumed() {
        return gasConsumed;
    }

    public void setGasConsumed(int gasConsumed) {
        this.gasConsumed = gasConsumed;
    }


    public String getTxHash() {
        return txHash;
    }

    public void setTxHash(String txHash) {
        this.txHash = txHash;
    }

    public int getState() {
        return state;
    }

    public void setState(int state) {
        this.state = state;
    }

    public TxStates[] getNotify() {
        return notify;
    }

    public void setNotify(TxStates[] notify) {
        this.notify = notify;
    }
}

public class Common {
	public JSONObject loadJson(String filepath) {
		String fileName = filepath;
		String contents = "";
		String line = "";
		try {
			BufferedReader in = new BufferedReader(new FileReader(fileName));
			line=in.readLine();
			while (line!=null) {
				contents = contents + line;
				line=in.readLine();
			}
			in.close();
		 } catch (IOException e) {
			e.printStackTrace(); 
		 }
		
		JSONObject jobj = JSON.parseObject(contents);

		return jobj;
	}
	
	public com.github.ontio.account.Account getDefaultAccount(WalletMgr walltemgr) {
	    try {
		    com.github.ontio.sdk.wallet.Account accountInfo = walltemgr.getDefaultAccount();
		    if (accountInfo == null) {
		    	 System.out.println("no default wallet..");
		    	 return null;
		    }
			return walltemgr.getAccount(accountInfo.address, Config.PWD, accountInfo.getSalt());
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	    
	    return null;
	}
	
	public com.github.ontio.account.Account getAccount(int index) {
		try {
			if (Config.TEST_MODE == true) {
				WalletMgr wm = new WalletMgr(Config.nodeWallet(0), OntTest.sdk().defaultSignScheme);
				Wallet w = wm.getWalletFile();
				List<com.github.ontio.sdk.wallet.Account> accountinfos = w.getAccounts();
		        System.out.println("init ont&ong in test mode: " + accountinfos.size());
		        if (accountinfos.size() <= index) {
		        	OntTest.logger().error("Get account: index out of range " + index);
		        	return null;
		        }
		        com.github.ontio.sdk.wallet.Account accountinfo = accountinfos.get(index);
		        return wm.getAccount(accountinfo.address, Config.PWD);
			} else {
				WalletMgr wm = new WalletMgr(Config.nodeWallet(index), OntTest.sdk().defaultSignScheme);
		        com.github.ontio.sdk.wallet.Account accountinfo = wm.getDefaultAccount();
		        return wm.getAccount(accountinfo.address, Config.PWD);
			}
		} catch(Exception e) {
			e.printStackTrace();
		}
		return null;
	}
	
	public boolean waitTransactionResult(String hash) {
        Object objEvent = null;
        for (int i = 0; i < 60; i++) {
            try {
                Thread.sleep(1000);
                try {
	                objEvent = OntTest.sdk().getConnect().getSmartCodeEvent(hash);
	                if (objEvent == null || objEvent.equals("")) {
	                    Thread.sleep(1000);
	                    continue;
	                }
                } catch(ConnectorException e) {
                	continue;
                }
                
                TxEvent events = JSON.parseObject(objEvent.toString(), TxEvent.class);
                OntTest.logger().print("...State:" + events.getState());
                OntTest.logger().print("...TxHash:" + events.getTxHash());
                OntTest.logger().print("...GasConsumed:" + events.getGasConsumed());
                if (events.getTxHash().equals(hash)) {
                	return events.getState() == 1;
                }      
            } catch (Exception e) {
            	e.printStackTrace();
            }
        }
        return false;
	}
	
	public Result waitWsResult(String action) {
		Object lock = OntTest.wsLock();
        try {
            
            for (int i = 0; i < 5; i++) {
                //lock.wait();
            	synchronized (lock) {
                    for (String e : MsgQueue.getResultSet()) {
                        Result rt = JSON.parseObject(e, Result.class);
                        MsgQueue.removeResult(e);
                        if (rt.Action.equals(action)) {
                        	return rt;
                        }
                    }
            	}
                
                Thread.sleep(1000);
            }
            
            return null;
            
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
	
	public boolean waitGenBlock() {
		try {
			int oldheight = OntTest.sdk().getConnect().getBlockHeight();
			for (int i = 0; i < 30; i ++) {
				Thread.sleep(10000);
				int newheight = OntTest.sdk().getConnect().getBlockHeight();
				if (oldheight != newheight) {
					return true;
				}
			}
			
			return false;
		} catch(Exception e) {
			e.printStackTrace();
			return false;
		}
	}
}
