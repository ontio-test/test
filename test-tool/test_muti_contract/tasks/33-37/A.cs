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
        [Appcall("7779864dd2a9a9d0e04c897656a009f6b0d1bae9")] //智能合约B的地址
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
				return "Invoke contractB's FuncA FAILED.";
			}
            return ret;
        }
    }
}

