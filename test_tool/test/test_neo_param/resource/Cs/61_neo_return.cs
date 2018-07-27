using Neo.SmartContract.Framework.Services.Neo;

namespace Neo.SmartContract
{
    public class Lock : Framework.SmartContract
    {
        public static object Main(string operation)
        {
            switch (operation)
            {
                case "test_neo_return_61":
                    return test_neo_return_61();
                default:
                    return false;
            }
        }

        public static byte[] test_neo_return_61()
        {
            byte[] a = {0x31, 0x32, 0x33, 0x34, 0x35,0x36,0x37,0x38,0x39};
            return a;
        }  
    }
}