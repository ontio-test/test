using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using System;
using System.Numerics;

namespace NativeContract
{
    public class Contract1 : SmartContract
    {
        struct State
        {
            public byte[] From;
            public byte[] To;
        }

        struct ApproveParam
        {
            public byte[] From;
            public byte[] To;
            public int Amount;
        }
        
        public static Object Main(string operation, params object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };
            byte[] from = (byte[])args[0];
            byte[] to = (byte[])args[1];
            int amount =  (int)args[2];

            State param_1 = new State { From =  from, To = to };
            ApproveParam param_2 = new ApproveParam {From =  to, To = from, Amount = amount};
            Native.Invoke(0, address, "approve", param_2);
            return Native.Invoke(0, address, "allowance", param_1);
        }
    }
}