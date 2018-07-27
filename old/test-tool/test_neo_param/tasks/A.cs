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
		public static object Main(string operation, object[] args)
		{   
		    if (operation == "int_to_int") {
		        return int_to_int((int)args[0]);
		    } else if (operation == "string_to_int") {
		        return string_to_int((string)args[0]);
		    } else if (operation == "bool_to_int") {
		        return bool_to_int((bool)args[0]);
		    } else if (operation == "byte_to_int") {
		        return byte_to_int((byte[])args[0]);
		    }
		    
            return false;
		}
		
		public static int int_to_int(int arg)
		{
			return 1;
		}

        public static int string_to_int(string arg)
		{
			return 1;
		}
		
		public static int bool_to_int(bool arg) 
		{
			return 1;
		}
		
		public static int byte_to_int(byte[] arg)
		{
			return 1;
		}

        //编译不过
        /*public static int func(bool args)
		{
			
		}
		
        public static int func(string arg)
		{
		}
		
		public static int func(bool arg)
		{
		}
		
		public static int func(byte[] arg)
		{
		}
		*/
		
	}
}
