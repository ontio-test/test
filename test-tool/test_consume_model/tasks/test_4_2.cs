using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using Neo.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;

namespace Example
{
    public class SecondContract : SmartContract
    {
        
        public static object Main(string operation, object[] args)
        {
           if (operation == "gas_price_20000")
           {
              return true;
           }
           return false;
        }
    }
}