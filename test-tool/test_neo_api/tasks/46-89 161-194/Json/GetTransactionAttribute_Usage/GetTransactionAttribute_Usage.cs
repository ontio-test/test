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
                case "GetTransactionAttribute_Usage":
                    return GetTransactionAttribute_Usage((byte[])args[0],(int)args[1]);
                default:
                    return false;
            }
        }

        public static byte GetTransactionAttribute_Usage(byte[] txid,int index)
        {
            Transaction tran = Blockchain.GetTransaction(txid);
            TransactionAttribute[] attr = tran.GetAttributes(); 
            return attr[index].Usage;
        }
    }
}
    
// 54c56b6c766b00527ac46c766b51527ac4616c766b00c36c766b52527ac46c766b52c3176765745472616e73616374696f6e417474726962757465876306006220006c766b51c300c36c766b51c351c3617c6521006c766b53527ac4620e00006c766b53527ac46203006c766b53c3616c756655c56b6c766b00527ac46c766b51527ac4616c766b00c361681d4e656f2e426c6f636b636861696e2e4765745472616e73616374696f6e6c766b52527ac46c766b52c361681d4e656f2e5472616e73616374696f6e2e476574417474726962757465736c766b53527ac46c766b53c36c766b51c3c36168164e656f2e4174747269627574652e47657455736167656c766b54527ac46203006c766b54c3616c7566

// Deploy contract:
//   Contract Address:TMio8iyg4YCZuHA3HvhGCeko18Pgjbes1Q
//   TxHash:1271bba31da28d0aa18d90166188fbed8262f45ec2e934379a730e93e27d6733

// Tip:
//   Using './ontology info status 1271bba31da28d0aa18d90166188fbed8262f45ec2e934379a730e93e27d6733' to query transaction status

