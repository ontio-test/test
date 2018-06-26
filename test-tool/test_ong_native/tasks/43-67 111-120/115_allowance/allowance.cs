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
        public struct AllowanceParam
        {
            public byte[] from;
            public byte[] to;
        }

        public static object Main(string operation, params object[] args)
        {
            if (operation == "allowance")
            {
                return AllowanceInvoke(args);
            }
            

            return false;
        }

        public static byte[] AllowanceInvoke(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2 };
            AllowanceParam allowanceParam;
            allowanceParam.from = (byte[])args[0];
            allowanceParam.to = (byte[])args[1];
            
            object[] allowanceArgs = new object[1];
            allowanceArgs[0] = allowanceParam.Serialize();
            
            byte[] ret = Native.Invoke(0, address, "allowance", allowanceArgs);
            return ret;
        }


    }
}