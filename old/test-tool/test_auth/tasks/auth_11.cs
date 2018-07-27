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
        struct initContractAdminParam
        {
            public byte[] AdminOntID;
        }
        
        struct VerifyTokenParam
        {
            public byte[] ContractAddr;
            public byte[] Caller;
            public string Fn;
            public int KeyNo;
        }

        struct assignFuncsToRoleParam
        {
            public string ContractAddr;
            public byte[] AdminOntID;
            public byte[] Role;
            public object[] Funcs;
            public int KeyNo;
        }

        struct assignOntIDsToRoleParam
        {
            public byte[] ContractAddr;
            public byte[] AdminOntID;
            public byte[] Role;
            public object[] Persons;
            public int KeyNo;
        }

        public struct Transfer
        {
            public byte[] From;
            public byte[] To;
            public int Value;
        }

        public struct delegateParam
        {
            public byte[] ContractAddr;
            public byte[] From;
            public byte[] To;
            public byte[] Role;
            public int Period;
            public int Level;
            public int KeyNo;
        }

        public struct withdrawParam
        {
            public byte[] ContractAddr;
            public byte[] Initiator;
            public byte[] Delegate;
            public byte[] Role;
            public int KeyNo;
        }
        
        public struct functions
        {
            public string Functions;
        }
        



        public static object Main(string operation, object[] token, object[] args)
        {
            if (operation == "initContractAdmin")
            {
                return InitContractAdmin();
            }

            if (operation == "A")
            {
                //we need to check if the caller is authorized to invoke foo
                if (!VerifyToken(operation, token)) return false;

                return A();
            }

            if (operation == "B")
            {
                //we need to check if the caller is authorized to invoke foo
                if (!VerifyToken(operation, token)) return false;

                return B();
            }

            if (operation == "transfer")
            {
                //we need to check if the caller is authorized to invoke foo
                if (!VerifyToken(operation, token)) return false;

                return InvokeTransfer(args);   
            }

            if (operation == "assignFuncsToRole")
            {
                return InvokeAssignFuncsToRole(args);   
            }
    
            return "222";
        }

        public static object A()
        {
            return "A";
        }

        public static object B()
        {
            return "B";
        }

        public static byte[] InvokeTransfer(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            byte[] from = (byte[])args[1];
            byte[] to = (byte[])args[2];
            int amount = (int)args[3];
            
            object[] param = new object[1];
            param[0] = new Transfer { From = from, To = to, Value = amount };

            return Native.Invoke(0, address, "transfer", param);
        }

        public static object InvokeAssignFuncsToRole(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            
            string contractAddr = (string)args[0];
            
            byte[] adminOntID = (byte[])args[1];
            
            byte[] role = (byte[])args[2];
            
            object[] funcs = new object[1];
            funcs[0] = new functions{Functions = (string)args[3]};
            
            int keyNo = (int)args[4];
            
            object[] param = new object[1];
            param[0] = new assignFuncsToRoleParam { ContractAddr = contractAddr, AdminOntID = adminOntID, Role = role, Funcs = funcs, KeyNo = keyNo};
            
            return Native.Invoke(0, address, "assignFuncsToRole", param);
        }

        public static byte[] InvokeAssignOntIDsToRole(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            byte[] contractAddr = (byte[])args[1];
            byte[] adminOntID = (byte[])args[2];

            object[] persons = new object[1];
            persons = (object[])args[3];
            
            int keyNo = (int)args[4];
            
            object[] param = new object[1];
            param[0] = new assignOntIDsToRoleParam { ContractAddr = contractAddr, AdminOntID = adminOntID, Persons = persons, KeyNo = keyNo};

            return Native.Invoke(0, address, "assignOntIDsToRole", param);
        }

        public static byte[] InvokeDelegate(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            byte[] contractAddr = (byte[])args[1];
            byte[] from = (byte[])args[2];
            byte[] to = (byte[])args[3];
            byte[] role = (byte[])args[4];
            int period = (int)args[5];
            int level = (int)args[6];
            int keyNo = (int)args[7];
            
            object[] param = new object[1];
            param[0] = new delegateParam { ContractAddr = contractAddr, From = from, To = to, Role = role, 
                                           Period = period, Level = level, KeyNo = keyNo};

            return Native.Invoke(0, address, "delegate", param);
        }
    
        public static byte[] InvokeWithdraw(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            byte[] contractAddr = (byte[])args[1];
            byte[] initiator = (byte[])args[2];
            byte[] _delegate = (byte[])args[3];
            byte[] role = (byte[])args[4];
            int keyNo = (int)args[5];
            
            object[] param = new object[1];
            param[0] = new withdrawParam { ContractAddr = contractAddr, Initiator = initiator, Delegate = _delegate, 
                                           Role = role, KeyNo = keyNo};

            return Native.Invoke(0, address, "withdraw", param);
        }

                //did:ont:
		public static readonly byte[] mAdminOntID = { 
                0x64, 0x69, 0x64, 0x3a, 0x6f, 0x6e, 0x74, 0x3a,
				0x41, 0x53, 0x38, 0x37, 0x65, 0x6b, 0x58, 0x64, 
                0x63, 0x77, 0x74, 0x7a, 0x59, 0x4d, 0x34, 0x36, 
                0x33, 0x4a, 0x6f, 0x79, 0x6a, 0x4a, 0x67, 0x71, 
                0x36, 0x71, 0x51, 0x6a, 0x53, 0x6b, 0x45, 0x54, 
                0x52, 0x70};
        public static object InitContractAdmin()
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            initContractAdminParam param = new initContractAdminParam { AdminOntID = mAdminOntID };
            byte[] ret = Native.Invoke(0, address, "initContractAdmin", param);
            return ret[0] == 1;
        }

        public static bool VerifyToken(string operation, object[] token)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            
            VerifyTokenParam param = new VerifyTokenParam{}; 
            byte[] con_add = {0x31, 0x32, 0x33};
            param.ContractAddr = con_add;
            param.Fn = operation;
            param.Caller = (byte[])token[0];
            param.KeyNo = (int)token[1];

            byte[] ret = Native.Invoke(0, address, "verifyToken", param);
            return ret[0] == 1;
        }

    }
}
