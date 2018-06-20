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

        public static object Main(string operation, object[] token, params object[] args)
        {
            if (operation == "initContractAdmin")
            {
                return InitContractAdmin(args);
            }

            if (operation == "A")
            {
                //we need to check if the caller is authorized to invoke foo
                if (!VerifyToken(operation, token)) return false;

                return A();
            }

            if (operation == "B")
            {
                //we need to check if the caller is authorized to invoke foo
                if (!VerifyToken(operation, token)) return false;

                return B();
            }
    
            return "111";
        }

        public static object A()
        {
            return "A";
        }

        public static object B()
        {
            return "B";
        }

        
        public static bool InitContractAdmin(object[] args)
        {
            byte[] address = { 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            byte[] adminOntID = (byte[])args[0];
            object[] param = new object[1];
            param[0] = new initContractAdminParam { AdminOntID = adminOntID };
            byte[] res = Native.Invoke(0, address, "initContractAdmin", param);
            return res[0] == 1;
        }

        public static bool VerifyToken(string operation, object[] token)
        {
            byte[] address = { 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            
            byte[] contractAddr = ExecutionEngine.ExecutingScriptHash;
            byte[] caller = (byte[])token[0];
            byte[] fn = operation.AsByteArray();
            int keyNo = (int)token[1];
            
            object[] param = new object[1];
            param[0] = new verifyTokenParam { ContractAddr = contractAddr, Caller = caller, Fn = fn, KeyNo = keyNo };
            byte[] res = Native.Invoke(0, address, "verifyToken", param);
            return res[0] == 1;
        }

    }
}
