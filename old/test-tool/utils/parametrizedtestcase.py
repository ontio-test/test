# -*- coding:utf-8 -*-
import unittest

class ParametrizedTestCase(unittest.TestCase):    
    """ TestCase classes that want to be parametrized should  
        inherit from this class.  
    """    

    def __init__(self, methodName='runTest', param=None):    
        super(ParametrizedTestCase, self).__init__(methodName)    
        self.param = param  