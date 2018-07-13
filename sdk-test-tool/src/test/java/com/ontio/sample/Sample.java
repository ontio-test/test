package com.ontio.sample;
 
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Base64;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.junit.*;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.annotation.JSONField;
import com.github.ontio.OntSdk;
import com.github.ontio.account.Account;
import com.github.ontio.common.Address;
import com.github.ontio.common.Helper;
import com.github.ontio.core.asset.State;
import com.github.ontio.core.transaction.Transaction;
import com.github.ontio.network.exception.RpcException;
import com.github.ontio.smartcontract.neovm.abi.AbiFunction;
import com.github.ontio.smartcontract.neovm.abi.AbiInfo;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;
import com.ontio.testtool.api.ContractApi;
import com.ontio.testtool.utils.*;


class UserAcct{
    String id;
    String address;
    String withdrawAddr;
    byte[] privkey;
    BigInteger ontBalance;
    BigInteger ongBalance;
    BigInteger nep5Balance;
}

class Balance{
    @JSONField(name="ont")
    String ont;
    @JSONField(name="ong")
    String ong;

    public String getOnt() {
        return ont;
    }

    public void setOnt(String ont) {
        this.ont = ont;
    }

    public String getOng() {
        return ong;
    }

    public void setOng(String ong) {
        this.ong = ong;
    }
}

class States{
    @JSONField(name="States")
    Object[] states;

    @JSONField(name="ContractAddress")
    String contractAddress;

    public Object[] getStates() {
        return states;
    }

    public void setStates(Object[] states) {
        this.states = states;
    }

    public String getContractAddress() {
        return contractAddress;
    }

    public void setContractAddress(String contractAddress) {
        this.contractAddress = contractAddress;
    }
}

class Event{
    @JSONField(name="GasConsumed")
    int gasConsumed;

    @JSONField(name="TxHash")
    String txHash;

    @JSONField(name="State")
    int state;

    @JSONField(name="Notify")
    States[] notify;

    public int getGasConsumed() {
        return gasConsumed;
    }

    public void setGasConsumed(int gasConsumed) {
        this.gasConsumed = gasConsumed;
    }


    public String getTxHash() {
        return txHash;
    }

    public void setTxHash(String txHash) {
        this.txHash = txHash;
    }

    public int getState() {
        return state;
    }

    public void setState(int state) {
        this.state = state;
    }

    public States[] getNotify() {
        return notify;
    }

    public void setNotify(States[] notify) {
        this.notify = notify;
    }
}

