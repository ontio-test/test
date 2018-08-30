package com.ontio.sdkapi;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import java.util.ArrayList;
import java.util.Base64;
import java.util.List;
import java.util.Map;
import java.util.ResourceBundle;

import javax.xml.bind.DatatypeConverter;

import org.junit.After;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import com.alibaba.fastjson.JSON;
import com.github.ontio.account.Account;
import com.github.ontio.common.Helper;
import com.github.ontio.core.payload.InvokeCode;
import com.github.ontio.core.transaction.Transaction;
import com.github.ontio.network.exception.RpcException;
import com.github.ontio.sdk.exception.SDKException;
import com.github.ontio.smartcontract.neovm.abi.BuildParams;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;
import com.ontio.testtool.utils.Config;

public class Invoke {
	@Rule public OntTestWatcher watchman= new OntTestWatcher();
	String invoke_address = this.getClass().getResource("invoke.cs").getPath();
	String two_address = this.getClass().getResource("20000.cs").getPath();
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
		OntTest.api().node().restartAll("ontology", "config.json", Config.DEFAULT_NODE_ARGS);
		OntTest.api().node().initOntOng();
		OntTest.logger().step("*******************init_ONGONT_Finish*******************");
	}
	
	@Before
	public void setUp() throws Exception {
		OntTest.logger().step("setUp");
	}
	
	@After
	public void TearDown() throws Exception {
		OntTest.logger().step("TearDown");
	}
	
	/************************************************************************/
	@Test
	public void test_base_001_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数codeAddr");
		
		try {
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
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			e.printStackTrace();
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_abnormal_002_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数codeAddr");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			codeAddr = codeAddr.substring(0,codeAddr.length()-3)+"abc";
			OntTest.logger().description("codeAddr = "+codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        //assertEquals(true,ret.equals(exp));
			assertTrue(false);
		} catch(RpcException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("error");
			int exp_errcode = 47001;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
//	@Test
//	public void test_abnormal_003_makeInvokeCodeTransaction() throws Exception {
//		OntTest.logger().description("测试makeInvokeCodeTransaction参数codeAddr");
//		
//		try {
//			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
//			String codeAddr = String.valueOf(ret_deploy.get("address"));
//			codeAddr = Helper.reverse(codeAddr);
//			//codeAddr为存在的地址但并非合约地址
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"a";
//			System.out.println(codeAddr);//智能合约地址
//			
//	        List list = new ArrayList<Object>();
//	        list.add("test".getBytes());
//	        List args = new ArrayList<Object>();
//	        args.add(1);
//	        list.add(args);
//	        
//	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
//	        byte[] params = BuildParams.createCodeParamsScript(list);
//	        
//	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
//	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
//	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
//	        System.out.println("b1: " + b1);
//	        String ret = String.valueOf(b1.get("Result"));
//	        String exp = "01";
//	        assertEquals(true,ret.equals(exp));
//		} catch(RpcException e) {
//			String ret_err = String.valueOf(e);
//			System.out.println(ret_err);
//			String exp_err = String.valueOf("com.github.ontio.network.exception.RpcException: {\"result\":\"\",\"id\":1,\"error\":47001,\"jsonrpc\":\"2.0\",\"desc\":\"SMARTCODE EXEC ERROR\"}");
//			assertEquals(true,ret_err.equals(exp_err));
//		} catch(Exception e) {
//			System.out.println(e);
//			OntTest.logger().error(e.toString());
//			fail();
//		}
//	}
	
	@Test
	public void test_abnormal_004_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数codeAddr");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			codeAddr = "ab"+ codeAddr;
			//codeAddr长度为35及以上
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
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        assertEquals(true,ret.equals(exp));
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(false);
		}  catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_005_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数codeAddr");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
			//34个字符的codeAddr中包含非法符号（%￥#）
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
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        assertEquals(true,ret.equals(exp));
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(false);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_006_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数codeAddr");
		
		try {
//			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
//			String codeAddr = String.valueOf(ret_deploy.get("address"));
//			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
			String codeAddr = "";
			//留空
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
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        assertEquals(true,ret.equals(exp));
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(false);
		}  catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_007_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数method");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
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
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_008_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数method");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
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
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_009_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数method");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
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
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_010_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数param");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
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
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_011_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数param");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
			OntTest.logger().description("codeAddr = "+codeAddr);//智能合约地址
			
//	        List list = new ArrayList<Object>();
//	        list.add("test".getBytes());
//	        List args = new ArrayList<Object>();
//	        args.add(Helper.hexToBytes("1"));
//	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        OntTest.logger().description("payerAddr = "+payerAddr);
//	        byte[] params = BuildParams.createCodeParamsScript(list);
			byte[] params = {1,2,3,4,5,6,7,8};
					 
			InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
			OntTest.logger().description("invokeTx = "+invokeTx);
			OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
			OntTest.logger().description("invokeTx.toHexString() = "+invokeTx.toHexString());
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        //assertEquals(true,ret.equals(exp));
			assertTrue(false);
		} catch(RpcException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("error");
			int exp_errcode = 47001;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_012_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数param");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			OntTest.logger().description(codeAddr);//智能合约地址
//	        List list = new ArrayList<Object>();
//	        list.add("test".getBytes());
//	        List args = new ArrayList<Object>();
//	        args.add(Helper.hexToBytes("01"));
//	        list.add(args);
			
			List list = new ArrayList();
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
			InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        //assertEquals(true,ret.equals(exp));
			assertTrue(false);
		} catch(RpcException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("error");
			int exp_errcode = 47001;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_013_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数payer");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
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
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_014_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数payer");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        payerAddr = payerAddr.substring(0,payerAddr.length()-2)+"7b";
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
			InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        //assertEquals(true,ret.equals(exp));
			assertTrue(false);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58004;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_015_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数payer");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        payerAddr = payerAddr + "7";
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
			InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        //assertEquals(true,ret.equals(exp));
			assertTrue(false);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58004;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_016_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数payer");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        payerAddr = payerAddr.substring(0,payerAddr.length()-2)+"#$";
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
			InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        //assertEquals(true,ret.equals(exp));
			assertTrue(false);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58004;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_017_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数payer");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
//	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
//	        payerAddr = payerAddr.substring(0,payerAddr.length()-2)+"7b";
	        String payerAddr = "";
	        
			InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        //assertEquals(true,ret.equals(exp));
			assertTrue(false);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58004;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_018_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数gaslimit");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        
			InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_019_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数gaslimit");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        
			InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, 0, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        int ret = (int) b1.get("State");
	        int exp = 1;
	        assertEquals(true,ret!=exp);
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(false);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_020_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数gaslimit");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        
			InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr,-20000, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        boolean b2 = OntTest.sdk().getConnect().sendRawTransaction(invokeTx.toHexString());
	        System.out.println("b2 = "+b2);
	        OntTest.logger().description("b1: " + b1);
	        int ret = (int) b1.get("State");
	        int exp = 1;
	        assertEquals(true,ret!=exp);
//		} catch(SDKException e) {
//	        Map err = (Map) JSON.parse(e.getMessage()); 
//			System.out.println("err = "+err);
//			int err_code = (int) err.get("Error");
//			int exp_errcode = 58004;
//			OntTest.logger().error(e.toString());
//			assertEquals(true,err_code==exp_errcode);
//		} catch(RpcException e) {
//	        Map err = (Map) JSON.parse(e.getMessage()); 
//			System.out.println("err = "+err);
//			int err_code = (int) err.get("error");
//			int exp_errcode = 43001;
//			OntTest.logger().error(e.toString());
//			assertEquals(true,err_code==exp_errcode);
		} catch(SDKException e) {
				System.out.println(e);
				assertTrue(false);
			 
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_021_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数gaslimit");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(two_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("Test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add("20000000000");
	        list.add(args);
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        
			InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
			//错误的数量gaslimit为20000（实际步数大于20000但ONG足够）
			OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        int ret = (int) b1.get("State");
	        int exp = 1;
	        //assertEquals(false,ret==exp);
	        assertTrue(false);
		} catch(RpcException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("error");
			int exp_errcode = 47001;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			e.printStackTrace();
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_022_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数gaslimit");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        Account acc0 = OntTest.common().getAccount(0);
	        String addr0 = acc0.getAddressU160().toBase58();
	        Account acc1 = OntTest.common().getAccount(1);
	        String addr1 = acc1.getAddressU160().toBase58();
	        
	        long ongnum = OntTest.sdk().nativevm().ong().queryBalanceOf(addr0);
	        OntTest.logger().description("目前包含ong数目: "+ongnum);
	        if(ongnum!=0L){
	        	OntTest.logger().description("ong转账");
	        	String txhash = OntTest.sdk().nativevm().ong().sendTransfer(acc0, addr1, ongnum, acc0, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        	OntTest.common().waitTransactionResult(txhash);
	        	assertEquals(true,false);
	        	OntTest.logger().description("目前包含ong数目(应该为0) : "+OntTest.sdk().nativevm().ong().queryBalanceOf(addr0));
	        }
	        
			InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, addr0, OntTest.sdk().DEFAULT_GAS_LIMIT, 10);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map ret0 = (Map) OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("ret0_sendRawTransactionPreExec: " + ret0);
	        int ret = (int) ret0.get("State");
	        int exp = 1;
//	        boolean ret1 = OntTest.sdk().getConnect().sendRawTransaction(invokeTx.toHexString());
//	        OntTest.logger().description("ret1: " + ret1);
////	        String  ret0 = String.valueOf(ret0.get("Result"));
////	        boolean exp = true;
	        //assertEquals(true,ret!=exp);
			assertTrue(false);
		} catch(RpcException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("error");
			int exp_errcode = 43001;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_023_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数gaslimit");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        
			InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, 1000000000L, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_024_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数gasprice");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        
			InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_abnormal_025_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数gasprice");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        
			InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, -10);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        boolean b2 = OntTest.sdk().getConnect().sendRawTransaction(invokeTx.toHexString());
	        System.out.println("b2 = "+b2);
	        OntTest.logger().description("b1: " + b1);
	        int ret = (int) b1.get("State");
	        int exp = 1;
	        assertEquals(true,ret!=exp);
