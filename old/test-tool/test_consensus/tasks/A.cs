using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using Neo.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;

namespace Example
{
  
    public class AppContract : SmartContract
    {
        struct State
        {
            public byte[] From;
            public byte[] To;
            public UInt64 Amount;
        }
        
        public struct StateSend
        {
            public byte[] Send;
            public byte[] From;
            public byte[] To;
            public UInt64 Amount;
        }
        public struct BalanceOfParam
        {
            public byte[] Address;
        }
        struct AllowenceParam
        {
            public byte[] From;
            public byte[] To;
        }
        
        public struct InitContractAdminParam
		{
			public byte[] adminOntID;
		}
		
		public struct VerifyTokenParam
		{
			public byte[] contractAddr;
			public byte[] caller;
			public string fn;
			public int keyNo;
		}
		
		//did:ont:
		//用户A 
		public static readonly byte[] mAdminOntID = { 
			0x64, 0x69, 0x64, 0x3a, 0x6f, 0x6e, 0x74, 0x3a,
			0x41 ,0x55 ,0x53 ,0x79 ,0x5a ,0x78 ,0x31 ,0x42 ,
			0x6f ,0x51 ,0x62 ,0x54 ,0x79 ,0x33 ,0x61 ,0x76 ,
			0x4d ,0x4b ,0x79 ,0x67 ,0x76 ,0x4a ,0x72 ,0x6b ,
			0x77 ,0x38 ,0x6d ,0x52 ,0x62 ,0x7a ,0x74 ,0x36 ,
			0x41 ,0x61};
        
        public static object Main(string operation, object[] token, object[] args)
        {
            if (operation == "init") return init();
            
            if (operation == "transfer")
            {
                return TransferInvoke(args);
            }
            if(operation == "approve")
            {
                return ApproveInvoke(args);
            }
            if(operation == "transferFrom")
            {   
                return TransferFromInvoke(args);
            }
            if(operation == "balanceOf")
            {
                return TransferFromInvoke(args);
            }
            if(operation == "allowence")
            {
                return TransferFromInvoke(args);
            }
            if (operation == "name")
            {
                return nameInvoke();
            }
            if (operation == "decimals")
            {
                return decimalsInvoke();
            }
            if (operation == "symbol")
            {
                return symbolInvoke();
            }
            if (operation == "totalSupply")
            {
                return totalSupplyInvoke();
            }
			if (operation == "put")
            {
				byte[] key = (byte[])args[0];
				byte[] value = (byte[])args[1];
                PutStorage(key, value);
                
                return true;
            }
			if (operation == "get")
            {
				byte[] key = (byte[])args[0];
                return GetStorage(key);
            }
			if (operation == "delete")
            {
				byte[] key = (byte[])args[0];
                DeleteStorage(key);
                return true;
            }
            
            if (operation == "auth_put")
            {
                if (!VerifyToken(operation, token)) return false;

                byte[] key = (byte[])args[0];
				byte[] value = (byte[])args[1];
                PutStorage(key, value);
                return true;
            }
            
            return false;
        }

        public static object init()
        {
			//must specify native contract's address in function scope
            byte[] authContractAddr = {
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x06 };
			
            InitContractAdminParam param = new InitContractAdminParam { adminOntID = mAdminOntID };
            byte[] ret = Native.Invoke(0, authContractAddr, "initContractAdmin", param);
            return ret[0] == 1;
        }

        public static bool VerifyToken(string operation, object[] token)
        {
			//must specify native contract's address in function scope
            byte[] authContractAddr = {
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x06 };
            VerifyTokenParam param = new VerifyTokenParam{}; 
            param.contractAddr = ExecutionEngine.ExecutingScriptHash;
            param.fn = operation;
            param.caller = (byte[])token[0];
            param.keyNo = (int)token[1];

            byte[] ret = Native.Invoke(0, authContractAddr, "verifyToken", param);
            return ret[0] == 1;
        }


        public static object TransferInvoke(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };            
			byte[] from = (byte[])args[0];
            byte[] to = (byte[])args[1];
            UInt64 amount = (UInt64)args[2];
            
            object[] param = new object[1];
            param[0] = new State { From = from, To = to, Amount = amount };
            
            return Native.Invoke(0, address, "transfer", param);
        }

        public static object ApproveInvoke(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };           
			byte[] from = (byte[])args[0];
            byte[] to = (byte[])args[1];
            UInt64 amount = (UInt64)args[2];
            
            object[] param = new object[1];
            param[0] = new State { From = from, To = to, Amount = amount };
            
            return Native.Invoke(0, address, "approve", param);
        }

        public static object TransferFromInvoke(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };           
			byte[] send = (byte[])args[0];
            byte[] from = (byte[])args[1];
            byte[] to = (byte[])args[2];
            UInt64 amount = (UInt64)args[3];
            
            object[] param = new object[1];
            param[0] = new StateSend { Send = send, From = from, To = to, Amount = amount };
            
            return Native.Invoke(0, address, "transferFrom", param);
        }
         public static byte[] nameInvoke()
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };           
			byte[] ret = Native.Invoke(0, address, "name", null);
            return ret;
        }
        public static byte[] symbolInvoke()
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };          
			byte[] ret = Native.Invoke(0, address, "symbol", null);
            return ret;
        }
        public static byte[] decimalsInvoke()
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };          
			byte[] ret = Native.Invoke(0, address, "decimals", null);
            return ret;
        }
         public static byte[] totalSupplyInvoke()
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };           
			byte[] ret = Native.Invoke(0, address, "totalSupply", null);
            return ret;
        }
        public static byte[] balanceInvoke(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };           
			byte[] add = (byte[])args[0];
            
            BalanceOfParam param = new BalanceOfParam {Address = add};
            
            byte[] ret = Native.Invoke(0, address, "balanceOf", param);
            return ret;
        }
        public static Object allowance(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };          
			byte[] from = (byte[])args[0];
            byte[] to = (byte[])args[1];

            AllowenceParam param_1 = new AllowenceParam { From =  from, To = to };
            return Native.Invoke(0, address, "allowance", param_1);
        }
		
		public static byte[] GetStorage(byte[] key)
        {
            return Storage.Get(Storage.CurrentContext, key);
        }

        public static void PutStorage(byte[] key, byte[] value)
        {
            Storage.Put(Storage.CurrentContext, key, value);
        }

        public static void DeleteStorage(byte[] key)
        {
            Storage.Delete(Storage.CurrentContext, key);
        }
    }
    }