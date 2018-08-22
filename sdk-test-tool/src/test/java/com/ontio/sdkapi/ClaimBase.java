package com.ontio.sdkapi;

import static org.junit.Assert.fail;

import java.util.HashMap;
import java.util.Map;

import static org.junit.Assert.assertEquals;

import org.junit.*;

import com.alibaba.fastjson.JSONObject;
import com.github.ontio.account.Account;
import com.github.ontio.core.transaction.Transaction;
import com.github.ontio.network.exception.RpcException;
import com.github.ontio.sdk.exception.SDKException;
import com.github.ontio.sdk.manager.WalletMgr;
import com.github.ontio.sdk.wallet.Identity;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;
import com.ontio.testtool.utils.Config;

public class ClaimBase {
	
	public static Identity identity = null;
	public static Identity identity2 = null;
	
@Rule public OntTestWatcher watchman= new OntTestWatcher();
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
		OntTest.api().node().restartAll();
		OntTest.api().node().initOntOng();
		
		try {
			String password = "123456";
			com.github.ontio.sdk.wallet.Account payer = OntTest.sdk().getWalletMgr().createAccount(password);
			com.github.ontio.account.Account payerAcct = OntTest.sdk().getWalletMgr().getAccount(payer.address,password,payer.getSalt());
			
			OntTest.logger().step("create identity1");
			identity = OntTest.sdk().getWalletMgr().createIdentity(password);
			String tx1 = OntTest.sdk().nativevm().ontId().sendRegister(identity,password,payerAcct,OntTest.sdk().DEFAULT_GAS_LIMIT,0);
			OntTest.common().waitTransactionResult(tx1);
			
			OntTest.logger().step("create identity2");
			identity2 = OntTest.sdk().getWalletMgr().createIdentity(password);
			String tx2 = OntTest.sdk().nativevm().ontId().sendRegister(identity2,password,payerAcct,OntTest.sdk().DEFAULT_GAS_LIMIT,0);
			OntTest.common().waitTransactionResult(tx2);
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
	public void test_base_001_getMerkleProof() throws Exception {
		OntTest.logger().description("test_api   : getMerkleProof");
		OntTest.logger().description("test_param : txhash - correct txhash");

		try {
			
			Account account = OntTest.common().getDefaultAccount(new WalletMgr(Config.nodeWallet(0), OntTest.sdk().defaultSignScheme));
			Transaction tx = OntTest.sdk().nativevm().ont().makeTransfer(account.getAddressU160().toBase58(), account.getAddressU160().toBase58(), 1, account.getAddressU160().toBase58(), 30000, 0);
			OntTest.sdk().addSign(tx, account);
			
			OntTest.sdk().getConnect().sendRawTransaction(tx.toHexString());	
			OntTest.common().waitTransactionResult(tx.hash().toHexString());
			
			Object rs1 = OntTest.sdk().nativevm().ontId().getMerkleProof(tx.hash().toHexString());
			
			assertEquals(false, rs1 == null);

		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_002_getMerkleProof() throws Exception {
		OntTest.logger().description("test_api   : getMerkleProof");
		OntTest.logger().description("test_param : txhash - irregular txhash");

		try {
			
			Account account = OntTest.common().getDefaultAccount(new WalletMgr(Config.nodeWallet(0), OntTest.sdk().defaultSignScheme));
			Transaction tx = OntTest.sdk().nativevm().ont().makeTransfer(account.getAddressU160().toBase58(), account.getAddressU160().toBase58(), 1, account.getAddressU160().toBase58(), 30000, 0);
			OntTest.sdk().addSign(tx, account);
			
			OntTest.sdk().getConnect().sendRawTransaction(tx.toHexString());
			OntTest.common().waitTransactionResult(tx.hash().toHexString());
			
			StringBuilder new_hash = new StringBuilder(tx.toHexString());
			new_hash.setCharAt(0, 'f');
			new_hash.setCharAt(1, 'f');
			new_hash.setCharAt(2, 'f');
			new_hash.setCharAt(3, 'f');
			
			System.out.println(new_hash.toString());
			
			OntTest.sdk().nativevm().ontId().getMerkleProof(new_hash.toString());
			
			assertEquals(false, true);
		} catch(RpcException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_003_getMerkleProof() throws Exception {
		OntTest.logger().description("test_api   : getMerkleProof");
		OntTest.logger().description("test_param : txhash - wrong txhash");

		try {
			
			Account account = OntTest.common().getDefaultAccount(new WalletMgr(Config.nodeWallet(0), OntTest.sdk().defaultSignScheme));
			Transaction tx = OntTest.sdk().nativevm().ont().makeTransfer(account.getAddressU160().toBase58(), account.getAddressU160().toBase58(), 1, account.getAddressU160().toBase58(), 30000, 0);
			OntTest.sdk().addSign(tx, account);
			
			OntTest.sdk().getConnect().sendRawTransaction(tx.toHexString());
			OntTest.common().waitTransactionResult(tx.hash().toHexString());
			
			StringBuilder new_hash = new StringBuilder(tx.toHexString());
			new_hash.setCharAt(0, 'Z');
			new_hash.setCharAt(1, 'Z');
			new_hash.setCharAt(2, 'z');
			new_hash.setCharAt(3, 'z');
			
			System.out.println(new_hash.toString());
			
			OntTest.sdk().nativevm().ontId().getMerkleProof(new_hash.toString());
			
			assertEquals(false, true);
		} catch(RpcException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_004_getMerkleProof() throws Exception {
		OntTest.logger().description("test_api   : getMerkleProof");
		OntTest.logger().description("test_param : txhash - txhash with longer length");

		try {
			
			Account account = OntTest.common().getDefaultAccount(new WalletMgr(Config.nodeWallet(0), OntTest.sdk().defaultSignScheme));
			Transaction tx = OntTest.sdk().nativevm().ont().makeTransfer(account.getAddressU160().toBase58(), account.getAddressU160().toBase58(), 1, account.getAddressU160().toBase58(), 30000, 0);
			OntTest.sdk().addSign(tx, account);
			
			OntTest.sdk().getConnect().sendRawTransaction(tx.toHexString());
			OntTest.common().waitTransactionResult(tx.hash().toHexString());
									
			OntTest.sdk().nativevm().ontId().getMerkleProof(tx.hash().toString()+"ffff");
			assertEquals(false, true);
			
		} catch(RpcException e) {
			System.out.println(e);
			assertEquals(true, true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_005_getMerkleProof() throws Exception {
		OntTest.logger().description("test_api   : getMerkleProof");
		OntTest.logger().description("test_param : txhash - null");

		try {
									
			OntTest.sdk().nativevm().ontId().getMerkleProof("");
			
			
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
	public void test_base_006_verifyMerkleProof() throws Exception {
		OntTest.logger().description("test_api   : verifyMerkleProof");
		OntTest.logger().description("test_param : claim - correct claim");

		try {
			OntTest.logger().step("get merkleproof");
			Account account = OntTest.common().getDefaultAccount(new WalletMgr(Config.nodeWallet(0), OntTest.sdk().defaultSignScheme));
			Transaction tx = OntTest.sdk().nativevm().ont().makeTransfer(account.getAddressU160().toBase58(), account.getAddressU160().toBase58(), 1, account.getAddressU160().toBase58(), 30000, 0);
			OntTest.sdk().addSign(tx, account);
			
			OntTest.sdk().getConnect().sendRawTransaction(tx.toHexString());
			OntTest.common().waitTransactionResult(tx.hash().toHexString());
			
			Object merkleproof = OntTest.sdk().nativevm().ontId().getMerkleProof(tx.hash().toHexString()); //getConnect().getMerkleProof(tx.hash().toHexString());
			
			System.out.println(merkleproof.toString());
			
			OntTest.logger().step("verify merkleproof");
			boolean b = OntTest.sdk().nativevm().ontId().verifyMerkleProof(JSONObject.toJSONString(merkleproof));
			
			assertEquals(true, b);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_007_verifyMerkleProof() throws Exception {
		OntTest.logger().description("test_api   : verifyMerkleProof");
		OntTest.logger().description("test_param : claim - wrong claim");

		try {
			OntTest.logger().step("get merkleproof");
			Account account = OntTest.common().getDefaultAccount(new WalletMgr(Config.nodeWallet(0), OntTest.sdk().defaultSignScheme));
			Transaction tx = OntTest.sdk().nativevm().ont().makeTransfer(account.getAddressU160().toBase58(), account.getAddressU160().toBase58(), 1, account.getAddressU160().toBase58(), 30000, 0);
			OntTest.sdk().addSign(tx, account);
			
			OntTest.sdk().getConnect().sendRawTransaction(tx.toHexString());
			OntTest.common().waitTransactionResult(tx.hash().toHexString());
			
			Object merkleproof = OntTest.sdk().nativevm().ontId().getMerkleProof(tx.hash().toHexString());
			
			System.out.println(merkleproof.toString());
			
			OntTest.logger().step("verify merkleproof");
			boolean b = OntTest.sdk().nativevm().ontId().verifyMerkleProof(JSONObject.toJSONString(merkleproof)+"1234");
			assertEquals(false, b);
			
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
	public void test_abnormal_008_verifyMerkleProof() throws Exception {
		OntTest.logger().description("test_api   : verifyMerkleProof");
		OntTest.logger().description("test_param : claim - null");

		try {
			
			OntTest.logger().step("verify merkleproof");
			boolean b = OntTest.sdk().nativevm().ontId().verifyMerkleProof("");
			assertEquals(false, b);
			
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
	public void test_base_009_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : signerOntid - correct signerOntid");

		try {
			String password = "123456";

			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "claim:context", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(true, b);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_010_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : signerOntid - wrong signerOntid");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim("12345", password, identity.controls.get(0).getSalt(), "claim:context", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(false, b);
			
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
	public void test_abnormal_011_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : signerOntid - null");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim("", password, identity.controls.get(0).getSalt(), "claim:context", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(false, b);
			
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
	public void test_normal_012_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : pwd - correct password");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "claim:context", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(true, b);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_013_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : pwd - wrong password");

		try {
			String wrong_password = "1234567";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;
			
			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, wrong_password, identity.controls.get(0).getSalt(), "claim:context", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(false, b);
			
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
	public void test_abnormal_014_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : pwd - null");

		try {			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, "", identity.controls.get(0).getSalt(), "claim:context", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(false, b);
			
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
	public void test_normal_015_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : salt - correct salt");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "claim:context", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(true, b);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_016_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : salt - wrong salt");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
	        byte[] wrong_salt = new byte[10];
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, wrong_salt, "claim:context", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(false, b);
			
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
	public void test_abnormal_017_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : salt - null");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, null, "claim:context", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(false, b);
			
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
	public void test_normal_018_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : context - correct context");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "claim:context", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(true, b);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_019_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : context - wrong context");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "!@#$%^", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(true, b);
			
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
	public void test_abnormal_020_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : context - null");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(false, b);
			
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
	public void test_normal_021_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : claimMap - correct claimMap");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "claim:context", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(true, b);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_022_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : claimMap - wrong claimMap");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("123456", "!@#$");
	        map.put("!@#$", "123456");
	        
	        Map<String, Object> meta_map = new HashMap<String, Object>();
	        meta_map.put("Issuer", identity.ontid);
	        meta_map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "claim:context", map, meta_map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			System.out.println(claim);
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(false, b);
			
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
	public void test_abnormal_023_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : claimMap - null");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;
			
	        Map<String, Object> meta_map = new HashMap<String, Object>();
	        meta_map.put("Issuer", identity.ontid);
	        meta_map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "claim:context", null, meta_map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(false, b);
			
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
	public void test_normal_024_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : metaData - correct metaData");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "claim:context", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(true, b);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_025_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : metaData - wrong metaData");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> meta_map = new HashMap<String, Object>();
	        meta_map.put("123456", identity.ontid);
	        meta_map.put("123456", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "claim:context", map, meta_map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(false, b);
			
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
	public void test_abnormal_026_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : metaData - null");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "claim:context", map, null, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(false, b);
			
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
	public void test_normal_027_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : clmRevMap - correct clmRevMap");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "claim:context", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(true, b);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_028_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : clmRevMap - wrong clmRevMap");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("123456", "!@#$");
	        clmRevMap.put("!@#$", "123456");
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "claim:context", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(true, b);
			
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
	public void test_abnormal_029_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : clmRevMap - null");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);

	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "claim:context", map, map, null, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(false, b);
			
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
	public void test_normal_030_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : expire - correct expire");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "claim:context", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(true, b);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_031_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : expire - wrong expire -1");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "claim:context", map, map, clmRevMap, -1);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(false, b);
			
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
	public void test_abnormal_032_createOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : createOntIdClaim");
		OntTest.logger().description("test_param : expire - null");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);

	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			@SuppressWarnings("null")
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "claim:context", map, map, clmRevMap, (Long)null);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(false, b);
			
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
	public void test_base_033_verifyOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : verifyOntIdClaim");
		OntTest.logger().description("test_param : claim - correct claim");

		try {
			String password = "123456";
			
			Identity identity = ClaimBase.identity;
			Identity identity2 = ClaimBase.identity2;

			Map<String, Object> map = new HashMap<String, Object>();
			map.put("Issuer", identity.ontid);
	        map.put("Subject", identity2.ontid);
	        
	        Map<String, Object> clmRevMap = new HashMap<String, Object>();
	        clmRevMap.put("typ","AttestContract");
	        clmRevMap.put("addr",identity.ontid.replace(com.github.ontio.common.Common.didont,""));
			
	        OntTest.logger().step("create OntIdClaim");
			String claim = OntTest.sdk().nativevm().ontId().createOntIdClaim(identity.ontid, password, identity.controls.get(0).getSalt(), "claim:context", map, map, clmRevMap, System.currentTimeMillis()/1000+100000);
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b = OntTest.sdk().nativevm().ontId().verifyOntIdClaim(claim);
			
			assertEquals(true, b);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_034_verifyOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : verifyOntIdClaim");
		OntTest.logger().description("test_param : claim - wrong claim");

		try {
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b2 = OntTest.sdk().nativevm().ontId().verifyOntIdClaim("123456!@#$");
			
			assertEquals(false, b2);
			
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
	public void test_normal_035_verifyOntIdClaim() throws Exception {
		OntTest.logger().description("test_api   : verifyOntIdClaim");
		OntTest.logger().description("test_param : claim - null");

		try {
			
			OntTest.logger().step("verify OntIdClaim");
			boolean b2 = OntTest.sdk().nativevm().ontId().verifyOntIdClaim("");
			
			assertEquals(true, b2);
			
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
