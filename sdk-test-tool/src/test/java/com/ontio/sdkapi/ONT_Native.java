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
import com.github.ontio.core.payload.InvokeCode;
import com.github.ontio.core.transaction.Transaction;
import com.github.ontio.network.exception.RpcException;
import com.github.ontio.sdk.exception.SDKException;
import com.github.ontio.smartcontract.neovm.abi.BuildParams;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;
import com.ontio.testtool.utils.Config;

public class ONT_Native {
	@Rule public OntTestWatcher watchman= new OntTestWatcher();
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
		
		OntTest.api().node().restartAll();
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
	public void test_base_001_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {			
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.logger().print("账户1 的address" + addr1);
			OntTest.logger().print("账户2 的address" + addr2);

			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为" + before_bala1);
			OntTest.logger().print("账户2 的余额为" + before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 1000L, acc1, 20000, 1L);
			OntTest.logger().print(ts);
			OntTest.common().waitTransactionResult(ts);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为" + after_bala1);
			OntTest.logger().print("账户2 的余额为" + after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("转账成功！");
				assertEquals(true, before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0);
			}
			else {
				OntTest.logger().print("转账失败！");
				assertEquals(true, false);
			}
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_002_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.logger().print("账户1 的address" + addr1);
			OntTest.logger().print("账户2 的address" + addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(null, addr2, 1000L, acc1, 20000L, 10L);
			OntTest.logger().print(ts);
			OntTest.common().waitTransactionResult(ts);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("转账成功！");
			}
			else {
				OntTest.logger().print("转账失败！");
			}
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_normal_004_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			Account acc3 = OntTest.common().getAccount(2);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			String addr3 = acc3.getAddressU160().toBase58();
			
			OntTest.logger().print("账户1 的address" + addr1);
			OntTest.logger().print("账户2 的address" + addr2);
			OntTest.logger().print("账户3 的address" + addr3);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			long before_bala3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr3);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			OntTest.logger().print("账户3 的ong余额为"+before_bala3);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 1000L, acc3, 20000L, 10L);
			OntTest.logger().print(ts);
			OntTest.common().waitTransactionResult(ts);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			long after_bala3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr3);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			OntTest.logger().print("账户3 的ong余额为"+after_bala3);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0 && before_bala3 - after_bala3 > 0) {
				OntTest.logger().print("转账成功！");
				assertEquals(true, true);
			}
			else {
				OntTest.logger().print("转账失败！");
				assertEquals(true, false);
			}
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_006_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.logger().print("账户1 的address" + addr1);
			OntTest.logger().print("账户2 的address" + addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, "", 1000L, acc1, 20000L, 10L);
			OntTest.logger().print(ts);
			OntTest.common().waitTransactionResult(ts);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("转账成功！");
			}
			else {
				OntTest.logger().print("转账失败！");
			}
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_008_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.logger().print("账户1 的address" + addr1);
			OntTest.logger().print("账户2 的address" + addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 0, acc1, 20000L, 10L);
			OntTest.logger().print(ts);
			OntTest.common().waitTransactionResult(ts);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("转账成功！");
			}
			else {
				OntTest.logger().print("转账失败！");
			}
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		 catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
			}
	}
	
	
	@Test
	public void test_abnormal_009_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.logger().print("账户1 的address" + addr1);
			OntTest.logger().print("账户2 的address" + addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, -2000L, acc1, 20000L, 10L);
			OntTest.logger().print(ts);
			OntTest.common().waitTransactionResult(ts);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("转账成功！");
				}
			else {
				OntTest.logger().print("转账失败！");
				}
			} 
		
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
			}
		}
	
	
	@Test
	public void test_abnormal_011_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.logger().print("账户1 的address" + addr1);
			OntTest.logger().print("账户2 的address" + addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10000000000L, acc1, 20000L, 10L);
			OntTest.logger().print(ts);
	
			boolean flag = OntTest.common().waitTransactionResult(ts);
			
			Object tr = OntTest.sdk().getRestful().getSmartCodeEvent(ts);
			OntTest.logger().print(tr.toString());
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("转账成功！");
				}
			else {
				OntTest.logger().print("转账失败！");
				}
			if(flag == false) {
				OntTest.logger().print("交易失败！");
				assertEquals(true,flag == false);
			}
			
			else {
				assertEquals(true,flag == true);
			}
			} 
		
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
			}
	}
	
	@Test
	public void test_normal_013_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.logger().print("账户1 的address" + addr1);
			OntTest.logger().print("账户2 的address" + addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 100L, acc1, 20000L, 10L);
			OntTest.logger().print(ts);
			OntTest.common().waitTransactionResult(ts);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("转账成功！");
				assertEquals(true, true);
				}
			else {
				OntTest.logger().print("转账失败！");
				assertEquals(true, false);
				}
			} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
			}
	}
	
	@Test
	public void test_abnormal_014_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.logger().print("账户1 的address" + addr1);
			OntTest.logger().print("账户2 的address" + addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 100L, null, 20000L, 10L);
			OntTest.logger().print(ts);
			OntTest.common().waitTransactionResult(ts);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("转账成功！");
				}
			else {
				OntTest.logger().print("转账失败！");
				}
			} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_abnormal_017_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.logger().print("账户1 的address" + addr1);
			OntTest.logger().print("账户2 的address" + addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 100L, acc1, -2000L, 10L);
			OntTest.logger().print(ts);
			OntTest.common().waitTransactionResult(ts);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("转账成功！");
				}
			else {
				OntTest.logger().print("转账失败！");
				}
			} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	
	@Test
	public void test_normal_020_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.logger().print("账户1 的address" + addr1);
			OntTest.logger().print("账户2 的address" + addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 100L, acc1, 20000L, 10L);
			OntTest.logger().print(ts);
			OntTest.common().waitTransactionResult(ts);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
		
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("转账成功！");
				assertEquals(true, true);
				}
			else {
				OntTest.logger().print("转账失败！");
				assertEquals(true, false);
				}
			} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	
	@Test
	public void test_abnormal_021_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.logger().print("账户1 的address" + addr1);
			OntTest.logger().print("账户2 的address" + addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 100L, acc1, 20000L, -10L);
			OntTest.logger().print(ts);
			OntTest.common().waitTransactionResult(ts);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("转账成功！");
				}
			else {
				OntTest.logger().print("转账失败！");
				}
			} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_022_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			com.github.ontio.sdk.wallet.Account acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			String addr1 = acc.address;
			Account acc1 = OntTest.sdk().getWalletMgr().getAccount(addr1, "123456");
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.logger().print("账户1 的address" + addr1);
			OntTest.logger().print("账户2 的address" + addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10L, acc1, 20000L, 1);
			OntTest.logger().print(ts);
			OntTest.common().waitTransactionResult(ts);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("转账成功！");
				}
			else {
				OntTest.logger().print("转账失败！");
				}
			} 
		catch(RpcException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("error").toString();
			if("43001".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_023_queryBalanceOf() throws Exception {
		OntTest.logger().description("----------queryBalanceOf----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			
			String addr1 = acc1.getAddressU160().toBase58();
			
			long l = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			String bal1 = String.valueOf(l);
			OntTest.logger().print(bal1);
			assertEquals(true, l >= 0);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_025_queryBalanceOf() throws Exception {
		OntTest.logger().description("----------queryBalanceOf----------");
		
		try {
			
			long l = OntTest.sdk().nativevm().ont().queryBalanceOf("AbwJsJYQPBSw67SVP7hctkWsfzgikwNkvh");
			String bal = String.valueOf(l);
			OntTest.logger().print(bal);
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58004".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_026_queryBalanceOf() throws Exception {
		OntTest.logger().description("----------queryBalanceOf----------");
		
		try {
			long l = OntTest.sdk().nativevm().ont().queryBalanceOf("AbwJsJYQPBSw%&#SVP7hctkWsfzgikwNkv");
			String bal = String.valueOf(l);
			OntTest.logger().print(bal);
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58004".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_027_queryBalanceOf() throws Exception {
		OntTest.logger().description("----------queryBalanceOf----------");
		
		try {
			
			long l = OntTest.sdk().nativevm().ont().queryBalanceOf("");
			String bal = String.valueOf(l);
			OntTest.logger().print(bal);
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_028_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.logger().step("1.调用sendapprove");
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			OntTest.common().waitTransactionResult(ts);
			OntTest.logger().step("2.调用queryAllowance");
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			OntTest.logger().print("queryAllowance:"+l);
			if(l == 10) {
				OntTest.logger().print("成功！");
				assertEquals(true, true);
			}
			else{
				OntTest.logger().print("失败！");
				assertEquals(true, false);
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_029_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(2);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1,addr2 );
			OntTest.logger().print("queryAllowance:"+l);
			
			if(l == 0) {
				OntTest.logger().print("成功！");
				assertEquals(true, true);
			}
			else{
				OntTest.logger().print("失败！");
				assertEquals(true, false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_031_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.logger().step("1.调用sendapprove");
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			OntTest.common().waitTransactionResult(ts);
	
			OntTest.logger().step("2.调用queryAllowance");
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1+"G", addr2);
			OntTest.logger().print("queryAllowance:"+l);
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58004".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_032_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.logger().step("1.调用sendapprove");
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			OntTest.common().waitTransactionResult(ts);
			
			OntTest.logger().step("2.调用queryAllowance");
			long l = OntTest.sdk().nativevm().ont().queryAllowance("Af296@#$TqHV5byLvXdCWCheW3HcpMpcNa", addr2);
			OntTest.logger().print("queryAllowance:"+l);
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58004".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_033_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		try {
			Account acc1 = OntTest.common().getAccount(1);
			Account acc2 = OntTest.common().getAccount(2);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.logger().step("1.调用sendapprove");
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			OntTest.common().waitTransactionResult(ts);
	
			OntTest.logger().step("2.调用queryAllowance");
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr2, addr1);
			OntTest.logger().print("queryAllowance:"+l);
			if(l == 0) {
				OntTest.logger().print("成功！");
				assertEquals(true, true);
			}
			else{
				OntTest.logger().print("失败！");
				assertEquals(true, true);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_034_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		try {
			Account acc1 = OntTest.common().getAccount(1);
			Account acc2 = OntTest.common().getAccount(2);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.logger().step("1.调用sendapprove");
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			OntTest.common().waitTransactionResult(ts);
			
			OntTest.logger().step("2.调用queryAllowance");
			long l = OntTest.sdk().nativevm().ont().queryAllowance("" , addr2);
			OntTest.logger().print("queryAllowance:"+l);
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_036_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		try {
			Account acc1 = OntTest.common().getAccount(2);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1,addr2);
			OntTest.logger().print("queryAllowance:"+l);
			
			if(l == 0) {
				OntTest.logger().print("成功！");
				assertEquals(true, true);
			}
			else{
				OntTest.logger().print("失败！");
				assertEquals(true, false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_038_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		try {
			Account acc1 = OntTest.common().getAccount(1);
			Account acc2 = OntTest.common().getAccount(2);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.logger().step("1.调用sendapprove");
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			OntTest.common().waitTransactionResult(ts);
			OntTest.logger().step("2.调用queryAllowance");
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1 , addr2+"G");
			OntTest.logger().print("queryAllowance:"+l);
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58004".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_039_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		try {
			Account acc1 = OntTest.common().getAccount(1);
			Account acc2 = OntTest.common().getAccount(2);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.logger().step("1.调用sendapprove");
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			OntTest.common().waitTransactionResult(ts);
			OntTest.logger().step("2.调用queryAllowance");
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1 , "AKv$%^sbk3ucmTHHg9hPK3kehoQHG5g9CG");
			OntTest.logger().print("queryAllowance:"+l);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_040_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		try {
			Account acc1 = OntTest.common().getAccount(1);
			Account acc2 = OntTest.common().getAccount(2);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			OntTest.common().waitTransactionResult(ts);
			OntTest.logger().step("2.调用queryAllowance");
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr2 , addr1);
			OntTest.logger().print("queryAllowance:"+l);
			
			if(l == 0) {
			OntTest.logger().print("成功！");
			assertEquals(true, true);
		}
		else{
			OntTest.logger().print("失败！");
			assertEquals(true, false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_041_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		try {
			Account acc1 = OntTest.common().getAccount(1);
			Account acc2 = OntTest.common().getAccount(2);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			OntTest.common().waitTransactionResult(ts);
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1 , "");
			OntTest.logger().print("queryAllowance:"+l);
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_042_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 0L);
			OntTest.common().waitTransactionResult(ts);
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			OntTest.logger().print("sendApprove:"+l);
			
			if(l >= 10) {
				OntTest.logger().print("成功！");
				assertEquals(true, true);
			}
			else{
				OntTest.logger().print("失败！");
				assertEquals(true, false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_043_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(null, addr2, 10L, acc1, 20000L, 0L);
			OntTest.common().waitTransactionResult(ts);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			String al = String.valueOf(s);
			OntTest.logger().print(al);
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_046_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2+"G", 10L, acc1, 20000L, 0L);
			OntTest.common().waitTransactionResult(ts);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			String al = String.valueOf(s);
			OntTest.logger().print(al);
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58004".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_048_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, "AKvRbmbk3ucmTHHg9hPK3kehoQHG5g%^&", 10L, acc1, 20000L, 0L);
			OntTest.common().waitTransactionResult(ts);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			String al = String.valueOf(s);
			OntTest.logger().print(al);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_049_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, "", 10L, acc1, 20000L, 0L);
			OntTest.common().waitTransactionResult(ts);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			String al = String.valueOf(s);
			OntTest.logger().print(al);
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	

	@Test
	public void test_normal_050_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10000L, acc1, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts);
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			OntTest.logger().print("sendApprove:"+l);
			
			if(l >= 10000) {
				OntTest.logger().print("成功！");
			}
			else{
				OntTest.logger().print("失败！");
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_051_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10000L, acc1, 0, 10L);
			OntTest.common().waitTransactionResult(ts);
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			OntTest.logger().print("sendApprove:"+l);
			
		}
		catch(RpcException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("error").toString();
			if("43001".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_054_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			com.github.ontio.sdk.wallet.Account acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			String addr1 = acc.address;
			
			Account acc1 = OntTest.sdk().getWalletMgr().getAccount(addr1, "123456");
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr2 = acc2.getAddressU160().toBase58();
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 5000000000L, acc1, 20000L, 0L);
			OntTest.common().waitTransactionResult(ts);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			OntTest.logger().print("sendApprove:"+s);
			
			if(s == 0) {
				OntTest.logger().print("失败！");
				assertEquals(true, s == 0);
			}
			else {
				assertEquals(true, false);
			}
		}
		
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_056_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10000L, null, 20000L, 0L);
			OntTest.common().waitTransactionResult(ts);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			String al = String.valueOf(s);
			OntTest.logger().print(al);
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_059_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10000L, acc1, -20000L, 1L);
			OntTest.common().waitTransactionResult(ts);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			String al = String.valueOf(s);
			OntTest.logger().print(al);
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
		
	
	@Test
	public void test_abnormal_065_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10000L, acc1, 20000L, -1L);
			OntTest.common().waitTransactionResult(ts);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			String al = String.valueOf(s);
			OntTest.logger().print(al);
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_066_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			com.github.ontio.sdk.wallet.Account acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			String addr1 = acc.address;
			
			Account acc1 = OntTest.sdk().getWalletMgr().getAccount(addr1, "123456");
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr2 = acc2.getAddressU160().toBase58();
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10000L, acc1, 200000L, 1000L);
			OntTest.common().waitTransactionResult(ts);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			String al = String.valueOf(s);
			OntTest.logger().print(al);
		}
		catch(RpcException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("error").toString();
			if("43001".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_068_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
				assertEquals(true, true);
			}
			else {
				OntTest.logger().print("失败！");
				assertEquals(true, false);
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_069_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(null, addr1, addr2, 100L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_normal_070_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10L);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc1, addr1, addr2, 100L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
				assertEquals(true, false);
			}
			else {
				OntTest.logger().print("失败！");
				assertEquals(true, true);
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_071_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			Account acc3 = OntTest.common().getAccount(2);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			String addr3 = acc3.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			long before_bala3 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr3);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			OntTest.logger().print("账户3 的余额为"+before_bala3);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String s = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr3, addr2, 100L, acc2, 20000L, 10L);
			boolean flag = OntTest.common().waitTransactionResult(s);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			long after_bala3 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr3);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			OntTest.logger().print("账户3 的余额为"+after_bala3);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
			}
			else {
				OntTest.logger().print("失败！");
			}
			if(flag == false) {
				OntTest.logger().print("交易失败！");
				assertEquals(true, flag == false);
			}
			else {
				assertEquals(true, false);
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_073_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
				assertEquals(true, true);
			}
			else {
				OntTest.logger().print("失败！");
				assertEquals(true, false);
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_074_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			com.github.ontio.sdk.wallet.Account temp = OntTest.sdk().getWalletMgr().createAccount("123456");

			String tempaddr = temp.address;
			
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, tempaddr, addr2, 100L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
				assertEquals(true, false);
				
			}
			else {
				OntTest.logger().print("失败！");
				assertEquals(true, true);
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_075_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, "G"+addr1, addr2, 100L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
			}
			else {
				OntTest.logger().print("失败！");
			}
			
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58004".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_076_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, "AKvRbmbk3ucmTHHg9hPK3kehoQHG5g%^&", addr2, 100L, acc2, 200000L, 1L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
			}
			else {
				OntTest.logger().print("失败！");
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_077_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr2, addr2, 100L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
				assertEquals(true, false);
			}
			else {
				OntTest.logger().print("失败！");
				assertEquals(true, true);
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_078_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, "", addr2, 100L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
			}
			else {
				OntTest.logger().print("失败！");
			}
			
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_080_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(2);
			Account acc2 = OntTest.common().getAccount(3);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
				assertEquals(true, false);
			}
			else {
				OntTest.logger().print("失败！");
				assertEquals(true, true);
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_082_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, "F"+addr2, 100L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
			}
			else {
				OntTest.logger().print("失败！");
			}
			
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58004".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_083_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, "AKv#$%sbk3ucmTHHg9hPK3kehoQHG5g9CG", 100L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
			}
			else {
				OntTest.logger().print("失败！");
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_084_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr1, 100L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
				assertEquals(true, false);
			}
			else {
				OntTest.logger().print("失败！");
				assertEquals(true, true);
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_085_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, "", 100L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
			}
			else {
				OntTest.logger().print("失败！");
			}
			
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_087_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 0, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 >= 0 && after_bala2 - before_bala2 >= 0) {
				OntTest.logger().print("成功！");
			}
			else {
				OntTest.logger().print("失败！");
			}
			
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_088_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, -100L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
			}
			else {
				OntTest.logger().print("失败！");
			}
			
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_090_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 10000000000000L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
				assertEquals(true, true);
			}
			else {
				OntTest.logger().print("失败！");
				assertEquals(true, true);
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_091_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
				assertEquals(true, true);
			}
			else {
				OntTest.logger().print("失败！");
				assertEquals(true, false);
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_092_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, null, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
			}
			else {
				OntTest.logger().print("失败！");
			}
			
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_095_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, acc2, -20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
			}
			else {
				OntTest.logger().print("失败！");
			}
			
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_098_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
				assertEquals(true, true);
			}
			else {
				OntTest.logger().print("失败！");
				assertEquals(true, false);
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_100_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, acc2, 20000L, -10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
			}
			else {
				OntTest.logger().print("失败！");
			}
			
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_101_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			com.github.ontio.sdk.wallet.Account acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			String addr1 = acc.address;
			Account acc1 = OntTest.sdk().getWalletMgr().getAccount(addr1, "123456");
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+before_bala1);
			OntTest.logger().print("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			OntTest.common().waitTransactionResult(ts);
			String ts1 = OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, acc2, 20000L, 10L);
			OntTest.common().waitTransactionResult(ts1);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			OntTest.logger().print("账户1 的余额为"+after_bala1);
			OntTest.logger().print("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				OntTest.logger().print("成功！");
			}
			else {
				OntTest.logger().print("失败！");
			}
			
		}
		catch(RpcException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("error").toString();
			if("43001".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_102_queryName() throws Exception {
			
		OntTest.logger().description("----------queryName----------");
			
		try {
			String acc = OntTest.sdk().nativevm().ont().queryName();
			OntTest.logger().print(acc);
			assertEquals(true, true);
			} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
			}
		}
	
	@Test
	public void test_base_103_querySymbol() throws Exception {
			
		OntTest.logger().description("----------querySymbol----------");
			
		try {
			String acc = OntTest.sdk().nativevm().ont().querySymbol();
			OntTest.logger().print(acc);
			assertEquals(true, true);
			} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
			}
	}
	
	
	@Test
	public void test_base_104_queryDecimals() throws Exception {
			
		OntTest.logger().description("----------queryDecimals----------");
			
		try {
			long acc = OntTest.sdk().nativevm().ont().queryDecimals();
			String acc1 = String.valueOf(acc);
			OntTest.logger().print(acc1);
			assertEquals(true, true);
			} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
			}
	}
	
	
	@Test
	public void test_base_105_queryTotalSupply() throws Exception {
			
		OntTest.logger().description("----------queryTotalSupply----------");
			
		try {
			long acc = OntTest.sdk().nativevm().ont().queryTotalSupply();
			String acc1 = String.valueOf(acc);
			OntTest.logger().print(acc1);
			assertEquals(true, true);
			} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
			}
	}
	
	
	
}
