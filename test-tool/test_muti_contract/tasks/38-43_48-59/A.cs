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
		struct Transfer
		{
			public byte[] From;
			public byte[] To;
			public UInt64 Amount;
		}
		
		struct Allowance
		{
			public byte[] From;
			public byte[] To;
		}
		
		public struct StateSend
		{
			public byte[] Send;
			public byte[] From;
			public byte[] To;
			public UInt64 Amount;
		}
		
		public struct Balance
		{
			public byte[] Account;
		}
		
		public struct InitContractAdminParam
		{
			public byte[] adminOntID;
		}
		
		public struct VerifyTokenParam
		{
			public byte[] contractAddr;
			public byte[] caller;
			public string fn;
			public int keyNo;
		}
		
		
		//did:ont:
		 public static readonly byte[] mAdminOntID = { 
				0x64, 0x69, 0x64, 0x3a, 0x6f, 0x6e, 0x74, 0x3a,
				0x41 ,0x55 ,0x53 ,0x79 ,0x5a ,0x78 ,0x31 ,0x42 ,
                0x6f ,0x51 ,0x62 ,0x54 ,0x79 ,0x33 ,0x61 ,0x76 ,
                0x4d ,0x4b ,0x79 ,0x67 ,0x76 ,0x4a ,0x72 ,0x6b ,
                0x77 ,0x38 ,0x6d ,0x52 ,0x62 ,0x7a ,0x74 ,0x36 ,
                0x41 ,0x61};

		public static object Main(string operation, object[] token, object[] args)
		{   
			if (operation == "init")
			{
				return init();
			}
			
			if (operation == "transfer")
			{
				if (!VerifyToken(operation, token)) return "Verify transfer FAILED";
				return transfer(args);
			}
			
			if(operation == "approve")
			{
				if (!VerifyToken(operation, token)) return "Verify approve FAILED";
				return approve(args);
			}
			if(operation == "transferFrom")
			{
				if (!VerifyToken(operation, token)) return "Verify transferFrom FAILED";
				return transferFrom(args);
			}
			if(operation == "allowance")
			{
				if (!VerifyToken(operation, token)) return "Verify allowance FAILED";
				return allowance(args);
			}
			if (operation == "balanceOf")
			{
				if (!VerifyToken(operation, token)) return "Verify balanceOf FAILED";
				return balanceOf(args);
			}

			return "not support " + operation;
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

		public static object transfer(object[] args)
		{
			byte[] address = { 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x01 };
				
			byte[] from = (byte[])args[0];
			byte[] to = (byte[])args[1];
			UInt64 amount = (UInt64)args[2];
			
			object[] param = new object[1];
			param[0] = new Transfer { From = from, To = to, Amount = amount };
			
			return Native.Invoke(0, address, "transfer", param);
		}

		public static object approve(object[] args)
		{
			byte[] address = { 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x01 };
				
			byte[] from = (byte[])args[0];
			byte[] to = (byte[])args[1];
			UInt64 amount = (UInt64)args[2];
			
			Transfer approveparam = new Transfer { From = from, To = to, Amount = amount };
			
			return Native.Invoke(0, address, "approve", approveparam);
		}
		
		public static object allowance(object[] args)
		{
			byte[] address = { 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x01 };
				
			byte[] from = (byte[])args[0];
			byte[] to = (byte[])args[1];
			
			Allowance allowanceparam = new Allowance { From = from, To = to};
			
			return Native.Invoke(0, address, "allowance", allowanceparam);
		}

		public static object transferFrom(object[] args)
		{
			byte[] address = { 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x01 };
				
			byte[] send = (byte[])args[0];
			byte[] from = (byte[])args[1];
			byte[] to = (byte[])args[2];
			UInt64 amount = (UInt64)args[3];
			
			object[] param = new object[1];
			param[0] = new StateSend { Send = send, From = from, To = to, Amount = amount };
			
			return Native.Invoke(0, address, "transferFrom", param);
		}
		
		public static object balanceOf(object[] args)
		{
			byte[] address = { 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x01 };
				
			byte[] account = (byte[])args[0];
			
			Balance accountparam = new Balance { Account = account };
			
			return Native.Invoke(0, address, "balanceOf", accountparam);
		}
		
		public static bool VerifyToken(string operation, object[] token)
		{
			//must specify native contract's address in function scope
			byte[] authContractAddr = {
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
				0x00, 0x00, 0x00, 0x06 };
			VerifyTokenParam param = new VerifyTokenParam{}; 
			param.contractAddr = ExecutionEngine.ExecutingScriptHash;
			param.fn = operation;
			param.caller = (byte[])token[0];
			param.keyNo = (int)token[1];

			byte[] ret = Native.Invoke(0, authContractAddr, "verifyToken", param);
			return ret[0] == 1;
		}

	}
}
