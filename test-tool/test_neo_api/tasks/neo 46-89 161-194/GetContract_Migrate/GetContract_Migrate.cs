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
                case "GetContract_Migrate":
                    return GetContract_Migrate((byte[])args[0],(bool)args[1],(string)args[2],(string)args[3],(string)args[4],(string)args[5],(string)args[6]);
                default:
                    return false;
            }
        }

        public static Contract GetContract_Migrate(byte[] script,bool flag, string name, string version, string author, string email, string desc)
        {
            Contract cre = Contract.Migrate(script,flag,name,version,author,email,desc);
            return cre;
        }
    }
}

// 54c56b6c766b00527ac46c766b51527ac4616c766b00c36c766b52527ac46c766b52c313476574436f6e74726163745f4d696772617465876306006260006c766b51c300c36c766b51c351c36c766b51c352c36c766b51c353c36c766b51c354c36c766b51c355c36c766b51c356c3615679517958727551727555795279577275527275547953795672755372756521006c766b53527ac4620e00006c766b53527ac46203006c766b53c3616c756659c56b6c766b00527ac46c766b51527ac46c766b52527ac46c766b53527ac46c766b54527ac46c766b55527ac46c766b56527ac4616c766b00c36c766b51c36c766b52c36c766b53c36c766b54c36c766b55c36c766b56c36156795179587275517275557952795772755272755479537956727553727568134e656f2e436f6e74726163742e4372656174656c766b57527ac46c766b57c36c766b58527ac46203006c766b58c3616c7566

// Deploy contract:
//   Contract Address:TMiRXSdSgsTCkxc5PDovYSz9uhMJMdpHyQ
//   TxHash:3b86027423ca63a9ada88f3800bd5ac111ed0b0c9eda2129943fa9bd3b44c2c3

// Tip:
//   Using './ontology info status 3b86027423ca63a9ada88f3800bd5ac111ed0b0c9eda2129943fa9bd3b44c2c3' to query transaction status
