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
            public uint64 amount;
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
            TransferParam transferParam;
            transferParam.from = (byte[])args[0];
            transferParam.to = (byte[])args[1];
            transferParam.amount = (uint64)args[2];
            
            object[] transferArgs = new object[1];
            transferArgs[0] = transferArgs.Serialize();
            
            byte[] ret = Native.Invoke(0, address, "transfer", transferArgs);
            return ret;
        }


    }
}