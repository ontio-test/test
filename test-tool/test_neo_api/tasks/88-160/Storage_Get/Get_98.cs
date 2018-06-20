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
                case "Get":
                    byte[] key = (byte[]) args[0];
                    byte[] value = (byte[]) args[1];
                    PutStorge(Storage.CurrentContext, key, value);
                    DeleteStorge(Storage.CurrentContext, key);
                    return GetStorge(Storage.CurrentContext, key);

                default:
                    return false;
            }
        }
        
        public static void PutStorge(StorageContext context, byte[] key, byte[] value)
        {
            Storage.Put(context, key, value);
        }

        public static void DeleteStorge(StorageContext context, byte[] key)
        {
            Storage.Delete(context, key);
        }

        public static byte[] GetStorge(StorageContext context, byte[] key)
        {
            return Storage.Get(context, key);
        }
    }
}