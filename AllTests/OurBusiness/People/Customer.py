class Customer:
    emails=[]
    def __init__(self, firstName, lastName, customerID, email):
        self.firstName = firstName
        self.lastName = lastName
        self.customerID = customerID
        self.email = email
        Customer.emails.append(email)
		
        

		
def allEmails():
	"""
	Returns a list containing all of the customer's email
	"""
	return Customer.emails