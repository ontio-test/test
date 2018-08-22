using Ont.SmartContract.Framework.Services.Ont;
using Ont.SmartContract.Framework;
using System;
using System.ComponentModel;

namespace Ont.SmartContract
{
    public class invokeTest : Framework.SmartContract
    {
        public static object Main(string operation, params object[] args)
        {
            switch (operation)
            {
                case "test":
                    return Test((string)args[0]);
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