package com.ontio.testtool;

import com.github.ontio.OntSdk;
import com.github.ontio.sdk.exception.SDKException;
import com.ontio.testtool.controller.OntNodeController;
import com.ontio.testtool.utils.Config;
import com.ontio.testtool.utils.Logger;

public class OntTest {
	private static OntSdk ontSdk = null;
	private static OntNodeController node = null;
	private static Logger logger = null;

	public static boolean init() {
		try {
			return bindNode(0);
		} catch (Exception e2) {
			return false;
		}
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
		    ontSdk.setWesocket(Config.wsUrl(index), new Object());
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
	
	public static OntNodeController node() {
		if (node == null) {
			node = new OntNodeController();
		}
		return node;
	}
	
	public static Logger logger() {
		logger = Logger.getInstance();
		return logger;
	}
}
