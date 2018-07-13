    using Neo.SmartContract.Framework;
    using Neo.SmartContract.Framework.Services.Neo;
    using Neo.SmartContract.Framework.Services.System;
    using System;
    using System.ComponentModel;
    using System.Numerics;
    
    namespace Example
    {
        public class AppContract : SmartContract
        {           
			public struct InitContractAdminParam
    		{
    			public byte[] adminOntID;
    		}
    		
            //did:ont:
    		 public static readonly byte[] mAdminOntID = { 
    				0x64, 0x69, 0x64, 0x3a, 0x6f, 0x6e, 0x74, 0x3a,
    				0x41, 0x4d, 0x31, 0x32, 0x46, 0x41, 0x62, 0x73, 
					0x68, 0x4e, 0x76, 0x75, 0x67, 0x4c, 0x61, 0x48,
					0x47, 0x34, 0x4b, 0x7a, 0x41, 0x66, 0x48, 0x47,
					0x76, 0x55, 0x47, 0x31, 0x74, 0x35, 0x53, 0x70,
					0x41, 0x76};
    
            public static object Main(string operation, object[] token, object[] args)
            {   
                if (operation == "init")
                {
                    return init();
                }
                
                if (operation == "B")
                {
                    return B();
                }
    
                return false;
            }
    
            public static object init()
            {
    			//must specify native contract's address in function scope
                byte[] authContractAddr = {
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x06 };
    			
                InitContractAdminParam param = new InitContractAdminParam { adminOntID = mAdminOntID };
                byte[] ret = Native.Invoke(0, authContractAddr, "initContractAdmin", param);
                return ret[0] == 1;
            }

            public static object B()
            {
				return Runtime.CheckWitness(ExecutionEngine.CallingScriptHash);
            }
        }
    }
