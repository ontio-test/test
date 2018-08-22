package com.ontio;

import java.util.HashSet;
import java.util.Set;

import org.junit.runner.Description;
import org.junit.runner.manipulation.Filter;

public class MethodNameFilter extends Filter {
    private final Set<String> excludedMethods = new HashSet<String>();
    private final Set<String> includeSheets = new HashSet<String>();
    private final Set<String> includeTypes = new HashSet<String>();
    private final Set<String> filterCases = new HashSet<String>();
    private final Set<String> includeClasses = new HashSet<String>();
    
    public MethodNameFilter(Set<String> includeSheets, Set<String> includeTypes, Set<String> filterCases, Set<String> excludedMethods, Set<String> includeClasses) {
        if (excludedMethods != null && excludedMethods.size() != 0){
        	for(String method : excludedMethods) {
                this.excludedMethods.add(method);
            }
        }
        
        if (includeSheets != null && includeSheets.size() != 0){
        	for(String includeSheet : includeSheets) {
                this.includeSheets.add(includeSheet);
            }
        }
        
        if (includeTypes != null && includeTypes.size() != 0){
        	for(String includeType : includeTypes) {
                this.includeTypes.add(includeType);
            }
        }
        
        if (filterCases != null && filterCases.size() != 0){
        	for(String filterCase : filterCases) {
                this.filterCases.add(filterCase);
            }
        }
        
        if (includeClasses != null && includeClasses.size() != 0){
        	for(String includeClass : includeClasses) {
                this.includeClasses.add(includeClass);
            }
        }
    	
    }
    
    @Override
    public boolean shouldRun(Description description) {
    	
        String methodName = description.getMethodName();
                
        if (methodName.equals("test_init")) {
        	return true;
    	}
        
        if (!excludedMethods.isEmpty() && excludedMethods.contains(methodName)){
        	return false;
    	}
        
        String[] typeLen = description.getClassName().split("\\.");
    	String m_file = typeLen[typeLen.length-1].toString();
    	
    	if (filterCases.isEmpty() && (includeTypes.isEmpty() || includeTypes.contains(methodName.split("_")[1].toString()))) {
    		if (includeSheets.isEmpty() || includeSheets.contains(m_file)) {
    			return true;
    		}
    	}
    	
    	if (includeTypes.isEmpty() && (filterCases.isEmpty() || (filterCases.contains(methodName) && includeClasses.contains(m_file)))) {
    		if (includeSheets.isEmpty() || includeSheets.contains(m_file)) {
    			return true;
    		}
    	}
        return false;
        
    }
    
    @Override
    public String describe() {
        return "";
    }
    
}