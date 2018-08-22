package com.ontio;

import org.junit.rules.TestName;
import org.junit.runner.Description;

import com.ontio.testtool.OntTest;

public class OntTestWatcher extends TestName {	
    @Override
    protected void starting(Description description) {
		OntTest.logger().open(description.getClassName() + "/" + description.getMethodName() + ".log", description.getMethodName());
    }
    @Override
    protected void failed(Throwable e, Description description) {
    	OntTest.logger().close("fail", e.toString());
    }

	@Override
	protected void succeeded(Description description) {
		OntTest.logger().close("pass", description.toString());
	}
} 
