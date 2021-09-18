# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right')
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')
    
    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(7,7,7),'Equilateral')
    
    def testInvalidInputsA(self): 
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput')

    def testInvalidInputsB(self): 
        self.assertEqual(classifyTriangle(201,201,201),'InvalidInput')
    
    def testInvalidInputsC(self): 
        self.assertEqual(classifyTriangle(-3,-4,-5),'InvalidInput')
    
    def testNotATriangleA(self): 
        self.assertEqual(classifyTriangle(28,10,18),'NotATriangle')

    def testNotATriangleB(self): 
        self.assertEqual(classifyTriangle(7,5,12),'NotATriangle')

    def testNotATriangleC(self): 
        self.assertEqual(classifyTriangle(35,23,12),'NotATriangle')

    def testScaleneTrianglesA(self): 
        self.assertEqual(classifyTriangle(12,13,11),'Scalene')
    
    def testScaleneTrianglesB(self): 
        self.assertEqual(classifyTriangle(5,10,14),'Scalene')

    def testScaleneTrianglesC(self): 
        self.assertEqual(classifyTriangle(91,32,74),'Scalene')

    def testIsocelesTrianglesA(self): 
        self.assertEqual(classifyTriangle(7,4,7),'Isoceles')

    def testIsocelesTrianglesB(self): 
        self.assertEqual(classifyTriangle(9,9,5),'Isoceles')
    
    def testIsocelesTrianglesC(self): 
        self.assertEqual(classifyTriangle(18,8,18),'Isoceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

