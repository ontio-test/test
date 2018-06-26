using Neo.SmartContract.Framework.Services.Neo;

namespace Neo.SmartContract
{
    public class Lock : Framework.SmartContract
    {
        public static object Main(string operation)
        {
            switch (operation)
            {
                case "test_neo_return_45":
                    return test_neo_return_45();
                default:
                    return false;
            }
        }

        public static int test_neo_return_45()
        {
            return false;
        }  
    }
}