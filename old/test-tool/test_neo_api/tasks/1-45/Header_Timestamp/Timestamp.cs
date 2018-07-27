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
                case "GetHeaderTimestamp":
                    return GetHeaderTimestamp(args[0]);
                default:
                    return false;
            }
        }

        public static uint GetHeaderTimestamp(object height)
        {
            Header header = GetHeader(height);
            return header.Timestamp;
        }
        
        public static Header GetHeader(object height)
        {
            uint _height = (uint)height;
            Header header = Blockchain.GetHeader(_height);
            return header;
        }
    }
}

