package com.ontio.testtool;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.PrintStream;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;

import com.github.ontio.OntSdk;
import com.github.ontio.sdk.exception.SDKException;
import com.ontio.testtool.api.ApiManager;
import com.ontio.testtool.utils.Common;
import com.ontio.testtool.utils.Config;
import com.ontio.testtool.utils.Logger;

public class OntTest {
	private static OntSdk ontSdk = null;
	private static ApiManager api = null;
	private static Logger logger = null;
	private static Common common = null;
	private static Object wsLock = null;

	public static boolean init() {
		try {
			PrintStream myStream = new PrintStream(System.out) {
			    @Override
			    public void println(Object x) {
			    	OntTest.logger().print(x.toString());
			    }
			    @Override
			    public void println(String x) {
			    	OntTest.logger().print(x);
			    }
			};
			System.setOut(myStream);
			
			//copy wallte tmp files
			for(int i = 0; i < Config.NODES.size(); i++) {
				String walletorg = Config.nodeWallet(i);
				File file = new File(walletorg);
				if (file.exists()) {
					file.delete();
				}
				
				BufferedReader br = new BufferedReader(new FileReader(walletorg.replace(".tmp", "")));
				BufferedWriter bw = new BufferedWriter(new FileWriter(walletorg));
				String line;
				while((line = br.readLine()) != null) {
					bw.write(line);
					bw.newLine();
					bw.flush();
				}
				bw.close();
				br.close();
			}
			
			return bindNode(0);
		} catch (Exception e2) {
			e2.printStackTrace();
			return false; 
		}
    }

	public static Object wsLock() {
		if (wsLock == null) {
			wsLock = new Object();
		}
		return wsLock;
	}
	
	public static boolean bindNode(int index) {
		try {
			if (index >= Config.NODES.size()) {
				logger().error("set node: index out of range (" + index + ")");
				return false;
			}		
 			ontSdk = OntSdk.getInstance();
		    ontSdk.setRpc(Config.rpcUrl(index));
		    ontSdk.setRestful(Config.restfulUrl(index));
		    ontSdk.setWesocket(Config.wsUrl(index), wsLock());
		    ontSdk.setSignServer(Config.cliUrl(index));
		    ontSdk.setDefaultConnect(ontSdk.getRpc());
		    ontSdk.openWalletFile(Config.nodeWallet(index));
		    System.out.println("bindNode: " + Config.nodeWallet(index));

		    return true;
		} catch (SDKException e) {
		    System.out.println("SDKException: " + e.toString());
			return false;
		} catch (Exception e2) {
		    System.out.println("Exception: " + e2.toString());

			return false;
		}
	}	
	
	public static OntSdk sdk() {
		return OntSdk.getInstance();
	}
	
	public static ApiManager api() {
		if (api == null) {
			api = new ApiManager();
		}
		return api;
	}
	
	public static Logger logger() {
		logger = Logger.getInstance();
		return logger;
	}
	
	public static Common common() {
		if (common == null) {
			common = new Common();
		}
		return common;
	}
}
