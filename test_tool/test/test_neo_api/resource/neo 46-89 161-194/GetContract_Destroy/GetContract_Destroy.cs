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
                case "GetContract_Destroy":
                    return GetContract_Destroy();
                default:
                    return false;
            }
        }

        public static bool GetContract_Destroy()
        {
             Contract.Destroy();
             return true;
        }
    }
}

Deploy contract:
  Contract Address:TMgPvAHwESBWdNH2bfqotSU2uTsgrrCjtZ
  TxHash:8f05cd9147dbf17725ed98e3450a5357b8ab419c95531db3abf12fb17d2eee7f

Tip:
  Using './ontology info status 8f05cd9147dbf17725ed98e3450a5357b8ab419c95531db3abf12fb17d2eee7f' to query transaction status
