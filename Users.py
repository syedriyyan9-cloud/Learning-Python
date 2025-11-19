'''A class to represent Users'''

class User:
    '''models a user'''

    def __init__(self,first_name,last_name):
        '''assigns values to attributes when arguments upon creating objects'''
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        '''prints summary of user's information'''
        print(f"User's first name: {self.first_name}")
        print(f"User's last name: {self.last_name}")

    def greet_user(self):
        '''prints greeting to user'''
        print(f"Hello, {self.first_name} {self.last_name}")