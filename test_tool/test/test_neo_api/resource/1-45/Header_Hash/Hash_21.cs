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
                case "GetHeaderHash":
                    return GetHeaderHash(args[0]);
                default:
                    return false;
            }
        }

        public static byte[] GetHeaderHash(object height)
        {
            uint _height = (uint)height;
            Header header = Blockchain.GetHeader(_height);
            header.Hash = 123;
            return header.Hash;
        }
    }
}