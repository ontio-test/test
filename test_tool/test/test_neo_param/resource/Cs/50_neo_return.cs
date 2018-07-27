using Neo.SmartContract.Framework.Services.Neo;

namespace Neo.SmartContract
{
    public class Lock : Framework.SmartContract
    {
        public static object Main(string operation)
        {
            switch (operation)
            {
                case "test_neo_return_50":
                    return test_neo_return_50();
                default:
                    return false;
            }
        }

        public static string test_neo_return_50()
        {
            byte[] a = ("111122223333").getBytes();	
            return a;
        }  
    }
}