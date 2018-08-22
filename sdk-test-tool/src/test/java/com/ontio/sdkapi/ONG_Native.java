package com.ontio.sdkapi;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import java.util.Map;

import org.junit.After;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import com.alibaba.fastjson.JSON;
import com.github.ontio.account.Account;
import com.github.ontio.network.exception.RpcException;
import com.github.ontio.sdk.exception.SDKException;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;
import com.ontio.testtool.utils.Config;

public class ONG_Native {
	@Rule public OntTestWatcher watchman= new OntTestWatcher();
	
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
	public void test_base_001_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			//正确的sendAcct
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("start:");
			OntTest.logger().description("ongnum1 = "+String.valueOf(ongnum1));
			OntTest.logger().description("ongnum2 = "+String.valueOf(ongnum2));
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Transfer);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("final:");
			OntTest.logger().description("ongnum3 = "+String.valueOf(ongnum3));
			OntTest.logger().description("ongnum4 = "+String.valueOf(ongnum4));			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			OntTest.logger().description(String.valueOf(inc));
			assertEquals(true,inc==1000000000);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_002_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			//Account acc1 = OntTest.common().getAccount(0);
			Account acc1 = null;
			//留空
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("start:");
			OntTest.logger().description("ongnum1 = "+String.valueOf(ongnum1));
			OntTest.logger().description("ongnum2 = "+String.valueOf(ongnum2));
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Transfer);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("final:");
			OntTest.logger().description("ongnum3 = "+String.valueOf(ongnum3));
			OntTest.logger().description("ongnum4 = "+String.valueOf(ongnum4));			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			OntTest.logger().description(String.valueOf(inc));
			assertEquals(true,inc==1000000000);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_004_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			addr2 = addr2.substring(0,addr2.length()-3)+"abc";
			//recvAddr不存在（乱码但符合recvAddr34个字符要求）
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("start:");
			OntTest.logger().description("ongnum1 = "+String.valueOf(ongnum1));;
			OntTest.logger().description("ongnum2 = "+String.valueOf(ongnum2));
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Transfer);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("final:");
			OntTest.logger().description("ongnum3 = "+String.valueOf(ongnum3));
			OntTest.logger().description("ongnum4 = "+String.valueOf(ongnum4));			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			OntTest.logger().description(String.valueOf(inc));
			assertEquals(true,inc==1000000000);
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
	public void test_abnormal_005_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			addr2 = "a" + addr2;
			//recvAddr35
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("start:");
			OntTest.logger().description("ongnum1 = "+String.valueOf(ongnum1));;
			OntTest.logger().description("ongnum2 = "+String.valueOf(ongnum2));
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Transfer);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("final:");
			OntTest.logger().description("ongnum3 = "+String.valueOf(ongnum3));
			OntTest.logger().description("ongnum4 = "+String.valueOf(ongnum4));			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			OntTest.logger().description(String.valueOf(inc));
			assertEquals(true,inc==1000000000);
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
	public void test_abnormal_006_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			addr2 = addr2.substring(0,addr2.length()-3)+"@#$";
			//recvAddr@#
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
//			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
//			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
//			OntTest.logger().description("start:");
//			OntTest.logger().description("ongnum1 = "+String.valueOf(ongnum1));;
//			OntTest.logger().description("ongnum2 = "+String.valueOf(ongnum2));
			System.out.println("11132");
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Transfer);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("final:");
			OntTest.logger().description("ongnum3 = "+String.valueOf(ongnum3));
			OntTest.logger().description("ongnum4 = "+String.valueOf(ongnum4));			
			
//			long dec = ongnum1-ongnum3;
//			long inc = ongnum4-ongnum2;
//			OntTest.logger().description(String.valueOf(inc));
			assertEquals(true,false);
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
	public void test_abnormal_007_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			//String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			String addr2 = "";
			//留空
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
//			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
//			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
//			OntTest.logger().description("start:");
//			OntTest.logger().description("ongnum1 = "+String.valueOf(ongnum1));;
//			OntTest.logger().description("ongnum2 = "+String.valueOf(ongnum2));
//			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Transfer);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("final:");
			OntTest.logger().description("ongnum3 = "+String.valueOf(ongnum3));
			OntTest.logger().description("ongnum4 = "+String.valueOf(ongnum4));			
