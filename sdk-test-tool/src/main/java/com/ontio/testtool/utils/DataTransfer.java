package com.ontio.testtool.utils;

import java.util.Base64;

public class DataTransfer {
	public byte[] string2salt(String salt) {
		return Base64.getDecoder().decode(salt);
	}
	
	public String salt2string(byte[] salt) {
		return new String(Base64.getEncoder().encode(salt));
	}
}
 