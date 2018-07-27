using Ont.SmartContract.Framework;
using Ont.SmartContract.Framework.Services.Ont;
using Ont.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;


namespace Ont.SmartContract
{
    public class BlockchainTest : Framework.SmartContract
    {
        public static object Main(string operation, params object[] args)
        {
            if(operation == "GetHeight")
            {
                return GetHeight();
            }
            else if(operation == "GetHeader")
            {
                 return GetHeader(args[0]);
            }
            else if(operation == "GetBlock")
            {
                return GetBlock(args[0]);
            }
            else if(operation == "GetTransaction")
            {
                return GetTransaction(args[0]);
            }
            else if(operation == "GetContract")
            {
                return GetContract(args[0]);
            }
            else if(operation == "GetHeaderHash")
            {
                return GetHeaderHash(args[0]);
            }
            else if(operation == "GetHeaderVersion")
            {
                return GetHeaderVersion(args[0]);
            }
            else if(operation == "GetHeaderPrevHash")
            {
                return GetHeaderPrevHash(args[0]);
            }
            else if(operation == "GetHeaderIndex")
            {
                return GetHeaderIndex(args[0]);
            }
            else if(operation == "GetHeaderMerkleRoot")
            {
                return GetHeaderMerkleRoot(args[0]);
            }
            else if(operation == "GetHeaderTimestamp")
            {
                return GetHeaderTimestamp(args[0]);
            }
            else if(operation == "GetHeaderConsensusData")
            {
                return GetHeaderConsensusData(args[0]);
            }
            else if(operation == "GetHeaderNextConsensus")
            {
                return GetHeaderNextConsensus(args[0]);
            }
            else if(operation == "GetBlockTransactionCount")
            {
                return GetBlockTransactionCount(args[0]);
            }
            else if(operation == "GetBlockTransactions")
            {
                return GetBlockTransactions(args[0]);
            }
            else if(operation == "GetBlockTransaction_40")
            {
                return GetBlockTransaction_40(args[0], args[1]);
            }
            else if(operation == "GetBlockTransaction_44")
            {
                return GetBlockTransaction_44(args[0]);
            }
            else if(operation == "GetBlockTransaction_45")
            {
                return GetBlockTransaction_45(args[0]);
            }
            else if(operation == "GetContract_Create")
            {
                return GetContract_Create((byte[])args[0],(bool)args[1],(string)args[2],(string)args[3],(string)args[4],(string)args[5],(string)args[6]);
            }
            else if(operation == "GetContract_Destroy")
            {
                return GetContract_Destroy();
            }
            else if(operation == "GetContract_Migrate")
            {
                return GetContract_Migrate((byte[])args[0],(bool)args[1],(string)args[2],(string)args[3],(string)args[4],(string)args[5],(string)args[6]);
            }
            else if(operation == "GetContract_Script")
            {
                return GetContract_Script((byte[])args[0]);
            }
            else if(operation == "GetStorageContext")
            {
                return GetStorageContext(args);
            }
            else if(operation == "GetContract_StorageContext")
            {
                return GetContract_StorageContext((byte[])args[0]);
            }
            else if(operation == "GetTransaction_Attribute")
            {
                return GetTransaction_Attribute((byte[])args[0]);
            }
            else if(operation == "GetTransaction_Hash")
            {
                return GetTransaction_Hash((byte[])args[0]);
            }
            else if(operation == "GetTransaction_Type")
            {
                return GetTransaction_Type((byte[])args[0]);
            }
            else if(operation == "GetTransactionAttribute_Data")
            {
                return GetTransactionAttribute_Data((byte[])args[0],(int)args[1]);
            }
            else if(operation == "GetTransactionAttribute_Usage")
            {
                return GetTransactionAttribute_Usage((byte[])args[0],(int)args[1]);
            }
            else if(operation == "GetTransaction_Attributes")
            {
                return GetTransaction_Attributes((byte[])args[0]);
            }
            else if(operation == "GetCallingScriptHash")
            {
                return GetCallingScriptHash();
            }
            else if(operation == "GetEntryScriptHash")
            {
                return GetEntryScriptHash();
            }
            else if(operation == "GetExecutingScriptHash")
            {
                return GetExecutingScriptHash();
            }
            else if(operation == "GetScriptContainer")
            {
                return GetScriptContainer();
            }
            else if(operation == "CheckWitness")
            {
                return GetCheckWitness((byte[])args[0]);
            }
            else if(operation == "Log_134")
            {
                Log_134();
                return true;
            }
            else if(operation == "Log_134")
            {
                Log_134();
                return true;
            }
            else if(operation == "Log_135")
            {
                Log_135();
                return true;
            }
            else if(operation == "Log_136")
            {
                Log_136(args);
                return true;
            }
            else if(operation == "Log_137")
            {
                Log_137();
                return true;
            }
            else if(operation == "Log_138")
            {
                Log_138();
                return true;
            }
            else if(operation == "Notify_130")
            {
                Notify_130();
                return true;
            }
            else if(operation == "Notify_131")
            {
                Notify_131();
                return true;
            }
            else if(operation == "Notify_132")
            {
                Notify_132();
                return true;
            }
            else if(operation == "Notify_133")
            {
                Notify_133();
                return true;
            }
            else if(operation == "GetTime")
            {
                return GetTime();
            }
            else if(operation == "GetCurrentContext")
            {
                return GetCurrentContext();
            }
            else if(operation == "Delete_114")
            {
                byte[] key = (byte[]) args[0];
                byte[] value = (byte[]) args[1];
                PutStorge(Storage.CurrentContext, key, value);
                DeleteStorge(Storage.CurrentContext, key);
                return GetStorge(Storage.CurrentContext, key);
            }
            else if(operation == "Delete_120")
            {
                byte[] key = (byte[]) args[0];
                byte[] value = (byte[]) args[1];
                // PutStorge(Storage.CurrentContext, key, value);
                DeleteStorge(Storage.CurrentContext, key);
                return GetStorge(Storage.CurrentContext, key);
            }
            else if(operation == "Delete_115")
            {
                byte[] key = (byte[]) args[0];
                byte[] value = (byte[]) args[1];
                PutStorge(Storage.CurrentContext, key, value);
                DeleteStorge(Storage.CurrentContext, key);
                DeleteStorge(Storage.CurrentContext, key);
                return GetStorge(Storage.CurrentContext, key);
            }
            else if(operation == "Delete_116")
            {
                byte[] key = (byte[]) args[0];
                byte[] value = (byte[]) args[1];
                PutStorge(Storage.CurrentContext, key, value);
                DeleteStorge(null, key);
                return GetStorge(Storage.CurrentContext, key);
            }
            else if(operation == "Get_92")
            {
                byte[] key = (byte[]) args[0];
                byte[] value = (byte[]) args[1];
                PutStorge(Storage.CurrentContext, key, value);
                return GetStorge(Storage.CurrentContext, key);
            }
            else if(operation == "Get_93")
            {
                byte[] key_1 = (byte[]) args[0];
                byte[] value = (byte[]) args[1];
                byte[] key_2 = (byte[]) args[2];
                // PutStorge(Storage.CurrentContext, key_1, value);
                return GetStorge(Storage.CurrentContext, key_2);
            }
            else if(operation == "Get_94")
            {
                byte[] key = (byte[]) args[0];
                byte[] value = (byte[]) args[1];
                PutStorge(Storage.CurrentContext, key, value);
                return GetStorge(null, key);
            }
            else if(operation == "Get_98")
            {
                byte[] key = (byte[]) args[0];
                byte[] value = (byte[]) args[1];
                PutStorge(Storage.CurrentContext, key, value);
                DeleteStorge(Storage.CurrentContext, key);
                return GetStorge(Storage.CurrentContext, key);
            }
            else if(operation == "Put_99")
            {
                byte[] key = (byte[]) args[0];
                byte[] value = (byte[]) args[1];
                PutStorge(Storage.CurrentContext, key, value);
                return GetStorge(Storage.CurrentContext, key);
            }
            else if(operation == "Put_100")
            {
                byte[] key = (byte[]) args[0];
                byte[] value = (byte[]) args[1];
                StorageContext _c = (StorageContext) args[1];
                PutStorge(_c, key, value);
                return GetStorge(_c, key);
            }
            else if(operation == "Put_101")
            {
                byte[] key = (byte[]) args[0];
                byte[] value = (byte[]) args[1];
                PutStorge(null, key, value);
                return GetStorge(Storage.CurrentContext, key);
            }
            else if(operation == "Put_107")
            {
                byte[] key = (byte[]) args[0];
                byte[] value_1 = (byte[]) args[1];
                byte[] value_2 = (byte[]) args[2];
                PutStorge(Storage.CurrentContext, key, value_1);
                PutStorge(Storage.CurrentContext, key, value_2);
                return GetStorge(Storage.CurrentContext, key);
            }
            else if(operation == "Put_108_1")
            {
                byte[] key = (byte[]) args[0];
                byte[] value = (byte[]) args[1];
                PutStorge(Storage.CurrentContext, key, value);
                return GetStorge(Storage.CurrentContext, key);
            }
            else
            {
                return false;
            }
        }

