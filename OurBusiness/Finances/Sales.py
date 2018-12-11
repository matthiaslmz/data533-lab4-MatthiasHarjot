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
    return Sale.totalSales