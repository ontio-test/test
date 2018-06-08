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

        public static Object Main(string operation, object[] token, object[] args)
        {
            if (operation == "init") return init(args);
            
            
            if (operation == "contractB_Func_A")
            {
                if (!verifyToken(operation, token)) return "Verify token fail";

                return contractB_Func_A(args);
            }

            return false; 
        }

        public static string contractB_Func_A(object[] args)
        {
            return "CntractB_Func_A invoke success";
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
57c56b6c766b00527ac46c766b51527ac46c766b52527ac4616c766b00c304696e6974876c766b53527ac46c766b53c36416006c766b52c36165d4006c766b54527ac46284006c766b00c310636f6e7472616374425f46756e635f41876c766b55527ac46c766b55c3645300616c766b00c36c766b51c3617c652d01009c6c766b56527ac46c766b56c3641f001156657269667920746f6b656e206661696c6c766b54527ac46221006c766b52c3616521006c766b54527ac4620e00006c766b54527ac46203006c766b54c3616c756652c56b6c766b00527ac4611e436e7472616374425f46756e635f4120696e766f6b6520737563636573736c766b51527ac46203006c766b51c3616c756655c56b6c766b00527ac46151c56c766b51527ac46c766b52c36c766b00c300c3007cc46c766b51c3006c766b52c36168154e656f2e52756e74696d652e53657269616c697a65c411696e6974436f6e747261637441646d696e6c766b51c3617c6706000000000000000000000000000000000000ff6c766b53527ac46c766b53c300517f519c6c766b54527ac46203006c766b54c3616c756656c56b6c766b00527ac46c766b51527ac46151c56c766b52527ac46c766b53c361682d53797374656d2e457865637574696f6e456e67696e652e476574457865637574696e6753637269707448617368007cc46c766b53c36c766b00c3527cc46c766b53c36c766b51c300c3517cc46c766b53c36c766b51c351c3537cc46c766b52c3006c766b53c36168154e656f2e52756e74696d652e53657269616c697a65c40b766572696679546f6b656e6c766b52c3617c6706000000000000000000000000000000000000ff6c766b54527ac46c766b54c300517f519c6c766b55527ac46203006c766b55c3616c7566
 */