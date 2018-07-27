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
                case "GetContract":
                    return GetContract(args[0]);
                default:
                    return false;
            }
        }

        public static byte[] GetContract(object script_hash)
        {
            byte[] _script_hash = (byte[])script_hash;
            Contract contract = Blockchain.GetContract(_script_hash);
            return contract.Script;
        }
    }
}
