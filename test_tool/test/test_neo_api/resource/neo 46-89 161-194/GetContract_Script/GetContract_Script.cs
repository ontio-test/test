using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using Neo.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;

namespace Neo.SmartContract
{
    public class Domain : Framework.SmartContract
    {
        public static object Main(string operation, params object[] args)
        {
            switch (operation)
            {
                case "GetContract_Script":
                    return GetContract_Script((byte[])args[0]);
                default:
                    return false;
            }
        }

        public static byte[] GetContract_Script(byte[] script_hash)
        {
            Contract cont = Blockchain.GetContract(script_hash);
            return cont.Script;
        }
    }
}

// Deploy contract:
//   Contract Address:TMfVtXcrk664meQzKXicRMrqzVBBnP8BNN
//   TxHash:975a0f610a228060d42c39ed4b223faf1782794025dc546542f5274f2b8bc19b

// Tip:
//   Using './ontology info status 975a0f610a228060d42c39ed4b223faf1782794025dc546542f5274f2b8bc19b' to query transaction status
