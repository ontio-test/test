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
        public struct ApproveParam
        {
            public byte[] from;
            public byte[] to;
            public UInt64 amount;
        }

        public static object Main(string operation, params object[] args)
        {
            if (operation == "approve")
            {
                return approveInvoke(args);
            }
            

            return false;
        }

        public static byte[] approveInvoke(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2 };
            ApproveParam approveParam;
            approveParam.from = (byte[])args[0];
            approveParam.to = (byte[])args[1];
            approveParam.amount = (UInt64)args[2];
            
            object[] approveArgs = new object[1];
            approveArgs[0] = approveArgs.Serialize();
            
            byte[] ret = Native.Invoke(0, address, "approve", approveArgs);
            return ret;
        }


    }
}