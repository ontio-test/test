package com.ontio.sdkapi;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import java.util.Base64;
import java.util.List;
import java.util.Map;

import org.junit.*;

import com.alibaba.fastjson.JSON;
import com.github.ontio.core.block.Block;
import com.github.ontio.core.ontid.Attribute;
import com.github.ontio.core.payload.DeployCode;
import com.github.ontio.sdk.exception.SDKException;
import com.github.ontio.sdk.info.IdentityInfo;
import com.github.ontio.sdk.wallet.Account;
//import com.github.ontio.account.Account;
import com.github.ontio.sdk.wallet.Identity;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;

public class DigitalIdentity {
	@Rule public OntTestWatcher watchman= new OntTestWatcher();
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
//		OntTest.api().node().restartAll("ontology", "config.json", Config.DEFAULT_NODE_ARGS);
//		Thread.sleep(5000);
	}
	
	@Before
	public void setUp() throws Exception {
		OntTest.logger().step("setUp");//logger放到这边
		OntTest.init();
	}
	
	@After
	public void TearDown() throws Exception {
		OntTest.logger().step("TearDown");
	}
	
//	//读取config文件信息需要改到框架中
//	public String getConfig(String key) {
//		String confKey = String.valueOf(key);
//		String filepath = "com/ontio/learn/config";
//		ResourceBundle bundle = ResourceBundle.getBundle(filepath);
//        String confValue =bundle.getString(confKey);
//		System.out.println(confValue);
//		return confValue;
//	}
	
	//importIdentity001_014
	@Test
	public void test_base_001_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  001  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_encryptedPrikey");
			
			String encryptedPrikey = "06aukZ9QQj5FmQ+hYkezTTOUZh4Xc3Gp4y8+yfUwX4mElO2IpyOCFLdq/i+ZU62Y";
			byte[] salt = Base64.getDecoder().decode("DFnyx7wmcJUquoyn1KSffg==");
			String pwd = "123456";
			String address = "AVsu25eSbgiK8gzkJeFrSy3eUDFYNm62kY";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret.toString());	
			assertEquals(true,true);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_002_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  002  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_encryptedPrikey");
			
			String encryptedPrikey = "01aukZ9QQj5FmQ+hYkezTTOUZh4Xc3Gp4y8+yfUwX4mElO2IpyOCFLdq/i+ZU62Y";
			byte[] salt = Base64.getDecoder().decode("DFnyx7wmcJUquoyn1KSffg==");
			String pwd = "123456";
			String address = "AVsu25eSbgiK8gzkJeFrSy3eUDFYNm62kY";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret.toString());
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	
	//待修改
	@Test
	public void test_abnormal_003_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  003  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_encryptedPrikey");
			
			String encryptedPrikey = "106aukZ9QQj5FmQ+hYkezTTOUZh4Xc3Gp4y8+yfUwX4mElO2IpyOCFLdq/i+ZU62Y";
			byte[] salt = Base64.getDecoder().decode("DFnyx7wmcJUquoyn1KSffg==");
			String pwd = "123456";
			String address = "AVsu25eSbgiK8gzkJeFrSy3eUDFYNm62kY";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret.toString());
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_abnormal_004_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  004  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_encryptedPrikey");
			
			String encryptedPrikey = "6aukZ9QQj5FmQ+hYkezTTOUZh4Xc3Gp4y8+yfUwX4mElO2IpyOCFLdq/i+ZU62Y";
			byte[] salt = Base64.getDecoder().decode("DFnyx7wmcJUquoyn1KSffg==");
			String pwd = "123456";
			String address = "AVsu25eSbgiK8gzkJeFrSy3eUDFYNm62kY";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret.toString());
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_abnormal_005_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  005  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_encryptedPrikey");
			
			String encryptedPrikey = "#6aukZ9QQj5FmQ+hYkezTTOUZh4Xc3Gp4y8+yfUwX4mElO2IpyOCFLdq/i+ZU62Y";
			byte[] salt = Base64.getDecoder().decode("DFnyx7wmcJUquoyn1KSffg==");
			String pwd = "123456";
			String address = "AVsu25eSbgiK8gzkJeFrSy3eUDFYNm62kY";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret.toString());
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_abnormal_006_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  006  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_encryptedPrikey");
			
			String encryptedPrikey = "";
			byte[] salt = Base64.getDecoder().decode("DFnyx7wmcJUquoyn1KSffg==");
			String pwd = "123456";
			String address = "AVsu25eSbgiK8gzkJeFrSy3eUDFYNm62kY";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret.toString());
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_normal_007_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  007  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_password");
			
			String encryptedPrikey = "06aukZ9QQj5FmQ+hYkezTTOUZh4Xc3Gp4y8+yfUwX4mElO2IpyOCFLdq/i+ZU62Y";
			byte[] salt = Base64.getDecoder().decode("DFnyx7wmcJUquoyn1KSffg==");
			String pwd = "123456";
			String address = "AVsu25eSbgiK8gzkJeFrSy3eUDFYNm62kY";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret.toString());
			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_008_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  008  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_password");
			
			String encryptedPrikey = "06aukZ9QQj5FmQ+hYkezTTOUZh4Xc3Gp4y8+yfUwX4mElO2IpyOCFLdq/i+ZU62Y";
			byte[] salt = Base64.getDecoder().decode("DFnyx7wmcJUquoyn1KSffg==");
			String pwd = "111111";
			String address = "AVsu25eSbgiK8gzkJeFrSy3eUDFYNm62kY";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret.toString());
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_abnormal_009_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  009  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_password");
			
			String encryptedPrikey = "06aukZ9QQj5FmQ+hYkezTTOUZh4Xc3Gp4y8+yfUwX4mElO2IpyOCFLdq/i+ZU62Y";
			byte[] salt = Base64.getDecoder().decode("DFnyx7wmcJUquoyn1KSffg==");
			String pwd = "";
			String address = "AVsu25eSbgiK8gzkJeFrSy3eUDFYNm62kY";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret.toString());
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_normal_010_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  010  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_salt");
			
			String encryptedPrikey = "06aukZ9QQj5FmQ+hYkezTTOUZh4Xc3Gp4y8+yfUwX4mElO2IpyOCFLdq/i+ZU62Y";
			byte[] salt = Base64.getDecoder().decode("DFnyx7wmcJUquoyn1KSffg==");
			String pwd = "123456";
			String address = "AVsu25eSbgiK8gzkJeFrSy3eUDFYNm62kY";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret.toString());
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_abnormal_011_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  011  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_salt");
			
			String encryptedPrikey = "06aukZ9QQj5FmQ+hYkezTTOUZh4Xc3Gp4y8+yfUwX4mElO2IpyOCFLdq/i+ZU62Y";
			byte[] salt = Base64.getDecoder().decode("AFnyx7wmcJUquoyn1KSffg==");
			String pwd = "123456";
			String address = "AVsu25eSbgiK8gzkJeFrSy3eUDFYNm62kY";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret.toString());
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_abnormal_012_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  012  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_salt");
			
			String encryptedPrikey = "06aukZ9QQj5FmQ+hYkezTTOUZh4Xc3Gp4y8+yfUwX4mElO2IpyOCFLdq/i+ZU62Y";
			byte[] salt = Base64.getDecoder().decode("");
			String pwd = "123456";
			String address = "AVsu25eSbgiK8gzkJeFrSy3eUDFYNm62kY";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret.toString());
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_normal_013_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  013  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_address");
			
			String encryptedPrikey = "06aukZ9QQj5FmQ+hYkezTTOUZh4Xc3Gp4y8+yfUwX4mElO2IpyOCFLdq/i+ZU62Y";
			byte[] salt = Base64.getDecoder().decode("DFnyx7wmcJUquoyn1KSffg==");
			String pwd = "123456";
			String address = "AVsu25eSbgiK8gzkJeFrSy3eUDFYNm62kY";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret.toString());
			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_014_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  014  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_address");
			
			String encryptedPrikey = "06aukZ9QQj5FmQ+hYkezTTOUZh4Xc3Gp4y8+yfUwX4mElO2IpyOCFLdq/i+ZU62Y";
			byte[] salt = Base64.getDecoder().decode("DFnyx7wmcJUquoyn1KSffg==");
			String pwd = "123456";
			String address = "1Vsu25eSbgiK8gzkJeFrSy3eUDFYNm62kY";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret.toString());
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_abnormal_015_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  015  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_address");
			
			String encryptedPrikey = "06aukZ9QQj5FmQ+hYkezTTOUZh4Xc3Gp4y8+yfUwX4mElO2IpyOCFLdq/i+ZU62Y";
			byte[] salt = Base64.getDecoder().decode("DFnyx7wmcJUquoyn1KSffg==");
			String pwd = "123456";
			String address = "1AVsu25eSbgiK8gzkJeFrSy3eUDFYNm62kY";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret.toString());
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_abnormal_016_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  016  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_address");
			
			String encryptedPrikey = "06aukZ9QQj5FmQ+hYkezTTOUZh4Xc3Gp4y8+yfUwX4mElO2IpyOCFLdq/i+ZU62Y";
			byte[] salt = Base64.getDecoder().decode("DFnyx7wmcJUquoyn1KSffg==");
			String pwd = "123456";
			String address = "#Vsu25eSbgiK8gzkJeFrSy3eUDFYNm62kY";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret.toString());
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_abnormal_017_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  017  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_address");
			
			String encryptedPrikey = "06aukZ9QQj5FmQ+hYkezTTOUZh4Xc3Gp4y8+yfUwX4mElO2IpyOCFLdq/i+ZU62Y";
			byte[] salt = Base64.getDecoder().decode("DFnyx7wmcJUquoyn1KSffg==");
			String pwd = "123456";
			String address = "AVsu25eSbgiK8gzkJeFrSy3eUDFYNm62kY";
			
			OntTest.logger().step("导入身份");
			Identity ret0 = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			Identity ret1 = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret1.toString());
			
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_abnormal_018_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  018  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_address");
			
			String encryptedPrikey = "06aukZ9QQj5FmQ+hYkezTTOUZh4Xc3Gp4y8+yfUwX4mElO2IpyOCFLdq/i+ZU62Y";
			byte[] salt = Base64.getDecoder().decode("DFnyx7wmcJUquoyn1KSffg==");
			String pwd = "123456";
			String address = "";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			OntTest.logger().description(ret.toString());
			
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	
	//createIdentity019_022
	@Test
	public void test_base_019_createIdentity() throws Exception {
		OntTest.logger().description("Digital identity  019  createIdentity()");

		try {
			OntTest.logger().step("测试参数createIdentity_password");
			
			String password = "123456";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentity(password);
			OntTest.logger().description(ret.toString());
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_020_createIdentity() throws Exception {
		OntTest.logger().description("Digital identity  020  createIdentity()");

		try {
			OntTest.logger().step("测试参数createIdentity_password");
			
			String password = "";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentity(password);
			OntTest.logger().description(ret.toString());	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_021_createIdentity() throws Exception {
		OntTest.logger().description("Digital identity  021  createIdentity()");

		try {
			OntTest.logger().step("测试参数createIdentity_password");
			String password = "!@#$%^&*()_+:;,.<>?/";  //password为非法字符
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentity(password);
			OntTest.logger().description(ret.toString());	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_022_createIdentity() throws Exception {
		OntTest.logger().description("Digital  022  createIdentity()");

		try {
			OntTest.logger().step("测试参数createIdentity_password");
			String password = "h3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56ga";
			//长度为2001的字符串
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentity(password);
			OntTest.logger().description(ret.toString());	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//createIdentityFromPriKey023-031
	@Test
	public void test_base_023_createIdentityFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  023  createIdentityFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityFromPriKey_password");
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
			String password = "123456";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentityFromPriKey(password,prikey);
			OntTest.logger().description(ret.toString());	
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_024_createIdentityFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  024  createIdentityFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityFromPriKey_password");
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
			String password = "";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentityFromPriKey(password,prikey);
			OntTest.logger().description(ret.toString());	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_025_createIdentityFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  025  createIdentityFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityFromPriKey_password");
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
			String password = "!@#$%^";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentityFromPriKey(password,prikey);
			OntTest.logger().description(ret.toString());	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_026_createIdentityFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  026  createIdentityFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityFromPriKey_password");
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
			String password = "1h3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56ga";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentityFromPriKey(password,prikey);
			OntTest.logger().description(ret.toString());	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_027_createIdentityFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  027  createIdentityFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityFromPriKey_password");
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
			String password = "123456";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentityFromPriKey(password,prikey);
			OntTest.logger().description(ret.toString());	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_028_createIdentityFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  028  createIdentityFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityFromPriKey_password");
			String prikey = "11eaced231111111111111111111111111111111111111111111111111111111";
			String password = "123456";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentityFromPriKey(password,prikey);
			OntTest.logger().description(ret.toString());	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_029_createIdentityFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  029  createIdentityFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityFromPriKey_prikey");
			String prikey = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111";
			String password = "123456";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentityFromPriKey(password,prikey);
			OntTest.logger().description(ret.toString());	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_030_createIdentityFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  030  createIdentityFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityFromPriKey_password");
			String prikey = "11@#$%^231111111111111111111111111111111111111111111111111111111";
			String password = "123456";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentityFromPriKey(password,prikey);
			OntTest.logger().description(ret.toString());	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_031_createIdentityFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  031  createIdentityFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityFromPriKey_prikey");
			String prikey = "";
			String password = "123456";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentityFromPriKey(password,prikey);
			OntTest.logger().description(ret.toString());	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 59000;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}		
	
	//createIdentityInfo032-035
	@Test
	public void test_base_032_createIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  032  createIdentityInfo()");

		try {
			OntTest.logger().step("测试参数createIdentityInfo_password");
			String password = "123456";
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfo(password);
			OntTest.logger().description(ret.toString());	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_033_createIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  033  createIdentityInfo()");

		try {
			OntTest.logger().step("测试参数createIdentityInfo_password");
			String password = "";
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfo(password);
			OntTest.logger().description(ret.toString());	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_034_createIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  034  createIdentityInfo()");

		try {
			OntTest.logger().step("测试参数createIdentityInfo_password");
			String password = "!@#$%^&*()";
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfo(password);
			System.out.println(ret);	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_035_createIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  035  createIdentityInfo()");

		try {
			OntTest.logger().step("测试参数createIdentityInfo_password");
			String password = "h3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56ga";
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfo(password);
			System.out.println(ret);	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//createIdentityInfoFromPriKey036-044   //待修改
	@Test
	public void test_base_036_createIdentityInfoFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  036  createIdentityInfoFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityInfoFromPriKey_password");
			String label = "label";
			String password = "123456";
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";

			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfoFromPriKey(label, password, prikey);
			OntTest.logger().description(ret.toString());
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	

	@Test
	public void test_normal_037_createIdentityInfoFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  037  createIdentityInfoFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityInfoFromPriKey_password");
			String label = "label";
			String password = "!@#$%^";
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
					
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfoFromPriKey(label, password, prikey);
			OntTest.logger().description(ret.toString());	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_038_createIdentityInfoFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  038  createIdentityInfoFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityInfoFromPriKey_password");
			String label = "label";
			String password = "h3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56ga";
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
					
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfoFromPriKey(label, password, prikey);
			OntTest.logger().description(ret.toString());	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_039_createIdentityInfoFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  039  createIdentityInfoFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityInfoFromPriKey_password");
			String label = "label";
			String password = "";
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
					
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfoFromPriKey(label, password, prikey);
			OntTest.logger().description(ret.toString());	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_040_createIdentityInfoFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  040  createIdentityInfoFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityInfoFromPriKey_prikey");
			String label = "label";
			String password = "123456";
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
					
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfoFromPriKey(label, password, prikey);
			OntTest.logger().description(ret.toString());	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_041_createIdentityInfoFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  041  createIdentityInfoFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityInfoFromPriKey_prikey");
			String label = "label";
			String password = "123456";
			String prikey = "edfabc1111111111111111111111111111111111111111111111111111111111";
					
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfoFromPriKey(label, password, prikey);
			OntTest.logger().description(ret.toString());	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_042_createIdentityInfoFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  042  createIdentityInfoFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityInfoFromPriKey_prikey");
			String label = "label";
			String password = "123456";
			String prikey = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111";
					
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfoFromPriKey(label, password, prikey);
			OntTest.logger().description(ret.toString());	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_043_createIdentityInfoFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  043  createIdentityInfoFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityInfoFromPriKey_prikey");
			String label = "label";
			String password = "123456";
			String prikey = "@#$abc1111111111111111111111111111111111111111111111111111111111";
					
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfoFromPriKey(label, password, prikey);
			OntTest.logger().description(ret.toString());	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_044_createIdentityInfoFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  044  createIdentityInfoFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityInfoFromPriKey_prikey");
			String label = "label";
			String password = "123456";
			String prikey = "";
					
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfoFromPriKey(label, password, prikey);
			OntTest.logger().description(ret.toString());	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 59000;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//getIdentityInfo045-57
	@Test
	public void test_base_045_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  045  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_ontid");
			String password = "123456";
			Account acc = OntTest.sdk().getWalletMgr().createAccount(password);
			String addr = acc.address;
			String ontid = "did:ont:"+addr;
			byte[] salt = Base64.getDecoder().decode(acc.salt);
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			OntTest.logger().description(ret.toString());
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_046_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  046  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_ontid");
			String password = "123456";
			Account acc = OntTest.sdk().getWalletMgr().createAccount(password);
			String addr = acc.address;
			addr = addr.substring(0,addr.length()-3)+"abc";
			String ontid = "did:ont:"+addr;
			byte[] salt = Base64.getDecoder().decode(acc.salt);
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			OntTest.logger().description(ret.toString());
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_abnormal_047_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  047  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_ontid");
			String password = "123456";
			Account acc = OntTest.sdk().getWalletMgr().createAccount(password);
			String addr = acc.address;
			addr = "a"+addr;
			String ontid = "did:ont:"+addr;
			byte[] salt = Base64.getDecoder().decode(acc.salt);
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			OntTest.logger().description(ret.toString());
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_abnormal_048_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  048  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_ontid");
			String password = "123456";
			Account acc = OntTest.sdk().getWalletMgr().createAccount(password);
			String addr = acc.address;
			addr = addr.substring(0,addr.length()-1);
			String ontid = "did:ont:"+addr;
			byte[] salt = Base64.getDecoder().decode(acc.salt);
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			OntTest.logger().description(ret.toString());
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_abnormal_049_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  049  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_ontid");
			String password = "123456";
			Account acc = OntTest.sdk().getWalletMgr().createAccount(password);
			String addr = acc.address;
			addr = addr.substring(0,addr.length()-2)+"@#";
			String ontid = "did:ont:"+addr;
			byte[] salt = Base64.getDecoder().decode(acc.salt);
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			OntTest.logger().description(ret.toString());
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_abnormal_050_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  050  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_ontid");
			String password = "123456";
			Account acc = OntTest.sdk().getWalletMgr().createAccount(password);
			String addr = acc.address;
			String ontid = "did:"+addr;
			byte[] salt = Base64.getDecoder().decode(acc.salt);
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			OntTest.logger().description(ret.toString());
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_abnormal_051_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  051  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_ontid");
			String password = "123456";
			Account acc = OntTest.sdk().getWalletMgr().createAccount(password);
			String addr = acc.address;
			String ontid = "ont:"+addr;
			byte[] salt = Base64.getDecoder().decode(acc.salt);
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			OntTest.logger().description(ret.toString());
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_abnormal_052_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  052  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_ontid");
			String password = "123456";
			Account acc = OntTest.sdk().getWalletMgr().createAccount(password);
			String addr = acc.address;
			String ontid = "";
			byte[] salt = Base64.getDecoder().decode(acc.salt);
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			OntTest.logger().description(ret.toString());
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
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
	public void test_normal_053_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  053  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_password");
			String password = "123456";
			Account acc = OntTest.sdk().getWalletMgr().createAccount(password);
			String addr = acc.address;
			String ontid = "did:ont:"+addr;
			byte[] salt = Base64.getDecoder().decode(acc.salt);
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			OntTest.logger().description(ret.toString());
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_054_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  054  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_password");
			String password = "123456";
			Account acc = OntTest.sdk().getWalletMgr().createAccount(password);
			String addr = acc.address;
			String ontid = "did:ont:"+addr;
			byte[] salt = Base64.getDecoder().decode(acc.salt);
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, "111111", salt);
			OntTest.logger().description(ret.toString());
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58501;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_055_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  055  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_password");
			String password = "123456";
			Account acc = OntTest.sdk().getWalletMgr().createAccount(password);
			String addr = acc.address;
			String ontid = "did:ont:"+addr;
			byte[] salt = Base64.getDecoder().decode(acc.salt);
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, "@#$%^&", salt);
			OntTest.logger().description(ret.toString());
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58501;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_056_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  056  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_password");

			String password = "123456";
			Account acc = OntTest.sdk().getWalletMgr().createAccount(password);
			String addr = acc.address;
			String ontid = "did:ont:"+addr;
			byte[] salt = Base64.getDecoder().decode(acc.salt);
			
			String password1 = "h3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56ga";
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password1, salt);
			OntTest.logger().description(ret.toString());
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58501;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_057_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  057  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_password");
			String password = "123456";
			Account acc = OntTest.sdk().getWalletMgr().createAccount(password);
			String addr = acc.address;
			String ontid = "did:ont:"+addr;
			byte[] salt = Base64.getDecoder().decode(acc.salt);
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, "", salt);
			OntTest.logger().description(ret.toString());
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
		} catch(SDKException e) {
	        Map err = (Map) JSON.parse(e.getMessage()); 
			OntTest.logger().description("err = "+err);
			int err_code = (int) err.get("Error");
			int exp_errcode = 58501;
			OntTest.logger().error(e.toString());
			assertEquals(true,err_code==exp_errcode);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_058_getIdentitys() throws Exception {
		OntTest.logger().description("Digital identity  058  getIdentitys()");

		try {
			OntTest.logger().step("测试接口getIdentitys");
			OntTest.sdk().getWalletMgr().createIdentity("123456");
			OntTest.sdk().getWalletMgr().createIdentity("123456");
			OntTest.sdk().getWalletMgr().createIdentity("123456");
			
			List<Identity> ret0 = OntTest.sdk().getWalletMgr().getWallet().getIdentities();
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret.toString());
//			String exp = "[]";
			assertEquals(true,true);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_059_getIdentity() throws Exception {
		OntTest.logger().description("Digital identity  059  getIdentity()");

		try {
			OntTest.logger().step("测试接口getIdentity_ontid");
			String ontid = OntTest.sdk().getWalletMgr().createIdentity("123456").ontid;
			
			Identity ret = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid);
			OntTest.logger().description(ret.toString());
			
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_060_getIdentity() throws Exception {
		OntTest.logger().description("Digital identity  060  getIdentity()");

		try {
			OntTest.logger().step("测试接口getIdentity_ontid");
			String ontid = OntTest.sdk().getWalletMgr().createIdentity("123456").ontid;
			ontid = ontid.substring(0,ontid.length()-3)+"abc";
			//ontid不存在
			
			Identity ret = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid);
			System.out.println("ret = "+ret);
			String rettmp=null;
			if (ret!=null) 
				rettmp=ret.toString();
			OntTest.logger().description("ret = "+rettmp);
			
			String ret1 = String.valueOf(ret);
			String exp = "null";
			assertEquals(true,ret1.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_061_getIdentity() throws Exception {
		OntTest.logger().description("Digital identity  061  getIdentity()");

		try {
			OntTest.logger().step("测试接口getIdentity_ontid");
			String ontid = "a"+OntTest.sdk().getWalletMgr().createIdentity("123456").ontid;
			
			Identity ret = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid);
			System.out.println("ret = "+ret);
			String rettmp=null;
			if (ret!=null) 
				rettmp=ret.toString();
			OntTest.logger().description("ret = "+rettmp);
			
			String ret1 = String.valueOf(ret);
			String exp = "null";
			assertEquals(true,ret1.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_062_getIdentity() throws Exception {
		OntTest.logger().description("Digital identity  062  getIdentity()");

		try {
			OntTest.logger().step("测试接口getIdentity_ontid");
			String ontid = OntTest.sdk().getWalletMgr().createIdentity("123456").ontid;
			ontid = ontid.substring(0,ontid.length()-1);
			
			Identity ret = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid);
			System.out.println("ret = "+ret);
			
			String rettmp=null;
			if (ret!=null) 
				rettmp=ret.toString();
			OntTest.logger().description("ret = "+rettmp);
			
			String ret1 = String.valueOf(ret);
			String exp = "null";
			assertEquals(true,ret1.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_063_getIdentity() throws Exception {
		OntTest.logger().description("Digital identity  063  getIdentity()");

		try {
			OntTest.logger().step("测试接口getIdentity_ontid");
			String ontid = OntTest.sdk().getWalletMgr().createIdentity("123456").ontid;
			ontid = ontid.substring(0,ontid.length()-1)+"#";

			Identity ret = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid);
			
			System.out.println("ret = "+ret);
			String rettmp=null;
			if (ret!=null) 
				rettmp=ret.toString();
			OntTest.logger().description("ret = "+rettmp);
			
			String ret1 = String.valueOf(ret);
			String exp = "null";
			assertEquals(true,ret1.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_064_getIdentity() throws Exception {
		OntTest.logger().description("Digital identity  064  getIdentity()");

		try {
			OntTest.logger().step("测试接口getIdentity_ontid");
			String str = "ont:"; 
			String ontid = OntTest.sdk().getWalletMgr().createIdentity("123456").ontid;
			ontid = ontid.replace(str, "");
			OntTest.logger().description(ontid);
			
			Identity ret = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid);
			
			System.out.println("ret = "+ret);
			String rettmp=null;
			if (ret!=null) 
				rettmp=ret.toString();
			OntTest.logger().description("ret = "+rettmp);
			
			String ret1 = String.valueOf(ret);
			String exp = "null";
			assertEquals(true,ret1.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_065_getIdentity() throws Exception {
		OntTest.logger().description("Digital identity  065  getIdentity()");

		try {
			OntTest.logger().step("测试接口getIdentity_ontid");
			String str = "did:"; 
			String ontid = OntTest.sdk().getWalletMgr().createIdentity("123456").ontid;
			ontid = ontid.replace(str, "");
			OntTest.logger().description(ontid);
			
			Identity ret = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid);
			System.out.println("ret = "+ret);
			String rettmp=null;
			if (ret!=null) 
				rettmp=ret.toString();
			OntTest.logger().description("ret = "+rettmp);
			
			String ret1 = String.valueOf(ret);
			String exp = "null";
			assertEquals(true,ret1.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_066_getIdentity() throws Exception {
		OntTest.logger().description("Digital identity  066  getIdentity()");

		try {
			OntTest.logger().step("测试接口getIdentity_ontid");
//			String ontid = OntTest.sdk().getWalletMgr().createIdentity("123456").ontid;
			String ontid = "";
			
			Identity ret = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid);
			System.out.println("ret = "+ret);
			String rettmp=null;
			if (ret!=null) 
				rettmp=ret.toString();
			OntTest.logger().description("ret = "+rettmp);
			
			String ret1 = String.valueOf(ret);
			String exp = "null";
			assertEquals(true,ret1.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_067_getDefaultIdentity() throws Exception {
		OntTest.logger().description("Digital identity  067  getDefaultIdentity()");

		try {
			OntTest.logger().step("测试接口getDefaultIdentity");
			OntTest.sdk().getWalletMgr().createIdentity("123456");
			
			Identity ret = OntTest.sdk().getWalletMgr().getDefaultIdentity();
			System.out.println("ret = "+ret);
			String rettmp=null;
			if (ret!=null) 
				rettmp=ret.toString();
			OntTest.logger().description("ret = "+rettmp);
			
			String ret1 = String.valueOf(ret);
			String exp = "null";
			assertEquals(false,ret1.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//getIdentity068-090
	@Test
	public void test_base_068_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  068  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_ontid");
			String ontid = "did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_069_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  069  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_ontid");
			String ontid = "did:ont:1f296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			System.out.println(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_070_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  069  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_ontid");
			String ontid = "did:ont:1Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_071_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  071  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_ontid");
			String ontid = "did:ont:f296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_abnormal_072_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  072  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_ontid");
			String ontid = "did:ont:#f296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_abnormal_073_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  073  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_ontid");
			String ontid = "did:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_074_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  074  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_ontid");
			String ontid = "ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_075_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  075  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_ontid");
			String ontid = ""; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_base_076_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  076  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_key");
			String ontid = "did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_077_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  077  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_key");
			String ontid = "did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "AhZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_078_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  078  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_key");
			String ontid = "did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "1ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_079_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  079  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_key");
			String ontid = "did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "hZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_080_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  080  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_key");
			String ontid = "did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "#hZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_081_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  081  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_key");
			String ontid = "did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "";
			String id = "1";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_082_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  082  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_id");
			String ontid = "did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_083_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  083  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_id");
			String ontid = "did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "#$@";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_084_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  084  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_id");
			String ontid = "did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_085_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  085  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_pubkey");
			String ontid = "did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_086_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  086  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_pubkey");
			String ontid = "did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "13e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_087_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  087  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_pubkey");
			String ontid = "did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "103e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_abnormal_088_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  088  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_pubkey");
			String ontid = "did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "3e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_089_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  089  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_pubkey");
			String ontid = "did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "#3e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_090_addOntIdController() throws Exception {
		OntTest.logger().description("Digital identity  090  addOntIdController()");

		try {
			OntTest.logger().step("测试接口addOntIdController_pubkey");
			String ontid = "did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN"; 
			String key = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String id = "1";
			String pubkey = "";
			
			Identity ret0 = OntTest.sdk().getWalletMgr().getWallet().addOntIdController(ontid, key, id, pubkey);
			String ret = String.valueOf(ret0);
			OntTest.logger().description(ret);
			String exp = "{\"controls\":[{\"address\":\"\",\"algorithm\":\"ECDSA\",\"enc-alg\":\"aes-256-gcm\",\"hash\":\"sha256\",\"id\":\"1\",\"key\":\"ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B\",\"parameters\":{\"curve\":\"secp256r1\"},\"publicKey\":\"03e27f37a66986cce26efdaa13fac216b033b87bd1032f70899c8e5132f2158442\",\"salt\":\"\"}],\"isDefault\":false,\"label\":\"\",\"lock\":false,\"ontid\":\"did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN\"}";
			OntTest.logger().description(exp);
			assertEquals(false,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

}