        public static byte[] GetStorge(StorageContext context, byte[] key)
        {
            return Storage.Get(context, key);
        }

        public static void PutStorge(StorageContext context, byte[] key, byte[] value)
        {
            Storage.Put(context, key, value);
        }

        public static void DeleteStorge(StorageContext context, byte[] key)
        {
            Storage.Delete(context, key);
        }

        public static object GetCurrentContext()
        {
            return Storage.CurrentContext;
        }

        public static object GetTime()
        {
            return Runtime.Time;
        }

        public static void Notify_133()
        {
            object[] param = new object[1];
            string b = "";
            param[0] = b;
            Runtime.Notify(param);
        }

        public static void Notify_132()
        {
            object[] param = new object[1];
            string b = "!@#%$&^*()_ +!~`";
            param[0] = b;
            Runtime.Notify(param);
        }

        public static void Notify_131()
        {
            object[] param = new object[1];
            byte[] b = {0x31, 0x32, 0x33};
            param[0] = b;
            Runtime.Notify(param);
        }

        public static void Notify_130()
        {
            object[] param = new object[1];
            param[0] = "12345";
            Runtime.Notify(param);
        }
        
        public static void Log_138()
        {
            string param = "";
            Runtime.Log(param);
        }

        public static void Log_137()
        {
            string param = "!@#%$&^*()_ +!~`";
            Runtime.Log(param);
        }

