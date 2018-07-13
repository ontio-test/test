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


        public static Object Main(string operation, object[] token, object[] args)
        {
            if (operation == "init") return init();
            
            
            if (operation == "contractB_Func_A")
            {
                if (!VerifyToken(operation, token)) return false;

                return contractB_Func_A(args);
            }

            return false; 
        }

        public static object contractB_Func_A(object[] args)
        {
            return "INVOKE contractB's FuncA SUCCESS";
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
    }
}

