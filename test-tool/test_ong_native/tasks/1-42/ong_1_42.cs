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
            public int Amount;
        }
        
        public struct StateSend
        {
            public byte[] Send;
            public byte[] From;
            public byte[] To;
            public int Amount;
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

        public static bool TransferInvoke(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };
            byte[] from = (byte[])args[0];
            byte[] to = (byte[])args[1];
            int amount = (int)args[2];
            
            object[] param = new object[1];
            param[0] = new State { From = from, To = to, Amount = amount };
            byte[] res = Native.Invoke(0, address, "transfer", param);
            return res[0] == 1;
        }

        public static bool ApproveInvoke(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };
            byte[] from = (byte[])args[0];
            byte[] to = (byte[])args[1];
            int amount = (int)args[2];
            
            State state = new State { From = from, To = to, Amount = amount };
            
            byte[] res = Native.Invoke(0, address, "approve", state);
            return res[0] == 1;
        }

        public static bool TransferFromInvoke(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };
            byte[] send = (byte[])args[0];
            byte[] from = (byte[])args[1];
            byte[] to = (byte[])args[2];
            int amount = (int)args[3];

            StateSend stateSend = new StateSend { Send = send, From = from, To = to, Amount = amount };
            
            byte[] res = Native.Invoke(0, address, "transferFrom", stateSend);
            return res[0] == 1;
        }

    }
}