//			
//			long dec = ongnum1-ongnum3;
//			long inc = ongnum4-ongnum2;
//			OntTest.logger().description(String.valueOf(inc));
//			assertEquals(true,inc==1000000000);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_008_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("start:");
			OntTest.logger().description("ongnum1 = "+String.valueOf(ongnum1));
			OntTest.logger().description("ongnum2 = "+String.valueOf(ongnum2));
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc2, gaslimit, gasprice);
			//gasacc为接受ongacc
			OntTest.logger().description(Transfer);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("final:");
			OntTest.logger().description("ongnum3 = "+String.valueOf(ongnum3));
			OntTest.logger().description("ongnum4 = "+String.valueOf(ongnum4));			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			OntTest.logger().description(String.valueOf(inc));
			assertEquals(true,inc==amount);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_010_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 0;
			//正确的数量0
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("start:");
			OntTest.logger().description("ongnum1 = "+String.valueOf(ongnum1));;
			OntTest.logger().description("ongnum2 = "+String.valueOf(ongnum2));
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Transfer);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("final:");
			OntTest.logger().description("ongnum3 = "+String.valueOf(ongnum3));
			OntTest.logger().description("ongnum4 = "+String.valueOf(ongnum4));			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			OntTest.logger().description(String.valueOf(inc));
			assertEquals(true,inc==1000000000);
		}catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_011_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = -1000000000;
			//amount为负数
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("start:");
			OntTest.logger().description("ongnum1 = "+String.valueOf(ongnum1));;
			OntTest.logger().description("ongnum2 = "+String.valueOf(ongnum2));
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Transfer);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("final:");
			OntTest.logger().description("ongnum3 = "+String.valueOf(ongnum3));
			OntTest.logger().description("ongnum4 = "+String.valueOf(ongnum4));			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			OntTest.logger().description(String.valueOf(inc));
			assertEquals(true,inc==1000000000);
		}catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_013_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			long amount = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			//amount=实际所有的ONG数量
			long gaslimit = 20000;
			long gasprice = 10;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("start:");
			OntTest.logger().description("ongnum1 = "+String.valueOf(ongnum1));;
			OntTest.logger().description("ongnum2 = "+String.valueOf(ongnum2));
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Transfer);
			boolean r = OntTest.common().waitGenBlock();
			assertEquals(true,r);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("final:");
			OntTest.logger().description("ongnum3 = "+String.valueOf(ongnum3));
			OntTest.logger().description("ongnum4 = "+String.valueOf(ongnum4));			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			OntTest.logger().description(String.valueOf(inc));

			assertEquals(true,inc==0);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_014_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			long amount = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1)+10000000L;
			//amount大于实际所有的ONG数量
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("start:");
			OntTest.logger().description("ongnum1 = "+String.valueOf(ongnum1));;
			OntTest.logger().description("ongnum2 = "+String.valueOf(ongnum2));
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Transfer);
			boolean r = OntTest.common().waitGenBlock();
			assertEquals(true,r);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("final:");
			OntTest.logger().description("ongnum3 = "+String.valueOf(ongnum3));
			OntTest.logger().description("ongnum4 = "+String.valueOf(ongnum4));			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			OntTest.logger().description(String.valueOf(inc));

			assertEquals(true,inc==0);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_017_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			Account payer = OntTest.common().getAccount(2);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("start:");
			OntTest.logger().description("ongnum1 = "+String.valueOf(ongnum1));;
			OntTest.logger().description("ongnum2 = "+String.valueOf(ongnum2));
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, payer, gaslimit, gasprice);
			//payer为第三方
			OntTest.logger().description(Transfer);
			boolean r = OntTest.common().waitGenBlock();
			assertEquals(true,r);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("final:");
			OntTest.logger().description("ongnum3 = "+String.valueOf(ongnum3));
			OntTest.logger().description("ongnum4 = "+String.valueOf(ongnum4));			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			OntTest.logger().description(String.valueOf(inc));
			assertEquals(true,inc==amount);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_018_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			//留空
			Account acc2 = OntTest.common().getAccount(1);
			Account payer = null;
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("start:");
			OntTest.logger().description("ongnum1 = "+String.valueOf(ongnum1));;
			OntTest.logger().description("ongnum2 = "+String.valueOf(ongnum2));
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, payer, gaslimit, gasprice);
			OntTest.logger().description(Transfer);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("final:");
			OntTest.logger().description("ongnum3 = "+String.valueOf(ongnum3));
			OntTest.logger().description("ongnum4 = "+String.valueOf(ongnum4));			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			OntTest.logger().description(String.valueOf(inc));
			assertEquals(true,inc==1000000000);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_021_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = -20000;
			//正确的数量gaslimit为负数（实际步数小于20000且ONG足够）
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("start:");
			OntTest.logger().description("ongnum1 = "+String.valueOf(ongnum1));;
			OntTest.logger().description("ongnum2 = "+String.valueOf(ongnum2));
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Transfer);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("final:");
			OntTest.logger().description("ongnum3 = "+String.valueOf(ongnum3));
			OntTest.logger().description("ongnum4 = "+String.valueOf(ongnum4));			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			OntTest.logger().description(String.valueOf(inc));
			assertEquals(true,inc==1000000000);
		}catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
