'''
Created on 02-Jul-2018

@author: adityaj
'''
import unittest
import os
import HTMLTestRunner
from Testcases import FirstTest
 
direct = os.getcwd()
 
class MyTestSuite(unittest.TestCase):
 
    def test_Issue(self):
 
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(FirstTest.PracticeFormTest),
        ])
 
        outfile = open(direct + "\SmokeTest.html", "w")
 
        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description='Smoke Tests'
        )
 
        runner1.run(smoke_test) 
 
if __name__ == '__main__':
    print('Running automated testing demo')
    result = unittest.main().result
    print(result)