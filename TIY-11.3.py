# Date: 27 november 2025
# Name: Riyyan

# 11-3. Employee: Write a class called Employee. The __init__() method should
# take in a first name, a last name, and an annual salary, and store each of 
# these as attributes. Write a method called give_raise() that adds $5000 to the
# annual salary by default but also accepts a different raise amount.
# Write a test case for Employee. Write two test methods, test_give_default
# _raise() and test_give_custom_raise(). Use the setUp() method so you don’t
# have to create a new employee instance in each test method. Run your test
# case, and make sure both tests pass.

# class Employee:
#     '''a class to represent an employee'''

#     def __init__(self, first_name, last_name, annual_salary):
#         '''constructor to store valeus given in parameters'''
#         self.first_name = first_name
#         self.last_name = last_name
#         self.annual_salary = annual_salary

#     def give_raise(self, increment = 5_000):
#         '''increments salary by 5,000 as default, but can take other values'''
#         self.annual_salary += increment

# the same class is present in Employee_class.py and is imported in
# Test_Employee_Class.py for testing.