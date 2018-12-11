Group members:
* Harjot Nijjar
* Matthias Lee




# Package: **ourBusiness**
---

**ourBusiness** is a python package that enables us to track our staff, customers, business expenses and sales. 

## Subpackage 1: **People**

### Module 1: **Staff**
* **`Staff`** class 
    * Parameters   
        * `firstName` - string
        * `lastName` - string
        * `employeeID` - integer
* **`Owner`** subclass of Staff 
    * Parameters
        * `firstName` - string
        * `lastName` - string
        * `employeeID` - integer
    
* **`Manager`** subclass of Staff
    * Parameters
        * `firstName` - string
        * `lastName` - string
        * `employeeID` - integer
        * `employeesManaged` - list of integers 
        * `shifts` - list of integers \**
    * Functions
        * `addShift(shift)` : 
            * shift : integer
            > Adds this shift to the shifts of a Manager

* **`OtherEmployee`** subclass of Staff
    * Parameters
        * `firstName` - string
        * `lastName` - string
        * `employeeID` - integer
        * `managerID` - integer 
        * `shifts` - list of integers \**
    * Functions
        * `addShift(shift)` : 
            * shift : int 
            > Adds this shift to the shifts of an OtherEmployee

### Module 2: Customer

* **`Customer`** class
    * Parameters
        * `firstName` - string
        * `lastName` - string
        * `customerID` - integer
        * `email` - string
        
* Functions
    * `allEmails()` : 
        > Retuns a list of strings containing all customer emails
    

### Subpackage 2: **Finances**
------
### Module 1: **Expenses**
* **`Expense`** class that takes parameters 
    * Parameters    
        * `name` - string
        * `cost` - float
        * `expenseDate` - string of format MM-DD-YYYY (ex. '10-15-2010')
        * `employeeID` - integer

* Functions
    * `totalExpenses()` : 
        > returns the total expenses by staff as a float

### Module 2: **Sales**
* **`Sale`** class 
    * Parameters    
        * `itemName` - string
        * `cost` - float
        * `saleDate` - string of format MM-DD-YYYY (ex. '10-15-2010')
        * `employeeID` - integer
        * `customerID` - integer


\** shifts are integers that correspond to different work shifts throughout the week:

| Integer | Shift Day | Start Time | End Time |
|--- | --- | --- | --- |
| 1 | Monday | 8:00AM | 12:00PM |
| 2 | Monday | 12:00PM | 4:00PM |
| 3 | Monday | 4:00PM | 8:00PM |
| 4 | Tuesday | 8:00AM | 12:00PM |
| 5 | Tuesday | 12:00PM | 4:00PM |
| 6 | Tuesday | 4:00PM | 8:00PM |
| 7 | Wednesday | 8:00AM | 12:00PM |
| 8 | Wednesday | 12:00PM | 4:00PM |
| 9 | Wednesday | 4:00PM | 8:00PM |
| 10 | Thursday | 8:00AM | 12:00PM |
| 11 | Thursday | 12:00PM | 4:00PM |
| 12 | Thursday | 4:00PM | 8:00PM |
| 13 | Friday | 8:00AM | 12:00PM |
| 14 | Friday | 12:00PM | 4:00PM |
| 15 | Friday | 4:00PM | 8:00PM |
