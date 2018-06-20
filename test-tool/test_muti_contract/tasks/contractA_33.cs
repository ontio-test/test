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
        [Appcall("80881676d7a87f5d9cd3d1656f819158584cc091")] //智能合约B的地址
        public static extern object ContractB(string op, object[] token, object[] args);

        public static object Main(string operation, object[] token)
        {
           if (operation == "contractA_Func_A")
           {
               return ContractA_Func_A(token);
           }
           return false;
        }

        public static object ContractA_Func_A(object[] token)
        {
            object ret = ContractB("contractB_Func_A", token, null);
            return ret;
        }

    }
}
/*
54c56b6c766b00527ac46c766b51527ac4616c766b00c310636f6e7472616374415f46756e635f41876c766b52527ac46c766b52c3641700616c766b51c3616521006c766b53527ac4620e00006c766b53527ac46203006c766b53c3616c756653c56b6c766b00527ac46110636f6e7472616374425f46756e635f416c766b00c3006152726791c04c585891816f65d1d39c5d7fa8d7761688806c766b51527ac46c766b51c36c766b52527ac46203006c766b52c3616c7566

 */

