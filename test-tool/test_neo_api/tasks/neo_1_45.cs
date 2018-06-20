using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using Neo.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;

namespace Neo.SmartContract
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
            else
            {
                return false;
            }
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
            Block block = GetBlockByHeight(height);
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