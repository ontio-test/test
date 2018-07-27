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
        public static object Main(string operation, object[] token, object[] args)
        {
			if (operation == "put")
            {
				byte[] key = (byte[])args[0];
				byte[] value = (byte[])args[1];
                PutStorage(key, value);
                
                return true;
            }
			if (operation == "get")
            {
				byte[] key = (byte[])args[0];
                return GetStorage(key);
            }
            
            return false;
        }
		
		public static byte[] GetStorage(byte[] key)
        {
            return Storage.Get(Storage.CurrentContext, key);
        }

        public static void PutStorage(byte[] key, byte[] value)
        {
            Storage.Put(Storage.CurrentContext, key, value);
        }

        public static void DeleteStorage(byte[] key)
        {
            Storage.Delete(Storage.CurrentContext, key);
        }
    }
    }