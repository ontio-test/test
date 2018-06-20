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
            byte[] script_hash = (byte[]) args[0];
            Contract con = Blockchain.GetContract(script_hash);

            return con.StorageContext;
        }
        
    }
}