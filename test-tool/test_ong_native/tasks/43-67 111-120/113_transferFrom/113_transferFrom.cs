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
        public struct TransferFromParam
        {
            public byte[] sender;
            public byte[] from;
            public byte[] to;
            public UInt64 amount;
        }

        public static object Main(string operation, params object[] args)
        {
            if (operation == "transferFrom")
            {
                return transferFromInvoke(args);
            }
            

            return false;
        }

        public static byte[] transferFromInvoke(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2 };
            TransferFromParam transferFromParam;
            transferFromParam.from = (byte[])args[0];
            transferFromParam.to = (byte[])args[1];
            transferFromParam.amount = (UInt64)args[2];
            
            object[] transferFromArgs = new object[1];
            transferFromArgs[0] = transferFromArgs.Serialize();
            
            byte[] ret = Native.Invoke(0, address, "transferFrom", transferFromArgs);
            return ret;
        }


    }
}