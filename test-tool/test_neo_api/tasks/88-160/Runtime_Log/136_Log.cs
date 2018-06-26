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
                case "Log":
                    SendLog(args);
                    return true;
                default:
                    return false;
            }
        }
        
        public static void SendLog(object[] args)
        {
            string param = (string)args[0];
            Runtime.Log(param);
        }
    }
}