using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using Neo.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;

namespace Neo.SmartContract
{
    public class BlockchainTest : Framework.SmartContract
    {
        public static object Main(string operation, params object[] args)
        {
            switch (operation)
            {
                case "GetTransaction":
                    return GetTransaction(args[0]);
                default:
                    return false;
            }
        }

        public static Transaction GetTransaction(object txid)
        {
            byte[] _txid = (byte[])txid;
            return Blockchain.GetTransaction(_txid);
        }
    }
}

