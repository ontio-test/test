using Neo.SmartContract.Framework.Services.Neo;

namespace Neo.SmartContract
{
    public class Lock : Framework.SmartContract
    {
        public static object Main(string operation, params object[] args)
        {
            switch (operation)
            {
                case "test_neo_param_bool":
                    return test_neo_param_bool((bool)args[0]);
                default:
                    return 0;
            }
        }

        public static int test_neo_param_bool(bool index)
        {
            return 1;
        }

        
    }
}