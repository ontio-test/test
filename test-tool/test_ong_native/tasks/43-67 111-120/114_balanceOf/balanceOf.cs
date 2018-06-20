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
        public struct BalanceOfParam
        {
            public byte[] address;
        }

        public static object Main(string operation, params object[] args)
        {
            if (operation == "balanceOf")
            {
                return BalanceOfInvoke(args);
            }
            

            return false;
        }

        public static byte[] BalanceOfInvoke(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };
            BalanceOfParam balanceOfParam;
            balanceOfParam.address = (byte[])args[0];
            
            object[] balanceOfArgs = new object[1];
            balanceOfArgs[0] = balanceOfParam.Serialize();
            
            byte[] ret = Native.Invoke(0, address, "balanceOf", balanceOfArgs);
            return ret;
        }


    }
}