import sys

sys.path.append('..')
sys.path.append('../..')

from api.nativecontract import NativeApi
from api.contract import ContractApi
from api.node import NodeApi
from api.restful import RestfulApi
from api.rpc import RPCApi
from api.websocket import WebSocketApi

class APIManager():
	#Singleton
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(APIManager, cls).__new__(cls)
		return cls.instance

	def __init__(self):
		self.nodeapi = NodeApi()
		self.contractapi = ContractApi()
		self.nativecontractapi = NativeApi()
		self.restfulapi = RestfulApi()
		self.rpcapi = RPCApi()
		self.websocketapi = WebSocketApi()

	def contract(self):
		return self.contractapi;

	def node(self):
		return self.nodeapi;

	def native(self):
		return self.nativecontractapi;

	def rpc(self):
		return self.rpcapi;

	def restful(self):
		return self.restfulapi;

	def ws(self):
		return self.websocketapi;

API = APIManager()