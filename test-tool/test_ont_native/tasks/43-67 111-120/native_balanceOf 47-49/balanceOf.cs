using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using System;
using System.Numerics;

namespace Example
{
  
    public class AppContract : SmartContract
    {
        public struct BalanceOfParam
        {
            public byte[] Address;
        }

        public static Object Main(string operation, params object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };
            byte[] add = (byte[])args[0];
            
            BalanceOfParam param = new BalanceOfParam {Address = add};
            
            byte[] ret = Native.Invoke(0, address, "balanceOf", param);
            return ret;
        }

    }
}