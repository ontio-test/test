package com.ontio.sdkapi;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import java.util.Base64;
import java.util.Map;

import javax.xml.bind.DatatypeConverter;

import org.bouncycastle.jcajce.util.JcaJceUtils;
import org.junit.After;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.github.ontio.common.WalletQR;
import com.github.ontio.core.block.Block;
import com.github.ontio.crypto.MnemonicCode;
import com.github.ontio.sdk.exception.SDKException;
import com.github.ontio.sdk.wallet.Account;
import com.github.ontio.sdk.wallet.Identity;
import com.github.ontio.sdk.wallet.Wallet;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;

public class MnemonicCodesStr {
	@Rule public OntTestWatcher watchman= new OntTestWatcher();
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
//		OntTest.api().node().restartAll("ontology", "config.json", Config.DEFAULT_NODE_ARGS);
//		Thread.sleep(5000);
	}
	
	@Before
	public void setUp() throws Exception {
		OntTest.logger().step("setUp");
	}
	
	@After
	public void TearDown() throws Exception {
		OntTest.logger().step("TearDown");
	}
	
	//generateMnemonicCodesStr001-006
	@Test
	public void test_base_001_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("助记词  001  exportIdentityQRCode()");

		try {
			OntTest.logger().step("测试参数exportIdentityQRCode_walletFile");
			
			Identity identity = OntTest.sdk().getWalletMgr().createIdentity("123456");
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			OntTest.logger().description(walletFile.toString());
			OntTest.logger().description(identity.toString());
			
			Map QRcode = WalletQR.exportIdentityQRCode(walletFile,identity);   
			OntTest.logger().description(QRcode.toString());
			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_normal_002_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("助记词  002  exportIdentityQRCode()");

		try {
			OntTest.logger().step("测试参数exportIdentityQRCode");
			
			Identity identity = OntTest.sdk().getWalletMgr().createIdentity("123456");
			Identity identity1 = OntTest.sdk().getWalletMgr().createIdentity("123456");
			OntTest.sdk().getWalletMgr().getWallet().clearIdentity();
			OntTest.sdk().getWalletMgr().getWallet().clearAccount();
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			OntTest.logger().description(walletFile.toString());
			OntTest.logger().description(identity1.toString());
			
			Map QRcode = WalletQR.exportIdentityQRCode(walletFile,identity1);   
			OntTest.logger().description(QRcode.toString());
			assertEquals(true,true);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_003_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("助记词  003  exportIdentityQRCode()");

		try {
			OntTest.logger().step("测试参数exportIdentityQRCode_walletFile");
			
			Identity identity = OntTest.sdk().getWalletMgr().createIdentity("123456");
			Wallet walletFile = null;
			
			Map QRcode = WalletQR.exportIdentityQRCode(walletFile,identity);
			OntTest.logger().description(QRcode.toString());
			assertEquals(true,false);
		}  catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_004_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("助记词  004  exportIdentityQRCode()");

		try {
			OntTest.logger().step("测试参数exportIdentityQRCode_identity");
			
			Identity identity = OntTest.sdk().getWalletMgr().createIdentity("123456");
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			Map QRcode = WalletQR.exportIdentityQRCode(walletFile,identity);   
			OntTest.logger().description(QRcode.toString());

			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	

	@Test
	public void test_normal_005_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("助记词  005  exportIdentityQRCode()");

		try {
			Identity identity = OntTest.sdk().getWalletMgr().createIdentity("123456");
			Identity identity1 = OntTest.sdk().getWalletMgr().createIdentity("123456");
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			walletFile.removeIdentity(identity1.ontid);
			OntTest.logger().description(walletFile.toString());
			OntTest.logger().description(identity1.toString());
			OntTest.logger().description(identity.toString());
			Map QRcode = WalletQR.exportIdentityQRCode(walletFile,identity1);  
			OntTest.logger().description(walletFile.toString());
			OntTest.logger().description(QRcode.toString());
			
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_abnormal_006_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("助记词  006  exportIdentityQRCode()");

		try {
			OntTest.logger().step("测试参数exportIdentityQRCode_identity");
			
			Identity identity = null;
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			Map QRcode = WalletQR.exportIdentityQRCode(walletFile,identity);   
			OntTest.logger().description(QRcode.toString());
			assertEquals(true,false);
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//exportAccountQRCode007-012
	@Test
	public void test_base_007_exportAccountQRCode() throws Exception {
		OntTest.logger().description("助记词  007  exportAccountQRCode()");

		try {
			OntTest.logger().step("测试参数exportAccountQRCode_walletFile");
			
			Account account = OntTest.sdk().getWalletMgr().createAccount("123456");
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			Map QRcode = WalletQR.exportAccountQRCode(walletFile, account);
			OntTest.logger().description(QRcode.toString());
			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_008_exportAccountQRCode() throws Exception {
		OntTest.logger().description("助记词  008  exportAccountQRCode()");

		try {
			Identity identity = OntTest.sdk().getWalletMgr().createIdentity("123456");
			Identity identity1 = OntTest.sdk().getWalletMgr().createIdentity("123456");
			OntTest.sdk().getWalletMgr().getWallet().clearIdentity();
			OntTest.sdk().getWalletMgr().getWallet().clearAccount();
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			OntTest.logger().description(walletFile.toString());
			OntTest.logger().description(identity1.toString());
			
			Map QRcode = WalletQR.exportIdentityQRCode(walletFile,identity1);   
			OntTest.logger().description(QRcode.toString());
			
			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_009_exportAccountQRCode() throws Exception {
		OntTest.logger().description("助记词  009  exportAccountQRCode()");

		try {
			OntTest.logger().step("测试参数exportAccountQRCode_walletFile");
			
			Account account = OntTest.sdk().getWalletMgr().createAccount("123456");
			Wallet walletFile = null;
			
			Map QRcode = WalletQR.exportAccountQRCode(walletFile, account);
			OntTest.logger().description(QRcode.toString());
			assertEquals(true,false);
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		}  catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_010_exportAccountQRCode() throws Exception {
		OntTest.logger().description("助记词  010  exportAccountQRCode()");

		try {
			OntTest.logger().step("测试参数exportAccountQRCode_account");
			
			Account account = OntTest.sdk().getWalletMgr().createAccount("123456");
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			OntTest.logger().description(account.toString());
			OntTest.logger().description(walletFile.toString());
			
			Map QRcode = WalletQR.exportAccountQRCode(walletFile,account);   
			OntTest.logger().description(QRcode.toString());	
			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_011_exportAccountQRCode() throws Exception {
		OntTest.logger().description("助记词  011  exportAccountQRCode()");

		try {
			OntTest.logger().step("测试参数exportAccountQRCode_account");
			
			Account account = OntTest.sdk().getWalletMgr().createAccount("123456");
			Account account1 = OntTest.sdk().getWalletMgr().createAccount("123456");
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			walletFile.removeAccount(account1.address);
			
			OntTest.logger().description(account1.toString());
			OntTest.logger().description(walletFile.toString());
			
			Map QRcode = WalletQR.exportAccountQRCode(walletFile,account1);   
			OntTest.logger().description(QRcode.toString());	
			
			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_012_exportAccountQRCode() throws Exception {
		OntTest.logger().description("助记词  012  exportAccountQRCode()");

		try {
			OntTest.logger().step("测试参数exportAccountQRCode_account");
			
			Account account = null;
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();

			OntTest.logger().description(account.toString());
			OntTest.logger().description(walletFile.toString());
			
			Map QRcode = WalletQR.exportAccountQRCode(walletFile,account);   
			OntTest.logger().description(QRcode.toString());	
			assertEquals(true,false);
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		}  catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//getPriKeyFromQrCode013-019
	@Test
	public void test_base_013_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("助记词  013  getPriKeyFromQrCode()");

		try {
			Identity identity = OntTest.sdk().getWalletMgr().createIdentity("123456");
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			Map QRcode_map = WalletQR.exportIdentityQRCode(walletFile,identity); 
			String qrcode = JSONObject.toJSONString(QRcode_map);
			OntTest.logger().description("QRcode= "+qrcode);
			String password = "123456";
			String PriKey = WalletQR.getPriKeyFromQrCode(qrcode, password);
			
			OntTest.logger().description("PriKey = "+PriKey);
			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_014_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("助记词  014  getPriKeyFromQrCode()");

		try {
//			Identity identity = OntTest.sdk().getWalletMgr().createIdentity("123456");
//			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
//			
//			Map QRcode_map = WalletQR.exportIdentityQRCode(walletFile,identity); 
//			String qrcode = JSONObject.toJSONString(QRcode_map);
			String qrcode = "aaaaaaa";
			OntTest.logger().description("QRcode= "+qrcode);
			String password = "123456";
			String PriKey = WalletQR.getPriKeyFromQrCode(qrcode, password);
			
			OntTest.logger().description("PriKey = "+PriKey);
			assertEquals(true,false);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_015_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("助记词  015  getPriKeyFromQrCode()");

		try {
			String qrcode = "";
			String password = "123456";
			String PriKey = WalletQR.getPriKeyFromQrCode(qrcode, password);
			
			OntTest.logger().description("PriKey = "+PriKey);
			assertEquals(true,false);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_016_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("助记词  016  getPriKeyFromQrCode()");

		try {
			Identity identity = OntTest.sdk().getWalletMgr().createIdentity("123456");
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			Map QRcode_map = WalletQR.exportIdentityQRCode(walletFile,identity); 
			String qrcode = JSONObject.toJSONString(QRcode_map);
			OntTest.logger().description("QRcode= "+qrcode);
			String password = "123456";
			String PriKey = WalletQR.getPriKeyFromQrCode(qrcode, password);
			
			OntTest.logger().description("PriKey = "+PriKey);
			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_017_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("助记词  017  getPriKeyFromQrCode()");

		try {
			Identity identity = OntTest.sdk().getWalletMgr().createIdentity("123456");
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			Map QRcode_map = WalletQR.exportIdentityQRCode(walletFile,identity); 
			String qrcode = JSONObject.toJSONString(QRcode_map);
			OntTest.logger().description("QRcode= "+qrcode);
			String password = "111111";
			String PriKey = WalletQR.getPriKeyFromQrCode(qrcode, password);			
			OntTest.logger().description("PriKey = "+PriKey);
			assertEquals(true, PriKey == null);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 51015;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_018_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("助记词  018  getPriKeyFromQrCode()");

		try {
			Identity identity = OntTest.sdk().getWalletMgr().createIdentity("123456");
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			Map QRcode_map = WalletQR.exportIdentityQRCode(walletFile,identity); 
			String qrcode = JSONObject.toJSONString(QRcode_map);
			OntTest.logger().description("QRcode= "+qrcode);
			String password = "@#$%^&";
			String PriKey = WalletQR.getPriKeyFromQrCode(qrcode, password);			
			OntTest.logger().description("PriKey = "+PriKey);
			assertEquals(true, PriKey == null);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 51015;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_019_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("助记词  019  getPriKeyFromQrCode()");

		try {
			Identity identity = OntTest.sdk().getWalletMgr().createIdentity("123456");
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			Map QRcode_map = WalletQR.exportIdentityQRCode(walletFile,identity); 
			String qrcode = JSONObject.toJSONString(QRcode_map);
			OntTest.logger().description("QRcode= "+qrcode);
			String password = "";
			String PriKey = WalletQR.getPriKeyFromQrCode(qrcode, password);
			OntTest.logger().description("PriKey = "+PriKey);
			assertEquals(true, PriKey == null);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 51015;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//generateMnemonicCodesStr020
	@Test
	public void test_base_020_generateMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  020  generateMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数generateMnemonicCodesStr");
			
			String codesStr = MnemonicCode.generateMnemonicCodesStr();
			OntTest.logger().description(codesStr);
//			assertEquals(true,ret.equals(exp));
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//getSeedFromMnemonicCodesStr021-025
	@Test
	public void test_base_021_getSeedFromMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  021  getSeedFromMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数getSeedFromMnemonicCodesStr_mnemonicCodesStr");
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			
			byte[] byte_seed = MnemonicCode.getSeedFromMnemonicCodesStr(mnemonicCodesStr);
			OntTest.logger().description("length = "+byte_seed.length);
			String ret = DatatypeConverter.printHexBinary(byte_seed);
			OntTest.logger().description(ret);
			
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_022_getSeedFromMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  022  getSeedFromMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数getSeedFromMnemonicCodesStr_mnemonicCodesStr");
			String mnemonicCodesStr = "!@#$$% smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			//包含非法字符
			
			byte[] byte_seed = MnemonicCode.getSeedFromMnemonicCodesStr(mnemonicCodesStr);
			System.out.println(byte_seed.length);
			String ret = DatatypeConverter.printHexBinary(byte_seed);
			OntTest.logger().description(ret);
			
			assertEquals(true,false);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}		
	
	@Test
	public void test_abnormal_023_getSeedFromMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  023  getSeedFromMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数getSeedFromMnemonicCodesStr_mnemonicCodesStr");
			String mnemonicCodesStr = "smooth salt lecture trophy wrong narrow chief pattern main retreat smooth mine craft";
			//多余一个助记词
			
			byte[] byte_seed = MnemonicCode.getSeedFromMnemonicCodesStr(mnemonicCodesStr);
			System.out.println(byte_seed.length);
			String ret = DatatypeConverter.printHexBinary(byte_seed);
			OntTest.logger().description(ret);
			
			assertEquals(true,false);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_024_getSeedFromMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  024  getSeedFromMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数getSeedFromMnemonicCodesStr_mnemonicCodesStr");
			String mnemonicCodesStr = "smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			//缺少一个助记词
			
			byte[] byte_seed = MnemonicCode.getSeedFromMnemonicCodesStr(mnemonicCodesStr);
			System.out.println(byte_seed.length);
			String ret = DatatypeConverter.printHexBinary(byte_seed);
			OntTest.logger().description(ret);
			
			assertEquals(true,false);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_025_getSeedFromMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  025  getSeedFromMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数getSeedFromMnemonicCodesStr_mnemonicCodesStr");
			String mnemonicCodesStr = "";
			//助记词不存在
			
			byte[] byte_seed = MnemonicCode.getSeedFromMnemonicCodesStr(mnemonicCodesStr);
			System.out.println(byte_seed.length);
			String ret = DatatypeConverter.printHexBinary(byte_seed);
			OntTest.logger().description(ret);
			
			assertEquals(true,false);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	//getPrikeyFromMnemonicCodesStrBip44 026-030
	@Test
	public void test_base_026_getPrikeyFromMnemonicCodesStrBip44() throws Exception {
		OntTest.logger().description("助记词  026  getPrikeyFromMnemonicCodesStrBip44()");

		try {
			OntTest.logger().step("测试参数getPrikeyFromMnemonicCodesStrBip44_mnemonicCodesStr");
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			
			byte[] byte_seed = MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
			System.out.println(byte_seed.length);
			String ret = DatatypeConverter.printHexBinary(byte_seed);
			OntTest.logger().description(ret);
			
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_027_getPrikeyFromMnemonicCodesStrBip44() throws Exception {
		OntTest.logger().description("助记词  027  getPrikeyFromMnemonicCodesStrBip44()");

		try {
			OntTest.logger().step("测试参数getPrikeyFromMnemonicCodesStrBip44_mnemonicCodesStr");
			String mnemonicCodesStr = "!@#$ smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			
			byte[] byte_seed = MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
			System.out.println(byte_seed.length);
			String ret = DatatypeConverter.printHexBinary(byte_seed);
			OntTest.logger().description(ret);
			
			assertEquals(true,false);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_028_getPrikeyFromMnemonicCodesStrBip44() throws Exception {
		OntTest.logger().description("助记词  028  getPrikeyFromMnemonicCodesStrBip44()");

		try {
			OntTest.logger().step("测试参数getPrikeyFromMnemonicCodesStrBip44_mnemonicCodesStr");
			String mnemonicCodesStr = "mine polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			
			byte[] byte_Prikey = MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
			System.out.println(byte_Prikey.length);
			String ret = DatatypeConverter.printHexBinary(byte_Prikey);
			OntTest.logger().description(ret);
			
			assertEquals(true,false);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_029_getPrikeyFromMnemonicCodesStrBip44() throws Exception {
		OntTest.logger().description("助记词  029  getPrikeyFromMnemonicCodesStrBip44()");

		try {
			OntTest.logger().step("测试参数getPrikeyFromMnemonicCodesStrBip44_mnemonicCodesStr");
			String mnemonicCodesStr = "smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			
			byte[] byte_seed = MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
			System.out.println(byte_seed.length);
			String ret = DatatypeConverter.printHexBinary(byte_seed);
			OntTest.logger().description(ret);
			
			assertEquals(true,false);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_030_getPrikeyFromMnemonicCodesStrBip44() throws Exception {
		OntTest.logger().description("助记词  030  getPrikeyFromMnemonicCodesStrBip44()");

		try {
			OntTest.logger().step("测试参数getPrikeyFromMnemonicCodesStrBip44_mnemonicCodesStr");
			String mnemonicCodesStr = "";
			
			byte[] byte_Prikey = MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
			System.out.println(byte_Prikey.length);
			String ret = DatatypeConverter.printHexBinary(byte_Prikey);
			OntTest.logger().description(ret);
			assertEquals(true,false);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//encryptMnemonicCodesStr 031-044
	@Test
	public void test_base_031_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  031  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_mnemonicCodesStr");
			
			String password = "123456";
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);

			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_032_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  032  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_mnemonicCodesStr");
			String password = "123456";
			String mnemonicCodesStr = "@#$%^ smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
			
	        assertEquals(true,false);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_033_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  033  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_mnemonicCodesStr");
			String password = "123456";
			String mnemonicCodesStr = "mine polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);	
			assertEquals(true,false);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_034_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  034  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_mnemonicCodesStr");
			String password = "123456";
			String mnemonicCodesStr = "salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
			assertEquals(true,false);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_035_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  035  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_mnemonicCodesStr");
			String password = "123456";
			String mnemonicCodesStr = "";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);

			assertEquals(true,false);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_036_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  036  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_password");
			String password = "123456";
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_037_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  037  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_password");
			String password = "111111";
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_038_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  038  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_password");
			String password = "@#$%^";
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_039_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  039  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_password");
			String password = "";
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_040_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  040  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_password");
			String password = "123456";
			String mnemonicCodesStr = MnemonicCode.generateMnemonicCodesStr();
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_041_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  041  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_address");
			String password = "123456";
			String mnemonicCodesStr = MnemonicCode.generateMnemonicCodesStr();
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String address = account.getAddressU160().toBase58();
	        address = address.substring(0,address.length()-3)+"abc";
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
			assertEquals(true,false);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_042_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  042  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_address");
			String password = "123456";
			String mnemonicCodesStr = MnemonicCode.generateMnemonicCodesStr();
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String address = account.getAddressU160().toBase58();
	        address = "a"+address;
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
			assertEquals(true,false);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_043_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  043  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_address");
			String password = "123456";
			String mnemonicCodesStr = MnemonicCode.generateMnemonicCodesStr();
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String address = account.getAddressU160().toBase58();
	        address = address.substring(0,address.length()-3)+"@#$";
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
			assertEquals(true,false);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_044_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  044  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_address");
			String password = "123456";
			String mnemonicCodesStr = MnemonicCode.generateMnemonicCodesStr();
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, "");
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
			assertEquals(true,false);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_base_045_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  045  decryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_decryptMnemonicCodesStr");
			
			String password = "123456";
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
	        String decryptStr = com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, account.getAddressU160().toBase58());
			OntTest.logger().description("decryptStr = "+decryptStr);
			assertEquals(true,decryptStr.equals(mnemonicCodesStr));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	

	@Test
	public void test_abnormal_046_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  046  decryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数decryptMnemonicCodesStr_encryptedMnemonicCodesStr");
			
			String password = "123456";
			String mnemonicCodesStr = com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        encryptedStr = encryptedStr.substring(0,encryptedStr.length()-3)+"@#$";
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
	        String decryptStr = com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, account.getAddressU160().toBase58());
			OntTest.logger().description("decryptStr = "+decryptStr);
			
			//assertEquals(false,decryptStr.equals(mnemonicCodesStr));
			assertTrue(false);
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_047_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  047  decryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数decryptMnemonicCodesStr_encryptedMnemonicCodesStr");
			
			String password = "123456";
			String mnemonicCodesStr = com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        encryptedStr = "a" + encryptedStr;
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
	        String decryptStr = com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, account.getAddressU160().toBase58());
			OntTest.logger().description("decryptStr = "+decryptStr);
			
			//assertEquals(false,decryptStr.equals(mnemonicCodesStr));
			assertTrue(false);
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_048_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  048  decryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数decryptMnemonicCodesStr_encryptedMnemonicCodesStr");
			
			String password = "123456";
			String mnemonicCodesStr = com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        encryptedStr = encryptedStr.substring(0,encryptedStr.length()-1);
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
	        String decryptStr = com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, account.getAddressU160().toBase58());
			OntTest.logger().description("decryptStr = "+decryptStr);
			
			//assertEquals(false,decryptStr.equals(mnemonicCodesStr));	
			assertTrue(false);
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_049_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  049  decryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数decryptMnemonicCodesStr_encryptedMnemonicCodesStr");
			
			String password = "123456";
			String mnemonicCodesStr = com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = "";
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
	        String decryptStr = com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, account.getAddressU160().toBase58());
			OntTest.logger().description("decryptStr = "+decryptStr);
			
			//assertEquals(true,decryptStr.equals(mnemonicCodesStr));	
			assertTrue(false);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 51014;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_050_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  050  decryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数decryptMnemonicCodesStr_password");
			
			String password = "123456";
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
	        String decryptStr = com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, account.getAddressU160().toBase58());
			OntTest.logger().description("decryptStr = "+decryptStr);
			
			assertEquals(true,decryptStr.equals(mnemonicCodesStr));	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_abnormal_051_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  051  decryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数decryptMnemonicCodesStr_password");
			
			String password = "123456";
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
	        String decryptStr = com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedStr, "111111", account.getAddressU160().toBase58());
			OntTest.logger().description("decryptStr = "+decryptStr);
			
			//assertEquals(true,decryptStr.equals(mnemonicCodesStr));	
			assertTrue(false);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			String exp_err = "com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"Account Error,Prikey length error\",\"Error\":51014}";
			OntTest.logger().error(e.toString());
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_052_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  052  decryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数decryptMnemonicCodesStr_password");
			
			String password = "123456";
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
	        String decryptStr = com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedStr, "!@#$%^", account.getAddressU160().toBase58());
			System.out.println("decryptStr = "+decryptStr);
			
			//assertEquals(true,decryptStr.equals(mnemonicCodesStr));	
			assertTrue(false);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 51014;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_053_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  053  decryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数decryptMnemonicCodesStr_password");
			
			String password = "123456";
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
	        String decryptStr = com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedStr, "", account.getAddressU160().toBase58());
			OntTest.logger().description("decryptStr = "+decryptStr);
			
			//assertEquals(true,decryptStr.equals(mnemonicCodesStr));	
			assertTrue(false);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 51014;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_054_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  054  decryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数decryptMnemonicCodesStr_address");
			
			String password = "123456";
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
	        String decryptStr = com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, account.getAddressU160().toBase58());
			OntTest.logger().description("decryptStr = "+decryptStr);
			
			assertEquals(true,decryptStr.equals(mnemonicCodesStr));	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_abnormal_055_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  055  decryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数decryptMnemonicCodesStr_address");
			
			String password = "123456";
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
	        String address = account.getAddressU160().toBase58();
	        OntTest.logger().description("原地址为"+address);
	        address = address.substring(0,address.length()-3)+"666";
	        OntTest.logger().description("修改后地址为"+address);
	        String decryptStr = com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, address);
			OntTest.logger().description("decryptStr = "+decryptStr);
			
			//assertEquals(true,decryptStr.equals(mnemonicCodesStr));	
			assertTrue(false);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 51014;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_abnormal_056_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  056  decryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数decryptMnemonicCodesStr_address");
			
			String password = "123456";
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
	        String address = account.getAddressU160().toBase58();
	        OntTest.logger().description("原地址为"+address);
	        address = "a"+address;
	        OntTest.logger().description("修改后地址为"+address);
	        String decryptStr = com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, address);
			OntTest.logger().description("decryptStr = "+decryptStr);
			
			//assertEquals(true,decryptStr.equals(mnemonicCodesStr));	
			assertTrue(false);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 51014;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_057_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  057  decryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数decryptMnemonicCodesStr_address");
			
			String password = "123456";
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
	        String address = account.getAddressU160().toBase58();
	        OntTest.logger().description("原地址为"+address);
	        address = address.substring(0,address.length()-3)+"@#%";
	        OntTest.logger().description("修改后地址为"+address);
	        String decryptStr = com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, address);
			OntTest.logger().description("decryptStr = "+decryptStr);
			
			//assertEquals(true,decryptStr.equals(mnemonicCodesStr));	
			assertTrue(false);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 51014;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_058_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  058  decryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数decryptMnemonicCodesStr_address");
			
			String password = "123456";
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        String encryptedStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        OntTest.logger().description("encryptedStr = "+encryptedStr);
	        String address = "";
	        String decryptStr = com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, address);
			OntTest.logger().description("decryptStr = "+decryptStr);
			
			//assertEquals(true,decryptStr.equals(mnemonicCodesStr));	
			assertTrue(false);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 51014;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
}
