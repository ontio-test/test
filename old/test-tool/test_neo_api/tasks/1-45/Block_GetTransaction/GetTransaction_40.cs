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
                case "GetBlockTransaction_40":
                    return GetBlockTransaction_40(args[0], args[1]);
                default:
                    return false;
            }
        }

        public static Transaction GetBlockTransaction_40(object height, object index)
        {
            Block block = GetBlock(height);
            int _index = (int)index;
            return block.GetTransaction(_index);
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