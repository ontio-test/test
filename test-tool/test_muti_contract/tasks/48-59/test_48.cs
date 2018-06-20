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
        public static extern bool transferFrom(byte[] sender,byte[] from,byte[] to,UInt64 amount);

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
            byte[] sender = (byte[])args[0];
            byte[] from = (byte[])args[1];
            byte[] to = (byte[])args[2];
            UInt64 amount = (UInt64)args[3];
            return transferFrom(sender,from,to,amount);
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
/*
54c56b6c766b00527ac46c766b51527ac4616c766b00c310636f6e7472616374415f46756e635f41876c766b52527ac46c766b52c3641700616c766b51c3616521006c766b53527ac4620e00006c766b53527ac46203006c766b53c3616c756653c56b6c766b00527ac46110636f6e7472616374425f46756e635f416c766b00c3006152726791c04c585891816f65d1d39c5d7fa8d7761688806c766b51527ac46c766b51c36c766b52527ac46203006c766b52c3616c7566

 */

