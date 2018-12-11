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
    return Expense.totalExpenses