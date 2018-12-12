import unittest
from OurBusiness.Finances import Sales

class TestTotalSales(unittest.TestCase):
    @classmethod    
    def setUpClass(cls):
        print('setupClass')
		
    def setUp(self):
        print('Set up')

    def tearDown(self):
        Sales.Sale.totalSales=0
        print('Tear Down')

    def test_total_sales(self):
        self.assertEqual(Sales.totalSales(), 0)
        self.S1 = Sales.Sale('rooibus tea latte',5.67,'11-28-2018',1,123)
        self.assertEqual(Sales.totalSales(), 5.67)        
        self.S2 = Sales.Sale('americano',3.50,'11-27-2018',5,123)
        self.assertEqual(Sales.totalSales(), 9.17)  
        self.S3 = Sales.Sale('cat toy',4.00,'11-29-2018',1,124)
        self.assertEqual(Sales.totalSales(), 13.17) 
        self.S2 = Sales.Sale('espresso',50.00,'11-30-2018',4,126)        
        self.assertEqual(Sales.totalSales(), 63.17) 
        self.S2 = Sales.Sale('espresso',-1000.00,'11-30-2018', 5, 127)   
        
    def test_total_expenses_nonfloat(self):
        self.S1 = Sales.Sale('rooibus tea latte',5,'11-28-2018',1,123)
        self.assertEqual(Sales.totalSales(), None)
		
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    
unittest.main(argv=[''], verbosity=2, exit=False) 