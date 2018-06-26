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
        struct initContractAdminParam
        {
            public byte[] AdminOntID;
        }

        //did:ont:
		 public static readonly byte[] mAdminOntID = { 
                };

        public static object Main(string operation, object[] token, params object[] args)
        {
            if (operation == "initContractAdmin")
            {
                return InitContractAdmin(args);
            }
    
            return "111";
        }

        public static object InitContractAdmin(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            object[] param = new object[1];
            param[0] = new initContractAdminParam { AdminOntID = mAdminOntID };
            
            return Native.Invoke(0, address, "initContractAdmin", param);
        }

    }
}
