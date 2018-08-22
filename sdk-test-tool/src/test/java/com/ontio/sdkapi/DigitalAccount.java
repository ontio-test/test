package com.ontio.sdkapi;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import java.util.Base64;
import java.util.List;
import java.util.Map;

import org.junit.After;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import com.alibaba.fastjson.JSON;
import com.github.ontio.common.WalletQR;
import com.github.ontio.sdk.exception.SDKException;
import com.github.ontio.sdk.info.AccountInfo;
import com.github.ontio.sdk.info.IdentityInfo;
import com.github.ontio.sdk.manager.WalletMgr;
import com.github.ontio.sdk.wallet.Account;
import com.github.ontio.sdk.wallet.Identity;
import com.github.ontio.sdk.wallet.Wallet;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;
import com.ontio.testtool.utils.Config;

public class DigitalAccount {
	@Rule public OntTestWatcher watchman= new OntTestWatcher();
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
		OntTest.api().node().restartAll();
		OntTest.api().node().initOntOng();
	}
	
	@Before
	public void setUp() throws Exception {
		OntTest.init();
	}
	
	@After
	public void TearDown() throws Exception {
		System.out.println("TearDown");
	}
	
	
	@Test
	public void test_base_001_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.logger().step("1.生成账户");
			String key = "QrxoFSIRPhjdNK1oVRimKVhGJOJZU/iQJE4NjmU+IEK2/5EYjZYjJu89VfympHTr";
			String password = "123456";
			String address = "AcNadNbsRwNDjN2XRAVyqD9LL4qSedd8WK";
			byte[] salt = Base64.getDecoder().decode("zCBkHt+u2iuytAXZfHfm+w==");

			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("001",key, password, address, salt);
			
			OntTest.logger().print(act.toString());
			assertEquals(true,act.address.equals(address));
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_002_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.logger().step("1.生成账户");
			Account temp = OntTest.sdk().getWalletMgr().createAccount("123456");
			String key = temp.getKey();
			String password = "123456";
			String address = "AcNadNbsRwNDjN2XRAVyqD9LL4qSedd8WK";
			byte[] salt = Base64.getDecoder().decode("zCBkHt+u2iuytAXZfHfm+w==");
			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("002", key, password, address, salt);
			
			OntTest.logger().print(act.toString());
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("51015".equals(er_code)) {
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
	public void test_abnormal_003_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.logger().step("1.生成账户");
			String key = "QrxoFSIRPhjdNK1oVRimKVhGJOJZU/iQJE4NjmU+IEK2/5EYjZYjJu89VfympHTrq";
			String password = "123456";
			String address = "AcNadNbsRwNDjN2XRAVyqD9LL4qSedd8WK";
			byte[] salt = Base64.getDecoder().decode("zCBkHt+u2iuytAXZfHfm+w==");

			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("003",key, password, address, salt);
			
			OntTest.logger().print(act.toString());
			
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_abnormal_004_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.logger().step("1.生成账户");
			String key = "QrxoFSIRPhjdNK1oVRimKVhGJOJZU/iQJE4NjmU+IEK2/5EYjZYjJu89VfympTr";
			String password = "123456";
			String address = "AcNadNbsRwNDjN2XRAVyqD9LL4qSedd8WK";
			byte[] salt = Base64.getDecoder().decode("zCBkHt+u2iuytAXZfHfm+w==");

			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("004",key, password, address, salt);
			
			OntTest.logger().print(act.toString());
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("51015".equals(er_code)) {
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
	public void test_abnormal_005_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.logger().step("1.生成账户");
			String key = "QrxoFSIRPhjdNK1oVRimKVhGJOJZU/!@#$%^&*()_+<?/5EYjZYjJu89VfympTr";
			String password = "123456";
			String address = "AcNadNbsRwNDjN2XRAVyqD9LL4qSedd8WK";
			byte[] salt = Base64.getDecoder().decode("zCBkHt+u2iuytAXZfHfm+w==");

			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("005",key, password, address, salt);
			
			OntTest.logger().print(act.toString());
			
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_006_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.logger().step("1.生成账户");
			String key = "";
			String password = "123456";
			String address = "AcNadNbsRwNDjN2XRAVyqD9LL4qSedd8WK";
			byte[] salt = Base64.getDecoder().decode("zCBkHt+u2iuytAXZfHfm+w==");
			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("006",key, password, address, salt);
			
			OntTest.logger().print(act.toString());
			
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("51015".equals(er_code)) {
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
	public void test_normal_007_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.sdk().getWalletMgr().createAccountInfo("123456");
			OntTest.logger().step("1.生成账户");
			String key = "QrxoFSIRPhjdNK1oVRimKVhGJOJZU/iQJE4NjmU+IEK2/5EYjZYjJu89VfympHTr";
			String password = "123456";
			String address = "AcNadNbsRwNDjN2XRAVyqD9LL4qSedd8WK";
			byte[] salt = Base64.getDecoder().decode("zCBkHt+u2iuytAXZfHfm+w==");
			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("007",key, password, address, salt);
			
			OntTest.logger().print(act.toString());
			assertEquals(true,act.address.equals(address));

		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_008_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.logger().step("1.生成账户");
			String key = "QrxoFSIRPhjdNK1oVRimKVhGJOJZU/iQJE4NjmU+IEK2/5EYjZYjJu89VfympHTr";
			String password = "654321";
			String address = "AcNadNbsRwNDjN2XRAVyqD9LL4qSedd8WK";
			byte[] salt = Base64.getDecoder().decode("zCBkHt+u2iuytAXZfHfm+w==");
			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("008",key, password, address, salt);
			
			OntTest.logger().print(act.toString());
			

		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("51015".equals(er_code)) {
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
	public void test_normal_009_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.logger().step("1.生成账户");
			String key = "WUoF55QJ/yo3/0x+OYcD6kQ6TGpyJeEHGi1AnoQBLe1AnRxgU0tQKxre3ny4SGDm";
			String password = "";
			String address = "AKcgbuwrXsnrH5YXtaYB7jYJg7VCQq2q8T";
			byte[] salt = Base64.getDecoder().decode("IjnXmLQTTJ0+UxWvkBUAUA==");
			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("009",key, password, address, salt);
			
			OntTest.logger().print(act.toString());
			assertEquals(true,act.address.equals(address));
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_normal_010_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.logger().step("1.生成账户");
			String key = "QrxoFSIRPhjdNK1oVRimKVhGJOJZU/iQJE4NjmU+IEK2/5EYjZYjJu89VfympHTr";
			String password = "123456";
			String address = "AcNadNbsRwNDjN2XRAVyqD9LL4qSedd8WK";
			byte[] salt = Base64.getDecoder().decode("zCBkHt+u2iuytAXZfHfm+w==");
			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("010",key, password, address, salt);
			
			OntTest.logger().print(act.toString());
			assertEquals(true,act.address.equals(address));
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_abnormal_011_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.logger().step("1.生成账户");
			Account temp = OntTest.sdk().getWalletMgr().createAccount("123456");
			String tpsalt = temp.salt;
			String key = "QrxoFSIRPhjdNK1oVRimKVhGJOJZU/iQJE4NjmU+IEK2/5EYjZYjJu89VfympHTr";
			String password = "123456";
			String address = "AcNadNbsRwNDjN2XRAVyqD9LL4qSedd8WK";
			byte[] salt = Base64.getDecoder().decode(tpsalt);
			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("011",key, password, address, salt);

			OntTest.logger().print(act.toString());
			assertEquals(false, address.equals(""));
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("51015".equals(er_code)) {
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
	public void test_abnormal_012_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.logger().step("1.生成账户");
			String key = "QrxoFSIRPhjdNK1oVRimKVhGJOJZU/iQJE4NjmU+IEK2/5EYjZYjJu89VfympHTr";
			String password = "123456";
			String address = "AcNadNbsRwNDjN2XRAVyqD9LL4qSedd8WK";
			byte[] salt = Base64.getDecoder().decode("");
			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("012",key, password, address, salt);

			OntTest.logger().print(act.toString());
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
	public void test_normal_013_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.logger().step("1.生成账户");
			String key = "QrxoFSIRPhjdNK1oVRimKVhGJOJZU/iQJE4NjmU+IEK2/5EYjZYjJu89VfympHTr";
			String password = "123456";
			String address = "AcNadNbsRwNDjN2XRAVyqD9LL4qSedd8WK";
			byte[] salt = Base64.getDecoder().decode("zCBkHt+u2iuytAXZfHfm+w==");
			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("013",key, password, address, salt);

			OntTest.logger().print(act.toString());
			assertEquals(true,act.address.equals(address));
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_014_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.logger().step("1.生成账户");
			String key = "QrxoFSIRPhjdNK1oVRimKVhGJOJZU/iQJE4NjmU+IEK2/5EYjZYjJu89VfympHTr";
			String password = "123456";
			String address = "123vweiutnaiutbvailwebtuyauiaybjetvjuwegtwjwa";
			byte[] salt = Base64.getDecoder().decode("zCBkHt+u2iuytAXZfHfm+w==");
			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("014",key, password, address, salt);

			OntTest.logger().print(act.toString());
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("51015".equals(er_code)) {
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
	public void test_abnormal_015_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.logger().step("1.生成账户");
			String key = "QrxoFSIRPhjdNK1oVRimKVhGJOJZU/iQJE4NjmU+IEK2/5EYjZYjJu89VfympHTr";
			String password = "123456";
			String address = "KDJFHkjf3rj4grvbksadjahkeakejJfsdvrdynrdmsetreymikuyeoirjt56897u0w3ithsglswaoi42395jtBHFD";
			byte[] salt = Base64.getDecoder().decode("zCBkHt+u2iuytAXZfHfm+w==");
			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("015",key, password, address, salt);

			OntTest.logger().print(act.toString());
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("51015".equals(er_code)) {
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
	public void test_abnormal_016_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.logger().step("1.生成账户");
			String key = "QrxoFSIRPhjdNK1oVRimKVhGJOJZU/iQJE4NjmU+IEK2/5EYjZYjJu89VfympHTr";
			String password = "123456";
			String address = "！@#￥%……？<>?:\\\\\\\"|}{+_)*$";
			byte[] salt = Base64.getDecoder().decode("zCBkHt+u2iuytAXZfHfm+w==");
			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("016",key, password, address, salt);

			OntTest.logger().print(act.toString());
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("51015".equals(er_code)) {
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
	public void test_abnormal_017_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.logger().step("1.生成账户");
			String key = "QrxoFSIRPhjdNK1oVRimKVhGJOJZU/iQJE4NjmU+IEK2/5EYjZYjJu89VfympHTr";
			String password = "123456";
			String address = "AcNadNbsRwNDjN2XRAVyqD9LL4qSedd8WK";
			byte[] salt = Base64.getDecoder().decode("zCBkHt+u2iuytAXZfHfm+w==");
			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("017",key, password, address, salt);
			Account act2 = OntTest.sdk().getWalletMgr().importAccount("017",key, password, address, salt);
			OntTest.logger().print(act2.toString());
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
	public void test_abnormal_018_importAccount() throws Exception {
		OntTest.logger().description("----------importAccount----------");
		
		try {
			OntTest.logger().step("1.生成账户");
			String key = "QrxoFSIRPhjdNK1oVRimKVhGJOJZU/iQJE4NjmU+IEK2/5EYjZYjJu89VfympHTr";
			String password = "123456";
			String address = "";
			byte[] salt = Base64.getDecoder().decode("zCBkHt+u2iuytAXZfHfm+w==");
			OntTest.logger().step("2.导入账户");
			Account act = OntTest.sdk().getWalletMgr().importAccount("018",key, password, address, salt);

			OntTest.logger().print(act.toString());
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("51015".equals(er_code)) {
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
	public void test_base_019_createAccount() throws Exception {
		OntTest.logger().description("----------createAccount----------");
		
		try {
			Account acc = OntTest.sdk().getWalletMgr().createAccount("019", "123456");
			OntTest.logger().print(acc.toString());
			assertEquals(true,acc.address.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_020_createAccount() throws Exception {
		OntTest.logger().description("----------createAccount----------");
		
		try {
			Account acc = OntTest.sdk().getWalletMgr().createAccount("020","");
			OntTest.logger().print(acc.toString());
			assertEquals(true,acc.address.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_021_createAccount() throws Exception {
		OntTest.logger().description("----------createAccount----------");
		
		try {
			Account acc = OntTest.sdk().getWalletMgr().createAccount("021",",./0-=/pojh/guiyg''[]-#$^&(*&^!#@~!@#$%^&*(");
			OntTest.logger().print(acc.toString());
			assertEquals(true,acc.address.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_normal_022_createAccount() throws Exception {
		OntTest.logger().description("----------createAccount----------");
		
		try {
		Account acc = OntTest.sdk().getWalletMgr().createAccount("022","cqn3784tvbqo9l2by4o2"
				+ "819439qv$vwqibbu8cwnxaiuwfryncuiwervyrtwvwetufynwaeoilweeitauaiewlc"
				+ "nkauiwrbhyvuiwervyiwarvyuwaeryvuwaeuwaeuwaeuwaeuwaeuwaetiauwtyiuyeckwuievqluervynhiwqlrcqwlierv"
				+ "qcwbueuqtfnkwcirwqfufufuweoq2m395rj8219630489671-7t6u[=`7cnu`	90 U`097NN	F98TY2489	Cun8curiu"
				+ "ncroh89y47w39p2ncuqxom,zepSQO,ADLWEM8RHJN398W4TV613TN8Qbo8i23fvyeuitvn983tv948w3[tmuw0i my"
				+ "q2m3p4987tvn03p4829q3vyvy8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro32q8tybnq3oy89on"
				+ "qcwbueuqtfnkwcirwqfufufuweoq2m395rj8219630489671qcwbueuqtfnkwcirwqfufufuweoq2m395rj8219630489671"
				+ "qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963048967p4987tvn03p4829q3vyvy8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro32"
				+ "1qcwbueuqtfnkwcirwqfufufuweoq2m395rj82196304p4987tvn03p4829q3vyvy8qo437ybtvo8q374ybtqo23"
				+ "oq2m395rj8219630489671-7t6u[=`7cnu`	90 U`097NNqcwbueuqtfnkwcirwqfufufuweoq2m395rj8219"
				+ "63048967p4987tvn03p4829q3vyvy8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro32"
				+ "oq2m395rj8219630489671-7t6u[=`7cnu`	90 U`097NN784yn5r2q894y5vnro3289671qcwbueuqtfnkwcirwqfufufuweoq2"
				+ "m395rj821963048967p4987tvn03p4829q3vyvy8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro32qcwbueuqtfnkwcirwq"
				+ "fufufuweoq2m395rj821963048967p4987tvn03p4829q3qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963048967p4987tvn03p4"
				+ "829q3vyvy8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro32r2q894y5vnro32q8tybnq3oy8r2q894y5vnro32q8tybnq3oy8"
				+ "vyvy8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro32qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963048967p4"
				+ "987tvn03p4829q3vyvy8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro32r2q894y5vnro32q8tybnq3oy8r2q894y5vnro32q8tybnq3oy8"
				+ "uweoq2m395rj821963048967p4987tvn03p4829q3qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963048967p498afwegb6547n7发第三个 sfawe"
				+ "m395rj821963048967p4987tvn03p4829q3qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963048m395rj821963048967p4987tvn"
				+ "03p4829q3qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963048fnkwcirwqfufufuweoq2m395rj8219630489671qcwbfnkwcirwqfufufuweoq2m395"
				+ "fnkwcirwqfufufuweoq2m395rj8219630489671qcwbfnkwcirwqfufufuweoq2m395rj8219630489671qcwbrj8219630489671qcwbfnkwcirwqfufufuweoq2m"
				+ "395rj8219630489671qcuqtfnkwcirwqfufufuweoq2m395rj8219630489671qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963"
				+ "uqtfnkwcirwqfufufuweoq2m395rj8219630489671qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963wbwbrj8219630489671qcwb");
			OntTest.logger().print(acc.toString());
			assertEquals(true,acc.address.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_023_createAccountFromPriKey() throws Exception {
		OntTest.logger().description("----------createAccountFromPriKey----------");
		
		try {
			Account acc = OntTest.sdk().getWalletMgr().createAccountFromPriKey("023","123456", "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef");
			OntTest.logger().print(acc.toString());
			assertEquals(true,acc.address.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_normal_024_createAccountFromPriKey() throws Exception {
		OntTest.logger().description("----------createAccountFromPriKey----------");
		
		try {
			Account acc = OntTest.sdk().getWalletMgr().createAccountFromPriKey("024","", "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef");
			OntTest.logger().print(acc.toString());
			assertEquals(true,acc.address.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_normal_025_createAccountFromPriKey() throws Exception {
		OntTest.logger().description("----------createAccountFromPriKey----------");
		
		try {
			Account acc = OntTest.sdk().getWalletMgr().createAccountFromPriKey("025","!@#$%^&*()_+,./\"<>\"", "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef");
			OntTest.logger().print(acc.toString());
			assertEquals(true,acc.address.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	
	@Test
	public void test_normal_026_createAccountFromPriKey() throws Exception {
		OntTest.logger().description("----------createAccountFromPriKey----------");
		
		try {
			Account acc = OntTest.sdk().getWalletMgr().createAccountFromPriKey("026","cqn3784tvbqo9l2by4o2819439qv$vwqibbu8cwnxaiuwfryncui"
					+ "wervyrtwvwetufynwaeoilweeitauaiewlcnkauiwrbhyvuiwervyiwarvyuwaeryvuwaeuwaeuwaeuwaeuwaeuwaetiauwtyiuyeckwuievq"
					+ "luervynhiwqlrcqwliervqcwbueuqtfnkwcirwqfufufuweoq2m395rj8219630489671-7t6u[=`7cnu`	90 U`097NN	F98TY2489	"
					+ "Cun8curiuncroh89y47w39p2ncuqxom,zepSQO,ADLWEM8RHJN398W4TV613TN8Qbo8i23fvyeuitvn983tv948w3[tmuw0i myq2m3p4987tv"
					+ "n03p4829q3vyvy8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro32q8tybnq3oy89onqcwbueuqtfnkwcirwqfufufuweoq2m395rj8219"
					+ "630489671qcwbueuqtfnkwcirwqfufufuweoq2m395rj8219630489671qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963048967p4987tv"
					+ "n03p4829q3vyvy8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro321qcwbueuqtfnkwcirwqfufufuweoq2m395rj82196304p4987tvn03"
					+ "p4829q3vyvy8qo437ybtvo8q374ybtqo23oq2m395rj8219630489671-7t6u[=`7cnu`	90 U`097NNqcwbueuqtfnkwcirwqfufufuweoq"
					+ "2m395rj821963048967p4987tvn03p4829q3vyvy8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro32oq2m395rj8219630489671-7t6u["
					+ "=`7cnu`	90 U`097NN784yn5r2q894y5vnro3289671qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963048967p4987tvn03p4829q3vyvy"
					+ "8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro32qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963048967p4987tvn03p4829q3qcwbu"
					+ "euqtfnkwcirwqfufufuweoq2m395rj821963048967p4987tvn03p4829q3vyvy8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro32r2q894"
					+ "y5vnro32q8tybnq3oy8r2q894y5vnro32q8tybnq3oy8vyvy8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro32qcwbueuqtfnkwcirwqfuf"
					+ "ufuweoq2m395rj821963048967p987tvn03p4829q3vyvy8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro32r2q894y5vnro32q8tybnq3oy"
					+ "8r2q894y5vnro32q8tybnq3oy8uweoq2m395rj821963048967p4987tvn03p4829q3qcwbueuqtfnkwcirwqfufufuweoq2m395rj82196304896"
					+ "7p498afwegb6547n7发第三个 sfawem395rj821963048967p4987tvn03p4829q3qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963048m395r"
					+ "j821963048967p4987tvn03p4829q3qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963048fnkwcirwqfufufuweoq2m395rj8219630489671q"
					+ "cwbfnkwcirwqfufufuweoq2m395fnkwcirwqfufufuweoq2m395rj8219630489671qcwbfnkwcirwqfufufuweoq2m395rj8219630489671qcwbr"
					+ "j8219630489671qcwbfnkwcirwqfufufuweoq2m395rj8219630489671qcuqtfnkwcirwqfufufuweoq2m395rj8219630489671qcwbueuqtfnkw"
					+ "cirwqfufufuweoq2m395rj821963uqtfnkwcirwqfufufuweoq2m395rj8219630489671qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963wbw"
					+ "brj8219630489671qcwb", "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef");
			OntTest.logger().print(acc.toString());
			assertEquals(true,acc.address.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_normal_027_createAccountFromPriKey() throws Exception {
		OntTest.logger().description("----------createAccountFromPriKey----------");
		
		try {
			Account acc = OntTest.sdk().getWalletMgr().createAccountFromPriKey("027","123456", "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef");
			OntTest.logger().print(acc.toString());
			assertEquals(true,acc.address.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_abnormal_028_createAccountFromPriKey() throws Exception {
		OntTest.logger().description("----------createAccountFromPriKey----------");
		
		try {
			Account acc = OntTest.sdk().getWalletMgr().createAccountFromPriKey("028","123456", "1234asdfghabcdef1234567890abcdef1234567890abcdef1234567890abcdef");
			OntTest.logger().print(acc.toString());
		}

		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_029_createAccountFromPriKey() throws Exception {
		OntTest.logger().description("----------createAccountFromPriKey----------");
		
		try {
			Account acc = OntTest.sdk().getWalletMgr().createAccountFromPriKey("029","123456", "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1");
			OntTest.logger().print(acc.toString());
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("59000".equals(er_code)) {
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
	public void test_abnormal_030_createAccountFromPriKey() throws Exception {
		OntTest.logger().description("----------createAccountFromPriKey----------");
		
		try {
			Account acc = OntTest.sdk().getWalletMgr().createAccountFromPriKey("030","123456", "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcde");
			OntTest.logger().print(acc.toString());
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("59000".equals(er_code)) {
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
	public void test_abnormal_031_createAccountFromPriKey() throws Exception {
		OntTest.logger().description("----------createAccountFromPriKey----------");
		
		try {
			Account acc = OntTest.sdk().getWalletMgr().createAccountFromPriKey("031","123456", "!@#$%^&*()abcdef1234567890abcdef1234567890abcdef1234567890abcdef");
			OntTest.logger().print(acc.toString());
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("59000".equals(er_code)) {
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
	public void test_abnormal_032_createAccountFromPriKey() throws Exception {
		OntTest.logger().description("----------createAccountFromPriKey----------");
		
		try {
			Account acc = OntTest.sdk().getWalletMgr().createAccountFromPriKey("032","123456", "");
			OntTest.logger().print(acc.toString());
		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("59000".equals(er_code)) {
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
	public void test_base_033_createAccountInfo() throws Exception {
		OntTest.logger().description("----------createAccountInfo----------");
		
		try {
			AccountInfo acc = OntTest.sdk().getWalletMgr().createAccountInfo("033","123456");
			OntTest.logger().print(acc.toString());
			assertEquals(true,true);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	
	@Test
	public void test_normal_034_createAccountInfo() throws Exception {
		OntTest.logger().description("----------createAccountInfo----------");
		
		try {
			AccountInfo acc = OntTest.sdk().getWalletMgr().createAccountInfo("034","");
			OntTest.logger().print(acc.toString());
			assertEquals(true,acc.addressBase58.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_normal_035_createAccountInfo() throws Exception {
		OntTest.logger().description("----------createAccountInfo----------");
		
		try {
			AccountInfo acc = OntTest.sdk().getWalletMgr().createAccountInfo("035",",./0-=/pojh/guiyg''[]-#$^&(*&^!#@~!@#$%^&*(\"");
			OntTest.logger().print(acc.toString());
			assertEquals(true,acc.addressBase58.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_036_createAccountInfo() throws Exception {
		OntTest.logger().description("----------createAccountInfo----------");
		
		try {
			AccountInfo acc = OntTest.sdk().getWalletMgr().createAccountInfo("036","cqn3784tvbqo9l2by4o2819439q"
					+ "v$vwqibbu8cwnxaiuwfryncuiwervyrtwvwetufynwaeoilweeitauaiewlcnkauiwrbhyvuiwervyiwarv"
					+ "yuwaeryvuwaeuwaeuwaeuwaeuwaeuwaetiauwtyiuyeckwuievqluervynhiwqlrcqwliervqcwbueuqtfnkw"
					+ "cirwqfufufuweoq2m395rj8219630489671-7t6u[=`7cnu`	90U`097NN	F98TY2489	Cun8curiuncroh8"
					+ "9y47w39p2ncuqxom,zepSQO,ADLWEM8RHJN398W4TV613TN8Qbo8i23fvyeuitvn983tv948w3[tmuw0imyq2m3p498"
					+ "7tvn03p4829q3vyvy8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro32q8tybnq3oy89onqcwbueuqtfnkwcirwqfuf"
					+ "ufuweoq2m395rj8219630489671qcwbueuqtfnkwcirwqfufufuweoq2m395rj8219630489671qcwbueuqtfnkwcirwqfufuf"
					+ "uweoq2m395rj821963048967p4987tvn03p4829q3vyvy8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro321qcwbueuqtfnk"
					+ "wcirwqfufufuweoq2m395rj82196304p4987tvn03p4829q3vyvy8qo437ybtvo8q374ybtqo23oq2m395rj8219630489671-7t6u[="
					+ "`7cnu`	90U`097NNqcwbueuqtfnkwcirwqfufufuweoq2m395rj821963048967p4987tvn03p4829q3vyvy8qo437ybtvo8q374ybtqo"
					+ "23784yn5r2q894y5vnro32oq2m395rj8219630489671-7t6u[=`7cnu`	90U`097NN784yn5r2q894y5vnro3289671qcwbueuqtfnkwc"
					+ "irwqfufufuweoq2m395rj821963048967p4987tvn03p4829q3vyvy8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro32qcwbueuqtfnkwc"
					+ "irwqfufufuweoq2m395rj821963048967p4987tvn03p4829q3qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963048967p4987tvn03p4829q3"
					+ "vyvy8qo437ybtvo8q374ybtqo23784yn5r2q894y5vnro32r2q894y5vnro32q8tybnq3oy8r2q894y5vnro32q8tybnq3oy8vyvy8qo437ybtvo8q37"
					+ "4ybtqo23784yn5r2q894y5vnro32qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963048967p4987tvn03p4829q3vyvy8qo437ybtvo8q374ybt"
					+ "qo23784yn5r2q894y5vnro32r2q894y5vnro32q8tybnq3oy8r2q894y5vnro32q8tybnq3oy8uweoq2m395rj821963048967p4987tvn03p482"
					+ "9q3qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963048967p498afwegb6547n7发第三个sfawem395rj821963048967p4987tvn03p4829"
					+ "q3qcwbueuqtfnkwcirwqfufufuweoq2m395rj821963048m395rj821963048967p4987tvn03p4829q3qcwbueuqtfnkwcirwqfufufuweo"
					+ "q2m395rj821963048fnkwcirwqfufufuweoq2m395rj8219630489671qcwbfnkwcirwqfufufuweoq2m395fnkwcirwqfufufuweoq2"
					+ "m395rj8219630489671qcwbfnkwcirwqfufufuweoq2m395rj8219630489671qcwbrj8219630489671qcwbfnkwcirwqfufufu"
					+ "weoq2m395rj8219630489671qcuqtfnkwcirwqfufufuweoq2m395rj8219630489671qcwbueuqtfnkwcirwqfufufuweoq"
					+ "2m395rj821963uqtfnkwcirwqfufufuweoq2m395rj8219630489671qcwbueuqtfnkwcirwqfufufuweoq2m395rj8219"
					+ "63wbwbrj8219630489671qcwb");
			OntTest.logger().print(acc.toString());
			assertEquals(true,acc.addressBase58.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_037_getAccountInfo() throws Exception {
		OntTest.logger().description("----------getAccountInfo----------");
		
		try {
			OntTest.logger().step("1.创建账户");
			Account createaccinfo = OntTest.sdk().getWalletMgr().createAccount("037","123456");
			OntTest.logger().print(createaccinfo.toString());
			String password = "123456";
			String address = createaccinfo.address;
			byte[] salt = createaccinfo.getSalt();
			OntTest.logger().step("2.获取账号信息");
			AccountInfo acc = OntTest.sdk().getWalletMgr().getAccountInfo(address, password, salt);
			OntTest.logger().print(acc.toString());
			assertEquals(true, acc.addressBase58.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_abnormal_038_getAccountInfoo() throws Exception {
		OntTest.logger().description("----------getAccountInfo----------");
		
		try {
			OntTest.logger().step("1.创建账户");
			Account createaccinfo = OntTest.sdk().getWalletMgr().createAccount("038","123456");
			OntTest.logger().print(createaccinfo.toString());
			String password = "123456";
			String address = "AcNadNbsRwNDjN2XRAVyqD9LL4qSedd8Wl";
			byte[] salt = createaccinfo.getSalt();
			OntTest.logger().step("2.获取账号信息");
			AccountInfo acc = OntTest.sdk().getWalletMgr().getAccountInfo(address, password, salt);
			OntTest.logger().print(acc.toString());

		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("59000".equals(er_code)) {
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
	public void test_abnormal_039_getAccountInfo() throws Exception {
		OntTest.logger().description("----------getAccountInfo----------");
		
		try {
			OntTest.logger().step("1.创建账户");
			Account createaccinfo = OntTest.sdk().getWalletMgr().createAccount("039","123456");
			OntTest.logger().print(createaccinfo.toString());
			String password = "123456";
			String address = "AcNadNbsRwNDjN2XRAVyqD9LL4qSedd8WKL";
			byte[] salt = createaccinfo.getSalt();
			OntTest.logger().step("2.获取账号信息");
			AccountInfo acc = OntTest.sdk().getWalletMgr().getAccountInfo(address, password, salt);
			OntTest.logger().print(acc.toString());

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
	public void test_abnormal_040_getAccountInfo() throws Exception {
		OntTest.logger().description("----------getAccountInfo----------");
		
		try {
			OntTest.logger().step("1.创建账户");
			Account createaccinfo = OntTest.sdk().getWalletMgr().createAccount("040","123456");
			OntTest.logger().print(createaccinfo.toString());
			String password = "123456";
			String address = "AcNadNbsRwNDjN2XRAV@#$9LL4qSedd8WK";
			byte[] salt = createaccinfo.getSalt();
			OntTest.logger().step("2.获取账号信息");
			AccountInfo acc = OntTest.sdk().getWalletMgr().getAccountInfo(address, password, salt);
			OntTest.logger().print(acc.toString());

		}catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_041_getAccountInfo() throws Exception {
		OntTest.logger().description("----------getAccountInfo----------");
		
		try {
			OntTest.logger().step("1.创建账户");
			String key = "QrxoFSIRPhjdNK1oVRimKVhGJOJZU/iQJE4NjmU+IEK2/5EYjZYjJu89VfympHTr";
			String password = "123456";
			String address = "AcNadNbsRwNDjN2XRAVyqD9LL4qSedd8WK";
			byte[] salt = Base64.getDecoder().decode("zCBkHt+u2iuytAXZfHfm+w==");
			OntTest.logger().step("2.import一个账户");
			OntTest.sdk().getWalletMgr().importAccount(key, password, address, salt);
			OntTest.logger().step("3.获取账号信息");
			AccountInfo acc = OntTest.sdk().getWalletMgr().getAccountInfo(address, password, salt);
			OntTest.logger().print(acc.toString());
			assertEquals(true, acc.addressBase58.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_042_getAccountInfo() throws Exception {
		OntTest.logger().description("----------getAccountInfo----------");
		
		try {
			OntTest.logger().step("1.创建账户");
			Account createaccinfo = OntTest.sdk().getWalletMgr().createAccount("123456");
			OntTest.logger().print(createaccinfo.toString());
			String password = "123456";
			String address = "";
			byte[] salt = createaccinfo.getSalt();
			OntTest.logger().step("2.获取账号信息");
			AccountInfo acc = OntTest.sdk().getWalletMgr().getAccountInfo(address, password, salt);
			OntTest.logger().print(acc.toString());

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
	public void test_normal_043_getAccountInfo() throws Exception {
		OntTest.logger().description("----------getAccountInfo----------");
		
		try {
			OntTest.logger().step("1.创建账户");
			Account createaccinfo = OntTest.sdk().getWalletMgr().createAccount("123456");
			OntTest.logger().print(createaccinfo.toString());
			String password = "123456";
			String address = createaccinfo.address;
			byte[] salt = createaccinfo.getSalt();
			OntTest.logger().step("2.获取账号信息");
			AccountInfo acc = OntTest.sdk().getWalletMgr().getAccountInfo(address, password, salt);
			OntTest.logger().print(acc.toString());

		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_abnormal_044_getAccountInfo() throws Exception {
		OntTest.logger().description("----------getAccountInfo----------");
		
		try {
			OntTest.logger().step("1.创建账户");
			Account createaccinfo = OntTest.sdk().getWalletMgr().createAccount("123456");
			OntTest.logger().print(createaccinfo.toString());
			String password = "654321";
			String address = createaccinfo.address;
			byte[] salt = createaccinfo.getSalt();
			OntTest.logger().step("2.获取账号信息");
			AccountInfo acc = OntTest.sdk().getWalletMgr().getAccountInfo(address, password, salt);
			OntTest.logger().print(acc.toString());

		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58501".equals(er_code)) {
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
	public void test_normal_045_getAccountInfo() throws Exception {
		OntTest.logger().description("----------getAccountInfo----------");
		
		try {
			OntTest.logger().step("1.创建账户");
			Account createaccinfo = OntTest.sdk().getWalletMgr().createAccount("!@#$%^");
			OntTest.logger().print(createaccinfo.toString());
			String password = "!@#$%^";
			String address = createaccinfo.address;
			byte[] salt = createaccinfo.getSalt();
			OntTest.logger().step("2.获取账号信息");
			AccountInfo acc = OntTest.sdk().getWalletMgr().getAccountInfo(address, password, salt);
			OntTest.logger().print(acc.toString());
			assertEquals(true, acc.addressBase58.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_normal_046_getAccountInfo() throws Exception {
		OntTest.logger().description("----------getAccountInfo----------");
		
		try {
			OntTest.logger().step("1.创建账户");
			Account createaccinfo = OntTest.sdk().getWalletMgr().createAccount("");
			OntTest.logger().print(createaccinfo.toString());
			String password = "";
			String address = createaccinfo.address;
			byte[] salt = createaccinfo.getSalt();
			OntTest.logger().step("2.获取账号信息");
			AccountInfo acc = OntTest.sdk().getWalletMgr().getAccountInfo(address, password, salt);
			OntTest.logger().print(acc.toString());
			assertEquals(true, acc.addressBase58.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_normal_047_getAccountInfo() throws Exception {
		OntTest.logger().description("----------getAccountInfo----------");
		
		try {
			OntTest.logger().step("1.创建账户");
			Account createaccinfo = OntTest.sdk().getWalletMgr().createAccount("123456");
			OntTest.logger().print(createaccinfo.toString());
			String password = "123456";
			String address = createaccinfo.address;
			byte[] salt = createaccinfo.getSalt();
			OntTest.logger().step("2.获取账号信息");
			AccountInfo acc = OntTest.sdk().getWalletMgr().getAccountInfo(address, password, salt);
			OntTest.logger().print(acc.toString());
			assertEquals(true, acc.addressBase58.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_048_getAccountInfo() throws Exception {
		OntTest.logger().description("----------getAccountInfo----------");
		
		try {
			OntTest.logger().step("1.创建账户");
			Account createaccinfo = OntTest.sdk().getWalletMgr().createAccount("123456");
			Account createaccinfo1 = OntTest.sdk().getWalletMgr().createAccount("123456");
			OntTest.logger().print(createaccinfo.toString());
			OntTest.logger().print(createaccinfo1.toString());			
			String password = "123456";
			String address = createaccinfo.address;
			byte[] salt = createaccinfo1.getSalt();
			OntTest.logger().step("2.获取账号信息");
			AccountInfo acc = OntTest.sdk().getWalletMgr().getAccountInfo(address, password, salt);
			OntTest.logger().print(acc.toString());

		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58501".equals(er_code)) {
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
	public void test_abnormal_049_getAccountInfo() throws Exception {
		OntTest.logger().description("----------getAccountInfo----------");
		
		try {
			OntTest.logger().step("1.创建账户");
			Account createaccinfo = OntTest.sdk().getWalletMgr().createAccount("123456");
			OntTest.logger().print(createaccinfo.toString());
			String password = "123456";
			String address = createaccinfo.address;
			byte[] salt = Base64.getDecoder().decode("");
			OntTest.logger().step("2.获取账号信息");
			AccountInfo acc = OntTest.sdk().getWalletMgr().getAccountInfo(address, password, salt);
			OntTest.logger().print(acc.toString());

		}
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58501".equals(er_code)) {
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
	public void test_base_050_getAccounts() throws Exception {
		OntTest.logger().description("----------getAccounts----------");
		
		try {
			OntTest.logger().step("1.创建账户");
			OntTest.sdk().getWalletMgr().createAccount("123456");
			OntTest.logger().print("第一个创建成功！");
			OntTest.sdk().getWalletMgr().createAccount("123456");
			OntTest.logger().print("第二个创建成功！");
			OntTest.sdk().getWalletMgr().createAccount("123456");
			OntTest.logger().print("第三个创建成功！");
			OntTest.logger().print("查询所有账号");
			
			List<Account> act = OntTest.sdk().getWalletMgr().getWallet().getAccounts();
			for(int i = 0; i < act.size(); i ++) {
				OntTest.logger().print(act.get(i).toString());
			}
			assertEquals(true, act.isEmpty()==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_051_getAccount() throws Exception {
		OntTest.logger().description("----------getAccount----------");
		
		try {
			OntTest.logger().print("1.创建账户");
			Account createaccinfo = OntTest.sdk().getWalletMgr().createAccount("051","123456");
			OntTest.logger().print(createaccinfo.toString());
			String address = createaccinfo.address;
			OntTest.logger().print("2.获取账号信息");
			Account acc = OntTest.sdk().getWalletMgr().getWallet().getAccount(address);
			OntTest.logger().print(acc.toString());
			assertEquals(true, acc.address.equals("")==false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_052_getAccount() throws Exception {
		OntTest.logger().description("----------getAccount----------");
		
		try {
			OntTest.logger().print("1.创建账户");
			Account createaccinfo = OntTest.sdk().getWalletMgr().createAccount("052","123456");
			OntTest.logger().print(createaccinfo.toString());
			String address = "Aa1TynaaMkeD2yVn1tjJ5RcxXTFd2CXFQ5";
			OntTest.logger().print("2.获取账号信息");
			Account acc = OntTest.sdk().getWalletMgr().getWallet().getAccount(address);
			OntTest.logger().print(acc.toString());
			
		}catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_abnormal_053_getAccount() throws Exception {
		OntTest.logger().description("----------getAccount----------");
		
		try {
			OntTest.logger().print("1.创建账户");
			Account createaccinfo = OntTest.sdk().getWalletMgr().createAccount("053","123456");
			OntTest.logger().print(createaccinfo.toString());
			String address = "Aa1TynKGMkeD2yVn1tjJ5RcxXTFd2CXFQ5123";
			OntTest.logger().print("2.获取账号信息");
			Account acc = OntTest.sdk().getWalletMgr().getWallet().getAccount(address);
			OntTest.logger().print(acc.toString());
			
		}catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_abnormal_054_getAccount() throws Exception {
		OntTest.logger().description("----------getAccount----------");
		
		try {
			OntTest.logger().print("1.创建账户");
			Account createaccinfo = OntTest.sdk().getWalletMgr().createAccount("054","123456");
			OntTest.logger().print(createaccinfo.toString());
			String address = "Aa1Ty!@#$%^&*()_+jJXTCX";
			OntTest.logger().print("2.获取账号信息");
			Account acc = OntTest.sdk().getWalletMgr().getWallet().getAccount(address);
			OntTest.logger().print(acc.toString());
			
		}catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_055_getAccount() throws Exception {
		OntTest.logger().description("----------getAccount----------");
		
		try {
			OntTest.logger().print("1.创建账户");
			Account createaccinfo = OntTest.sdk().getWalletMgr().createAccount("055","123456");
			OntTest.logger().print(createaccinfo.toString());
			String address = "";
			OntTest.logger().print("2.获取账号信息");
			Account acc = OntTest.sdk().getWalletMgr().getWallet().getAccount(address);
			OntTest.logger().print(acc.toString());
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_base_056_getDefaultAccount() throws Exception {
		OntTest.logger().description("----------getDefaultAccount----------");
		
		try {
			OntTest.logger().step("获取默认账户");
			Account acc = OntTest.sdk().getWalletMgr().getDefaultAccount();
			System.out.println(acc.address);
			OntTest.logger().print(acc.toString());
			
			assertEquals(true, OntTest.common().getAccount(0).getAddressU160().toBase58().equals(acc.address));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
}
