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
                case "GetTransactionAttribute_Data":
                    return GetTransactionAttribute_Data((byte[])args[0],(int)args[1]);
                default:
                    return false;
            }
        }

        public static byte[] GetTransactionAttribute_Data(byte[] txid,int index)
        {
            Transaction tran = Blockchain.GetTransaction(txid);
            TransactionAttribute[] attr = tran.GetAttributes(); 
            return attr[index].Data;
        }
    }
}
	
Deploy contract:
  Contract Address:TMi6qvzcBiQyx3AYK6N4BAcvkHiZyQHvzN
  TxHash:f2c08e2a137f2f2b99adaa482126804e83734c5cd650d47798df45eb78acdff2

Tip:
  Using './ontology info status f2c08e2a137f2f2b99adaa482126804e83734c5cd650d47798df45eb78acdff2' to query transaction status
