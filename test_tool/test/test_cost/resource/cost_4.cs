using Ont.SmartContract.Framework.Services.Ont;
using Ont.SmartContract.Framework;
using System;
using System.ComponentModel;

namespace Ont.SmartContract
{
    public class HelloWorld : Framework.SmartContract
    {
        public static object Main(string operation, params object[] args)
        {
            switch (operation)
            {
                case "run":
                    run((int)args[0]);
                    return true;
                default:
                    return false;
            }
        }
        public static void run(int length)
        {
            for(int i = 0; i < length; i++) {
                int ii = 0;
                int jj= 0;
                ii = jj;
            }
        }
    }
}