public class Sample {
	@Rule public OntTestWatcher watchman= new OntTestWatcher();
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
		//OntTest.node().restartAll("ontology", "config.json", Config.DEFAULT_NODE_ARGS);
		//Thread.sleep(5000);
	}
	
	@Before
	public void setUp() throws Exception {
	}
	
	@After
	public void TearDown() throws Exception {
		System.out.println("TearDown");
	}
	
	/************************************************************************/
	@Test
	public void testSample1() throws Exception {
		OntTest.logger().description("合约开发-CLI 部署及调用");
		try {
			OntTest.bindNode(7);
			OntTest.logger().step("开启一个同步节点");
			OntTest.logger().step("在中间开始继续同步区块，并同步到最新区块");
			OntTest.logger().step("开启节点REST服务");
			OntTest.logger().step("开启 --testmode");
			OntTest.node().restart(7, "ontology", "config.json", "--testmode");
			Thread.sleep(6000);
			
			OntTest.logger().step("分配ONG给默认账户");
			Account defaultAccount = ContractApi.getDefaultAccount();
            State st = new State(defaultAccount.getAddressU160(),defaultAccount.getAddressU160(),100000L);
            Transaction tx = OntTest.sdk().nativevm().ont().makeTransfer(new State[]{st}, defaultAccount.getAddressU160().toBase58(), 30000, 0);
            OntTest.sdk().addSign(tx,defaultAccount);
            OntTest.sdk().addSign(tx, defaultAccount);
            OntTest.sdk().getConnect().sendRawTransaction(tx.toHexString());
            String txhash = tx.hash().toHexString();
            OntTest.logger().print("++++ txhash :"+txhash);
            Object event = OntTest.sdk().getConnect().getMemPoolTxState(txhash);
            OntTest.logger().print(event.toString());
			
			OntTest.logger().step("部署合约。。。");
			Map contractState = ContractApi.deployContract("resources/neo/sample.cs", null);
			
			OntTest.logger().step("调用合约方法。。。");
			AbiInfo abiinfo = JSON.parseObject((String)contractState.get("abi"), AbiInfo.class);
            AbiFunction func = abiinfo.getFunction("Main");
            OntTest.logger().print(func.toString());
            func.name = "Main";
            func.setParamsValue("Hello11", null);
            Object obj = OntTest.sdk().neovm().sendTransaction((String)contractState.get("address"), ContractApi.getDefaultAccount(), ContractApi.getDefaultAccount(), OntTest.sdk().DEFAULT_GAS_LIMIT, 0, func, true);
            OntTest.logger().print("1111111111111: " + obj);
			
			OntTest.logger().step("网络切换到主网，并打开rest服务，完成同步");
			OntTest.node().restart(7, "ontology", "config.json", Config.DEFAULT_NODE_ARGS);
			Thread.sleep(5000);
			while(true) {
				Thread.sleep(1000);
				OntTest.bindNode(7);
				int height = OntTest.sdk().getConnect().getBlockHeight();
				OntTest.bindNode(0);
				int height2 = OntTest.sdk().getConnect().getBlockHeight();
				if (height == height2) {
					break;
				} else {
					OntTest.logger().print("wait sync block:" + height + " to " + height2);
				}
			}
			OntTest.bindNode(7);
			Map contractState2 = ContractApi.deployContract("resources/neo/sample.cs", null);
			AbiInfo abiinfo2 = JSON.parseObject((String)contractState2.get("abi"), AbiInfo.class);
            AbiFunction func2 = abiinfo.getFunction("Hello");
            OntTest.logger().print(func.toString());
            func.setParamsValue("hello success");
            Object obj2 = OntTest.sdk().neovm().sendTransaction((String)contractState2.get("address"), ContractApi.getDefaultAccount(), ContractApi.getDefaultAccount(), 0, 0, func, true);
            OntTest.logger().print((String)obj);
			
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void testSample2() throws Exception {
        //simulate a database using hashmap     
		OntTest.bindNode(6);
        final HashMap<String,UserAcct> database = new HashMap<String,UserAcct>();
        final OntSdk ontSdk = OntTest.sdk();
        final Account initAccount = ContractApi.getDefaultAccount();
        final Account feeAct = initAccount;
        final String FEE_PROVIDER = feeAct.getAddressU160().toBase58();
		final String INIT_ACCT_ADDR = initAccount.getAddressU160().toBase58();
		final String ONT_NATIVE_ADDRESS = Helper.reverse(ontSdk.nativevm().ont().getContractAddress());
		final String ONG_NATIVE_ADDRESS = Helper.reverse(ontSdk.nativevm().ong().getContractAddress());
		final BigInteger ONT_NUM = BigInteger.valueOf(1000);//充值金额
		OntTest.bindNode(7);
		final Account mainAccount = ContractApi.getDefaultAccount();
		final Address mainAccountAddr = mainAccount.getAddressU160();
        Account withdrawAcct1 = new Account(ontSdk.defaultSignScheme);
		final String WITHDRAW_ADDRESS = withdrawAcct1.getAddressU160().toBase58();

		OntTest.logger().description("交易所应用");
		try {
			OntTest.logger().step("启动交易所节点");
			OntTest.node().restart(7, "ontology", "config.json", Config.DEFAULT_NODE_ARGS);
			Thread.sleep(5000);
			while(true) {
				Thread.sleep(1000);
				OntTest.bindNode(7);
				int height = OntTest.sdk().getConnect().getBlockHeight();
				OntTest.bindNode(6);
				int height2 = OntTest.sdk().getConnect().getBlockHeight();
				if (height == height2) {
					break;
				} else {
					OntTest.logger().print("wait sync block:" + height + " to " + height2);
				}
			}
			OntTest.logger().step("给交易所转账");
			
	        //NEP5_NEOVM_ADDRESS = "";
			OntTest.logger().step("starting simulate exchange process ...");
			OntTest.logger().step("create a random account for user");
	        String id1 = "id1";
	        Account acct1 = new Account(ontSdk.defaultSignScheme);
	        String pubkey =  acct1.getAddressU160().toBase58();
	        byte[] privkey = acct1.serializePrivateKey();
	        OntTest.logger().print("random account address is " + acct1.getAddressU160().toBase58());
	       
	        UserAcct usr = new UserAcct();
	        usr.id = id1;
	        usr.privkey = privkey;
	        usr.address = pubkey;
	        usr.ontBalance = BigInteger.valueOf(0);
	        usr.ongBalance = BigInteger.valueOf(0);
	        usr.withdrawAddr = WITHDRAW_ADDRESS;
	        database.put(acct1.getAddressU160().toBase58(),usr);
	        //all transfer fee is provide from this account

	        //create a multi-sig account as a main account
	        //Account mutiSeedAct1 = ontSdk.getWalletMgr().getAccount(MUTI_SIG_ACCT_SEED1_ADDR,PWD,Base64.getDecoder().decode(MUTI_SIG_ACCT_SEED1_SALT));
	        //Account mutiSeedAct2 = ontSdk.getWalletMgr().getAccount(MUTI_SIG_ACCT_SEED2_ADDR,PWD,Base64.getDecoder().decode(MUTI_SIG_ACCT_SEED2_SALT));
	        //Account mutiSeedAct3 = ontSdk.getWalletMgr().getAccount(MUTI_SIG_ACCT_SEED3_ADDR,PWD,Base64.getDecoder().decode(MUTI_SIG_ACCT_SEED3_SALT));
	        //Address.addressFromMultiPubKeys(3,mutiSeedAct1.serializePublicKey(),mutiSeedAct2.serializePublicKey(),mutiSeedAct3.serializePublicKey());
	        OntTest.logger().print("++++ Main Account Address is :" + mainAccountAddr.toBase58());
	        //monitor the charge and withdraw thread
	        Thread t = new Thread(new Runnable() {
	            long lastblocknum = 0 ;
	            @Override
	            public void run() {
	                while(true){
	                    try{
	                        //get latest blocknum:
	                        //TODO fix lost block
	                        int height = ontSdk.getConnect().getBlockHeight() - 1;
	                        OntTest.logger().print("height: " + height);
	                        OntTest.logger().print("lastblocknum: " + lastblocknum);
	                        if (height > lastblocknum){	
	                            Object event = ontSdk.getConnect().getSmartCodeEvent(height);
	                            if(event == null){
	                                lastblocknum = height;
	                                Thread.sleep(1000);
	                                continue;
	                            }	
	                            List<Event> events = JSON.parseArray(event.toString(), Event.class);
	                            if(events == null){
	                                lastblocknum = height;
	                                Thread.sleep(1000);
	                                continue;
	                            }
	                            if (events.size()> 0){
	                                for(Event ev:events){
	                                    OntTest.logger().print("===== State:" + ev.getState());
	                                    OntTest.logger().print("===== TxHash:" + ev.getTxHash());
	                                    OntTest.logger().print("===== GasConsumed:" + ev.getGasConsumed());
	
	                                    for(States state:ev.notify){
	
	                                        OntTest.logger().print("===== Notify - ContractAddress:" + state.getContractAddress());
	                                        OntTest.logger().print("===== Notify - States[0]:" + state.getStates()[0]);
	                                        OntTest.logger().print("===== Notify - States[1]:" + state.getStates()[1]);
	                                        OntTest.logger().print("===== Notify - States[2]:" + state.getStates()[2]);
	                                        OntTest.logger().print("===== Notify - States[3]:" + state.getStates()[3]);
	
	                                        if (ev.getState() == 1){  //exec succeed
	                                            Set<String> keys = database.keySet();
	                                            //
	                                            if ("transfer".equals(state.getStates()[0]) && keys.contains(state.getStates()[2])) {
	                                                BigInteger amount = new BigInteger(state.getStates()[3].toString());
	                                                if (ONT_NATIVE_ADDRESS.equals(state.getContractAddress())){
	                                                    OntTest.logger().print("===== charge ONT :"+state.getStates()[2] +" ,amount:"+amount);
	                                                    database.get(state.getStates()[2]).ontBalance = amount.add(database.get(state.getStates()[2]).ontBalance);
	                                                    assertEquals(ONT_NUM, amount);
	                                                } else {
	                                                    OntTest.logger().print("unkonw address: " + state.getContractAddress());
	                                                }
	                                            }
	
	                                            //withdraw case
	                                            if("transfer".equals(state.getStates()[0]) && mainAccountAddr.toBase58().equals(state.getStates()[1])){
	                                                for(UserAcct ua: database.values()){
	                                                    if (ua.withdrawAddr.equals((state.getStates()[2]))){
	                                                        BigInteger amount = new BigInteger(state.getStates()[3].toString());
	                                                        if (ONT_NATIVE_ADDRESS.equals(state.getContractAddress())){
	                                                            OntTest.logger().print("===== widtdraw "+ amount +" ont to " + ua.withdrawAddr + " confirmed!");
	                                                            assertEquals(ONT_NUM, amount);
	                                                        }
	                                                    }
	                                                }
	                                            }
	                                        }
	                                    }
	                                }
	                            }
	
	                            lastblocknum = height;
	                        }
	                        Thread.sleep(1000);
	
	                    }catch(Exception e){
	                        OntTest.logger().print("exception 1:"+ e.getMessage());
	                    }
	                }
	            }
	        });
	
	        //monitor the collect
	        Thread t2 = new Thread(new Runnable() {
	            @Override
	            public void run() {
	                try{
	                    while (true){
	                        Set<String> keys = database.keySet();
	                        List<Account> ontAccts = new ArrayList<Account>() ;
	                        List<State> ontStates = new ArrayList<State>();
	                        List<Account> ongAccts = new ArrayList<Account>() ;
	                        List<State> ongStates = new ArrayList<State>();
	                        for(String key:keys){
	                            Object balance = ontSdk.getConnect().getBalance(key);
	                            Balance b = JSON.parseObject(balance.toString(),Balance.class);
	                            BigInteger ontbalance = new BigInteger(b.ont);
	                            BigInteger ongbalance = new BigInteger(b.ong);
	                            if (ontbalance.compareTo(new BigInteger("0")) > 0){
	                                //transfer ont to main wallet
	                                UserAcct ua = database.get(key);
	                                Account acct = new Account(ua.privkey,ontSdk.defaultSignScheme);
	                                ontAccts.add(acct);
	                                State st = new State(Address.addressFromPubKey(acct.serializePublicKey()),mainAccountAddr,ua.ontBalance.longValue());
	                                ontStates.add(st);
	                            }
	                        }
	
	                        //construct ont transfer tx
	                        if (ontStates.size() > 0) {
	                            OntTest.logger().print("----- Will collect ont to main wallet");
	                            Transaction ontTx = ontSdk.nativevm().ont().makeTransfer(ontStates.toArray(new State[ontStates.size()]), FEE_PROVIDER, 30000, 0);
	                            for (Account act : ontAccts) {
	                                ontSdk.addSign(ontTx, act);
	                            }
	                            //add fee provider account sig
	                            ontSdk.addSign(ontTx, feeAct);
	                            ontSdk.getConnect().sendRawTransaction(ontTx.toHexString());
	                        }

	                        Thread.sleep(10000);
	                    }
	                }catch (Exception e){
	                    e.printStackTrace();
	                    OntTest.logger().print("exception 2:"+e.getMessage());
	                }
	
	            }
	        });
	
	        t.start();
	        t2.start();
	
	        Thread.sleep(2000);
	        OntTest.logger().step("charge some ont to acct1 from init account");
	        State st = new State(initAccount.getAddressU160(),acct1.getAddressU160(),1000L);
	        Transaction tx = ontSdk.nativevm().ont().makeTransfer(new State[]{st}, FEE_PROVIDER, 30000, 0);
	        ontSdk.addSign(tx, initAccount);
	        ontSdk.addSign(tx, feeAct);
	        ontSdk.getConnect().sendRawTransaction(tx.toHexString());
	        String txhash = tx.hash().toHexString();
	        OntTest.logger().print("++++ txhash :"+txhash);
	        Object event = ontSdk.getConnect().getMemPoolTxState(txhash);
	        OntTest.logger().print(event.toString());
	        Thread.sleep(5000);

	       
	        //simulate a withdraw
	        //todo must add check the user balance of database
	        OntTest.logger().step("withdraw 1000 onts to " + usr.withdrawAddr );
	        //reduce the withdraw amount first
	        BigInteger wdAmount = new BigInteger("1000");
	        if(usr.ontBalance.compareTo(wdAmount) > 0) {
	            database.get(usr.address).ontBalance = database.get(usr.address).ontBalance.subtract(wdAmount);
	            OntTest.logger().print("++++  " + usr.address + " ont balance : " + database.get(usr.address).ontBalance);
	            State wdSt = new State(mainAccountAddr, Address.decodeBase58(usr.withdrawAddr), 500);
	            Transaction wdTx = ontSdk.nativevm().ont().makeTransfer(new State[]{wdSt}, FEE_PROVIDER, 30000, 0);
	            //ontSdk.addMultiSign(wdTx, 3, new byte[][]{mutiSeedAct1.serializePublicKey(),mutiSeedAct2.serializePublicKey(),mutiSeedAct3.serializePublicKey()},mutiSeedAct1);
	            //ontSdk.addMultiSign(wdTx, 3, new byte[][]{mutiSeedAct1.serializePublicKey(),mutiSeedAct2.serializePublicKey(),mutiSeedAct3.serializePublicKey()},mutiSeedAct2);
	            //ontSdk.addMultiSign(wdTx, 3, new byte[][]{mutiSeedAct1.serializePublicKey(),mutiSeedAct2.serializePublicKey(),mutiSeedAct3.serializePublicKey()},mutiSeedAct3);
	            ontSdk.addSign(wdTx, feeAct);
	            ontSdk.getConnect().sendRawTransaction(wdTx.toHexString());
	        }
	
	        Thread.sleep(15000);
		} catch(RpcException e) {
			if (e.code == 40001) {
				OntTest.logger().print("do something");
			} else {
				OntTest.logger().error(e.toString());
			}
			fail();
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
}
     