        public static void Log_136(object[] args)
        {
            string param = (string)args[0];
            Runtime.Log(param);
        }

        public static void Log_135()
        {
            string param = "123";
            Runtime.Log(param);
        }

        public static void Log_134()
        {
            string param = "test";
            Runtime.Log(param);
        }

        public static bool GetCheckWitness(byte[] Pubkey)
        {
            return Runtime.CheckWitness(Pubkey);
        }

        public static object GetScriptContainer()
        {
            return ExecutionEngine.ScriptContainer;
        }

        public static object GetExecutingScriptHash()
        {
            return ExecutionEngine.ExecutingScriptHash;
        }

        public static object GetEntryScriptHash()
        {
            return ExecutionEngine.EntryScriptHash;
        }

        public static object GetCallingScriptHash()
        {
            return ExecutionEngine.CallingScriptHash;
        }

        public static object GetStorageContext(object[] args)
        {
            byte[] script_hash = (byte[]) args[0];
            Contract con = Blockchain.GetContract(script_hash);

            return con.StorageContext;
        }

        public static TransactionAttribute[] GetTransactionAttribute_Usage(byte[] txid,int index)
        {
            Block block = GetBlockByHeight(index);
            Transaction tran = block.GetTransactions()[0];
            TransactionAttribute[] attr = tran.GetAttributes(); 
            return attr;
        }

        public static TransactionAttribute[] GetTransaction_Attributes(byte[] txid)
        {
            Transaction tran = Blockchain.GetTransaction(txid);
            TransactionAttribute[] attr = tran.GetAttributes(); 
            return attr;
        }

        public static TransactionAttribute[] GetTransactionAttribute_Data(byte[] txid,int index)
        {
            Transaction tran = Blockchain.GetTransaction(txid);
            TransactionAttribute[] attr = tran.GetAttributes(); 
            return attr;
        }

        public static byte GetTransaction_Type(byte[] txid)
        {
            Transaction tran = Blockchain.GetTransaction(txid);
            return tran.Type;
        }

        public static byte[] GetTransaction_Hash(byte[] txid)
        {
            Transaction tran = Blockchain.GetTransaction(txid);
            return tran.Hash;
        }