//		} catch(RpcException e) {
//	        Map err = (Map) JSON.parse(e.getMessage()); 
//			System.out.println("err = "+err);
//			int err_code = (int) err.get("error");
//			int exp_errcode = 43001;
//			OntTest.logger().error(e.toString());
//			assertEquals(true,err_code==exp_errcode);
		} catch(SDKException e) {
			System.out.println(e);
			assertTrue(false);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_026_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数gasprice");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        Account acc0 = OntTest.common().getAccount(0);
	        String addr0 = acc0.getAddressU160().toBase58();
	        Account acc1 = OntTest.common().getAccount(1);
	        String addr1 = acc1.getAddressU160().toBase58();
	        
	        long ongnum = OntTest.sdk().nativevm().ong().queryBalanceOf(addr0);
	        OntTest.logger().description(String.valueOf(ongnum));
	        if(ongnum!=0L){
	        	OntTest.logger().description("ong转账");
	        	String txhash = OntTest.sdk().nativevm().ong().sendTransfer(acc0, addr1, ongnum, acc0, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        	OntTest.common().waitTransactionResult(txhash);
	        	assertEquals(true,false);;
	        }
	        
			InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, addr0, OntTest.sdk().DEFAULT_GAS_LIMIT, 10);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        int ret = (int) b1.get("State");
	        int exp = 1;
	        assertEquals(true,ret!=exp);
		}  catch(SDKException e) {
			System.out.println(e);
			assertTrue(false);
		}catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_normal_027_makeInvokeCodeTransaction() throws Exception {
		OntTest.logger().description("测试makeInvokeCodeTransaction参数gasprice");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract(invoke_address, null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
//			codeAddr = codeAddr.substring(0,codeAddr.length()-1)+"#";
			OntTest.logger().description(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        
			InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 1000000000L);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        OntTest.logger().description("b1: " + b1);
	        String  ret = String.valueOf(b1.get("Result"));
	        String exp = "01";
	        assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
}
