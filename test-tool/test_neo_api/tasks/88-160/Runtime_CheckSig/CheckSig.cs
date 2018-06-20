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
                case "CheckSig":
                if(CheckSig((byte[]) args[0], (byte[]) args[1], (byte[]) args[2])){
                    return "success";
                }
                else{
                    return "failed";
                }
                default:
                    return false;
            }
        }
        
        public static bool CheckSig(byte[] Pubkey, byte[] Data, byte[] Sig)
        {
            return Runtime.CheckSig(Pubkey, Data, Sig);
        }
    }
}