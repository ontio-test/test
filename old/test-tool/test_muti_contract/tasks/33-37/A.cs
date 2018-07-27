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
        [Appcall("a836bac33389c60c22591030248016a8a7f008da")] //智能合约B的地址
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
			if ((bool)ret == false) {
				return false;
			}
            return ret;
        }
    }
}

