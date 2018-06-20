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
                case "GetHeader":
                    return GetHeader(args[0]);
                default:
                    return false;
            }
        }

        public static Header GetHeader(object height)
        {
            uint _height = (uint)height;
            return Blockchain.GetHeader(_height);
        }
    }
}

