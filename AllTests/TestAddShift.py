import unittest
from OurBusiness.People import Staff



class TestAddShift(unittest.TestCase):
    @classmethod    
    def setUpClass(cls):
        print('setupClass')
        
    def setUp(self):
        self.E1 = Staff.OtherEmployee('Chris', "Cross", 4, 2, ['Shift 1', 'Shift 5'])
        self.M1 = Staff.Manager('Jill', 'Volley', 2, [4,5], [])
        print('Set up')

    def tearDown(self):
        print('Tear Down')

    def test_add_shift(self):
        self.assertEqual(self.E1.shifts ,['Shift 1', 'Shift 5'])
        self.E1.addShift('Shift 6')
        self.assertEqual(self.E1.shifts ,['Shift 1', 'Shift 5', 'Shift 6'])
        self.assertEqual(self.M1.shifts , [])
        self.M1.addShift('Shift 1')
        self.assertEqual(self.M1.shifts, ['Shift 1'])
        self.M1.addShift('Shift 5')
        self.assertEqual(self.M1.shifts, ['Shift 1', 'Shift 5'])  


    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    
unittest.main(argv=[''], verbosity=2, exit=False) 