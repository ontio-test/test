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
                case "GetBlockTransaction_45":
                    return GetBlockTransaction_45(args[0]);
                default:
                    return false;
            }
        }

        public static Transaction GetBlockTransaction_45(object height)
        {
            Block block = GetBlock(height);
            int count = block.GetTransactionCount();
            return block.GetTransaction(count);
        }
        
        public static Block GetBlock(object height)
        {
            uint _height = (uint)height;
            Header header = Blockchain.GetHeader(_height);
            Block block = Blockchain.GetBlock(header.Hash);
            return block;
        }
    }
}


