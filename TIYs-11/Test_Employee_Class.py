import unittest

from Employee_class import Employee

class Test_Employee_Class(unittest.TestCase):
    '''a class to test employee class'''
    
    def setUp(self):
        '''method to create an object to avoid creating it all the time for test'''
        self.employee = Employee('syed','hassan',1_000)

    def test_give_default_raise(self):
        '''test to see if the salary increases by 5000 if no arg is provided'''
        self.employee.give_raise()
        self.assertEqual(6_000,self.employee.annual_salary)

    def test_give_custom_raise(self):
        '''test to see if the salary increase by the desired amount'''
        self.employee.give_raise(10_000)
        self.assertEqual(11_000, self.employee.annual_salary)

if __name__ == '__main__':
    unittest.main()