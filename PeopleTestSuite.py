import unittest

from AllTests.TestAddShift import TestAddShift

from AllTests.TestAllEmails import TestAllEmails

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestAllEmails))
    suite.addTest(unittest.makeSuite(TestAddShift))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()