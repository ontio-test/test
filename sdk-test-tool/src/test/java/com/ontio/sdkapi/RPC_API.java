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

import com.alibaba.fastjson.JSON;
import com.github.ontio.account.Account;
import com.github.ontio.common.Helper;
import com.github.ontio.core.block.Block;
import com.github.ontio.core.payload.InvokeCode;
import com.github.ontio.core.transaction.Transaction;
import com.github.ontio.network.exception.RpcException;
import com.github.ontio.smartcontract.neovm.abi.BuildParams;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;
import com.ontio.testtool.utils.Config;

public class RPC_API {
	@Rule 
	public OntTestWatcher watchman= new OntTestWatcher();
	String invoke_address = this.getClass().getResource("invoke.cs").getPath();
	String rpcapi_address = this.getClass().getResource("rpcapi.cs").getPath();

	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
		OntTest.api().node().restartAll("ontology", "config.json", Config.DEFAULT_NODE_ARGS);
		OntTest.api().node().initOntOng();
	}
	
	@Before
	public void setUp() throws Exception {
		OntTest.logger().step("setUp");
	}
	
	@After
	public void TearDown() throws Exception {
		OntTest.logger().step("TearDown");
	}
	
	@Test
	public void test_base_001_getNodeCount() throws Exception {
		OntTest.logger().description("RPC_API 001 getNodeCount");

		try {
			OntTest.logger().step("测试getNodeCount()");
			
			int num = OntTest.sdk().getRpc().getNodeCount();
			OntTest.logger().description("actual_nodenum = "+num);
			int exp = Config.NODES.size();
			OntTest.logger().description("expect_nodenum = "+exp);
			
			assertEquals(true,exp==(num+1));
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_002_getBlock() throws Exception {
		OntTest.logger().description("RPC_API 002 getBlock");

		try {
			OntTest.logger().step("测试getBlock()");
			
			int height = OntTest.sdk().getRpc().getBlockHeight();
			Block Block = OntTest.sdk().getRpc().getBlock(height-1);
			OntTest.logger().description("Block : "+Block);
			int ret = Block.height;
			OntTest.logger().description("Block_height = "+ret);
			int exp = height-1;
			
			assertEquals(true,ret==exp);	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	

	@Test
	public void test_base_003_getBlockJson() throws Exception {
		OntTest.logger().description("RPC_API 003 getBlockJson");

		try {
			OntTest.logger().step("测试getBlock()");
			
			int block_height = OntTest.sdk().getRpc().getBlockHeight();
			Object ret_block = OntTest.sdk().getRpc().getBlockJson(block_height-1);
			OntTest.logger().description("ret_blockJson : "+ret_block);
			String hash = String.valueOf(OntTest.sdk().getRpc().getBlock(block_height-1).hash());
			Object exp_block = OntTest.sdk().getRpc().getBlockJson(hash);
			OntTest.logger().description("exp_blockJson : "+exp_block);
			
			assertEquals(true,ret_block.equals(exp_block));	
		} catch(RpcException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("error");
			int exp_errcode = 42002;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_004_getBlockJson() throws Exception {
		OntTest.logger().description("RPC_API 004 getBlockJson");

		try {
			OntTest.logger().step("测试getBlockJson()");
			
			int block_height = OntTest.sdk().getRpc().getBlockHeight();
			Block block = OntTest.sdk().getRpc().getBlock(block_height-1);
			OntTest.logger().description("block : "+block);
			String hash = String.valueOf(block.hash());
			OntTest.logger().description("block_hash : "+hash);
			
			Object hash_blockJson = OntTest.sdk().getRpc().getBlockJson(hash);
			OntTest.logger().description("ret_blockJson : "+hash_blockJson);
			Object height_blockJson = OntTest.sdk().getRpc().getBlockJson(block_height-1);
			OntTest.logger().description("exp_blockJson : "+height_blockJson);			
			
			assertEquals(true,hash_blockJson.equals(height_blockJson));	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_005_getBlock() throws Exception {
		OntTest.logger().description("RPC_API 005 getBlockJson");

		try {
			OntTest.logger().step("测试getBlock()");
			
			int block_height = OntTest.sdk().getRpc().getBlockHeight();
			Block height_block = OntTest.sdk().getRpc().getBlock(block_height-1);
			OntTest.logger().description("height_block : "+height_block);
			String hash = String.valueOf(height_block.hash());
			OntTest.logger().description("block_hash : "+hash);
			
			Block hash_block = OntTest.sdk().getRpc().getBlock(hash);
			OntTest.logger().description(hash_block.toString());

			assertEquals(true,hash_block.equals(height_block));	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_006_getBlockHeight() throws Exception {
		OntTest.logger().description("RPC_API 006 getBlockHeight");

		try {
			OntTest.logger().step("测试getBlockHeight()");
			
			int h = OntTest.sdk().getRpc().getBlockHeight();
			OntTest.logger().description("heigth = "+String.valueOf(h));
			
			assertEquals(true,true);	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_007_getTransaction() throws Exception {
		OntTest.logger().description("RPC_API 007 getTransaction");

		try {
			OntTest.logger().step("测试getTransaction()");

			Account acc = OntTest.common().getAccount(0);
			String addr = acc.getAddressU160().toBase58();
			String txhash = OntTest.sdk().nativevm().ont().sendTransfer(acc, addr, 1L, acc, 20000L, 0L);
			OntTest.logger().description("txhash : "+txhash);
			boolean r = OntTest.common().waitGenBlock();
			assertEquals(true,r);
			//交易哈希
			Transaction Transaction = OntTest.sdk().getRpc().getTransaction(txhash);
			OntTest.logger().description("Transaction : "+Transaction);	

			assertEquals(true,true);	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_008_getStorage() throws Exception {
		OntTest.logger().description("RPC_API 008 getStorage");

		try {
			OntTest.logger().step("测试getStorage()");
			OntTest.logger().description("contract_address = "+rpcapi_address);
			Map ret_deploy = OntTest.api().contract().deployContract(rpcapi_address, null);
			OntTest.logger().description("ret_deploy = "+ret_deploy);
			String codeAddr0 = String.valueOf(ret_deploy.get("address"));
			String codeAddr1 = Helper.reverse(codeAddr0);
			OntTest.logger().description(codeAddr1);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("6b6579303039")); //为字符串key009的16进制
	        args.add(Helper.hexToBytes("76616c7565303039")); //为字符串value009的16进制
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr1, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.logger().description("invokeTx : "+invokeTx);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1 : "+b1);
	        boolean b2 = OntTest.sdk().getConnect().sendRawTransaction(invokeTx.toHexString());
	        OntTest.logger().description("b2 : "+b2);
	        OntTest.common().waitTransactionResult(invokeTx.hash().toHexString());
			
	        String key = "6b6579303039";
			String Storage = OntTest.sdk().getRpc().getStorage(codeAddr0, key);
			OntTest.logger().description(Storage);
			
			assertEquals(true,Storage.equals("76616c7565303039"));		
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_009_getStorage() throws Exception {
		OntTest.logger().description("RPC_API 009 getStorage");

		try {
			OntTest.logger().step("测试getStorage()");
			OntTest.logger().description("contract_address = "+rpcapi_address);
			Map ret_deploy = OntTest.api().contract().deployContract(rpcapi_address, null);
			OntTest.logger().description("ret_deploy = "+ret_deploy);
			String codeAddr0 = String.valueOf(ret_deploy.get("address"));
			String codeAddr1 = Helper.reverse(codeAddr0);
			OntTest.logger().description(codeAddr1);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("6b6579303039")); //为字符串key009的16进制
	        args.add(Helper.hexToBytes("76616c7565303039")); //为字符串value009的16进制
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr1, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.logger().description("invokeTx : "+invokeTx);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1 : "+b1);
	        boolean b2 = OntTest.sdk().getConnect().sendRawTransaction(invokeTx.toHexString());
	        OntTest.logger().description("b2 : "+b2);
	        OntTest.common().waitTransactionResult(invokeTx.hash().toHexString());
			
	        String key = "6b6579303039";
			String Storage = OntTest.sdk().getRpc().getStorage(codeAddr0, key);
			OntTest.logger().description(Storage);
			
			assertEquals(true,Storage.equals("76616c7565303039"));		
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	

	@Test
	public void test_base_010_getBalance() throws Exception {
		OntTest.logger().description("RPC_API 010 getBalance");

		try {
			OntTest.logger().step("测试getBalance()");
			String addr = OntTest.common().getAccount(0).getAddressU160().toBase58();
			Object Balance = OntTest.sdk().getRpc().getBalance(addr);
			OntTest.logger().description(Balance.toString());
			
			assertEquals(true,true);	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_011_getContractJson() throws Exception {
		OntTest.logger().description("RPC_API 011 getContractJson");

		try {
			OntTest.logger().step("测试getContractJson()");
			OntTest.logger().description("contract_address = "+invoke_address);
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
	        
			Object Contract = OntTest.sdk().getRpc().getContractJson(codeAddr);
			OntTest.logger().description(Contract.toString());
			
			assertEquals(true,true);	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_012_getSmartCodeEvent() throws Exception {
		OntTest.logger().description("RPC_API 012 getSmartCodeEvent");

		try {
			OntTest.logger().step("测试getSmartCodeEvent()");
			
			Account acc = OntTest.common().getAccount(0);
			String addr = acc.getAddressU160().toBase58();
			String txhash = OntTest.sdk().nativevm().ont().sendTransfer(acc, addr, 100L, acc, 20000L, 0L);
			OntTest.logger().description("txhash = "+txhash);
			OntTest.common().waitTransactionResult(txhash);
			int height = OntTest.sdk().getRpc().getBlockHeightByTxHash(txhash);
			OntTest.logger().description("height = "+height);
			Object SmartCodeEvent = OntTest.sdk().getRpc().getSmartCodeEvent(height);
			
			OntTest.logger().description(SmartCodeEvent.toString());
			
			assertEquals(true,true);	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_013_getSmartCodeEvent() throws Exception {
		OntTest.logger().description("RPC_API 013 getSmartCodeEvent");

		try {
			OntTest.logger().step("测试getSmartCodeEvent()");
			Account acc = OntTest.common().getAccount(0);
			String addr = acc.getAddressU160().toBase58();
			String txhash = OntTest.sdk().nativevm().ont().sendTransfer(acc, addr, 100L, acc, 20000L, 0L);
			OntTest.logger().description(txhash);
			OntTest.common().waitTransactionResult(txhash);
			Object SmartCodeEvent = OntTest.sdk().getRpc().getSmartCodeEvent(txhash);
			OntTest.logger().description(SmartCodeEvent.toString());
			
			assertEquals(true,true);	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_014_getBlockHeightByTxHash() throws Exception {
		OntTest.logger().description("RPC_API 014 getBlockHeightByTxHash");

		try {
			OntTest.logger().step("测试getBlockHeightByTxHash()");
			
			Account acc = OntTest.common().getAccount(0);
			String addr = acc.getAddressU160().toBase58();
			String txhash = OntTest.sdk().nativevm().ont().sendTransfer(acc, addr, 100L, acc, 20000L, 0L);
			int height0 = OntTest.sdk().getRpc().getBlockHeight();
			OntTest.logger().description("height0 = "+height0);
			OntTest.logger().description(txhash);
			boolean r = OntTest.common().waitGenBlock();
			assertEquals(true,r);
			
			int height = OntTest.sdk().getRpc().getBlockHeightByTxHash(txhash);
			OntTest.logger().description(String.valueOf(height));
			
			assertEquals(true,true);	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_015_getMerkleProof() throws Exception {
		OntTest.logger().description("RPC_API 015 getMerkleProof");

		try {
			OntTest.logger().step("测试getMerkleProof()");

			Account acc = OntTest.common().getAccount(0);
			String addr = acc.getAddressU160().toBase58();
			String txhash = OntTest.sdk().nativevm().ont().sendTransfer(acc, addr, 100L, acc, 20000L, 0L);
			OntTest.logger().description(txhash);
			boolean r = OntTest.common().waitGenBlock();
			assertEquals(true,r);
			
			Object MerkleProof = OntTest.sdk().getRpc().getMerkleProof(txhash);
			OntTest.logger().description(MerkleProof.toString());
			
			assertEquals(true,true);	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_016_sendRawTransaction() throws Exception {
		OntTest.logger().description("RPC_API 016 sendRawTransaction");

		try {
			OntTest.logger().step("测试sendRawTransaction()");
			
			OntTest.logger().description("contract_address = "+invoke_address);
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        boolean RawTransaction = OntTest.sdk().getRpc().sendRawTransaction(invokeTx.toHexString());
			OntTest.logger().description("RawTransactionResult = "+String.valueOf(RawTransaction));
			
			assertEquals(true,RawTransaction);	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_017_sendRawTransaction() throws Exception {
		OntTest.logger().description("RPC_API 017 sendRawTransaction");

		try {
			OntTest.logger().step("测试sendRawTransaction()");

			OntTest.logger().description("contract_address = "+invoke_address);
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        Transaction transaction = OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        boolean RawTransaction = OntTest.sdk().getRpc().sendRawTransaction(transaction);
			OntTest.logger().description("RawTransactionResult = "+String.valueOf(RawTransaction));
			
			assertEquals(true,RawTransaction);	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_base_018_sendRawTransactionPreExec() throws Exception {
		OntTest.logger().description("RPC_API 018 sendRawTransactionPreExec");

		try {
			OntTest.logger().step("测试sendRawTransactionPreExec()");
			
			OntTest.logger().description("contract_address = "+invoke_address);
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map rawTransaction = (Map)OntTest.sdk().getRpc().sendRawTransactionPreExec(invokeTx.toHexString());
			OntTest.logger().description("RawTransactionResult = "+String.valueOf(rawTransaction));
			String ret = (String) rawTransaction.get("Result");
			
			assertEquals(true,ret.equals("01"));
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_base_019_getAllowance() throws Exception {
		OntTest.logger().description("RPC_API 019 getAllowance");

		try {
			OntTest.logger().step("测试getAllowance()");
			
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();

			String ret0 = OntTest.sdk().nativevm().ont().sendApprove(acc1,addr2, 1L, acc1, 20000L,0L);
			boolean r = OntTest.common().waitTransactionResult(ret0);
			assertEquals(true,r);
			long ret1 = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(ret1));
			String exp = String.valueOf(ret1);
			
			String Allowance = OntTest.sdk().getRpc().getAllowance("ont",addr1,addr2);
			OntTest.logger().description(Allowance);
			assertEquals(true,Allowance.equals(exp));	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_020_getAllowance() throws Exception {
		OntTest.logger().description("RPC_API 020 getAllowance");

		try {
			OntTest.logger().step("测试getAllowance()");
			
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();

			String ret0 = OntTest.sdk().nativevm().ont().sendApprove(acc1,addr2, 1L, acc1, 20000L,0L);
			boolean r = OntTest.common().waitTransactionResult(ret0);
			assertEquals(true,r);
			long ret1 = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(ret1));
			String exp = String.valueOf(ret1);
			
			String Allowance = OntTest.sdk().getRpc().getAllowance("ont",addr1,addr2);
			OntTest.logger().description(Allowance);
			assertEquals(true,Allowance.equals(exp));	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_021_getAllowance() throws Exception {
		OntTest.logger().description("RPC_API 021 getAllowance");

		try {
			OntTest.logger().step("测试getAllowance()");
			
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();

			String ret0 = OntTest.sdk().nativevm().ont().sendApprove(acc1,addr2, 1L, acc1, 20000L,0L);
			boolean r = OntTest.common().waitTransactionResult(ret0);
			assertEquals(true,r);
			long ret1 = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(ret1));
			String exp = String.valueOf(ret1);
			
			String Allowance = OntTest.sdk().getRpc().getAllowance("ont",addr1,addr2);
			OntTest.logger().description(Allowance);
			assertEquals(true,Allowance.equals(exp));	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_022_getMemPoolTxCount() throws Exception {
		OntTest.logger().description("RPC_API 022 getMemPoolTxCount");

		try {
			OntTest.logger().step("测试getMemPoolTxCount()");
			
			Account acc = OntTest.common().getAccount(0);
			String addr = acc.getAddressU160().toBase58();
			String txhash = OntTest.sdk().nativevm().ont().sendTransfer(acc, addr, 1L, acc, 20000L, 0L);
			OntTest.logger().description(txhash);
			Object MemPoolTxCount = OntTest.sdk().getRpc().getMemPoolTxCount();
			OntTest.logger().description(MemPoolTxCount.toString());
			assertEquals(true,true);	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_023_getMemPoolTxState() throws Exception {
		OntTest.logger().description("RPC_API 023 getMemPoolTxState");

		try {
			OntTest.logger().step("测试getMemPoolTxState()");
			
			Account acc = OntTest.common().getAccount(0);
			String addr = acc.getAddressU160().toBase58();
			String txhash = OntTest.sdk().nativevm().ont().sendTransfer(acc, addr, 100L, acc, 20000L, 0L);
			Object MemPoolTxState = OntTest.sdk().getRpc().getMemPoolTxState(txhash);
			OntTest.logger().description(MemPoolTxState.toString());
			assertEquals(true,true);	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_024_syncSendRawTransaction() throws Exception {
		OntTest.logger().description("RPC_API 024 syncSendRawTransaction");

		try {
			OntTest.logger().step("测试syncSendRawTransaction()");
			
			OntTest.logger().description("contract_address = "+invoke_address);
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        Transaction transaction = OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
			
			Map sync = (Map) OntTest.sdk().getRestful().syncSendRawTransaction(invokeTx.toHexString());
			OntTest.logger().description("sync = "+sync);
			int state = (int) sync.get("State");
			
			assertEquals(true,state==1);	
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
}
	
