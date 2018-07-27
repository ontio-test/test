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
                case "GetContract_Create":
                    return GetContract_Create((byte[])args[0],(bool)args[1],(string)args[2],(string)args[3],(string)args[4],(string)args[5],(string)args[6]);
                default:
                    return false;
            }
        }

        public static Contract GetContract_Create(byte[] script,bool flag, string name, string version, string author, string email, string desc)
        {
            Contract cre = Contract.Create(script,flag,name,version,author,email,desc);
            return cre;
        }
    }
}

Deploy contract:
  Contract Address:80c7a32949f61d2e719f72d03041f1dd81e5d1c0
  TxHash:3e506179cb940bcab62004ee154b372f94c8c9251aaf183af091eda50a80b250

Tip:
  Using './ontology info status 3e506179cb940bcab62004ee154b372f94c8c9251aaf183af091eda50a80b250' to query transaction status
