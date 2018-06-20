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
        public static object Main(string operation)
        {
            if (operation == "decimals")
            {
                return decimalsInvoke();
            }
            

            return false;
        }

        public static byte[] decimalsInvoke()
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };
            byte[] ret = Native.Invoke(0, address, "decimals", null);
            return ret;
        }
    }
}