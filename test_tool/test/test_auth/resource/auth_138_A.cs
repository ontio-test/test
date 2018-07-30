using Ont.SmartContract.Framework;
using Ont.SmartContract.Framework.Services.Ont;
using Ont.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;

namespace Ont.SmartContract
{
    public class AppContract : Framework.SmartContract
    {
        //  "77c526f7922789612a087aca4406125a50f484b5"
        [Appcall("77c526f7922789612a087aca4406125a50f484b5")]
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