//	@Test
//	public void test_abnormal_022_sendTransfer() throws Exception {
//		OntTest.logger().description("测试sendTransfer参数sendAcct");
//		
//		try {
//			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
//			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
//			 
//			Account acc1 = OntTest.common().getAccount(0);
//			Account acc2 = OntTest.common().getAccount(1);
//			long amount = 1000000000;
//			long gaslimit = 20000;
//			//错误的数量gaslimit为20000（实际步数大于20000但ONG足够）
//			long gasprice = 0;
//			
//			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
//			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
//			System.out.println("start:");
//			System.out.println(ongnum1);
//			System.out.println(ongnum2);
//			
//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			System.out.println(Transfer);
//			boolean r = OntTest.common().waitTransactionResult(Transfer);
//			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
//			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
//			System.out.println("final:");
//			System.out.println(ongnum3);
//			System.out.println(ongnum4);			
//			
//			long dec = ongnum1-ongnum3;
//			long inc = ongnum4-ongnum2;
//			System.out.println(inc);
//			assertEquals(true,inc==1000000000);
//		} catch(Exception e) {
//			System.out.println(e);
//			OntTest.logger().error(e.toString());
//			fail();
//		}
//	}

	@Test
	public void test_abnormal_027_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = -1000000;
			//错误的数量（负数）
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("start:");
			OntTest.logger().description("ongnum1 = "+String.valueOf(ongnum1));;
			OntTest.logger().description("ongnum2 = "+String.valueOf(ongnum2));
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Transfer);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("final:");
			OntTest.logger().description("ongnum3 = "+String.valueOf(ongnum3));
			OntTest.logger().description("ongnum4 = "+String.valueOf(ongnum4));			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			OntTest.logger().description(String.valueOf(inc));
			assertEquals(true,inc==1000000000);
		}catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_028_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1)+10000000L;
			long gaslimit = 20000;
			long gasprice = 1000000L;
			//错误的数量10（ONG小于gaslimit与gasprice的乘积加上amount）
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("start:");
			OntTest.logger().description("ongnum1 = "+String.valueOf(ongnum1));;
			OntTest.logger().description("ongnum2 = "+String.valueOf(ongnum2));;
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Transfer);
			boolean r = OntTest.common().waitGenBlock();
			assertEquals(true,r);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			OntTest.logger().description("final:");
			OntTest.logger().description("ongnum3 = "+String.valueOf(ongnum3));;
			OntTest.logger().description("ongnum4 = "+String.valueOf(ongnum4));			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			OntTest.logger().description(String.valueOf(inc));
			assertEquals(true,inc==0);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_031_queryBalanceOf() throws Exception {
		OntTest.logger().description("测试queryBalanceOf参数address");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();	
			//正确的address值
			long ongnum = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			OntTest.logger().description(String.valueOf(ongnum));

			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_032_queryBalanceOf() throws Exception {
		OntTest.logger().description("测试queryBalanceOf参数address");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();	
			addr1 = addr1.substring(0,addr1.length()-3)+"abc";
			//address不存在，未创建的地址（34个字符）
			long ongnum = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			OntTest.logger().description(String.valueOf(ongnum));

			assertEquals(true,false);
		}catch(SDKException e) {
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
	public void test_abnormal_033_queryBalanceOf() throws Exception {
		OntTest.logger().description("测试queryBalanceOf参数address");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			addr1 = "a"+addr1;
			//address长度为35及以上
			long ongnum = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			OntTest.logger().description(String.valueOf(ongnum));

			assertEquals(true,false);
		}catch(SDKException e) {
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
	public void test_abnormal_034_queryBalanceOf() throws Exception {
		OntTest.logger().description("测试queryBalanceOf参数address");
		
		try {
			//String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();	
			String addr1 = "";
			//留空
			long ongnum = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			OntTest.logger().description(String.valueOf(ongnum));

			assertEquals(true,true);
		}catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_abnormal_035_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数fromAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			//fromAddr存在，但并没有前提sendApprove
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			OntTest.logger().description(String.valueOf(Allowance));
			long Allowance1 = Long.valueOf(OntTest.sdk().getRpc().getAllowance("ong",add1,add2));
			OntTest.logger().description(String.valueOf(Allowance1));
			assertEquals(true,Allowance==Allowance1);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_036_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数fromAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			//正确的fromAddr值
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(true,Allowance==1000000000);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_037_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数fromAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			add1 = add1.substring(0,add1.length()-3)+"abc";
			//fromAddr不存在，未创建的地址（34个字符）
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(true,Allowance==1000000000);
		}catch(SDKException e) {
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
	public void test_abnormal_038_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数fromAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			add1 = "a"+add1;
			//fromAddr长度为35及以上
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(false,Allowance==1000000000);
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
	public void test_abnormal_039_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数fromAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			//String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String add1 = "";
			//留空
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(false,Allowance==1000000000);
		}catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		}catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_040_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数fromAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			//fromAddr和toAddr与sendApprove时相反
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add2, add1);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(false,Allowance==1000000000);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_042_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数toAddr");
		
		try {
			OntTest.api().node().restartAll("ontology", "config.json", Config.DEFAULT_NODE_ARGS);
			OntTest.api().node().initOntOng();
			OntTest.logger().step("*******************init_ONGONT_Finish*******************");
			
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();	
			//toAddr存在，但并没有前提sendApprove
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			OntTest.logger().description(String.valueOf(Allowance));
			long Allowance1 = Long.valueOf(OntTest.sdk().getRpc().getAllowance("ong",add1,add2));
			OntTest.logger().description(String.valueOf(Allowance1));
			assertEquals(true,Allowance==Allowance1);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_043_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数toAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			add2 = add2.substring(0,add2.length()-3)+"abc";
			//toAddr不存在，未创建的地址（34个字符）
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(true,Allowance==1000000000);
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
	public void test_abnormal_044_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数toAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			add2 = "a"+add2;
			//toAddr长度为35及以上
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(false,Allowance==1000000000);
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
	public void test_abnormal_045_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数toAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			add2 = add2.substring(0,add2.length()-1);
			//toAddr长度为33及以下
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(true,Allowance==1000000000);
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
	public void test_abnormal_046_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数toAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			//String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();	
			String add2 = "";
			//留空
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(true,Allowance==1000000000);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_047_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			//正确的sendAcct（与payerAcct一致）
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(true,Allowance==1000000000);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_048_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			//Account acc1 = OntTest.common().getAccount(0);
			Account acc1 = null;
			//留空
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(false,Allowance==1000000000);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_050_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			addr2 = addr2.substring(0,addr2.length()-3)+"abc";
			//recvAddr不存在（乱码但符合recvAddr34个字符要求）
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(false,Allowance==1000000000);
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
	public void test_abnormal_051_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			addr2 = "a"+addr2;
			//recvAddr长度为35及以上
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(false,Allowance==1000000000);
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
	public void test_abnormal_052_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			addr2 = addr2.substring(0,addr2.length()-3)+"#@$";
			//34个字符的recvAddr中包含非法符号（%￥#）
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(false,Allowance==1000000000);
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
	public void test_abnormal_053_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			//String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			String addr2 = "";
			//留空
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(false,Allowance==1000000000);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_055_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 0;
			//正确的数量0，sendAcct也有足够ONG
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(false,Allowance==1000000000);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_056_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = -1000000000;
			//amount为负数，sendAcct也有足够ONG
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(false,Allowance==1000000000);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_059_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1)+10000000L;
			//amount大于实际所有的ONG数量
			long gaslimit = 20000;
			long gasprice = 0;
			
			long Allowance1 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description("Allowance1:"+Allowance1);
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance2 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description("Allowance2:"+Allowance2);

			assertEquals(true,Allowance2==amount);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_061_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			String addr3 = OntTest.common().getAccount(2).getAddressU160().toBase58();
			
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			Account acc3 = OntTest.common().getAccount(2);
			long amount = 1000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve0 = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, 1, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve0);
			boolean r = OntTest.common().waitTransactionResult(Approve0);
			assertEquals(true,r);
			
			long Allowance1 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description("Allowance1:"+Allowance1);
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc3, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r2 = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r2);
			
			long Allowance2 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description("Allowance2:"+Allowance2);


			assertEquals(true,Allowance2==1000000);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_062_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数payerAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, null, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(false,Allowance==1000000000);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_065_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = -20000;
			//正确的数量gaslimit为负数（实际步数小于20000且ONG足够）
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(true,Allowance==1000000000);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_067_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, 1L, acc1, 20000L, 0L);
			OntTest.common().waitGenBlock();
			OntTest.logger().description("ONG(addr1) = "+ OntTest.sdk().nativevm().ong().queryBalanceOf(addr1));
			long amount = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1)+2000000000L;
			OntTest.logger().description("amount : "+amount);
			long gaslimit = 20000;
			//错误的数量20000，ONG小于gaslimit与gasprice的乘积加上amount
			long gasprice = 0L;
			
			long Allowance1 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description("Allowance1 : "+Allowance1);
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.common().waitGenBlock();
			OntTest.logger().description("ONG_now(addr1) = "+ OntTest.sdk().nativevm().ong().queryBalanceOf(addr1));
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance2 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description("Allowance2 : "+Allowance2);

			assertEquals(true,amount==Allowance2);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_071_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = -10000;
			//正确的数量（负数）
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(true,Allowance==1000000000);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_072_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1)+1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			//正确的数量10（ONG小于gaslimit与gasprice的乘积加上amount）
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance));

			assertEquals(true,Allowance==amount);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_075_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {	
			OntTest.api().node().restartAll("ontology", "config.json", Config.DEFAULT_NODE_ARGS);
			OntTest.api().node().initOntOng();
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			//正确的sendAcct
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			OntTest.logger().description("amount = "+amount);
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			OntTest.logger().description("addr1 has "+ongnum+" ong");
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description("Allowance0 = "+Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc2, gaslimit, gasprice);
				OntTest.logger().description(TransferFrom);
				boolean r2 = OntTest.common().waitTransactionResult(TransferFrom);
				assertEquals(true,r2);
				
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_076_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc1, addr1, addr2, amount, acc2, gaslimit, gasprice);
				//sendAcct并非sendApprove的账户
				OntTest.logger().description(TransferFrom);
				boolean r2 = OntTest.common().waitGenBlock();
				assertEquals(true,r2);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(false,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_077_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(null, addr1, addr2, amount, acc2, gaslimit, gasprice);
				//sendacct留空
				OntTest.logger().description(TransferFrom);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,false);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_079_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数fromAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			String addr3 = OntTest.common().getAccount(2).getAddressU160().toBase58();
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr3, addr2, amount, acc2, gaslimit, gasprice);
				//fromAddr存在，但并非sendApprove的地址
				OntTest.logger().description(TransferFrom);
				boolean r2 = OntTest.common().waitGenBlock();
				assertEquals(true,r2);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(false,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_082_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, "", addr2, amount, acc2, gaslimit, gasprice);
				//fromaddr留空
				OntTest.logger().description(TransferFrom);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,false);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_084_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			String addr3 = OntTest.common().getAccount(2).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr3, amount, acc2, gaslimit, gasprice);
				//toAddr存在，但并非sendApprove的地址
				OntTest.logger().description(TransferFrom);
				boolean r2 = OntTest.common().waitGenBlock();
				assertEquals(true,r2);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(false,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_086_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, "a"+addr2, amount, acc2, gaslimit, gasprice);
				//toAddr长度为35及以上
				OntTest.logger().description(TransferFrom);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,false);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
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
	public void test_abnormal_087_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2.substring(0,addr2.length()-1), amount, acc2, gaslimit, gasprice);
				//toAddr长度为33及以下
				OntTest.logger().description(TransferFrom);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,false);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
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
	public void test_abnormal_088_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, "", amount, acc2, gaslimit, gasprice);
				//留空
				OntTest.logger().description(TransferFrom);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,false);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_090_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, 0L, acc2, gaslimit, gasprice);
				//正确的数量0
				OntTest.logger().description(TransferFrom);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,false);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_091_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, -100000L, acc2, gaslimit, gasprice);
				//amount为负数
				OntTest.logger().description(TransferFrom);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,false);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_092_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, Allowance0+1000000000L, acc2, gaslimit, gasprice);
				//amount大于Allowance中实际所有的ONG数量
				OntTest.logger().description(TransferFrom);
				boolean r2 = OntTest.common().waitGenBlock();
				assertEquals(true,r2);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==0);
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_094_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			Account acc3 = OntTest.common().getAccount(2);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc3, gaslimit, gasprice);
				//payerAcct为第三方，与sendAcct不一致
				OntTest.logger().description(TransferFrom);
				boolean r2 = OntTest.common().waitGenBlock();
				assertEquals(true,r2);
				
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==amount);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_095_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, null, gaslimit, gasprice);
				//payer留空
				OntTest.logger().description(TransferFrom);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,false);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_097_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数gaslimit");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc2, 0, gasprice);
				//gaslimit错误的数量0（但实际步数大于0小于20000且ONG足够）
				OntTest.logger().description(TransferFrom);
				boolean r2 = OntTest.common().waitTransactionResult(TransferFrom);
				assertEquals(true,r2);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,false);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
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
	public void test_abnormal_098_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc2, -20000L, gasprice);
				//正确的数量gaslimit为负数（实际步数小于20000且ONG足够）
				OntTest.logger().description(TransferFrom);
				boolean r2 = OntTest.common().waitTransactionResult(TransferFrom);
				assertEquals(true,r2);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,false);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
