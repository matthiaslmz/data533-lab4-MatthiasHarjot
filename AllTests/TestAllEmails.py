import unittest
from OurBusiness.People import Customer


class TestAllEmails(unittest.TestCase):
    @classmethod    
    def setUpClass(cls):
        print('setupClass')
        
    def setUp(self):
        print('Set up')

    def tearDown(self):
        Customer.Customer.emails=[]
        print('Tear Down')

    def test_all_emails(self):
        self.assertEqual(Customer.allEmails() ,[])
        self.C1 = Customer.Customer('holly', 'jolly', 123, 'hollyjolly@jolly.ca')
        self.assertEqual(Customer.allEmails() ,['hollyjolly@jolly.ca'])
        self.C2 = Customer.Customer('noway', 'jose', 124, 'jose@jose.ca')
        self.assertEqual(Customer.allEmails() ,['hollyjolly@jolly.ca','jose@jose.ca'])                                    
        self.C3 = Customer.Customer('hi', 'bye', 333, 'hi@hi.ca')                                    
        self.assertEqual(Customer.allEmails() ,['hollyjolly@jolly.ca','jose@jose.ca','hi@hi.ca'])
        self.C4 = Customer.Customer('hi1', 'bye1', 335, 'hi2@hi.ca')                                    
        self.assertEqual(Customer.allEmails() ,['hollyjolly@jolly.ca','jose@jose.ca','hi@hi.ca','hi2@hi.ca'])
        self.C3 = Customer.Customer('nooo', 'yesss', 60000, 'yes@no.com')                                    
        self.assertEqual(Customer.allEmails() ,['hollyjolly@jolly.ca','jose@jose.ca','hi@hi.ca','hi2@hi.ca','yes@no.com']) 

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    
unittest.main(argv=[''], verbosity=2, exit=False) 