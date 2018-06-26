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
        public struct regIDWithPublicKey
        {
            public string ontId;
            public byte[] publicKey;
        }
		public struct addKey
        {
            public string ontId;
            public byte[] newPublicKey;
			public byte[] userxPublicKey;
        }
		public struct removeKey
        {
            public string ontId;
            public byte[] newPublicKey;
			public byte[] userPublicKey;
        }
        public struct addRecovery
        {
            public string ontId;
            public byte[] recovery;
			public byte[] userPublicKey;
        }
        public struct changeRecovery
        {
            public string ontId;
            public byte[] newRecovery;
			public byte[] oldRecovery;
        }
		public struct regIDWithAttributes
        {
            public string ontId;
            public byte[] publicKey;
			public object[] attributes;
        }
        public struct addAttributes
        {
            public string ontId;
			public object[] attributes;
            public byte[] publicKey;
        }
        public struct removeAttribute
        {
            public string ontId;
			public byte[] attributePath;
            public byte[] publicKey;
        }
		public struct getPublicKeys
        {
            public string ontId;
        }
		public struct getKeyState
        {
            public string ontId;
			public int KeyNo;
        }
        public struct getAttributes
        {
            public string ontId;
        }
        public struct getDDO
        {
            public string ontId;
        }
        public struct verifySignature
        {
            public string ontId;
			public int KeyNo;
        }
		
        public static object Main(string operation,  object[] args)
        {
            

            if (operation == "regIDWithPublicKey")
            {
                return InvokeRegIDWithPublicKey(args);
            }
			if (operation == "addKey")
            {
                return InvokeAddKey(args);
            }
			if (operation == "removeKey")
            {
                return InvokeRemoveKey(args);
            }
			if (operation == "addRecovery")
            {
                return InvokeAddRecovery(args);
            }
			if (operation == "changeRecovery")
            {
                return InvokeChangeRecovery(args);
            }
			if (operation == "regIDWithAttributes")
            {
                return InvokeRegIDWithAttributes(args);
            }
			if (operation == "addAttributes")
            {
                return InvokeAddAttributes(args);
            }
			if (operation == "removeAttribute")
            {
                return InvokeRemoveAttribute(args);
            }
			if (operation == "getPublicKeys")
            {
                return InvokeGetPublicKeys(args);
            }
			if (operation == "getKeyState")
            {
                return InvokeGetKeyState(args);
            }
			if (operation == "getAttributes")
            {
                return InvokeGetAttributes(args);
            }
			if (operation == "getDDO")
            {
                return InvokeGetDDO(args);
            }
			if (operation == "verifySignature")
            {
                return InvokeVerifySignature(args);
            }
            return operation;
        }
		public static byte[] InvokeRegIDWithPublicKey(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3};
            string ontId1 = (string) args[0];
            byte[] publicKey1 = (byte[])args[1];
            
            regIDWithPublicKey param = new regIDWithPublicKey { ontId = ontId1, publicKey = publicKey1};

            return Native.Invoke(0, address, "regIDWithPublicKey", param);
        }
		public static byte[] InvokeAddKey(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3};
            string ontId1 = (string) args[0];
            byte[] newPublicKey1 = (byte[])args[1];
            byte[] userxPublicKey1 = (byte[])args[2];
            addKey param = new addKey { ontId = ontId1, newPublicKey = newPublicKey1,userxPublicKey=userxPublicKey1};

            return Native.Invoke(0, address, "addKey", param);
        }
		public static byte[] InvokeRemoveKey(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3};
            string ontId1 = (string) args[0];
            byte[] newPublicKey1 = (byte[])args[1];
            byte[] userxPublicKey1 = (byte[])args[2];
            removeKey param = new removeKey { ontId = ontId1, newPublicKey = newPublicKey1,userPublicKey=userxPublicKey1};

            return Native.Invoke(0, address, "removeKey", param);
        }
		public static byte[] InvokeAddRecovery(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3};
            string ontId1 = (string) args[0];
            byte[] recovery1 = (byte[])args[1];
            byte[] userPublicKey1 = (byte[])args[2];
            addRecovery param = new addRecovery { ontId = ontId1, recovery = recovery1,userPublicKey=userPublicKey1};

            return Native.Invoke(0, address, "addRecovery", param);
        }
		
		public static byte[] InvokeChangeRecovery(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3};
            string ontId1 = (string) args[0];
            byte[] newRecovery1 = (byte[])args[1];
            byte[] oldRecovery1 = (byte[])args[2];
            changeRecovery param = new changeRecovery { ontId = ontId1, newRecovery = newRecovery1,oldRecovery=oldRecovery1};

            return Native.Invoke(0, address, "changeRecovery", param);
        }
		
		public static byte[] InvokeRegIDWithAttributes(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3};
            string ontId1 = (string) args[0];
            byte[] publicKey1 = (byte[])args[1];
            object[] attributes1= (object[])args[2];
            regIDWithAttributes param = new regIDWithAttributes { ontId = ontId1, publicKey = publicKey1,attributes=attributes1};

            return Native.Invoke(0, address, "regIDWithAttributes", param);
        }	
		public static byte[] InvokeAddAttributes(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3};
            string ontId1 = (string) args[0];
            byte[] publicKey1 = (byte[])args[2];
            object[] attributes1= (object[])args[1];
            addAttributes param = new addAttributes { ontId = ontId1, attributes=attributes1,publicKey = publicKey1};

            return Native.Invoke(0, address, "addAttributes", param);
        }
		public static byte[] InvokeRemoveAttribute(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3};
            string ontId1 = (string) args[0];
			byte[] attributePath1=(byte[])args[1];
            byte[] publicKey1 = (byte[])args[2];
            removeAttribute param = new removeAttribute { ontId = ontId1, attributePath=attributePath1,publicKey = publicKey1};

            return Native.Invoke(0, address, "removeAttribute", param);
        }
		
		public static byte[] InvokeGetPublicKeys(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3};
            string ontId1 = (string) args[0];
            getPublicKeys param = new getPublicKeys { ontId = ontId1};

            return Native.Invoke(0, address, "getPublicKeys", param);
        }
		public static byte[] InvokeGetKeyState(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3};
            string ontId1 = (string) args[0];
            int keyNo1 = (int) args[1];
            getKeyState param = new getKeyState { ontId = ontId1,KeyNo=keyNo1};

            return Native.Invoke(0, address, "getKeyState", param);
        }
		public static byte[] InvokeGetAttributes(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3};
            string ontId1 = (string) args[0];
            getAttributes param = new getAttributes { ontId = ontId1};

            return Native.Invoke(0, address, "getAttributes", param);
        }
		public static byte[] InvokeGetDDO(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3};
            string ontId1 = (string) args[0];
            getDDO param = new getDDO { ontId = ontId1};

            return Native.Invoke(0, address, "getDDO", param);
        }
		public static byte[] InvokeVerifySignature(object[] args)
        {
   
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3};
            string ontId1 = (string) args[0];
            int keyNo1 = (int) args[1];
            verifySignature param = new verifySignature { ontId = ontId1,KeyNo=keyNo1};

            return Native.Invoke(0, address, "verifySignature", param);
        }

    }
}