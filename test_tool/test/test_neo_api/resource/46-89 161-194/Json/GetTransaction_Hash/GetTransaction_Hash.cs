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
                case "GetTransaction_Hash":
                    return GetTransaction_Hash((byte[])args[0]);
                default:
                    return false;
            }
        }

        public static byte[] GetTransaction_Hash(byte[] txid)
        {
            Transaction tran = Blockchain.GetTransaction(txid);
            return tran.Hash;
        }
    }
}

Deploy contract:
  Contract Address:TMfUZxYQNar9DpDTgNxZSCTV9wS6ksgw9B
  TxHash:190e365ea8b35dd30a02a94dbc612c44fd2e6cfa5f26b594b179bd3075f83076

Tip:
  Using './ontology info status 190e365ea8b35dd30a02a94dbc612c44fd2e6cfa5f26b594b179bd3075f83076' to query transaction status


