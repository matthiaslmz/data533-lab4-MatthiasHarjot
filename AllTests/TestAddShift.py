import unittest
from OurBusiness.People import Staff



class TestAddShift(unittest.TestCase):
    @classmethod    
    def setUpClass(cls):
        print('setupClass')
        
    def setUp(self):
        self.E1 = Staff.OtherEmployee('Chris', "Cross", 4, 2, [1,5])
        self.M1 = Staff.Manager('Jill', 'Volley', 2, [4,5], [])
        print('Set up')

    def tearDown(self):
        print('Tear Down')

    def test_add_shift(self):
        self.assertEqual(self.E1.shifts ,[1,5])
        self.E1.addShift(6)
        self.assertEqual(self.E1.shifts ,[1,5,6])
        self.assertEqual(self.M1.shifts , [])
        self.M1.addShift(1)
        self.assertEqual(self.M1.shifts, [1])
        self.M1.addShift(5)
        self.assertEqual(self.M1.shifts, [1,5])
        self.M1.addShift(-5)
        self.assertEqual(self.M1.shifts, [1,5])
        self.M1.addShift(5.00)
        self.assertEqual(self.M1.shifts, [1,5])

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    
unittest.main(argv=[''], verbosity=2, exit=False) 