//	@Test
//	public void test_abnormal_099_sendTransferFrom() throws Exception {
//		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
//		
//		try {
//			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
//			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
//			 
//			Account acc1 = OntTest.common().getAccount(0);
//			Account acc2 = OntTest.common().getAccount(1);
//			long amount = 1000000000;
//			long gaslimit = 20000;
//			long gasprice = 0;
//			
//			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			System.out.println(Approve);
//			boolean r = OntTest.common().waitTransactionResult(Transfer);
//			
//			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
//			System.out.println(Allowance0);
//			if(Allowance0==1000000000) {
//				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
//				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
//				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc2, gaslimit, gasprice);
//				//错误的数量gaslimit为20000（实际步数大于20000但ONG足够）
//				System.out.println(TransferFrom);
//				boolean r = OntTest.common().waitTransactionResult(Transfer);
//				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
//				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
//				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
//			}else {
//				System.out.println("Allowance与sendApprove的amount不一致");
//				assertEquals(true,false);
//			}
//		} catch(Exception e) {
//			System.out.println(e);
//			OntTest.logger().error(e.toString());
//			fail();
//		}
//	}
	
	@Test
	public void test_abnormal_100_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("before ong : "+ongnum_addr2);
				String ongtf = OntTest.sdk().nativevm().ong().sendTransfer(acc2, addr1, ongnum_addr2, acc2, 20000L, 0L);
				boolean r2 = OntTest.common().waitTransactionResult(ongtf);
				assertEquals(true,r2);
				long ongnum_addr_should0 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2_should0 has "+ongnum_addr_should0+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc2, gaslimit, 1000000000L);
				//错误的数量20000，自身ONG小于gaslimit与gasprice的乘积
				OntTest.logger().description(TransferFrom);
				boolean r3 = OntTest.common().waitTransactionResult(TransferFrom);
				assertEquals(true,r3);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
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
	public void test_abnormal_101_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			OntTest.logger().step("***************************restart all nodes***************************");
			OntTest.api().node().restartAll("ontology", "config.json", Config.DEFAULT_NODE_ARGS);
			OntTest.logger().step("***************************restart finish***************************");
			OntTest.logger().step("***************************init_ONT_ONG***************************");
			OntTest.api().node().initOntOng();
			OntTest.logger().step("***************************init finish***************************");

			
			
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description("allowance = "+String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+String.valueOf(ongnum_addr2)+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc2, 9223372036854775807L, 1L);
				//错误的数量1000000000，sendAcct的ONG充足
				System.out.println(TransferFrom);
				boolean r2 = OntTest.common().waitTransactionResult(TransferFrom);
				assertEquals(true,r2);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+String.valueOf(ongnum_addr3)+" ong");
				long inc = ongnum_addr3-ongnum_addr2;
				OntTest.logger().description("实际到帐: "+String.valueOf(inc));
				assertEquals(true,inc==999980000);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_103_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc2, gaslimit, -100000L);
				//正确的数量（负数）
				OntTest.logger().description(TransferFrom);
				boolean r2 = OntTest.common().waitTransactionResult(TransferFrom);
				assertEquals(true,r2);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,false);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_104_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			OntTest.logger().description(Approve);
			boolean r = OntTest.common().waitTransactionResult(Approve);
			assertEquals(true,r);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			OntTest.logger().description(String.valueOf(Allowance0));
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				String ongnum_ret = OntTest.sdk().nativevm().ong().sendTransfer(acc2, addr1, ongnum_addr2, acc2, 20000L, 0L);
				boolean r1 = OntTest.common().waitTransactionResult(ongnum_ret);
				assertEquals(true,r1);
				
				long ongnum_addr_should0 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("start : addr2_should0 has "+ongnum_addr_should0+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc2, gaslimit, 1000000000L);
				//错误的数量10（自身ONG小于gaslimit与gasprice的乘积）
				OntTest.logger().description(TransferFrom);
				boolean r3 = OntTest.common().waitTransactionResult(TransferFrom);
				assertEquals(true,r3);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.logger().description("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,false);
			}else {
				OntTest.logger().description("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(RpcException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("error");
			int exp_errcode = 43001;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_106_queryName() throws Exception {
		OntTest.logger().description("测试queryName");
		
		try {
			String ret = OntTest.sdk().nativevm().ong().queryName();
			OntTest.logger().description(ret);
			String exp = "ONG Token";
			assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_107_querySymbol() throws Exception {
		OntTest.logger().description("测试querySymbol");
		
		try {
			String ret = OntTest.sdk().nativevm().ong().querySymbol();
			OntTest.logger().description(ret);
			String exp = "ONG";
			assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_108_queryDecimals() throws Exception {
		OntTest.logger().description("测试queryDecimals");
		
		try {
			long ret = OntTest.sdk().nativevm().ong().queryDecimals();
			OntTest.logger().description(String.valueOf(ret));
			long exp = 9;
			assertEquals(true,ret==exp);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_109_queryTotalSupply() throws Exception {
		OntTest.logger().description("测试queryTotalSupply");
		
		try {
			long ret = OntTest.sdk().nativevm().ong().queryTotalSupply();
			OntTest.logger().description(String.valueOf(ret));
			long exp = 1000000000000000000L;
			assertEquals(true,ret==exp);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_110_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			//正确的sendAcct
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;

			String Transfer = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr1, amount, acc1, gaslimit, gasprice);
			boolean r =OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true, r);

			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1, addr1, amount, acc1, gaslimit, gasprice);
				OntTest.logger().description(withdrawOng);
				boolean r2 = OntTest.common().waitTransactionResult(withdrawOng);
				assertEquals(true,r2);
				
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				OntTest.logger().description("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_111_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;

			String Transfer = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr1, amount, acc1, gaslimit, gasprice);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(null, addr1, amount, acc1, gaslimit, gasprice);
				//留空
				OntTest.logger().description(withdrawOng);
				boolean r2 = OntTest.common().waitTransactionResult(withdrawOng);
				assertEquals(true,r2);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("final : "+addr1_Ong2);
				
				assertEquals(true,false);
			}else {
				OntTest.logger().description("可提取的ong数量不足");
				assertEquals(true,false);
			}
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
	public void test_abnormal_113_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;

			String Transfer = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr1, amount, acc1, gaslimit, gasprice);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1.substring(0,addr1.length()-3)+"abc", amount, acc1, gaslimit, gasprice);
				//toAddr不存在（乱码但符合toAddr34个字符要求）
				OntTest.logger().description(withdrawOng);
				boolean r2 = OntTest.common().waitTransactionResult(withdrawOng);
				assertEquals(true,r2);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("final : "+addr1_Ong2);
				
				assertEquals(true,false);
			}else {
				OntTest.logger().description("可提取的ong数量不足");
				assertEquals(true,false);
			}
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
	public void test_abnormal_114_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;

			String Transfer = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr1, amount, acc1, gaslimit, gasprice);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1 ,"a"+addr1, amount, acc1, gaslimit, gasprice);
				//toAddr长度为35及以上
				OntTest.logger().description(withdrawOng);
				boolean r2 = OntTest.common().waitTransactionResult(withdrawOng);
				assertEquals(true,r2);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("final : "+addr1_Ong2);
				
				assertEquals(true,false);
			}else {
				OntTest.logger().description("可提取的ong数量不足");
				assertEquals(true,false);
			}
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
	public void test_abnormal_115_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();

			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;

			String Transfer = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr1, amount, acc1, gaslimit, gasprice);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1.substring(0,addr1.length()-3)+"@#$", amount, acc1, gaslimit, gasprice);
				//34个字符的toAddr中包含非法符号（%￥#）
				OntTest.logger().description(withdrawOng);
				boolean r2 = OntTest.common().waitGenBlock();
				assertEquals(true,r2);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("final : "+addr1_Ong2);
				
				assertEquals(true,false);
			}else {
				OntTest.logger().description("可提取的ong数量不足");
				assertEquals(true,false);
			}
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
	public void test_abnormal_116_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;

			String Transfer = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr1, amount, acc1, gaslimit, gasprice);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,"", amount, acc1, gaslimit, gasprice);
				//留空
				OntTest.logger().description(withdrawOng);
				boolean r2 = OntTest.common().waitTransactionResult(withdrawOng);
				assertEquals(true,r2);
				
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("final : "+addr1_Ong2);
				
				assertEquals(true,false);
			}else {
				OntTest.logger().description("可提取的ong数量不足");
				assertEquals(true,false);
			}
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
	public void test_abnormal_118_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 0;
			//错误的数量0
			long gaslimit = 20000;
			long gasprice = 0;

			String Transfer = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr1, amount, acc1, gaslimit, gasprice);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1, amount, acc1, gaslimit, gasprice);
				OntTest.logger().description(withdrawOng);
				boolean r2 = OntTest.common().waitTransactionResult(withdrawOng);
				assertEquals(true,r2);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("final : "+addr1_Ong2);
				assertEquals(true,false);
			}else {
				OntTest.logger().description("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_119_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = -1000000000;
			//正确的数量（负数）
			long gaslimit = 20000;
			long gasprice = 0;

			String Transfer = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr1, amount, acc1, gaslimit, gasprice);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));
			if(ongnum>1) {
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1, addr1, amount, acc1, gaslimit, gasprice);
				OntTest.logger().description(withdrawOng);
				assertEquals(true,false);
			}else {
				OntTest.logger().description("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_120_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount0 = 1;
			//错误的数量（超出未提取的ONG数量）
			long gaslimit = 20000;
			long gasprice = 0;

			String Transfer = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr1, amount0, acc1, gaslimit, gasprice);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));
			long amount = ongnum+100000000L;
			OntTest.logger().description(String.valueOf(amount));
			
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1, amount, acc1, gaslimit, gasprice);
				OntTest.logger().description(withdrawOng);
				boolean r2 = OntTest.common().waitGenBlock();
				assertEquals(true,r2);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==0);
			}else {
				OntTest.logger().description("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_121_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;

			OntTest.logger().description(String.valueOf(OntTest.sdk().nativevm().ong().queryBalanceOf(addr1)));
			String Transfer = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr1, amount, acc1, gaslimit, gasprice);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1, amount, acc1, gaslimit, gasprice);
				//正确的payerAcct
				OntTest.logger().description(withdrawOng);
				boolean r2 = OntTest.common().waitTransactionResult(withdrawOng);
				assertEquals(true,r2);
				
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				OntTest.logger().description("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_122_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Transfer = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr1, amount, acc1, gaslimit, gasprice);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1, amount, acc2, gaslimit, gasprice);
				//payerAcct与sendAcct不一致，payerAcct为第三方
				OntTest.logger().description(withdrawOng);
				boolean r2 = OntTest.common().waitTransactionResult(withdrawOng);
				assertEquals(true,r2);
				
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				OntTest.logger().description("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_123_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;

			String Transfer = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr1, amount, acc1, gaslimit, gasprice);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1, amount, null, gaslimit, gasprice);
				//留空
				OntTest.logger().description(withdrawOng);
				boolean r2 = OntTest.common().waitTransactionResult(Transfer);
				assertEquals(true,r2);
				
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				OntTest.logger().description("可提取的ong数量不足");
				assertEquals(true,false);
			}
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
	public void test_abnormal_126_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = -20000;
			long gasprice = 0;

			String Transfer = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr1, amount, acc1, gaslimit, gasprice);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1, amount, acc1, gaslimit, gasprice);
				//正确的数量gaslimit为负数（实际步数小于20000且ONG足够）
				OntTest.logger().description(withdrawOng);
				boolean r2 = OntTest.common().waitTransactionResult(withdrawOng);
				assertEquals(true,r2);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				OntTest.logger().description("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_128_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 100000L;

			String Transfer = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr1, amount, acc1, gaslimit, 0);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				String ret = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, addr1_Ong1, acc1, gaslimit, 0);
				boolean r2 = OntTest.common().waitTransactionResult(ret);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("start(should be 0) : "+addr1_Ong2);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1, amount, acc1, gaslimit, 100000L);
				//错误的数量20000，自身ONG小于gaslimit与gasprice的乘积
				OntTest.logger().description(withdrawOng);
				boolean r3 = OntTest.common().waitTransactionResult(withdrawOng);
				assertEquals(true,r3);
				long addr1_Ong3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("final : "+addr1_Ong3);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				OntTest.logger().description("可提取的ong数量不足");
				assertEquals(true,false);
			}
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
	public void test_abnormal_131_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = -100000L;
			//正确的数量（负数）

			String Transfer = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr1, amount, acc1, gaslimit, 0);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));
			if(ongnum>1) {
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1, addr1, amount, acc1, gaslimit, gasprice);
				OntTest.logger().description(withdrawOng);
				boolean r2 = OntTest.common().waitTransactionResult(withdrawOng);
				assertEquals(true,r2);
			}else {
				OntTest.logger().description("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_132_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 100000L;

			String Transfer = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr1, amount, acc1, gaslimit, 0);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				String ret = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, addr1_Ong1, acc1, gaslimit, 0);
				boolean r2 = OntTest.common().waitGenBlock();
				assertEquals(true,r2);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("start(should be 0) : "+addr1_Ong2);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1, amount, acc1, gaslimit, gasprice);
				//错误的数量10（自身ONG小于gaslimit与gasprice的乘积）
				OntTest.logger().description(withdrawOng);
				boolean r3 = OntTest.common().waitGenBlock();
				assertEquals(true,r3);
				long addr1_Ong3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.logger().description("final : "+addr1_Ong3);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				OntTest.logger().description("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
//		} catch(RpcException e) {
//	        Map err = (Map) JSON.parse(e.getMessage()); 
//			System.out.println("err = "+err);
//			int err_code = (int) err.get("error");
//			int exp_errcode = 43001;
//			OntTest.logger().error(e.toString());
//			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_134_unclaimOng() throws Exception {
		OntTest.logger().description("测试unclaimOng参数address");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;

			String Transfer = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr1, 1, acc1, gaslimit, gasprice);
			boolean r = OntTest.common().waitTransactionResult(Transfer);
			assertEquals(true,r);
			System.out.println("1111");
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			//正确的address值
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));

			assertEquals(true,ongnum!=0);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_135_unclaimOng() throws Exception {
		OntTest.logger().description("测试unclaimOng参数address");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			addr1 = addr1.substring(0,addr1.length()-3)+"abc";
//			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
//			 
//			Account acc1 = OntTest.common().getAccount(0);
//			Account acc2 = OntTest.common().getAccount(1);
//			long amount = 1000000000;
//			long gaslimit = 20000;
//			long gasprice = 0;
//
//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr1, amount, acc1, gaslimit, gasprice);
//			OntTest.common().waitTransactionResult(txhash);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			//address不存在，未创建的地址（34个字符）
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));

			assertEquals(true,false);
		} catch(RpcException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("error");
			int exp_errcode = 42002;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_136_unclaimOng() throws Exception {
		OntTest.logger().description("测试unclaimOng参数address");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			addr1 = "a"+addr1;
//			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
//			 
//			Account acc1 = OntTest.common().getAccount(0);
//			Account acc2 = OntTest.common().getAccount(1);
//			long amount = 1000000000;
//			long gaslimit = 20000;
//			long gasprice = 0;
//
//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr1, amount, acc1, gaslimit, gasprice);
//			OntTest.common().waitTransactionResult(txhash);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			//address长度为35及以上
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));

			assertEquals(true,false);
		} catch(RpcException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("error");
			int exp_errcode = 42002;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_137_unclaimOng() throws Exception {
		OntTest.logger().description("测试unclaimOng参数address");
		
		try {
//			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
//			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
//			 
//			Account acc1 = OntTest.common().getAccount(0);
//			Account acc2 = OntTest.common().getAccount(1);
//			long amount = 1000000000;
//			long gaslimit = 20000;
//			long gasprice = 0;
//
//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr1, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng("");
			//留空
			long ongnum = Long.valueOf(unboundOng);
			OntTest.logger().description(String.valueOf(ongnum));

			assertEquals(true,false);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			System.out.println("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58005;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
}
