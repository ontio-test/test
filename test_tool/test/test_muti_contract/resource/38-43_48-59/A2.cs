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

		public static object Main(string operation, object[] token, object[] args)
		{   
			if (operation == "init")
			{
				return init();
			}
			
			if (operation == "transfer")
			{
				return transfer(args);
			}
			
			if(operation == "approve")
			{
				return approve(args);
			}
			if(operation == "transferFrom")
			{
				return transferFrom(args);
			}
			if(operation == "allowance")
			{
				return allowance(args);
			}
			if (operation == "balanceOf")
			{
				return balanceOf(args);
			}
			
			if (operation == "transfer_ong")
			{
				return transfer_ong(args);
			}
			
			if(operation == "approve_ong")
			{
				return approve_ong(args);
			}
			if(operation == "transferFrom_ong")
			{
				return transferFrom_ong(args);
			}
			if(operation == "allowance_ong")
			{
				return allowance_ong(args);
			}
			if (operation == "balanceOf_ong")
			{
				return balanceOf_ong(args);
			}

			return "not support " + operation;
		}

		public static object init()
		{
			return true;
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
		
		public static object transfer_ong(object[] args)
		{
			byte[] address = { 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x02 };
				
			byte[] from = (byte[])args[0];
			byte[] to = (byte[])args[1];
			UInt64 amount = (UInt64)args[2];
			
			object[] param = new object[1];
			param[0] = new Transfer { From = from, To = to, Amount = amount };
			
			return Native.Invoke(0, address, "transfer", param);
		}

		public static object approve_ong(object[] args)
		{
			byte[] address = { 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x02 };
				
			byte[] from = (byte[])args[0];
			byte[] to = (byte[])args[1];
			UInt64 amount = (UInt64)args[2];
			
			Transfer approveparam = new Transfer { From = from, To = to, Amount = amount };
			
			return Native.Invoke(0, address, "approve", approveparam);
		}
		
		public static object allowance_ong(object[] args)
		{
			byte[] address = { 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x02 };
				
			byte[] from = (byte[])args[0];
			byte[] to = (byte[])args[1];
			
			Allowance allowanceparam = new Allowance { From = from, To = to};
			
			return Native.Invoke(0, address, "allowance", allowanceparam);
		}

		public static object transferFrom_ong(object[] args)
		{
			byte[] address = { 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x02 };
				
			byte[] send = (byte[])args[0];
			byte[] from = (byte[])args[1];
			byte[] to = (byte[])args[2];
			UInt64 amount = (UInt64)args[3];
			
			object[] param = new object[1];
			param[0] = new StateSend { Send = send, From = from, To = to, Amount = amount };
			
			return Native.Invoke(0, address, "transferFrom", param);
		}
		
		public static object balanceOf_ong(object[] args)
		{
			byte[] address = { 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
				0x00, 0x00, 0x00, 0x02 };
				
			byte[] account = (byte[])args[0];
			
			Balance accountparam = new Balance { Account = account };
			
			return Native.Invoke(0, address, "balanceOf", accountparam);
		}
	}
}
