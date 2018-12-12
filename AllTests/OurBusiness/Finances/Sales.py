class NegativeNumberError(Exception):
    pass

class NonFloatError(Exception):
    pass

class Sale:
    totalSales=0
    def __init__(self, itemName, cost, saleDate, employeeID, customerID):
        self.itemName = itemName
        self.cost = cost
        self.saleDate = saleDate
        self.employeeID = employeeID
        self.customerID = customerID
        Sale.totalSales += cost 
        

def totalSales():
    """
    Returns the total sales
    """
    try:
        if Sale.totalSales < 0:
            raise NegativeNumberError()
        elif type(Sale.totalSales) != float and Sale.totalSales != 0:
            raise NonFloatError()
        return Sale.totalSales    
        
    except NegativeNumberError:
        print("Negative expenses does not make sense")
    except NonFloatError:
        print("Cost of products must be entered as float")
