class Employee:
    '''a class to represent an employee'''

    def __init__(self, first_name, last_name, annual_salary):
        '''constructor to store valeus given in parameters'''
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary

    def give_raise(self, increment = 5_000):
        '''increments salary by 5,000 as default, but can take other values'''
        self.annual_salary += increment