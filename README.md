### Group members:
***Harjot Nijjar, Matthias Lee***


## Travis CI Status:
[![Build Status](https://travis-ci.com/matthiaslmz/data533-lab4-MatthiasHarjot.svg?branch=master)](https://travis-ci.com/matthiaslmz/data533-lab4-MatthiasHarjot)  
-------------
## Path to functions with exceptions:
OurBusiness -> People -> Staff -> addShift()

OurBusiness -> Finances -> Sales -> totalSales()

OurBusiness -> Finances -> Expenses -> totalExpenses()

--------------
## OurBusiness (package)


#### Subpackage 1 - **People**

Function 1: `addShift(Shift)`

>Adds a Shift to list of shifts for a given employee or manager

* Input: Shift, which is an integer corresponding to a specific shift (see documentation)
* Output: none

Function 2: `allEmails()`

* Input: None
* Output: Returns a list of strings that contains the emails of all customers

---

#### Subpackage 2 - **Finances**

Function 1: `totalExpenses()`

* Input: none
* Output: Returns the cost of all expenses incurred so far as a float

Function 2: `totalSales()`
* Input: none
* Output: returns the total amount of sales so far as a float
