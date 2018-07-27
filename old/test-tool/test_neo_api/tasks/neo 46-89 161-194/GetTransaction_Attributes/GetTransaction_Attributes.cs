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
                case "GetTransaction_Attribute":
                    return GetTransaction_Attribute((byte[])args[0]);
                default:
                    return false;
            }
        }

        public static TransactionAttribute[] GetTransaction_Attribute(byte[] txid)
        {
            Transaction tran = Blockchain.GetTransaction(txid);
            TransactionAttribute[] attr = tran.GetAttributes(); 
            return attr;
        }
    }
}

Deploy contract:
  Contract Address:TMeQd5zpQZJXatzBD3gdC3CP5iX1LxoF3i
  TxHash:8ffdd390ce52253563169ab7bfae67fa6f279cb83a8d1b4d7ed4ba9e99541e41

Tip:
  Using './ontology info status 8ffdd390ce52253563169ab7bfae67fa6f279cb83a8d1b4d7ed4ba9e99541e41' to query transaction status


