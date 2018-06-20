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
        public struct TransferParam
        {
            public byte[] from;
            public byte[] to;
            public UInt64 amount;
        }

        public static object Main(string operation, params object[] args)
        {
            if (operation == "transfer")
            {
                return transferInvoke(args);
            }
            

            return false;
        }

        public static byte[] transferInvoke(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };
            
            byte[] From = (byte[])args[0];
            byte[] To = (byte[])args[1];
            UInt64 Amount = (UInt64)args[2];
            
            TransferParam param = new TransferParam{from = From, to = To, amount = Amount};
            
            byte[] ret = Native.Invoke(0, address, "transfer", param);
            return ret;
        }


    }
}