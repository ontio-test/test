import sys
sys.path.append('..')
sys.path.append('../..')

from utils.config import Config
class test_config():

	node_self = 5
	ontID_self_pubKey = Config.NODES[node_self]["pubkey"]
	#ontid_map[node_self] = ontID_self_pubKey

	node_A = 1
	ontID_A_pubkey = Config.NODES[node_A]["pubkey"]
	#ontid_map[ontID_A] = ontID_A_pubkey

	node_B = 6
	ontID_B_pubkey = Config.NODES[node_B]["pubkey"]
	#ontid_map[ontID_B] = ontID_B_pubkey
	####################################################
	#config
	tc001_ontid="did:ont:AR72FVnZZ8EfeyyhGobEVWox9jwd7Uqe8d"
	tc002_ontid="did:ont:AQhDgYDY42AwfBdRDu1Wnf224EXKQ5ypGc"
	tc002_ontid2="did:ont:AGuu4L6LQiBGtCNXaCm35mDJGX6Hf1Fdev"
	tc003_ontid="did:ont:AR7jzsPWSqJTM7hf41jDbTVUgpurVGBvfk"
	tc004_ontid="did:ont:AMrKfXtwdCaxkF8cCGYodz5FXD1GcwbW7M"
	tc001_pubkey1=ontID_A_pubkey
	tc001_pubkey2=ontID_self_pubKey
	tc002_pubkey1=ontID_A_pubkey
	tc002_pubkey2=ontID_self_pubKey
	tc003_pubkey1=ontID_A_pubkey
	tc003_pubkey2=ontID_self_pubKey
	tc004_pubkey1=ontID_A_pubkey
	tc004_pubkey2=ontID_self_pubKey
	tc004_pubkey3=ontID_B_pubkey