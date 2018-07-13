package com.ontio.testtool.api;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.net.MalformedURLException;
import java.util.HashMap;
import java.util.Map;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.github.ontio.OntSdk;
import com.github.ontio.account.Account;
import com.github.ontio.common.Address;
import com.github.ontio.common.ErrorCode;
import com.github.ontio.common.Helper;
import com.github.ontio.core.payload.DeployCode;
import com.github.ontio.core.transaction.Transaction;
import com.github.ontio.crypto.SignatureScheme;
import com.github.ontio.network.exception.RpcException;
import com.ontio.testtool.utils.Config;
import com.ontio.testtool.utils.Logger;
import com.ontio.testtool.utils.RpcClient;

public class ContractApi {
	static RpcClient smartxclient = null;
	static OntSdk ontSdk = OntSdk.getInstance();
	
	static public Map deployContract(String codePath, JSONObject options) {
		try {
			File codefile = new File(codePath);
			if (!codefile.exists()) {
				System.out.println("deployContract: file not exists(" + codePath + ")");
				return null;
			}
			
			if (smartxclient == null) {
				smartxclient = new RpcClient("http://139.219.97.24:8080/api/v1.0/compile");
			}
			
			String codeContent = "";
	        BufferedReader codefilereader = null;  
        	codefilereader = new BufferedReader(new FileReader(codePath));  
            String tempString = null;  
            while ((tempString = codefilereader.readLine()) != null) {
        		codeContent += tempString;
            }  
            codefilereader.close();  
	
	        String avmcode = "";
	        String abi = "";
			Map request = new HashMap();
	        request.put("code", codeContent);
	        request.put("type", "CSharp");
			Map response = (Map) smartxclient.send(request);
	        if (response == null) {
	        	return null;
	        } else if ((Integer)response.get("errcode") == 0) {
	        	avmcode  = (String)response.get("avm");
	        	if (avmcode.startsWith("b'")) {
	        		avmcode = avmcode.substring(2);
	        	}
	        	if (avmcode.endsWith("'")) {
	        		avmcode = avmcode.substring(0, avmcode.length() - 1);
	        	}
	        	
	        	abi = (String)response.get("abi");
	        	if (abi.startsWith("b'")) {
	        		abi = abi.substring(2);
	        	}
	        	if (abi.endsWith("'")) {
	        		abi = abi.substring(0, abi.length() - 1);
	        	}
	        	abi = abi.replace("\\n", "");

	        	System.out.println(avmcode);
	        	System.out.println(abi);
	        } else {
	        	return null;
	        }

			System.out.println("ContractAddress:" + Address.AddressFromVmCode(avmcode).toHexString());
	        ontSdk.vm().setCodeAddress(Address.AddressFromVmCode(avmcode).toHexString());
	
	        com.github.ontio.account.Account account = getDefaultAccount();
	        
	        Transaction tx = ontSdk.vm().makeDeployCodeTransaction(avmcode, true, "name",
	                "v1.0", "author", "email", "desp", account.getAddressU160().toBase58(),ontSdk.DEFAULT_DEPLOY_GAS_LIMIT,0);
	        ontSdk.signTx(tx, new Account[][]{{account}});
	        String txHex = Helper.toHexString(tx.toArray());
	        Object result = ontSdk.getConnect().sendRawTransaction(txHex);
            //System.out.println(result);
            //System.out.println("txhash:" + tx.hash().toString());
            String txhash = tx.hash().toHexString();
            Thread.sleep(6000);
            //DeployCode t = (DeployCode) ontSdk.getConnect().getTransaction(txhash);
            //System.out.println(t.txType.value() & 0xff);
            Map smartevent = (Map)ontSdk.getConnect().getSmartCodeEvent(txhash);
            if ((int)smartevent.get("State") == 1) {
            	Map ret = new HashMap();
            	ret.put("address", Address.AddressFromVmCode(avmcode).toHexString());
            	ret.put("abi", abi);
            	return ret;
            }
			return null;
		}
		catch (Exception e) {
			Logger.getInstance().error("deployContract: " + e.toString());
			e.printStackTrace();
			return null;
		}
	}

	public static com.github.ontio.account.Account getDefaultAccount() {
	    try {
		    com.github.ontio.sdk.wallet.Account accountInfo = ontSdk.getWalletMgr().getDefaultAccount();
		    if (accountInfo == null) {
		    	 System.out.println("no default wallet..");
		    	 return null;
		    }

			return ontSdk.getWalletMgr().getAccount(accountInfo.address, Config.PWD, accountInfo.getSalt());
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	    
	    return null;
	}
	
}
