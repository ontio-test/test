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
			0x41, 0x58, 0x6d, 0x4b, 0x67, 0x48, 0x67, 0x55, 
			0x36, 0x64, 0x77, 0x73, 0x48, 0x4e, 0x45, 0x64, 
			0x57, 0x52, 0x65, 0x7a, 0x52, 0x38, 0x58, 0x6a, 
			0x32, 0x52, 0x31, 0x4b, 0x63, 0x6b, 0x44, 0x64, 
			0x57, 0x76};


        public static Object Main(string operation, object[] token, object[] args)
        {
            if (operation == "init") return init();
            
            
            if (operation == "contractB_Func_A")
            {
                if (!VerifyToken(operation, token)) return "Verify contractB's FuncA FAILED";

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

