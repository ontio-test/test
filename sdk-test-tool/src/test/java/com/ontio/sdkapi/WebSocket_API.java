package com.ontio.sdkapi;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.junit.After;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import com.github.ontio.account.Account;
import com.github.ontio.common.Helper;
import com.github.ontio.common.UInt256;
import com.github.ontio.core.payload.InvokeCode;
import com.github.ontio.core.transaction.Transaction;
import com.github.ontio.network.websocket.Result;
import com.github.ontio.smartcontract.neovm.abi.BuildParams;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;
import com.ontio.testtool.utils.Config;

public class WebSocket_API {
	@Rule public OntTestWatcher watchman= new OntTestWatcher();
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
		
		//OntTest.api().node().restartAll();
		//OntTest.api().node().initOntOng();
		
		OntTest.sdk().getWebSocket().startWebsocketThread(true);
		Thread.sleep(5000);
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

			OntTest.sdk().getWebSocket().getNodeCount();
			Result result = OntTest.common().waitWsResult("getconnectioncount");
			System.out.println("result:" + result.Result.toString());
			
			assertEquals(nodes - 1, Integer.parseInt(result.Result.toString()));
			
		} catch(Exception e) {
			e.printStackTrace();
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_002_getBlock() throws Exception {
		OntTest.logger().description("----------getBlock----------");
		
		try {
			OntTest.logger().step("get block height");
			OntTest.sdk().getWebSocket().getBlockHeight();
			Result result = OntTest.common().waitWsResult("getblockheight");
			int height = Integer.parseInt(result.Result.toString())-1;
			System.out.println("blockheight: " + height);
			
			OntTest.logger().step("get block");
			OntTest.sdk().getWebSocket().getBlock(height);
			Result result1 = OntTest.common().waitWsResult("getblockbyheight");
			
			assertEquals(false, result1==null);
			System.out.println("result:" + result1.Result.toString());

		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_base_003_getBlockJson() throws Exception {
		OntTest.logger().description("----------getBlockJson----------");
		
		try {
			OntTest.logger().step("get block height");
			OntTest.sdk().getWebSocket().getBlockHeight();
			Result result = OntTest.common().waitWsResult("getblockheight");
			System.out.println("blockheight: " + result.Result.toString());
			int height = Integer.parseInt(result.Result.toString())-1;
			
			OntTest.logger().step("ws get block json");
			OntTest.sdk().getWebSocket().getBlockJson(height);
			Result result1 = OntTest.common().waitWsResult("getblockbyheight");
			System.out.println("result:" + result1.Result.toString());
			
			OntTest.logger().step("rpc get block json");
			Object result2 = OntTest.sdk().getRpc().getBlockJson(height);
			System.out.println("result:" + result2.toString());
			
			assertEquals(result1.Result.toString(), result2.toString());
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_004_getBlockJson() throws Exception {
		OntTest.logger().description("----------getBlockJson----------");
		
		try {
			OntTest.logger().step("get block height");
			OntTest.sdk().getWebSocket().getBlockHeight();
			Result result = OntTest.common().waitWsResult("getblockheight");
			int height = Integer.parseInt(result.Result.toString())-1;
			
			OntTest.logger().step("get block hash");
			System.out.println("blockheight: " + height);
			UInt256 hash = OntTest.sdk().getRpc().getBlock(height).hash();
			
			OntTest.logger().step("ws get block json");
			OntTest.sdk().getWebSocket().getBlockJson(hash.toHexString());
			Result result1 = OntTest.common().waitWsResult("getblockbyhash");
			System.out.println("result:" + result1.Result.toString());
			
			OntTest.logger().step("rpc get block json");
			Object result2 = OntTest.sdk().getRpc().getBlockJson(height);
			System.out.println("result:" + result2.toString());
			
			assertEquals(result1.Result.toString(), result2.toString());
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_base_005_getBlock() throws Exception {
		OntTest.logger().description("----------getBlock----------");
		
		try {
			OntTest.logger().step("get block height");
			OntTest.sdk().getWebSocket().getBlockHeight();
			Result result = OntTest.common().waitWsResult("getblockheight");
			int height = Integer.parseInt(result.Result.toString())-1;
			
			OntTest.logger().step("get block hash");
			System.out.println("blockheight: " + height);
			UInt256 hash = OntTest.sdk().getRpc().getBlock(height).hash();
			System.out.println("blockhash: " + hash.toHexString());
			
			OntTest.logger().step("get block by hash");
			OntTest.sdk().getWebSocket().getBlock(hash.toHexString());
			Result result1 = OntTest.common().waitWsResult("getblockbyhash");
			
			assertEquals(false, result1==null);
			System.out.println("result:" + result1.Result.toString());

		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_base_006_getBlockHeight() throws Exception {
		OntTest.logger().description("----------getBlockHeight----------");
		
		try {
			
			OntTest.logger().step("ws get block height");
			OntTest.sdk().getWebSocket().getBlockHeight();
			Result result = OntTest.common().waitWsResult("getblockheight");
			assertEquals(false, result==null);
			
			int height1 = Integer.parseInt(result.Result.toString());
			System.out.println("blockheight1: " + height1);
			
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
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.logger().step("send transfer");
			String s = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10L, acc1, 20000L, 0L);
			OntTest.common().waitTransactionResult(s);
			System.out.println(s);

			OntTest.logger().step("ws get transaction");
			OntTest.sdk().getWebSocket().getTransaction(s);
			Result rs = OntTest.common().waitWsResult("gettransaction");
			assertEquals(false, rs==null);
			
			System.out.println(rs.Result.toString());
			
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_008_getStorage() throws Exception {
		OntTest.logger().description("----------getStorage----------");
		
		try {
			String key = "01";
			String value = "06";
			
			String url = this.getClass().getResource("rest.cs").getPath();
			Map<?,?> dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr1 = String.valueOf(dec.get("address"));
			String codeAddr2 = Helper.reverse(codeAddr1);
			
			List<Object> list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List<Object> args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes(key));
	        args.add(Helper.hexToBytes(value));
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr2, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map<?,?> b1 = (Map<?,?>)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        System.out.println("b1"+b1);

			OntTest.sdk().getConnect().sendRawTransaction(invokeTx.toHexString());
			OntTest.common().waitTransactionResult(invokeTx.hash().toHexString());
			
			OntTest.sdk().getWebSocket().getStorage(codeAddr1, key);
			
			Result rs = OntTest.common().waitWsResult("getstorage");
			System.out.println(rs.Result.toString());
			
			assertEquals(rs.Result.toString(), value);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_normal_009_getStorage() throws Exception {
		OntTest.logger().description("----------getStorage----------");
		
		try {
			String key = "01";
			String value = "06";
			
			String url = this.getClass().getResource("rest.cs").getPath();
			Map<?,?> dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr1 = String.valueOf(dec.get("address"));
			String codeAddr2 = Helper.reverse(codeAddr1);
			
			List<Object> list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        
	        List<Object> args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes(key));
	        args.add(Helper.hexToBytes(value));
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr2, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map<?,?> b1 = (Map<?,?>)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        System.out.println("b1"+b1);

			OntTest.sdk().getConnect().sendRawTransaction(invokeTx.toHexString());
			OntTest.common().waitTransactionResult(invokeTx.hash().toHexString());

			OntTest.sdk().getWebSocket().getStorage(codeAddr1, key);
			Result rs = OntTest.common().waitWsResult("getstorage");
			System.out.println(rs.Result.toString());
			
			assertEquals(rs.Result.toString(), value);
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
			
			OntTest.logger().step("ws get balance");
			OntTest.sdk().getWebSocket().getBalance(addr1);
			Result rs = OntTest.common().waitWsResult("getbalance");
			System.out.println(rs.Result.toString());
			
			OntTest.logger().step("rpc get balance");
			Object rs2 = OntTest.sdk().getRpc().getBalance(addr1);
			System.out.println(rs2.toString());
			
			assertEquals(rs.Result.toString(), rs2.toString());
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_011_getContractJson() throws Exception {
		OntTest.logger().description("----------getContractJson----------");
		
		try {
			OntTest.logger().step("deploy contract");
			String url = this.getClass().getResource("rest.cs").getPath();
			Map<?,?> dec = OntTest.api().contract().deployContract(url, null);
			
			OntTest.logger().step("ws get contract json");
			String codeAddr = String.valueOf(dec.get("address"));
			OntTest.sdk().getWebSocket().getContractJson(codeAddr);
			Result rs = OntTest.common().waitWsResult("getcontract");
			System.out.println(rs.Result.toString());
			
			OntTest.logger().step("rpc get contract json");
			Object rs2 = OntTest.sdk().getRpc().getContractJson(codeAddr);
			System.out.println(rs2.toString());
			
			assertEquals(rs.Result.toString(), rs2.toString());
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
			
			long bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			
			System.out.println("balance of account 1:"+bala1);
			System.out.println("balance of account 2:"+bala2);
			
			Transaction tx = OntTest.sdk().nativevm().ont().makeTransfer(addr1, addr2, 10L,addr1, 20000L, 0);
	        OntTest.sdk().signTx(tx, new Account[][]{{acc1}});
	        boolean b = OntTest.sdk().getConnect().sendRawTransaction(tx.toHexString());
	        String s = "";
	        if (b) {
	            s = tx.hash().toHexString();
	        }
			OntTest.common().waitTransactionResult(s);
			
			int height = OntTest.sdk().getRpc().getBlockHeightByTxHash(s);
			System.out.println("height: " + height);
			
			OntTest.sdk().getWebSocket().getSmartCodeEvent(height);
			Result rs = OntTest.common().waitWsResult("getsmartcodeeventtxs");
			assertEquals(false, rs==null);
			System.out.println("result: "+rs.Result.toString());

		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
//	
//	
//	
//	
	@Test
	public void test_base_013_getSmartCodeEvent() throws Exception {
		OntTest.logger().description("----------getSmartCodeEvent----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			
			System.out.println("balance of account 1:"+bala1);
			System.out.println("balance of account 2:"+bala2);
			
			Transaction tx = OntTest.sdk().nativevm().ont().makeTransfer(acc1.getAddressU160().toBase58(), addr2, 10L, acc1.getAddressU160().toBase58(), 20000L, 0);
	        OntTest.sdk().signTx(tx, new Account[][]{{acc1}});
	        boolean b = OntTest.sdk().getConnect().sendRawTransaction(tx.toHexString());
	        String s = "";
	        if (b) {
	            s = tx.hash().toHexString();
	        }
			
			OntTest.common().waitTransactionResult(s);
			System.out.println(s);
			OntTest.sdk().getWebSocket().getSmartCodeEvent(s);
			Result rs = OntTest.common().waitWsResult("getsmartcodeevent");
			
			assertEquals(false, rs==null);
			System.out.println(rs.Result.toString());
			
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
			
			String addr2 = acc2.getAddressU160().toBase58();

			String s = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10L, acc1, 20000L, 0L);
			OntTest.common().waitTransactionResult(s);
			
			OntTest.logger().step("ws get block height by tx hash");
			OntTest.sdk().getWebSocket().getBlockHeightByTxHash(s);
			Result rs = OntTest.common().waitWsResult("getblockheightbytxhash");
			System.out.println(rs.Result.toString());
			
			OntTest.logger().step("rpc get block height by tx hash");
			int rs2 = OntTest.sdk().getRpc().getBlockHeightByTxHash(s);
			
			assertEquals(rs2, Integer.parseInt(rs.Result.toString()));
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
			
			String addr2 = acc2.getAddressU160().toBase58();

			String s = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10L, acc1, 20000L, 0L);
			OntTest.common().waitTransactionResult(s);
			
			OntTest.logger().step("ws get merkle proof");
			OntTest.sdk().getWebSocket().getMerkleProof(s);
			Result rs = OntTest.common().waitWsResult("getmerkleproof");
			System.out.println(rs.Result.toString());
			
			OntTest.logger().step("rpc get merkle proof");
			Object rs2 = OntTest.sdk().getRpc().getMerkleProof(s);
			
			assertEquals(rs2.toString(), rs.Result.toString());
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
			Map<?,?> dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr = String.valueOf(dec.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			System.out.println("contract address:"+codeAddr);

			List<Object> list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List<Object> args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        // OntTest.common().waitTransactionResult(tx.hash().toHexString());

			OntTest.sdk().getWebSocket().sendRawTransaction(invokeTx.toHexString());
			Result rs = OntTest.common().waitWsResult("sendrawtransaction");
			System.out.println(rs.Result.toString());
			
			assertEquals(true, OntTest.common().waitTransactionResult(invokeTx.hash().toHexString()));
			
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
			Map<?,?> dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr = String.valueOf(dec.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			System.out.println("contract address:"+codeAddr);

			List<Object> list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List<Object> args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        Transaction A= OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        // OntTest.common().waitTransactionResult(A.hash().toHexString());
	        
			OntTest.sdk().getWebSocket().sendRawTransaction(A);
			Result rs = OntTest.common().waitWsResult("sendrawtransaction");
			System.out.println(rs.Result.toString());
			
			assertEquals(true, OntTest.common().waitTransactionResult(invokeTx.hash().toHexString()));
		} catch(Exception e) {
			e.printStackTrace();
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_018_sendRawTransactionPreExec() throws Exception {
		OntTest.logger().description("----------sendRawTransactionPreExec----------");
		
		try {
			String url = this.getClass().getResource("rest.cs").getPath();
			Map<?,?> dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr = String.valueOf(dec.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			System.out.println("contract address:"+codeAddr);

			List<Object> list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List<Object> args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        // OntTest.common().waitTransactionResult(tx.hash().toHexString());
			
	        OntTest.sdk().getWebSocket().sendRawTransactionPreExec(invokeTx.toHexString());
			Result rs = OntTest.common().waitWsResult("sendrawtransaction");
			assertEquals(false, rs == null); 
			System.out.println(rs.Result.toString());
			
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
			String s = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100, acc1, 20000, 0);
			OntTest.common().waitTransactionResult(s);
			
			OntTest.sdk().getWebSocket().getAllowance("ont", addr1, addr2);
			Result rs = OntTest.common().waitWsResult("getallowance");
			System.out.println(rs.Result.toString());
			
			String rs2 = OntTest.sdk().getRpc().getAllowance("ont", addr1, addr2);
			assertEquals(rs2.toString(), rs.Result.toString());

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
			String approvetxhash = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100, acc1, 20000, 0);
			OntTest.common().waitTransactionResult(approvetxhash);
			
			OntTest.sdk().getWebSocket().getAllowance("ont", addr1, addr2);
			Result rs = OntTest.common().waitWsResult("getallowance");
			System.out.println(rs.Result.toString());
			
			String rs2 = OntTest.sdk().getRpc().getAllowance("ont", addr1, addr2);
			assertEquals(rs2.toString(), rs.Result.toString());
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
			String approvetxhash = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100, acc1, 20000, 0);
			OntTest.common().waitTransactionResult(approvetxhash);
			
			OntTest.sdk().getWebSocket().getAllowance("ont", addr1, addr2);
			Result rs = OntTest.common().waitWsResult("getallowance");
			System.out.println(rs.Result.toString());
			
			String rs2 = OntTest.sdk().getRpc().getAllowance("ont", addr1, addr2);
			assertEquals(rs2.toString(), rs.Result.toString());
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
			OntTest.sdk().getWebSocket().getMemPoolTxCount();
			Result rs = OntTest.common().waitWsResult("getmempooltxcount");
			System.out.println(rs.Result.toString());
			
			Object rs1 = OntTest.sdk().getRpc().getMemPoolTxCount();
			System.out.println(rs1.toString());
			
			assertEquals(rs.Result.toString(), rs1.toString());
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_base_023_getMemPoolTxState() throws Exception {
		OntTest.logger().description("----------getMemPoolTxState----------");
		
		try {
			Account acc = OntTest.common().getAccount(0);
			String addr = acc.getAddressU160().toBase58();
			String txhash = OntTest.sdk().nativevm().ont().sendTransfer(acc, addr, 100L, acc, 20000L, 0L);
			
			OntTest.sdk().getWebSocket().getMemPoolTxState(txhash);
			Result rs = OntTest.common().waitWsResult("getmempooltxstate");
			System.out.println(rs.Result.toString());
			
			assertEquals(false, rs.Result.toString()==null);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	

	
	@Test(timeout=60000)
	public void test_base_024_syncSendRawTransaction() throws Exception {
		OntTest.logger().description("----------syncSendRawTransaction----------");
		
		try {
			String url = this.getClass().getResource("rest.cs").getPath();
			System.out.println(url);
			Map<?,?> dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr = String.valueOf(dec.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			System.out.println("contract address:"+codeAddr);

			List<Object> list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List<Object> args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        // OntTest.common().waitTransactionResult(tx.hash().toHexString());
	        
			OntTest.sdk().getWebSocket().sendRawTransaction(invokeTx.toHexString());
			assertEquals(true, OntTest.common().waitTransactionResult(invokeTx.hash().toHexString()));
			
			Result rs = OntTest.common().waitWsResult("Notify");
			System.out.println(rs.Result.toString());
			
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
}
