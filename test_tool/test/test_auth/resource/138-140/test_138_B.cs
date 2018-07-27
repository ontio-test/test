using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using Neo.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;

namespace Example
{
    struct initContractAdminParam
    {
        public byte[] AdminOntID;
    }
    
    struct VerifyTokenParam
    {
        public byte[] ContractAddr;
        public byte[] Caller;
        public string Fn;
        public int KeyNo;
    }

    public class AppContract : SmartContract
    {
        public static Object Main(string operation, object[] token, object[] args)
        {
            if (operation == "initContractAdmin") return init();
            
            
            if (operation == "contractB_Func_A")
            {
                if (!VerifyToken(operation, token)) return "1";

                return contractB_Func_A(args);
            }

            return false; 
        }

        public static bool contractB_Func_A(object[] args)
        {
            return true;
        }

        public static readonly byte[] mAdminOntID = { 
                0x64, 0x69, 0x64, 0x3a, 0x6f, 0x6e, 0x74, 0x3a,
				0x41, 0x4b, 0x37, 0x77, 0x7a, 0x6d, 0x6b, 0x64, 
                0x67, 0x6a, 0x4b, 0x78, 0x62, 0x58, 0x41, 0x4a, 
                0x42, 0x69, 0x61, 0x57, 0x39, 0x31, 0x59, 0x68, 
                0x55, 0x6f, 0x6b, 0x54, 0x75, 0x39, 0x70, 0x61, 
                0x35, 0x58};
        public static object init()
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            initContractAdminParam param = new initContractAdminParam { AdminOntID = mAdminOntID };
            byte[] ret = Native.Invoke(0, address, "initContractAdmin", param);
            return ret[0] == 1;
        }

        public static bool VerifyToken(string operation, object[] token)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            
            VerifyTokenParam param = new VerifyTokenParam{}; 
            param.ContractAddr = ExecutionEngine.ExecutingScriptHash;
            param.Fn = operation;
            param.Caller = (byte[])token[0];
            param.KeyNo = (int)token[1];

            byte[] ret = Native.Invoke(0, address, "verifyToken", param);
            return ret[0] == 1;
        }
    }
}

