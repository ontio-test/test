# -*- coding:utf-8 -*-
import unittest

from utils.error import Error

class ParametrizedTestCase(unittest.TestCase):    
    """ TestCase classes that want to be parametrized should  
    inherit from this class.  
    """  
    def __init__(self, methodName='runTest', param=None):
        self.param = param
        self.m_result = "init" #pass, fail, block
        self.m_assertcount = 0
        try:   
            super(ParametrizedTestCase, self).__init__(methodName)
        except Exception as e:
            print(e)

    def setUp(self):
        self.m_assertcount = 0
        pass
                
    def result(self):
        if self.m_result == "init":
            if self.m_assertcount > 0:
                self.m_result = "pass"
            else:
                self.m_result = "block"

        return self.m_result   

    def ASSERT(self, result, info = ""):
        self.m_assertcount = self.m_assertcount + 1
        if not result:
            self.m_result = "fail"
            raise Error(info)

    def BLOCK(self, result, info = ""):
        if not result:
            self.m_result = "block"
            raise Error(info)        