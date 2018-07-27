using Neo.SmartContract.Framework.Services.Neo;

namespace Neo.SmartContract
{
    public class Lock : Framework.SmartContract
    {
        public static object Main(string operation, params object[] args)
        {
            switch (operation)
            {
                case "test_neo_param_int":
                    return test_neo_param_int((int)args[0]);
                default:
                    return 0;
            }
        }

        public static int test_neo_param_int(int index)
        {
            return 1;
        }
    }
}

// Deploy contract:
//  Contract Address:809a96b5eadaac49ab2a1737e2be6c22c669f2d6
//   TxHash:b282606c752f5fb77db08982908eefed8897a0b02e4cb442ff1f3c685c878a71


// Tip:
//   Using './ontology info status e3506549c004f42bd41c95a4cda8d0788eb21b1af0b6567d079c5a3949725802' to query transaction status
