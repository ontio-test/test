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
                case "GetTransaction_Type":
                    GetTransaction_Type((byte[])args[0]);
                    return true;
                default:
                    return false;
            }
        }

        public static byte GetTransaction_Type(byte[] txid)
        {
            Transaction tran = Blockchain.GetTransaction(txid);
            return tran.Type;
        }
    }
}


// Deploy contract:
//   Contract Address:TMiWQZRh6qkUpkCyhcNGxXPDKWkVJ6a6D9
//   TxHash:87af873c1fa8726810bb738d14d3d378baaf034a54102c7fb4075b84501269e9

// Tip:
//   Using './ontology info status 87af873c1fa8726810bb738d14d3d378baaf034a54102c7fb4075b84501269e9' to query transaction status

    
