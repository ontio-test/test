using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using Neo.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;

namespace Example
{
    public class FirstContract : SmartContract
    {
        [Appcall("8097bd5ece1a5dbee83854c22350055c232809d3")]
        public static extern byte[] SecondContract(string op, object[] args);
        
        public static object Main(string operation, object[] args)
        {
           if (operation == "gas_price_10000")
           {
              return SecondContract("gas_price_20000", null);
           }
           return false;
        }
    }
}