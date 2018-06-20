using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using Neo.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;

namespace Example
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

    public class AppContract : SmartContract
    {
        public static readonly byte[] adminOntID = { 0x01, 0x02 };
        
        [Appcall("ff00000000000000000000000000000000000006")]
        public static extern byte[] AuthContract(string op, object[] args);

        [Appcall("ff00000000000000000000000000000000000001")]
        public static extern bool balanceOf(byte[] address);

        public static Object Main(string operation, object[] token, object[] args)
        {
            if (operation == "init") return init(args);
            if (operation == "method_A")
            {
                return method_A(args);
            }
            return false; 
        }

        public static bool method_A(object[] args)
        {
            byte[] address = (byte[])args[0];
            return balanceOf(address);
        }

        public static bool init(object[] args)
        {
            object[] _args = new object[1]; 
            initContractAdminParam param;
            param.adminOntID = (byte[]) args[0];
            _args[0] = Neo.SmartContract.Framework.Helper.Serialize(param);
            byte[] ret = AuthContract("initContractAdmin", _args);
            return ret[0] == 1;
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

