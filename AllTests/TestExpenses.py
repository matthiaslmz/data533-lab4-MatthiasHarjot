import unittest
from OurBusiness.Finances import Expenses



class TestTotalExpenses(unittest.TestCase):
    @classmethod    
    def setUpClass(cls):
        print('setupClass')
		
    def setUp(self):
        print('Set up')

    def tearDown(self):
        Expenses.Expense.totalExpenses=0
        print('Tear Down')

    def test_total_expenses(self):
        self.assertEqual(Expenses.totalExpenses(), 0)
        self.EXP1 = Expenses.Expense('printer',69.69,'11-28-2018',1)
        self.assertEqual(Expenses.totalExpenses(), 69.69)        
        self.EXP2 = Expenses.Expense('dog',1750.00,'11-27-2018',2)
        self.assertEqual(Expenses.totalExpenses(), 1819.69)
        self.EXP3 = Expenses.Expense('tank',1.00,'11-29-2018',4)        
        self.assertEqual(Expenses.totalExpenses(), 1820.69)
        self.EXP4 = Expenses.Expense('plane',100.00,'11-29-2018',4)
        self.assertEqual(Expenses.totalExpenses(), 1920.69)

    
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    
unittest.main(argv=[''], verbosity=2, exit=False) 