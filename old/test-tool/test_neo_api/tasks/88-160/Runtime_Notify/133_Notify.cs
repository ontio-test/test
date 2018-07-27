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
                case "Notify":
                    SendNotify();
                    return true;
                default:
                    return false;
            }
        }
        
        public static void SendNotify()
        {
            object[] param = new object[1];
            string b = "";
            param[0] = b;
            Runtime.Notify(param);
        }
    }
}