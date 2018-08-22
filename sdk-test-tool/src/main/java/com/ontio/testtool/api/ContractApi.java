package com.ontio.testtool.api;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Map;

import com.alibaba.fastjson.JSONObject;
import com.github.ontio.OntSdk;
import com.github.ontio.account.Account;
import com.github.ontio.common.Address;
import com.github.ontio.common.Helper;
import com.github.ontio.core.transaction.Transaction;
import com.ontio.testtool.OntTest;
import com.ontio.testtool.utils.Common;
import com.ontio.testtool.utils.Logger;
import com.ontio.testtool.utils.RpcClient;

public class ContractApi {
	static RpcClient smartxclient = null;
	static OntSdk ontSdk = OntSdk.getInstance();
	
	public Map deployContract(String codePath, JSONObject options) {
		try {
			File codefile = new File(codePath);
			if (!codefile.exists()) {
				System.out.println("deployContract: file not exists(" + codePath + ")");
				return null;
			} 
			
			String codeContent = "";
	        BufferedReader codefilereader = null;  
        	codefilereader = new BufferedReader(new FileReader(codePath));  
            String tempString = null;  
            while ((tempString = codefilereader.readLine()) != null) {
        		codeContent += tempString;
            }  
            codefilereader.close();  

	        String avmcode = codeContent;
	        String abi = "";
	        
	        if (codefile.getName().contains(".cs")) {
				if (smartxclient == null) {
					smartxclient = new RpcClient("http://42.159.94.234:8080/api/v1.0/compile");
				}
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
	        }

			System.out.println("ContractAddress:" + Address.AddressFromVmCode(avmcode).toHexString());
	        ontSdk.vm().setCodeAddress(Address.AddressFromVmCode(avmcode).toHexString());
	
	        com.github.ontio.account.Account account = OntTest.common().getDefaultAccount(ontSdk.getWalletMgr());
	        
	        Transaction tx = ontSdk.vm().makeDeployCodeTransaction(avmcode, true, "name",
	                "v1.0", "author", "email", "desp", account.getAddressU160().toBase58(),ontSdk.DEFAULT_DEPLOY_GAS_LIMIT,0);
	        ontSdk.signTx(tx, new Account[][]{{account}});
	        String txHex = Helper.toHexString(tx.toArray());
	        Object result = ontSdk.getConnect().sendRawTransaction(txHex);
            //System.out.println(result);
            //System.out.println("txhash:" + tx.hash().toString());
            String txhash = tx.hash().toHexString();
	        boolean txstate = OntTest.common().waitTransactionResult(txhash);
	        if (txstate) {
	        	Map ret = new HashMap();
            	ret.put("address", Address.AddressFromVmCode(avmcode).toHexString());
            	ret.put("abi", abi);
            	return ret;
	        }
            //DeployCode t = (DeployCode) ontSdk.getConnect().getTransaction(txhash);
            //System.out.println(t.txType.value() & 0xff);
			return null;
		}
		catch (Exception e) {
			Logger.getInstance().error("deployContract: " + e.toString());
			e.printStackTrace();
			return null;
		}
	}

}
