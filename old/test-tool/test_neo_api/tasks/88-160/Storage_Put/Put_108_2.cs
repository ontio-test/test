using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using Neo.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;

namespace Neo.SmartContract
{
    public class Domain : Framework.SmartContract
    {
        public static object Main(string operation, params object[] args)
        {
            switch (operation)
            {
                case "Put":
                    byte[] key = (byte[]) args[0];
                    byte[] value_1 = (byte[]) args[1];
                    byte[] value_2 = (byte[]) args[2];
                    PutStorge(Storage.CurrentContext, key, value_1);
                    return GetStorge(Storage.CurrentContext, key);

                default:
                    return false;
            }
        }
        
        public static void PutStorge(StorageContext context, byte[] key, byte[] value)
        {
            Storage.Put(context, key, value);
        }

        public static byte[] GetStorge(StorageContext context, byte[] key)
        {
            return Storage.Get(context, key);
        }
    }
}