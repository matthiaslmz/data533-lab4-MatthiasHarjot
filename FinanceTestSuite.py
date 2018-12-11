import unittest

from AllTests.TestExpenses import TestTotalExpenses

from AllTests.TestSales import TestTotalSales

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestTotalExpenses))
    suite.addTest(unittest.makeSuite(TestTotalSales))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()