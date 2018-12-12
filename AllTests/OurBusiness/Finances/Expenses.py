
class NegativeNumberError(Exception):
    pass

class NonFloatError(Exception):
    pass

class Expense:
    totalExpenses=0
    def __init__(self, name, cost, expenseDate, employeeID):
        self.name = name
        self.cost = cost
        self.expenseDate = expenseDate
        self.employeeID = employeeID
        Expense.totalExpenses += cost

def totalExpenses():
    """
    Returns the total expenses by employee(s)
    """
    try:
        if Expense.totalExpenses < 0:
            raise NegativeNumberError()
        elif type(Expense.totalExpenses) != float and Expense.totalExpenses!= 0:
            raise NonFloatError()
        return Expense.totalExpenses    
        
    except NegativeNumberError:
        print("Negative expenses does not make sense")
    except NonFloatError:
        print("Cost of products must be entered as float")
