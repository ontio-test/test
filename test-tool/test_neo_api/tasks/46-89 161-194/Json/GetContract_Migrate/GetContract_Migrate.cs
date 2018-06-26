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
                case "GetContract_Migrate":
                    return GetContract_Migrate((byte[])args[0],(bool)args[1],(string)args[2],(string)args[3],(string)args[4],(string)args[5],(string)args[6]);
                default:
                    return false;
            }
        }

        public static Contract GetContract_Migrate(byte[] script,bool flag, string name, string version, string author, string email, string desc)
        {
            Contract cre = Contract.Migrate(script,flag,name,version,author,email,desc);
            return cre;
        }
    }
}