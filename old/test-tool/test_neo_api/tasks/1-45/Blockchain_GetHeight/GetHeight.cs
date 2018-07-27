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
                case "GetHeight":
                    return GetHeight();
                default:
                    return false;
            }
        }

        public static uint GetHeight()
        {
            return Blockchain.GetHeight();
        }
    }
}


54c56b6c766b00527ac46c766b51527ac4616c766b00c36c766b52527ac46c766b52c30947657448656967687487630600621100616521006c766b53527ac4620e00006c766b53527ac46203006c766b53c3616c756651c56b616168184e656f2e426c6f636b636861696e2e4765744865696768746c766b00527ac46203006c766b00c3616c7566


Deploy contract:
  Contract Address:TMfpcNRpATsdop9T7BVmjwXWvKvuPuNrm6
  TxHash:63d68be445e2683ab80d9ea95d7d7af8afe6176b75e03681e1b533c96ceb5eea

Tip:
  Using './ontology info status 63d68be445e2683ab80d9ea95d7d7af8afe6176b75e03681e1b533c96ceb5eea' to query transaction status
