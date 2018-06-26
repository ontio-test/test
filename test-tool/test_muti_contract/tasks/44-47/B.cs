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
    				0x41, 0x4c, 0x70, 0x32, 0x7a, 0x76, 0x41, 0x71, 
					0x4e, 0x32, 0x70, 0x53, 0x38, 0x51, 0x65, 0x6a, 
					0x51, 0x74, 0x53, 0x44, 0x78, 0x77, 0x35, 0x61,
					0x42, 0x51, 0x47, 0x48, 0x47, 0x61, 0x53, 0x4b,
					0x64, 0x34};
    
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
