package com.ontio.testtool.api;

public class ApiManager {
	static ContractApi contract = null;
	static NodeApi node = null;

	public ContractApi contract() {
		if (contract == null) {
			contract = new ContractApi();
		}
		
		return contract;
	}
	 
	public NodeApi node() {
		if (node == null) {
			node = new NodeApi();
		}
		
		return node;
	}
}
