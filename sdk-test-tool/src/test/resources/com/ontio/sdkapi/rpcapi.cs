using Ont.SmartContract.Framework;
using Ont.SmartContract.Framework.Services.Ont;
using Ont.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;


namespace Ont.SmartContract
{
    public class rpcapiTest : Framework.SmartContract
    {
        public static object Main(string operation, params object[] args)
        {
            
            switch (operation)
            {	
            	case "test":
	                byte[] key = (byte[]) args[0];
	                byte[] value = (byte[]) args[1];
	                PutStorge(Storage.CurrentContext, key, value);
	                return GetStorge(Storage.CurrentContext, key);
	            default:
                    return false;
            }
        }

        public static byte[] GetStorge(StorageContext context, byte[] key)
        {
            return Storage.Get(context, key);
        }

        public static void PutStorge(StorageContext context, byte[] key, byte[] value)
        {
            Storage.Put(context, key, value);
        }
    }
}