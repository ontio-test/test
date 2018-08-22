using Ont.SmartContract.Framework.Services.Ont;
using Ont.SmartContract.Framework;
using System;
using System.ComponentModel;

namespace Ont.SmartContract
{
    public class invoke2 : Framework.SmartContract
    {
        public static object Main(string operation, params object[] args)
        {
            switch (operation)
            {
                case "Test":
					long count = 0;
					Console.WriteLine("{0}",(long)args[0]);
                    for (int i = 0;i<(long)args[0];i++)
					{
						count = count++;
					}
					return true;
				default:
                    return false;
            }
        }
        public static object Test(string msg)
        {
            return true;
        }
    }
}