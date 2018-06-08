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
        public struct initContractAdminParam
        {
            public byte[] adminOntID;
        }
        
        public struct verifyTokenParam
        {
            public byte[] contractAddr;
            public byte[] caller;
            public byte[] fn;
            public int keyNo;
        }
        
        [Appcall("ff00000000000000000000000000000000000006")]
        public static extern byte[] AuthContract(string op, object[] args);

        public static object Main(string operation, params object[] args)
        {
            if (operation == "init")
            {
                return init(args);
            }

            if (operation == "A")
            {
                if (!verifyToken(operation, args)) return false;
                return A();
            }
            
            if (operation == "B")
            {
                if (!verifyToken(operation, args)) return false;
                return B();
            }

            if (operation == "C")
            {
                if (!verifyToken(operation, args)) return false;
                return C();
            }
            
            return false;
        }


        public static int A()
        {
            return 1 + 1;
        }

        public static int B()
        {
            return 1 + 2;
        }

        public static int C()
        {
            return 2 + 2;
        }
        
        public static int init(object[] args)
        {
            object[] _args = new object[1]; 

            initContractAdminParam param;
            param.adminOntID = (byte[]) args[0];

            _args[0] = Neo.SmartContract.Framework.Helper.Serialize(param);
            byte[] ret = AuthContract("initContractAdmin", _args);

            return ret[0];
        }
        
        public static bool verifyToken(string operation, object[] token)
        {
            object[] _args = new object[1];

            verifyTokenParam param;
            param.contractAddr = ExecutionEngine.ExecutingScriptHash;
            param.fn = operation.AsByteArray();
            param.caller = (byte[])token[0];
            param.keyNo = (int)token[1];

            _args[0] = param.Serialize();
            byte[] ret = AuthContract("verifyToken", _args);

            return ret[0] == 1;
        }

    }
}
