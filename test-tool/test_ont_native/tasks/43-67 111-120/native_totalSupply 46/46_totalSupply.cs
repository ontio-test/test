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
            if (operation == "totalSupply")
            {
                return totalSupplyInvoke();
            }
            

            return false;
        }

        public static byte[] totalSupplyInvoke()
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };
            byte[] ret = Native.Invoke(0, address, "totalSupply", null);
            return ret;
        }
    }
}