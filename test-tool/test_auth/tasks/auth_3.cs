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
        
        struct verifyTokenParam
        {
            public byte[] ContractAddr;
            public byte[] Caller;
            public byte[] Fn;
            public int KeyNo;
        }

        struct assignFuncsToRoleParam
        {
            public byte[] ContractAddr;
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

        //did:ont:
		 public static readonly byte[] mAdminOntID = { 
                };

        public static object Main(string operation, object[] token, params object[] args)
        {
            if (operation == "initContractAdmin")
            {
                return InitContractAdmin(args);
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
    
            return "111";
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

        public static byte[] InvokeAssignFuncsToRole(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            byte[] contractAddr = (byte[])args[1];
            byte[] adminOntID = (byte[])args[2];

            object[] funcs = new object[1];
            funcs = (object[])args[3];

            int keyNo = (int)args[4];
            
            object[] param = new object[1];
            param[0] = new assignFuncsToRoleParam { ContractAddr = contractAddr, AdminOntID = adminOntID, Funcs = funcs, KeyNo = keyNo};

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

        
        public static object InitContractAdmin(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            object[] param = new object[1];
            param[0] = new initContractAdminParam { AdminOntID = mAdminOntID };
            
            return Native.Invoke(0, address, "initContractAdmin", param);
        }

        public static bool VerifyToken(string operation, object[] token)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            
            byte[] contractAddr = ExecutionEngine.ExecutingScriptHash;
            byte[] caller = (byte[])token[0];
            byte[] fn = operation.AsByteArray();
            int keyNo = (int)token[1];
            
            object[] param = new object[1];
            param[0] = new verifyTokenParam { ContractAddr = contractAddr, Caller = caller, Fn = fn, KeyNo = keyNo };
            byte[] res = Native.Invoke(0, address, "verifyToken", param);
            return true;
        }

    }
}
