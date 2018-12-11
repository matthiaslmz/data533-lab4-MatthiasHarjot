class Staff:
    def __init__(self, firstName, lastName, employeeID):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeID = employeeID
        
class Owner(Staff):
    def __init__(self, firstName, lastName, employeeID):
        Staff.__init__(self, firstName, lastName, employeeID)
        
class Manager(Staff):
    def __init__(self, firstName, lastName, employeeID, employeesManaged=[], shifts=[]):
        Staff.__init__(self, firstName, lastName, employeeID)
        self.shifts=shifts
        self.employeesManaged=employeesManaged
    
    def addShift(self,shift):
        """
        Adds this shifts to the shifts of a Manager 
        """
        self.shifts.append(shift)
        
class OtherEmployee(Staff):
    def __init__(self, firstName, lastName, employeeID, managerID, shifts=[]):
        Staff.__init__(self, firstName, lastName, employeeID)
        self.shifts=shifts
        self.managerID=managerID
        
    def addShift(self,shift):
        """
        Adds shifts to the shifts of an OtherEmployee 
        """
        self.shifts.append(shift)