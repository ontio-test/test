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
            [Appcall("54b9121e8a389ab14defb307b685c433b3032280")] //智能合约B的地址
            public static extern object ContractB(string op,  object[] token, object[] args);
         
			public struct InitContractAdminParam
    		{
    			public byte[] adminOntID;
    		}
    	
            //did:ont:
    		 public static readonly byte[] mAdminOntID = { 
    				0x64, 0x69, 0x64, 0x3a, 0x6f, 0x6e, 0x74, 0x3a,
    				0x41, 0x58, 0x6d, 0x4b, 0x67, 0x48, 0x67, 0x55, 
					0x36, 0x64, 0x77, 0x73, 0x48, 0x4e, 0x45, 0x64, 
					0x57, 0x52, 0x65, 0x7a, 0x52, 0x38, 0x58, 0x6a, 
					0x32, 0x52, 0x31, 0x4b, 0x63, 0x6b, 0x44, 0x64, 
					0x57, 0x76};
    
            public static object Main(string operation, object[] token, object[] args)
            {   
                if (operation == "init")
                {
                    return init();
                }
                
                if (operation == "A")
                {
                    return A();
                }
				
				if (operation == "A2")
                {
                    return A2();
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

            public static object A()
            {
                object ret = ContractB("B", null, null);
    			if ((bool)ret == true) {
    				return "Invoke A Success.";
    			} else {
					return false;
				}
            }
			
			public static object A2()
            {
                object ret = Runtime.CheckWitness(ExecutionEngine.CallingScriptHash);
				if ((bool)ret == false) {
    				return false;
    			}
                ret = ContractB("B", null, null);
    			if ((bool)ret == false) {
    				return false;
    			}
				
				return "Invoke A2 Success.";
            }
        }
    }
