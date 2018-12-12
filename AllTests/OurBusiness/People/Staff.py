class NonPositiveNumberError(Exception):
    pass

class NonIntegerError(Exception):
    pass


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
        try:
            if shift <= 0:
                raise NonPositiveNumberError()
            elif type(shift) != int:
                raise NonIntegerError()
            self.shifts.append(shift)    
            
        except NonPositiveNumberError:
            print("Shifts are non-negative integers starting from 1")
        except NonIntegerError:
            print("Shift must be an integer")
        
        
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