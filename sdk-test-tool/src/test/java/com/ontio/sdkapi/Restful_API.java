package com.ontio.sdkapi;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import java.net.URL;
import java.security.Key;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Map;

import org.junit.After;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.github.ontio.account.Account;
import com.github.ontio.common.Helper;
import com.github.ontio.common.UInt256;
import com.github.ontio.core.block.Block;
import com.github.ontio.core.payload.InvokeCode;
import com.github.ontio.core.transaction.Transaction;
import com.github.ontio.smartcontract.neovm.abi.BuildParams;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;
import com.ontio.testtool.utils.Config;

public class Restful_API {
	@Rule public OntTestWatcher watchman= new OntTestWatcher();
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
		OntTest.api().node().restartAll();
		OntTest.sdk().getWebSocket().startWebsocketThread(true);
		OntTest.api().node().initOntOng();
	}
	
	@Before
	public void setUp() throws Exception {
		
	}
	
	@After
	public void TearDown() throws Exception {
		System.out.println("TearDown");
	}
	
	@Test
	public void test_base_001_getNodeCount() throws Exception {
		OntTest.logger().description("----------getNodeCount----------");
		
		try {
			int nodes = Config.NODES.size();
			OntTest.logger().print("nodes: "+nodes);
			int acc = OntTest.sdk().getRestful().getNodeCount();
			OntTest.logger().print("getNodeCount: "+acc);
			assertEquals(true, nodes -1 == acc);
			
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_002_getBlock() throws Exception {
		OntTest.logger().description("----------getBlock----------");
		
		try {
			int height = OntTest.sdk().getRestful().getBlockHeight() - 1;
			OntTest.logger().print("blockheight: "+height);
			Block acc = OntTest.sdk().getRestful().getBlock(height);
			OntTest.logger().print("blockheight: "+acc.height);
			assertEquals(true, acc.height == height);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_base_003_getBlockJson() throws Exception {
		OntTest.logger().description("----------getBlockJson----------");
		
		try {
			int height = OntTest.sdk().getRestful().getBlockHeight() - 1;
			OntTest.logger().print("blockheight: "+height);
			
			String hash = OntTest.sdk().getRestful().getBlock(height).hash().toHexString();
			OntTest.logger().print("hsah: "+hash);
			JSONObject acc = (JSONObject)OntTest.sdk().getRestful().getBlockJson(height);
			OntTest.logger().print(acc.toString());
			OntTest.logger().print(acc.getString("Hash"));
			
			assertEquals(true,acc.getString("Hash").equals(hash));
			assertEquals(true, acc.toString().indexOf(hash) > 0);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_004_getBlockJson() throws Exception {
		OntTest.logger().description("----------getBlockJson----------");
		
		try {
			OntTest.logger().print("1.获取hash");
			int height = OntTest.sdk().getRestful().getBlockHeight() - 1;
			OntTest.logger().print("blockheight: "+height);
			UInt256 hash = OntTest.sdk().getRestful().getBlock(height).hash();
			OntTest.logger().print(hash.toHexString());
			OntTest.logger().print("2.getBlockJson");
			JSONObject acc = (JSONObject)OntTest.sdk().getRestful().getBlockJson(hash.toHexString());

			OntTest.logger().print(acc.getString("Hash"));
			
			assertEquals(true,acc.getString("Hash").equals(hash.toHexString()));
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_base_005_getBlock() throws Exception {
		OntTest.logger().description("----------getBlock----------");
		
		try {
			OntTest.logger().print("1.获取hash");
			int height = OntTest.sdk().getRestful().getBlockHeight() - 1;
			OntTest.logger().print("blockheight: "+height);
			UInt256 hash = OntTest.sdk().getRestful().getBlock(height).hash();
			OntTest.logger().print(hash.toHexString());
			OntTest.logger().print("2.getBlockJson");
			Block acc = OntTest.sdk().getRestful().getBlock(hash.toHexString());

			OntTest.logger().print(acc.hash().toHexString());
//			OntTest.logger().print(acc.toString());
			assertEquals(true, acc.hash().toHexString().equals(hash.toHexString()));
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_base_006_getBlockHeight() throws Exception {
		OntTest.logger().description("----------getBlockHeight----------");
		
		try {
			int acc = OntTest.sdk().getRestful().getBlockHeight();
			OntTest.logger().print("getBlockHeight: "+acc);
			String hash = OntTest.sdk().getRestful().getBlock(acc).hash().toHexString();
			
			OntTest.logger().print(hash);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_007_getTransaction() throws Exception {
		OntTest.logger().description("----------getTransaction----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long bala1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long bala2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			
			OntTest.logger().print("账户1 的余额为： "+bala1);
			OntTest.logger().print("账户2 的余额为： "+bala2);
			
			String s = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10L, acc1, 20000L, 0L);
			OntTest.common().waitTransactionResult(s);
			OntTest.logger().print(s);
			Transaction trs = OntTest.sdk().getRestful().getTransaction(s);
			OntTest.logger().print(trs.hash().toHexString());
			assertEquals(true, trs.hash().toHexString().equals(s));
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_008_getStorage() throws Exception {
		OntTest.logger().description("----------getStorage----------");
		
		try {
			String url = this.getClass().getResource("rest.cs").getPath();
			Map dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr1 = String.valueOf(dec.get("address"));
			String codeAddr2 = Helper.reverse(codeAddr1);
			
			List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        args.add(Helper.hexToBytes("06"));
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr2, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().print("b1"+b1);

			OntTest.sdk().getConnect().sendRawTransaction(invokeTx.toHexString());
			OntTest.common().waitTransactionResult(invokeTx.hash().toHexString());
			String acc = OntTest.sdk().getRestful().getStorage(codeAddr1, "01");
			OntTest.logger().print(acc);
			assertEquals(true, acc.equals("06"));
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_normal_009_getStorage() throws Exception {
		OntTest.logger().description("----------getStorage----------");
		
		try {
			String url = this.getClass().getResource("rest.cs").getPath();
			Map dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr1 = String.valueOf(dec.get("address"));
			String codeAddr2 = Helper.reverse(codeAddr1);
			
			List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        args.add(Helper.hexToBytes("06"));
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr2, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().print("b1"+b1);

			OntTest.sdk().getConnect().sendRawTransaction(invokeTx.toHexString());
			OntTest.common().waitTransactionResult(invokeTx.hash().toHexString());
			String acc = OntTest.sdk().getRestful().getStorage(codeAddr1, "01");
			OntTest.logger().print(acc);
			assertEquals(true, acc.equals("06"));
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	
	@Test
	public void test_base_010_getBalance() throws Exception {
		OntTest.logger().description("----------getBalance----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			
			String addr1 = acc1.getAddressU160().toBase58();
			JSONObject acc = (JSONObject)OntTest.sdk().getRestful().getBalance(addr1);
			OntTest.logger().print(acc.toString());
			
			String ont = acc.getString("ont");
			
			long qb = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			OntTest.logger().print("ont: "+qb);
			assertEquals(true, String.valueOf(qb).equals(ont));
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_011_getContractJson() throws Exception {
		OntTest.logger().description("----------getContractJson----------");
		
		try {
			String url = this.getClass().getResource("invoke.cs").getPath();
			Map dec = OntTest.api().contract().deployContract(url, null);

			String codeAddr = String.valueOf(dec.get("address"));

			JSONObject acc = (JSONObject)OntTest.sdk().getRestful().getContractJson(codeAddr);
			
			
			OntTest.logger().print(acc.toString());
			assertEquals(true, acc.getString("NeedStorage").equals("true"));
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_012_getSmartCodeEvent() throws Exception {
		OntTest.logger().description("----------getSmartCodeEvent----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			String s = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10L, acc1, 20000L, 0L);
			OntTest.common().waitTransactionResult(s);
			int height = OntTest.sdk().getRestful().getBlockHeightByTxHash(s);
			OntTest.logger().print("height:"+height);
			JSONArray acc = (JSONArray)OntTest.sdk().getRestful().getSmartCodeEvent(height);

			OntTest.logger().print(acc.toString());
			assertEquals(true, s.equals(acc.getJSONObject(0).getString("TxHash")));
			
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	
	@Test
	public void test_base_013_getSmartCodeEvent() throws Exception {
		OntTest.logger().description("----------getSmartCodeEvent----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			String s = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10L, acc1, 20000L, 0L);
			
			OntTest.common().waitTransactionResult(s);
			JSONObject acc = (JSONObject)OntTest.sdk().getRestful().getSmartCodeEvent(s);
			OntTest.logger().print(acc.toString());
			
			assertEquals(true, s.equals(acc.getString("TxHash")));

		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	
	@Test
	public void test_base_014_getBlockHeightByTxHash() throws Exception {
		OntTest.logger().description("----------getBlockHeightByTxHash----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();

			String s = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10L, acc1, 20000L, 0L);
			OntTest.common().waitTransactionResult(s);
			int acc = OntTest.sdk().getRestful().getBlockHeightByTxHash(s);
			
			Transaction b = OntTest.sdk().getRestful().getTransaction(s);

			OntTest.logger().print("getBlockHeightByTxHash: "+acc);
			assertEquals(true, s.equals(b.hash().toHexString()));
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_base_015_getMerkleProof() throws Exception {
		OntTest.logger().description("----------getMerkleProof----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();

			String s = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10L, acc1, 20000L, 0L);
			
			OntTest.common().waitTransactionResult(s);

			JSONObject acc = (JSONObject)OntTest.sdk().getRestful().getMerkleProof(s);
			
			
			OntTest.logger().print(acc.toString());
			assertEquals(true, acc.getString("TransactionsRoot").equals(s));
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_base_016_sendRawTransaction() throws Exception {
		OntTest.logger().description("----------sendRawTransaction----------");
		
		try {
			String url = this.getClass().getResource("rest.cs").getPath();
			Map dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr = String.valueOf(dec.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			//codeAddr为存在的地址但并非合约地址
			OntTest.logger().print(codeAddr);//智能合约地址

	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        Transaction A= OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});

			boolean acc = OntTest.sdk().getRestful().sendRawTransaction(invokeTx.toHexString());
			OntTest.logger().print(String.valueOf(acc));
			assertEquals(true, acc == true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_base_017_sendRawTransaction() throws Exception {
		OntTest.logger().description("----------sendRawTransaction----------");
		
		try {
			String url = this.getClass().getResource("rest.cs").getPath();
			Map dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr = String.valueOf(dec.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			//codeAddr为存在的地址但并非合约地址
			OntTest.logger().print(codeAddr);//智能合约地址

	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        Transaction A= OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});

			boolean acc = OntTest.sdk().getRestful().sendRawTransaction(A);
			OntTest.logger().print(String.valueOf(acc));
			assertEquals(true, acc == true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_018_sendRawTransactionPreExec() throws Exception {
		OntTest.logger().description("----------sendRawTransactionPreExec----------");
		
		try {
			String url = this.getClass().getResource("rest.cs").getPath();
			Map dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr = String.valueOf(dec.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			//codeAddr为存在的地址但并非合约地址
			OntTest.logger().print(codeAddr);//智能合约地址

	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);

			JSONObject acc = (JSONObject)OntTest.sdk().getRestful().sendRawTransactionPreExec(invokeTx.toHexString());
			OntTest.logger().print(acc.toString());
			assertEquals(true, acc.getString("State").equals("1"));
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_019_getAllowance() throws Exception {
		OntTest.logger().description("----------getAllowance----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long amount = 1000;
			
			String s = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, amount, acc1, 20000, 0);
			OntTest.common().waitTransactionResult(s);
			Object acc = OntTest.sdk().getRestful().getAllowance("ont", addr1, addr2);
			OntTest.logger().print(acc.toString());
			assertEquals(true, acc.toString().equals(String.valueOf(amount)));
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_normal_020_getAllowance() throws Exception {
		OntTest.logger().description("----------getAllowance----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long amount = 1000;
			String s = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, amount, acc1, 20000, 0);
			OntTest.common().waitTransactionResult(s);
			Object acc = OntTest.sdk().getRestful().getAllowance("ont", addr1, addr2);
			OntTest.logger().print(acc.toString());
			assertEquals(true, acc.toString().equals(String.valueOf(amount)));
		} 
		catch(Exception e) {
		OntTest.logger().error(e.toString());
		fail();
		}
	}
	
	
	
	
	@Test
	public void test_normal_021_getAllowance() throws Exception {
		OntTest.logger().description("----------getAllowance----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long amount = 1000;

			String s = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, amount, acc1, 20000, 0);
			OntTest.common().waitTransactionResult(s);
			Object acc = OntTest.sdk().getRestful().getAllowance("ont", addr1, addr2);
			OntTest.logger().print(acc.toString());
			assertEquals(true, acc.toString().equals(String.valueOf(amount)));
		} 
		catch(Exception e) {
		OntTest.logger().error(e.toString());
		fail();
		}
	}
	
	
	
	@Test
	public void test_base_022_getMemPoolTxCount() throws Exception {
		OntTest.logger().description("----------getMemPoolTxCount----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			String s = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 100, acc1, 20000, 0);
			String s1 = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 100, acc1, 20000, 0);
			Object acc = OntTest.sdk().getRestful().getMemPoolTxCount();
			OntTest.logger().print(acc.toString());
			assertEquals(true, acc.toString().equals("[2,0]"));
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_023_getMemPoolTxState() throws Exception {
		OntTest.logger().description("----------getMemPoolTxState----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			String s = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 100, acc1, 20000, 0);
			OntTest.logger().print(s);
			JSONObject acc = (JSONObject)OntTest.sdk().getRestful().getMemPoolTxState(s);
			OntTest.logger().print(acc.toString());
			assertEquals(true, acc.toString().charAt(18) == '1');
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	

	
	@Test
	public void test_base_024_syncSendRawTransaction() throws Exception {
		OntTest.logger().description("----------syncSendRawTransaction----------");
		
		try {
			String url = this.getClass().getResource("rest.cs").getPath();
			OntTest.logger().print(url);
			Map dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr = String.valueOf(dec.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			//codeAddr为存在的地址但并非合约地址
			OntTest.logger().print(codeAddr);//智能合约地址
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        Transaction A= OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});

			JSONObject acc = (JSONObject)OntTest.sdk().getRestful().syncSendRawTransaction(invokeTx.toHexString());
			OntTest.logger().print(acc.toString());
			

			assertEquals(true, A.hash().toHexString().equals(acc.getString("TxHash")));
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
}
