package com.ontio.testtool.utils;

public class OntTestException extends Exception {
	private static final long serialVersionUID = 1110386521472879043L;
	
	public OntTestException(String message) {
		super(message);
	}
	
	public OntTestException(String message, Throwable ex) {
		super(message, ex);
	}
}
 