        public static TransactionAttribute[] GetTransaction_Attribute(byte[] txid)
        {
            Transaction tran = Blockchain.GetTransaction(txid);
            TransactionAttribute[] attr = tran.GetAttributes(); 
            return attr;
        }

        public static StorageContext GetContract_StorageContext(byte[] script_hash)
        {
            Contract cont = Blockchain.GetContract(script_hash);
            return cont.StorageContext;
        }

        public static byte[] GetContract_Script(byte[] script_hash)
        {
            Contract cont = Blockchain.GetContract(script_hash);
            return cont.Script;
        }

        public static Contract GetContract_Migrate(byte[] script,bool flag, string name, string version, string author, string email, string desc)
        {
            Contract cre = Contract.Migrate(script,flag,name,version,author,email,desc);
            return cre;
        }

        public static bool GetContract_Destroy()
        {
             Contract.Destroy();
             return true;
        }

        public static Contract GetContract_Create(byte[] script,bool flag, string name, string version, string author, string email, string desc)
        {
            Contract cre = Contract.Create(script,flag,name,version,author,email,desc);
            return cre;
        }

        public static uint GetHeight()
        {
            return Blockchain.GetHeight();
        }

        public static Header GetHeader(object height)
        {
            uint _height = (uint)height;
            return Blockchain.GetHeader(_height);
        }

        public static Block GetBlock(object hash)
        {
            byte[] _hash = (byte[])hash;
            return Blockchain.GetBlock(_hash);
        }

        public static Transaction GetTransaction(object txid)
        {
            byte[] _txid = (byte[])txid;
            return Blockchain.GetTransaction(_txid);
        }

        public static Contract GetContract(object script_hash)
        {
            byte[] _script_hash = (byte[])script_hash;
            return Blockchain.GetContract(_script_hash);
        }

        public static byte[] GetHeaderHash(object height)
        {
            uint _height = (uint)height;
            Header header = Blockchain.GetHeader(_height);
            return header.Hash;
        }

        public static uint GetHeaderVersion(object height)
        {
            uint _height = (uint)height;
            Header header = Blockchain.GetHeader(_height);
            return header.Version;
            return 1;
        }

        public static byte[] GetHeaderPrevHash(object height)
        {
            uint _height = (uint)height;
            Header header = Blockchain.GetHeader(_height);
            return header.PrevHash;
        }

        public static uint GetHeaderIndex(object height)
        {
            Header header = GetHeader(height);
            return header.Index;
            return 1;
        }

        public static byte[] GetHeaderMerkleRoot(object height)
        {
            Header header = GetHeader(height);
            return header.MerkleRoot;
        }

        public static uint GetHeaderTimestamp(object height)
        {
            Header header = GetHeader(height);
            return header.Timestamp;
        }

        public static ulong GetHeaderConsensusData(object height)
        {
            Header header = GetHeader(height);
            return header.ConsensusData;
        }

        public static byte[] GetHeaderNextConsensus(object height)
        {
            Header header = GetHeader(height);
            return header.NextConsensus;
        }
        
        public static int GetBlockTransactionCount(object height)
        {
            Block block = GetBlockByHeight(height);
            return block.GetTransactionCount();
        }

        public static Transaction[] GetBlockTransactions(object height)
        {
            Block block = GetBlockByHeight(height);
            return block.GetTransactions();
        }

        public static Transaction GetBlockTransaction_40(object height, object index)
        {
            Block block = GetBlockByHeight((int)height);
            int _index = (int)index;
            return block.GetTransaction(_index);
        }

        public static Transaction GetBlockTransaction_44(object height)
        {
            Block block = GetBlockByHeight(height);
            int count = block.GetTransactionCount();
            return block.GetTransaction(count-1);
        }

        public static Transaction GetBlockTransaction_45(object height)
        {
            Block block = GetBlock(height);
            int count = block.GetTransactionCount();
            return block.GetTransaction(count);
        }
        
        public static Header GetHeaderByHeight(object height)
        {
            uint _height = (uint)height;
            return Blockchain.GetHeader(_height);
        }

        public static Block GetBlockByHeight(object height)
        {
            uint _height = (uint)height;
            Header header = Blockchain.GetHeader(_height);
            Block block = Blockchain.GetBlock(header.Hash);
            return block;
        }
    }
}