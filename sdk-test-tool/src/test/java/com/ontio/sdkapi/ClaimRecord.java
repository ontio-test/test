package com.ontio.sdkapi;

import static org.junit.Assert.fail;

import java.util.Arrays;
import java.util.Map;

import static org.junit.Assert.assertEquals;

import org.junit.*;

import com.alibaba.fastjson.JSONObject;
import com.github.ontio.sdk.exception.SDKException;
import com.github.ontio.sdk.wallet.Identity;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;

public class ClaimRecord {
@Rule public OntTestWatcher watchman= new OntTestWatcher();
    public static Identity identity = null;
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
		OntTest.api().node().restartAll();
		OntTest.api().node().initOntOng();
		
		try {
			String password = "123456";
			com.github.ontio.sdk.wallet.Account payer = OntTest.sdk().getWalletMgr().createAccount(password);
			com.github.ontio.account.Account payerAcct = OntTest.sdk().getWalletMgr().getAccount(payer.address,password,payer.getSalt());
			
			OntTest.logger().step("create identity");
			ClaimRecord.identity = OntTest.sdk().getWalletMgr().createIdentity(password);
			String tx1 = OntTest.sdk().nativevm().ontId().sendRegister(identity,password,payerAcct,OntTest.sdk().DEFAULT_GAS_LIMIT,0);
			OntTest.common().waitTransactionResult(tx1);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
		}
		
	}
	
	@Before
	public void setUp() throws Exception {
		System.out.println("setUp");
	}
	
	@After
	public void TearDown() throws Exception {
		System.out.println("TearDown");
	}
	
	@Test
	public void test_base_001_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("test_api   : exportIdentityQRCode");
		OntTest.logger().description("test_param : walletFile - correct walletFiles");

		try {
			com.github.ontio.sdk.wallet.Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
	
			Identity identity = ClaimRecord.identity;
			
	        OntTest.logger().step("export identity QRCode");
	        Map<?,?> ret = com.github.ontio.common.WalletQR.exportIdentityQRCode(walletFile, identity);
	        
	        System.out.println(ret.toString());
			
			assertEquals(false, ret == null);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_002_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("test_api   : exportIdentityQRCode");
		OntTest.logger().description("test_param : walletFile - wrong walletFiles");

		try {
			com.github.ontio.sdk.wallet.Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			System.out.println(walletFile.toString());
			walletFile.clearAccount();
			walletFile.clearIdentity();
			walletFile.setExtra("123456");
			System.out.println(walletFile.toString());
			
			Identity identity = ClaimRecord.identity;
	        
	        OntTest.logger().step("export identity QRCode");
	        Map<?,?> ret = com.github.ontio.common.WalletQR.exportIdentityQRCode(walletFile, identity);
	        
	        System.out.println(ret.toString());
			
	        assertEquals(false, ret == null);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_003_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("test_api   : exportIdentityQRCode");
		OntTest.logger().description("test_param : walletFile - null");

		try {			
			Identity identity = ClaimRecord.identity;
	        
	        OntTest.logger().step("export identity QRCode");
	        Map<?,?> ret = com.github.ontio.common.WalletQR.exportIdentityQRCode((com.github.ontio.sdk.wallet.Wallet)null, identity);
	        
	        System.out.println(ret.toString());
			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_004_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("test_api   : exportIdentityQRCode");
		OntTest.logger().description("test_param : identity - correct identity");

		try {
			com.github.ontio.sdk.wallet.Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			Identity identity = ClaimRecord.identity;
	        
	        OntTest.logger().step("export identity QRCode");
	        Map<?,?> ret = com.github.ontio.common.WalletQR.exportIdentityQRCode(walletFile, identity);
	        
	        System.out.println(ret.toString());
			
			assertEquals(false, ret == null);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	/*
	@Test
	public void test_abnormal_005_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("test_api   : exportIdentityQRCode");
		OntTest.logger().description("test_param : identity - wrong identity");

		try {
			String password = "123456";
			com.github.ontio.sdk.wallet.Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			com.github.ontio.sdk.wallet.Account payer = OntTest.sdk().getWalletMgr().createAccount(password);
			com.github.ontio.account.Account payerAcct = OntTest.sdk().getWalletMgr().getAccount(payer.address,password,payer.getSalt());
			
			OntTest.logger().step("create identity");
			Identity identity = OntTest.sdk().getWalletMgr().createIdentity(password);
			OntTest.sdk().nativevm().ontId().sendRegister(identity,password,payerAcct,OntTest.sdk().DEFAULT_GAS_LIMIT,0);
	        Thread.sleep(6000);
	        System.out.println(identity.toString());
	        	        
	        OntTest.logger().step("export identity QRCode");
	        Map<?,?> ret = com.github.ontio.common.WalletQR.exportIdentityQRCode(walletFile, identity);
	        
	        System.out.println(ret.toString());
			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	*/
	@Test
	public void test_abnormal_006_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("test_api   : exportIdentityQRCode");
		OntTest.logger().description("test_param : identity - null");

		try {
			com.github.ontio.sdk.wallet.Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
	        OntTest.logger().step("export identity QRCode");
	        Map<?,?> ret = com.github.ontio.common.WalletQR.exportIdentityQRCode(walletFile, null);
	        
	        System.out.println(ret.toString());
			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_007_exportAccountQRCode() throws Exception {
		OntTest.logger().description("test_api   : exportAccountQRCode");
		OntTest.logger().description("test_param : walletFile - correct walletFiles");

		try {
			String password = "123456";
			com.github.ontio.sdk.wallet.Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			OntTest.logger().step("get account");
			com.github.ontio.sdk.wallet.Account account = OntTest.sdk().getWalletMgr().createAccount(password);
			    
	        OntTest.logger().step("export account QRCode");
	        Map<?,?> ret = com.github.ontio.common.WalletQR.exportAccountQRCode(walletFile, account);
	        
	        System.out.println(ret.toString());
			
			assertEquals(false, ret == null);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_008_exportAccountQRCode() throws Exception {
		OntTest.logger().description("test_api   : exportAccountQRCode");
		OntTest.logger().description("test_param : walletFile - wrong walletFiles");

		try {
			String password = "123456";
			com.github.ontio.sdk.wallet.Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			System.out.println(walletFile.toString());
			walletFile.clearAccount();
			walletFile.clearIdentity();
			walletFile.setExtra("123456");
			System.out.println(walletFile.toString());
			
			OntTest.logger().step("get account");
			com.github.ontio.sdk.wallet.Account account = OntTest.sdk().getWalletMgr().createAccount(password);
			    
	        OntTest.logger().step("export account QRCode");
	        Map<?,?> ret = com.github.ontio.common.WalletQR.exportAccountQRCode(walletFile, account);
	        
	        System.out.println(ret.toString());
			
			assertEquals(false, ret == null);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_009_exportAccountQRCode() throws Exception {
		OntTest.logger().description("test_api   : exportAccountQRCode");
		OntTest.logger().description("test_param : walletFile - null");

		try {
			String password = "123456";
			
			OntTest.logger().step("get account");
			com.github.ontio.sdk.wallet.Account account = OntTest.sdk().getWalletMgr().createAccount(password);
			    
	        OntTest.logger().step("export account QRCode");
	        Map<?,?> ret = com.github.ontio.common.WalletQR.exportAccountQRCode((com.github.ontio.sdk.wallet.Wallet)null, account);
	        
	        System.out.println(ret.toString());
			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_010_exportAccountQRCode() throws Exception {
		OntTest.logger().description("test_api   : exportAccountQRCode");
		OntTest.logger().description("test_param : account - correct account");

		try {
			String password = "1234567";
			com.github.ontio.sdk.wallet.Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			OntTest.logger().step("get account");
			com.github.ontio.sdk.wallet.Account account = OntTest.sdk().getWalletMgr().createAccount(password);
			    
	        OntTest.logger().step("export account QRCode");
	        Map<?,?> ret = com.github.ontio.common.WalletQR.exportAccountQRCode(walletFile, account);
	        
	        System.out.println(ret.toString());
			
			assertEquals(false, ret == null);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	/*
	@Test
	public void test_abnormal_011_exportAccountQRCode() throws Exception {
		OntTest.logger().description("test_api   : exportAccountQRCode");
		OntTest.logger().description("test_param : account - wrong account");

		try {
			String password = "123456";
			com.github.ontio.sdk.wallet.Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			OntTest.logger().step("get account");
			com.github.ontio.sdk.wallet.Account account = OntTest.sdk().getWalletMgr().createAccount(password);
			OntTest.sdk().getWalletMgr().getWallet().removeAccount(account.address);

	        OntTest.logger().step("export account QRCode");
	        Map<?,?> ret = com.github.ontio.common.WalletQR.exportAccountQRCode(walletFile, account);
	        
	        System.out.println(ret.toString());
			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	*/
	@Test
	public void test_abnormal_012_exportAccountQRCode() throws Exception {
		OntTest.logger().description("test_api   : exportAccountQRCode");
		OntTest.logger().description("test_param : account - null");

		try {
			com.github.ontio.sdk.wallet.Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
	        OntTest.logger().step("export account QRCode");
	        Map<?,?> ret = com.github.ontio.common.WalletQR.exportAccountQRCode(walletFile, null);
	        
	        System.out.println(ret.toString());
			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_013_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("test_api   : getPriKeyFromQrCode");
		OntTest.logger().description("test_param : qrcode - correct qrcode");

		try {
			String password = "123456";
			com.github.ontio.sdk.wallet.Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			OntTest.logger().step("get account");
			com.github.ontio.sdk.wallet.Account account = OntTest.sdk().getWalletMgr().createAccount(password);
			    
	        OntTest.logger().step("export account QRCode");
	        Map<?,?> qrcode = com.github.ontio.common.WalletQR.exportAccountQRCode(walletFile, account);
			    
	        OntTest.logger().step("get private Key from QrCode");
	        String ret= com.github.ontio.common.WalletQR.getPriKeyFromQrCode(JSONObject.toJSONString(qrcode), password);
	        
	        System.out.println(ret);
			
			assertEquals(false, ret == null);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	/*
	@Test
	public void test_abnormal_014_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("test_api   : getPriKeyFromQrCode");
		OntTest.logger().description("test_param : qrcode - wrong qrcode 123");

		try {
			String password = "123456";
			com.github.ontio.sdk.wallet.Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			OntTest.logger().step("get account");
			com.github.ontio.sdk.wallet.Account account = OntTest.sdk().getWalletMgr().createAccount(password);
			    
	        OntTest.logger().step("export account QRCode");
	        Map<?,?> qrcode = com.github.ontio.common.WalletQR.exportAccountQRCode(walletFile, account);
	        			    
	        OntTest.logger().step("get private Key from QrCode");
	        String ret= com.github.ontio.common.WalletQR.getPriKeyFromQrCode((String)123, password);
	        
	        System.out.println(ret);
			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	*/
	
	@Test
	public void test_abnormal_015_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("test_api   : getPriKeyFromQrCode");
		OntTest.logger().description("test_param : qrcode - wrong qrcode messy code");

		try {
			String password = "123456";
			    
	        OntTest.logger().step("get private Key from QrCode");
	        String ret= com.github.ontio.common.WalletQR.getPriKeyFromQrCode("abcd1234", password);
	        
	        System.out.println(ret);
			
			assertEquals(true, ret == null);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_016_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("test_api   : getPriKeyFromQrCode");
		OntTest.logger().description("test_param : qrcode - null");

		try {
			String password = "123456";
	        			    
	        OntTest.logger().step("get private Key from QrCode");
	        String ret= com.github.ontio.common.WalletQR.getPriKeyFromQrCode("", password);
	        
	        System.out.println(ret);
			
			assertEquals(true, ret == null);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_017_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("test_api   : getPriKeyFromQrCode");
		OntTest.logger().description("test_param : password - correct password");

		try {
			String password = "123456";
			com.github.ontio.sdk.wallet.Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			OntTest.logger().step("get account");
			com.github.ontio.sdk.wallet.Account account = OntTest.sdk().getWalletMgr().createAccount(password);
			   
	        OntTest.logger().step("export account QRCode");
	        Map<?,?> qrcode = com.github.ontio.common.WalletQR.exportAccountQRCode(walletFile, account);
	        			    
	        OntTest.logger().step("get private Key from QrCode");
	        String ret= com.github.ontio.common.WalletQR.getPriKeyFromQrCode(JSONObject.toJSONString(qrcode), password);
	        
	        System.out.println(ret);
			
	        assertEquals(false, ret == null);		
	        
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_018_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("test_api   : getPriKeyFromQrCode");
		OntTest.logger().description("test_param : password - correct password");

		try {
			String password = "123456";
			com.github.ontio.sdk.wallet.Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			OntTest.logger().step("get account");
			com.github.ontio.sdk.wallet.Account account = OntTest.sdk().getWalletMgr().createAccount(password);
			   
	        OntTest.logger().step("export account QRCode");
	        Map<?,?> qrcode = com.github.ontio.common.WalletQR.exportAccountQRCode(walletFile, account);
	        			    
	        OntTest.logger().step("get private Key from QrCode");
	        String ret= com.github.ontio.common.WalletQR.getPriKeyFromQrCode(JSONObject.toJSONString(qrcode), "12345");
	        			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_019_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("test_api   : getPriKeyFromQrCode");
		OntTest.logger().description("test_param : password - wrong password");

		try {
			String password = "123456";
			com.github.ontio.sdk.wallet.Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			OntTest.logger().step("get account");
			com.github.ontio.sdk.wallet.Account account = OntTest.sdk().getWalletMgr().createAccount(password);
			   
	        OntTest.logger().step("export account QRCode");
	        Map<?,?> qrcode = com.github.ontio.common.WalletQR.exportAccountQRCode(walletFile, account);
	        			    
	        OntTest.logger().step("get private Key from QrCode");
	        String ret= com.github.ontio.common.WalletQR.getPriKeyFromQrCode(JSONObject.toJSONString(qrcode), "!@#$%^");
	        			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_020_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("test_api   : getPriKeyFromQrCode");
		OntTest.logger().description("test_param : password - null");

		try {
			String password = "123456";
			com.github.ontio.sdk.wallet.Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			OntTest.logger().step("get account");
			com.github.ontio.sdk.wallet.Account account = OntTest.sdk().getWalletMgr().createAccount(password);
			   
	        OntTest.logger().step("export account QRCode");
	        Map<?,?> qrcode = com.github.ontio.common.WalletQR.exportAccountQRCode(walletFile, account);
	        			    
	        OntTest.logger().step("get private Key from QrCode");
	        String ret= com.github.ontio.common.WalletQR.getPriKeyFromQrCode(JSONObject.toJSONString(qrcode), "");
	        			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_021_generateMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : generateMnemonicCodesStr");
		try {
			
			OntTest.logger().step("generate mnemonic codes string");
	        String ret= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        System.out.println("output:" + ret);
			
			assertEquals(false, ret == null);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_022_getSeedFromMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : getSeedFromMnemonicCodesStr");
		OntTest.logger().description("test_param : mnemonicCodesStr - correct mnemonicCodesStr");
		try {
			
			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        System.out.println(mnemonicCodesStr);
	        
	        OntTest.logger().step("get seed from mnemonic codes string");
	        byte[] ret = com.github.ontio.crypto.MnemonicCode.getSeedFromMnemonicCodesStr(mnemonicCodesStr);
	        
	        System.out.println(Arrays.toString(ret));
			
			assertEquals(false, ret == null);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_023_getSeedFromMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : getSeedFromMnemonicCodesStr");
		OntTest.logger().description("test_param : mnemonicCodesStr - wrong mnemonicCodesStr messy code");
		try {
	        
	        OntTest.logger().step("get seed from mnemonic codes string");
	        byte[] ret = com.github.ontio.crypto.MnemonicCode.getSeedFromMnemonicCodesStr("!@#$qwer");
	        
	        System.out.println(Arrays.toString(ret));
			
			assertEquals(true, ret == null);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_024_getSeedFromMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : getSeedFromMnemonicCodesStr");
		OntTest.logger().description("test_param : mnemonicCodesStr - null mnemonicCodesStr");
		try {
	        
	        OntTest.logger().step("get seed from mnemonic codes string");
	        byte[] ret = com.github.ontio.crypto.MnemonicCode.getSeedFromMnemonicCodesStr("");
	        
	        System.out.println(Arrays.toString(ret));
			
			assertEquals(true, ret == null);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_025_getPrikeyFromMnemonicCodesStrBip44() throws Exception {
		OntTest.logger().description("test_api   : getPrikeyFromMnemonicCodesStrBip44");
		OntTest.logger().description("test_param : mnemonicCodesStr - correct mnemonicCodesStr");
		try {
			
			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("get private key from mnemonic codes string");
	        byte[] ret = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        
	        System.out.println(Arrays.toString(ret));
			
			assertEquals(false, ret == null);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_026_getPrikeyFromMnemonicCodesStrBip44() throws Exception {
		OntTest.logger().description("test_api   : getPrikeyFromMnemonicCodesStrBip44");
		OntTest.logger().description("test_param : mnemonicCodesStr - wrong mnemonicCodesStr messy code");
		try {
	        
	        OntTest.logger().step("get private key from mnemonic codes string");
	        byte[] ret = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44("qwertasdfg");
	        
	        System.out.println(Arrays.toString(ret));
			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_027_getPrikeyFromMnemonicCodesStrBip44r() throws Exception {
		OntTest.logger().description("test_api   : getPrikeyFromMnemonicCodesStrBip44");
		OntTest.logger().description("test_param : mnemonicCodesStr - null mnemonicCodesStr");
		try {
	        
	        OntTest.logger().step("get private key from mnemonic codes string");
	        byte[] ret = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44("");
	        
	        System.out.println(Arrays.toString(ret));
			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_028_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : encryptMnemonicCodesStr");
		OntTest.logger().description("test_param : mnemonicCodesStr - correct mnemonicCodesStr");
		try {
			String password = "123456";
			
			OntTest.logger().step("create account");
			com.github.ontio.sdk.wallet.Account payer = OntTest.sdk().getWalletMgr().createAccount(password);
			
			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String ret = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, payer.address);
	        
	        System.out.println(ret.toString());
			
	        assertEquals(false, ret == null);	
	        
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_029_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : encryptMnemonicCodesStr");
		OntTest.logger().description("test_param : mnemonicCodesStr - wrong mnemonicCodesStr");
		try {
			String password = "123456";
			
			OntTest.logger().step("create account");
			com.github.ontio.sdk.wallet.Account payer = OntTest.sdk().getWalletMgr().createAccount(password);
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String ret = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr("!@#$1234abcd", password, payer.address);
	        
	        System.out.println(ret.toString());
			
	        assertEquals(true, false);
	        
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_030_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : encryptMnemonicCodesStr");
		OntTest.logger().description("test_param : mnemonicCodesStr - null");
		try {
			String password = "123456";
			
			OntTest.logger().step("create account");
			com.github.ontio.sdk.wallet.Account payer = OntTest.sdk().getWalletMgr().createAccount(password);
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String ret = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr("", password, payer.address);
	        
	        System.out.println(ret.toString());
			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_031_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : encryptMnemonicCodesStr");
		OntTest.logger().description("test_param : password - correct password");
		try {
			String password = "123456";
			
			OntTest.logger().step("create account");
			com.github.ontio.sdk.wallet.Account payer = OntTest.sdk().getWalletMgr().createAccount(password);
			
			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String ret = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, payer.address);
	        
	        System.out.println(ret.toString());
			
			assertEquals(false, ret == null);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_032_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : encryptMnemonicCodesStr");
		OntTest.logger().description("test_param : password - wrong password 12345");
		try {
			String password = "123456";
			
			OntTest.logger().step("create account");
			com.github.ontio.sdk.wallet.Account payer = OntTest.sdk().getWalletMgr().createAccount(password);
			
			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String ret = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, "12345", payer.address);
	        
	        System.out.println(ret.toString());
			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_033_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : encryptMnemonicCodesStr");
		OntTest.logger().description("test_param : password - wrong password messy code");
		try {
			String password = "123456";
			
			OntTest.logger().step("create account");
			com.github.ontio.sdk.wallet.Account payer = OntTest.sdk().getWalletMgr().createAccount(password);
			
			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String ret = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, "!@#$1234", payer.address);
	        
	        System.out.println(ret.toString());
			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_034_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : encryptMnemonicCodesStr");
		OntTest.logger().description("test_param : password - null");
		try {
			String password = "123456";
			
			OntTest.logger().step("create account");
			com.github.ontio.sdk.wallet.Account payer = OntTest.sdk().getWalletMgr().createAccount(password);
			
			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String ret = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, "", payer.address);
	        
	        System.out.println(ret.toString());
			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_035_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : encryptMnemonicCodesStr");
		OntTest.logger().description("test_param : address - correct address");
		try {
			String password = "123456";
			
			OntTest.logger().step("create account");
			com.github.ontio.sdk.wallet.Account payer = OntTest.sdk().getWalletMgr().createAccount(password);
			
			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String ret = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, payer.address);
	        
	        System.out.println(ret.toString());
			
			assertEquals(false, ret == null);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_036_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : encryptMnemonicCodesStr");
		OntTest.logger().description("test_param : address - wrong address messy code with 34 bytes");
		try {
			String password = "123456";
			
			OntTest.logger().step("create account");
			com.github.ontio.sdk.wallet.Account payer = OntTest.sdk().getWalletMgr().createAccount(password);
			
			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        StringBuilder new_address = new StringBuilder(payer.address);
	        new_address.setCharAt(0, 'f');
	        new_address.setCharAt(1, 'f');
	        new_address.setCharAt(2, 'f');
	        new_address.setCharAt(3, 'f');
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String ret = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, new_address.toString());
	        
	        System.out.println(ret.toString());
			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_037_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : encryptMnemonicCodesStr");
		OntTest.logger().description("test_param : address - wrong address with 35 chars");
		try {
			String password = "123456";
			
			OntTest.logger().step("create account");
			com.github.ontio.sdk.wallet.Account payer = OntTest.sdk().getWalletMgr().createAccount(password);
			
			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String ret = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, payer.address+"1");
	        
	        System.out.println(ret.toString());
			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_038_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : encryptMnemonicCodesStr");
		OntTest.logger().description("test_param : address - wrong address messy code with 34 chars of [%$#]");
		try {
			String password = "123456";
			
			OntTest.logger().step("create account");
			com.github.ontio.sdk.wallet.Account payer = OntTest.sdk().getWalletMgr().createAccount(password);
			
			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        StringBuilder new_address = new StringBuilder(payer.address);
	        new_address.setCharAt(0, '%');
	        new_address.setCharAt(1, '$');
	        new_address.setCharAt(2, '@');
	        new_address.setCharAt(3, '#');
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String ret = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, new_address.toString());
	        
	        System.out.println(ret.toString());
			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_039_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : encryptMnemonicCodesStr");
		OntTest.logger().description("test_param : address - null");
		try {
			String password = "123456";
			
			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String ret = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, "");
	        
	        System.out.println(ret.toString());
			
			assertEquals(true, ret == null);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_040_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : decryptMnemonicCodesStr");
		OntTest.logger().description("test_param : encryptedMnemonicCodesStr - correct encryptedMnemonicCodesStr");
		try {
			String password = "123456";

			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("get private key");
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        
	        OntTest.logger().step("get account");
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String encryptedMnemonicCodesStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        
	        OntTest.logger().step("decrypt mnemonic codes string");
	        com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedMnemonicCodesStr, password, account.getAddressU160().toBase58());
	        			
			assertEquals(true, true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_041_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : decryptMnemonicCodesStr");
		OntTest.logger().description("test_param : encryptedMnemonicCodesStr - wrong encryptedMnemonicCodesStr messy code");
		try {
			String password = "123456";

			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("get private key");
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        
	        OntTest.logger().step("get account");
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String encryptedMnemonicCodesStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        
	        StringBuilder new_encryptedMnemonicCodesStr = new StringBuilder(encryptedMnemonicCodesStr);
	        new_encryptedMnemonicCodesStr.setCharAt(0, '!');
	        new_encryptedMnemonicCodesStr.setCharAt(1, '@');
	        new_encryptedMnemonicCodesStr.setCharAt(2, '#');
	        new_encryptedMnemonicCodesStr.setCharAt(3, '$');
	        
	        OntTest.logger().step("decrypt mnemonic codes string");
	        com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(new_encryptedMnemonicCodesStr.toString(), password, account.getAddressU160().toBase58());
	        
	        assertEquals(true, false);
	        
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_042_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : decryptMnemonicCodesStr");
		OntTest.logger().description("test_param : encryptedMnemonicCodesStr - null");
		try {
			String password = "123456";

			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("get private key");
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        
			
			OntTest.logger().step("get account");
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        
	        OntTest.logger().step("decrypt mnemonic codes string");
	        com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr("", password, account.getAddressU160().toBase58());
	        			
	        assertEquals(true, false);
	        
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_043_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : decryptMnemonicCodesStr");
		OntTest.logger().description("test_param : password - correct password");
		try {
			String password = "123456";

			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("get private key");
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        
	        OntTest.logger().step("get account");
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String encryptedMnemonicCodesStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        
	        OntTest.logger().step("decrypt mnemonic codes string");
	        com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedMnemonicCodesStr, password, account.getAddressU160().toBase58());
	        			
			assertEquals(true, true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_044_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : decryptMnemonicCodesStr");
		OntTest.logger().description("test_param : password - wrong password");
		try {
			String password = "123456";

			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("get private key");
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        
	        OntTest.logger().step("get account");
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String encryptedMnemonicCodesStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        
	        OntTest.logger().step("decrypt mnemonic codes string");
	        com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedMnemonicCodesStr, "12345", account.getAddressU160().toBase58());
	        		
	        assertEquals(true, false);
	        
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_045_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : decryptMnemonicCodesStr");
		OntTest.logger().description("test_param : password - wrong password messy code");
		try {
			String password = "123456";

			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("get private key");
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        
	        OntTest.logger().step("get account");
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String encryptedMnemonicCodesStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        
	        OntTest.logger().step("decrypt mnemonic codes string");
	        com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedMnemonicCodesStr, "!@#$1234", account.getAddressU160().toBase58());
	        			
	        assertEquals(true, false);
	        
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_046_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : decryptMnemonicCodesStr");
		OntTest.logger().description("test_param : password - null");
		try {
			String password = "123456";

			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("get private key");
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        
	        OntTest.logger().step("get account");
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String encryptedMnemonicCodesStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        
	        OntTest.logger().step("decrypt mnemonic codes string");
	        com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedMnemonicCodesStr, "", account.getAddressU160().toBase58());
	        		
	        assertEquals(true, false);
	        
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_047_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : decryptMnemonicCodesStr");
		OntTest.logger().description("test_param : address - correct address");
		try {
			String password = "123456";

			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("get private key");
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        
	        OntTest.logger().step("get account");
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String encryptedMnemonicCodesStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        
	        OntTest.logger().step("decrypt mnemonic codes string");
	        com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedMnemonicCodesStr, password, account.getAddressU160().toBase58());
	        			
			assertEquals(true, true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_048_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : decryptMnemonicCodesStr");
		OntTest.logger().description("test_param : address - wrong address");
		try {
			String password = "123456";

			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("get private key");
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        
	        OntTest.logger().step("get account");
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        
	        StringBuilder new_address = new StringBuilder(account.getAddressU160().toBase58());
	        new_address.setCharAt(0, 'f');
	        new_address.setCharAt(1, 'f');
	        new_address.setCharAt(2, 'f');
	        new_address.setCharAt(3, 'f');
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String encryptedMnemonicCodesStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        
	        OntTest.logger().step("decrypt mnemonic codes string");
	        com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedMnemonicCodesStr, password, new_address.toString());
	        			
			assertEquals(true, false);
						
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_049_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : decryptMnemonicCodesStr");
		OntTest.logger().description("test_param : address - wrong address with 35 chars");
		try {
			String password = "123456";

			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("get private key");
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        
	        OntTest.logger().step("get account");
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String encryptedMnemonicCodesStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        
	        OntTest.logger().step("decrypt mnemonic codes string");
	        com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedMnemonicCodesStr, password, account.getAddressU160().toBase58()+"1");
	        			
			assertEquals(true, false);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_050_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : decryptMnemonicCodesStr");
		OntTest.logger().description("test_param : address - wrong address with [!@#$]");
		try {
			String password = "123456";

			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("get private key");
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        
	        OntTest.logger().step("get account");
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        
	        StringBuilder new_address = new StringBuilder(account.getAddressU160().toBase58());
	        new_address.setCharAt(0, '!');
	        new_address.setCharAt(1, '@');
	        new_address.setCharAt(2, '#');
	        new_address.setCharAt(3, '$');
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String encryptedMnemonicCodesStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        
	        OntTest.logger().step("decrypt mnemonic codes string");
	        com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedMnemonicCodesStr, password, new_address.toString());
	        			
			assertEquals(true, false);
			
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_051_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("test_api   : decryptMnemonicCodesStr");
		OntTest.logger().description("test_param : address - null");
		try {
			String password = "123456";

			OntTest.logger().step("generate mnemonic codes string");
	        String mnemonicCodesStr= com.github.ontio.crypto.MnemonicCode.generateMnemonicCodesStr();
	        
	        OntTest.logger().step("get private key");
	        byte[] privatekey = com.github.ontio.crypto.MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
	        
	        OntTest.logger().step("get account");
	        com.github.ontio.account.Account account = new com.github.ontio.account.Account(privatekey,com.github.ontio.crypto.SignatureScheme.SHA256WITHECDSA);
	        
	        OntTest.logger().step("encrypt mnemonic codes string");
	        String encryptedMnemonicCodesStr = com.github.ontio.crypto.MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, account.getAddressU160().toBase58());
	        
	        OntTest.logger().step("decrypt mnemonic codes string");
	        com.github.ontio.crypto.MnemonicCode.decryptMnemonicCodesStr(encryptedMnemonicCodesStr, password, "");
	        						
		} catch(SDKException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
}
