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
                case "GetBlock":
                    return GetBlock(args[0]);
                default:
                    return false;
            }
        }

        public static Block GetBlock(object hash)
        {
            byte[] _hash = (byte[])hash;
            return Blockchain.GetBlock(_hash);
        }
    }
}