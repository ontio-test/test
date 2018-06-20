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
                case "GetBlockTransactionCount":
                    return GetBlockTransactionCount(args[0]);
                default:
                    return false;
            }
        }

        public static int GetBlockTransactionCount(object height)
        {
            Block block = GetBlock(height);
            return block.GetTransactionCount();
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


54c56b6c766b00527ac46c766b51527ac4616c766b00c36c766b52527ac46c766b52c318476574426c6f636b5472616e73616374696f6e436f756e74876306006218006c766b51c300c3616521006c766b53527ac4620e00006c766b53527ac46203006c766b53c3616c756653c56b6c766b00527ac4616c766b00c3616542006c766b51527ac46c766b51c361681d4e656f2e426c6f636b2e4765745472616e73616374696f6e436f756e746c766b52527ac46203006c766b52c3616c756655c56b6c766b00527ac4616c766b00c36c766b51527ac46c766b51c36168184e656f2e426c6f636b636861696e2e4765744865616465726c766b52527ac46c766b52c36168124e656f2e4865616465722e476574486173686168174e656f2e426c6f636b636861696e2e476574426c6f636b6c766b53527ac46c766b53c36c766b54527ac46203006c766b54c3616c7566