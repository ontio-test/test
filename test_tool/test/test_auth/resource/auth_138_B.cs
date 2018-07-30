using Ont.SmartContract.Framework;
using Ont.SmartContract.Framework.Services.Ont;
using Ont.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;

namespace Ont.SmartContract
{
    struct initContractAdminParam
    {
        public byte[] AdminOntID;
    }
    
    struct verifyTokenParam
    {
        public byte[] ContractAddr;
        public byte[] Caller;
        public byte[] Fn;
        public int KeyNo;
    }

    public class AppContract : Framework.SmartContract
    {
        public static Object Main(string operation, object[] token, object[] args)
        {
            if (operation == "initContractAdmin") return InitContractAdmin(args);
            
            
            if (operation == "contractB_Func_A")
            {
                if (!VerifyToken(operation, token)) return false;

                return contractB_Func_A(args);
            }

            return false; 
        }

        public static bool contractB_Func_A(object[] args)
        {
            return true;
        }

        public static object InitContractAdmin(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            byte[] adminOntID = (byte[])args[0];
            object[] param = new object[1];
            param[0] = new initContractAdminParam { AdminOntID = adminOntID };
            
            return Native.Invoke(0, address, "initContractAdmin", param);
        }

        public static bool VerifyToken(string operation, object[] token)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            
            byte[] contractAddr = ExecutionEngine.ExecutingScriptHash;
            byte[] caller = (byte[])token[0];
            byte[] fn = operation.AsByteArray();
            int keyNo = (int)token[1];
            
            object[] param = new object[1];
            param[0] = new verifyTokenParam { ContractAddr = contractAddr, Caller = caller, Fn = fn, KeyNo = keyNo };
            byte[] res = Native.Invoke(0, address, "verifyToken", param);
            return true;
        }
    }
}

