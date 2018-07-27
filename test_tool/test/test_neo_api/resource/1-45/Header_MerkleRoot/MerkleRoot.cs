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
                case "GetHeaderMerkleRoot":
                    return GetHeaderMerkleRoot(args[0]);
                default:
                    return false;
            }
        }

        public static byte[] GetHeaderMerkleRoot(object height)
        {
            Header header = GetHeader(height);
            return header.MerkleRoot;
        }
        
        public static Header GetHeader(object height)
        {
            uint _height = (uint)height;
            Header header = Blockchain.GetHeader(_height);
            return header;
        }
    }
}

