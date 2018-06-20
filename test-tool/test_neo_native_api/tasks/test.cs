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
        struct State
        {
            public byte[] From;
            public byte[] To;
            public UInt64 Amount;
        }
        
        public struct StateSend
        {
            public byte[] Send;
            public byte[] From;
            public byte[] To;
            public UInt64 Amount;
        }

        public static object Main(string operation, params object[] args)
        {
            if (operation == "transfer")
            {
                return TransferInvoke(args);
            }
            
            if(operation == "approve")
            {
                return ApproveInvoke(args);
            }
            if(operation == "transferFrom")
            {
                return TransferFromInvoke(args);
            }

            return false;
        }

        public static object TransferInvoke(object[] args)
        {
            byte[] address = { 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };
            byte[] from = (byte[])args[0];
            byte[] to = (byte[])args[1];
            UInt64 amount = (UInt64)args[2];
            
            object[] param = new object[1];
            param[0] = new State { From = from, To = to, Amount = amount };
            
            return Native.Invoke(0, address, "transfer", param);
        }

        public static object ApproveInvoke(object[] args)
        {
            byte[] address = { 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };
            byte[] from = (byte[])args[0];
            byte[] to = (byte[])args[1];
            UInt64 amount = (UInt64)args[2];
            
            object[] param = new object[1];
            param[0] = new State { From = from, To = to, Amount = amount };
            
            return Native.Invoke(0, address, "approve", param);
        }

        public static object TransferFromInvoke(object[] args)
        {
            byte[] address = { 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };
            byte[] send = (byte[])args[0];
            byte[] from = (byte[])args[1];
            byte[] to = (byte[])args[2];
            UInt64 amount = (UInt64)args[3];
            
            object[] param = new object[1];
            param[0] = new StateSend { Send = send, From = from, To = to, Amount = amount };
            
            return Native.Invoke(0, address, "transferFrom", param);
        }

    }
}
