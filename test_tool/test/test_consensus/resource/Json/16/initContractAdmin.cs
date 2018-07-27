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
        public struct initContractAdminParam
        {
            public byte[] adminOntID;
        }

        [Appcall("ff00000000000000000000000000000000000006")]//ScriptHash
        public static extern byte[] AuthContract(string op, object[] args);

        public static object Main(string operation, params object[] args)
        {
            byte[] key = (byte[]) args[0];
            
            if (operation == "init")
            {
                return init(args);
            }

             if (operation ==  "Put")
             { 
                byte[] value = (byte[]) args[1];
                PutStorge(Storage.CurrentContext, key, value);
                return GetStorge(Storage.CurrentContext, key);
             }

             if (operation ==  "Get")
             { 
                return GetStorge(Storage.CurrentContext, key);
             }

            return false;
        }

        public static bool init(object[] args)
        {
            object[] _args = new object[1]; 

            initContractAdminParam param;
            param.adminOntID = (byte[]) args[0];

            _args[0] = Neo.SmartContract.Framework.Helper.Serialize(param);
            byte[] ret = AuthContract("initContractAdmin", _args);

            return ret[0] == 1;
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
