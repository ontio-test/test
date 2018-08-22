package com.ontio;

import org.junit.runner.Request;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import org.junit.runner.Description;
import org.junit.runner.JUnitCore;

import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import com.ontio.MethodNameFilter;

import com.alibaba.fastjson.JSONObject;
import com.ontio.sdkapi.ClaimBase;
import com.ontio.sdkapi.ClaimRecord;
import com.ontio.sdkapi.DigitalAccount;
import com.ontio.sdkapi.DigitalIdentity;
import com.ontio.sdkapi.Invoke;
import com.ontio.sdkapi.MnemonicCodesStr;
import com.ontio.sdkapi.ONG_Native;
import com.ontio.sdkapi.ONT_Native;
import com.ontio.sdkapi.Ontid;
import com.ontio.sdkapi.RPC_API;
import com.ontio.sdkapi.Restful_API;
import com.ontio.sdkapi.WebSocket_API;
import com.ontio.testtool.OntTest;

import com.ontio.TestMonitor;

public class RunAllTest {
    public static void main(String[] args) throws ClassNotFoundException {
    	OntTest.init();
    	
    	String prarameter_c = "";  
    	String prarameter_t = "";  
    	String prarameter_f = "";  
    	String prarameter_e = "";  
    	
    	int optSetting = 0;  
        for (; optSetting < args.length; optSetting++) {  
            if ("-c".equals(args[optSetting]) || "--config".equals(args[optSetting])) {  
            	prarameter_c = args[++optSetting];  
            } else if ("-t".equals(args[optSetting]) || "--type".equals(args[optSetting])) {  
            	prarameter_t = args[++optSetting];  
            } else if ("-f".equals(args[optSetting]) || "--filter".equals(args[optSetting])) {  
            	prarameter_f = args[++optSetting];  
            } else if ("-e".equals(args[optSetting]) || "--exclude".equals(args[optSetting])) {  
            	prarameter_e = args[++optSetting];  
            }  
        }
        
        // prarameter_t = "base";  
        // prarameter_f = "ClaimRecord.test_normal_002_exportIdentityQRCode";  
        
        // prarameter_c = "C:\\Users\\tpc\\Desktop\\a.json";
        // prarameter_e = "ClaimRecord.test_base_001_exportIdentityQRCode";
        
        Set<String> _classes = new HashSet<String>();
        Set<String> _methods = new HashSet<String>();
        Set<String> _excludes = new HashSet<String>();
        Set<String> _types = new HashSet<String>();
        Set<String> _files = new HashSet<String>();
        
        if (!prarameter_f.equals("")){
        	String[] cases = prarameter_f.split(",");
            for (String _case : cases){
            	_classes.add(_case.split("\\.")[0]);
            	_methods.add(_case.split("\\.")[1]);
            }
        }
        
        if (!prarameter_t.equals("")){
        	if (prarameter_t.equals("base")) {
        		_types.add("base");
        	} else if (prarameter_t.equals("normal")){
        		_types.add("base");
        		_types.add("normal");
        	} else if (prarameter_t.equals("abnormal")){
        		_types.add("abnormal");
        	}
        }
        
        if (!prarameter_e.equals("")){
        	String[] cases = prarameter_e.split(",");
        	for (String _case : cases){
        		_excludes.add(_case.split("\\.")[1]);
            }
        }
        
        if (!prarameter_c.equals("")){	
        	JSONObject _json = OntTest.common().loadJson(prarameter_c);
        	Set<String> keys = _json.keySet();
        	for (String _key : keys) {
        		if (_json.getString(_key).equals("true")) {
        			_files.add(_key);
        		}
        	}
        }
        // System.out.println(_files.toString());
        
        List<Class<?>> all_class = new ArrayList<Class<?>>();
        all_class.add(ClaimBase.class);
        all_class.add(ClaimRecord.class);
        all_class.add(DigitalAccount.class);
        all_class.add(DigitalIdentity.class);
        all_class.add(Invoke.class);
        all_class.add(MnemonicCodesStr.class);
        all_class.add(ONG_Native.class);
        all_class.add(ONT_Native.class);
        all_class.add(RPC_API.class);
        all_class.add(Ontid.class);
        all_class.add(Restful_API.class);
        all_class.add(WebSocket_API.class);
		
        JUnitCore junitRunner = new JUnitCore();
        junitRunner.addListener(new TestMonitor());
        
        double faultTolerance = 1;
        
        for (Class<?> _class : all_class) {
        	int total_cases = 0;
            int failed_cases = 0;
            Result result = null;
        	
	        Request request = Request.aClass(_class);
	        request = request.filterWith(new MethodNameFilter(_files, _types, _methods, _excludes, _classes));
	        
	        // if request is empty, continue
	        if (request.getRunner().getClass().getMethods()[0].getDeclaringClass().toString().toLowerCase().contains("error")) {
	        	continue;
	        }
	        
	        request = request.sortWith(new Comparator<Description>(){
				@Override
				public int compare(Description d1, Description d2) {
					if (d1.getClassName().equals(d2.getClassName())) {
						return d1.getMethodName().split("_")[2].toString().compareTo(d2.getMethodName().split("_")[2].toString());
					} else {
						return d1.getClassName().compareTo(d1.getClassName());
					}
				}
	        });
	        try{
		        long startTime = System.currentTimeMillis();
		        long endtime = startTime;
		        long costtime = 0;
		        SimpleDateFormat dateformat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		        
		        result = junitRunner.run(request);
		        
	            endtime = System.currentTimeMillis();
	            costtime = endtime - startTime;
	            String reportstr ="[time]" + "\n" +
						"start=" + dateformat.format(startTime) + "\n" +
						"end=" + dateformat.format(endtime)  + "\n" +
						"cost=" + (costtime / 1000);
	            String repotepath = OntTest.logger().logfile().getParentFile().getAbsolutePath() + "/report.ini";
				FileWriter reportFileWriter = new FileWriter(repotepath, false);
				reportFileWriter.write(reportstr);
				reportFileWriter.close();
				
				System.out.println(result.wasSuccessful());
	        } catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
	        
	        total_cases = result.getRunCount();
	        System.out.println(result.getRunCount());
	        List<Failure> failedCases = result.getFailures();
	        
	        failed_cases = result.getFailureCount();
	        System.out.println(result.getFailureCount());
	        
	        System.out.println(TestMonitor.blockDescription.isEmpty());
	        if (!TestMonitor.blockDescription.isEmpty()) {
	        	
	        	for (int i = 0; i < TestMonitor.blockDescription.size(); i++){
	        		Description blockDescription = TestMonitor.blockDescription.get(i);
	        		System.out.println("*********");
	        		Request retryRequest = Request.method(blockDescription.getTestClass(), blockDescription.getMethodName());
	        		result = junitRunner.run(retryRequest);
	        		if (!result.wasSuccessful()) {
	        			OntTest.logger().setBlock();
	        		}
	        		
	        		// System.out.println(result.wasSuccessful());
	        	}
	        	TestMonitor.blockDescription.clear();
	    		System.out.println(TestMonitor.blockDescription.isEmpty());
	        }
	        
	        System.out.println(failed_cases / (double)total_cases);
	        
	        if (failed_cases / (double)total_cases > faultTolerance) {
	        	// recover
	    		OntTest.api().node().restartAll();
	        	
	        	for (Failure failedCase : failedCases){
	        		System.out.println(failedCase.getClass().toString());
	        		System.out.println(failedCase.getDescription().getClass().toString());
	        		Request retryRequest = Request.method(failedCase.getDescription().getTestClass(), failedCase.getDescription().getMethodName());
	        		result = junitRunner.run(retryRequest);
	        		if (!result.wasSuccessful()) {
	        			OntTest.logger().setBlock();
	        		}
	        		// System.out.println(result.wasSuccessful());
	        	}
	        }
	        
        }
        
        System.exit(0);
    }
	
}


