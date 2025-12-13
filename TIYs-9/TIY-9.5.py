# Date: 17 november 2025
# Name: Riyyan

# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called increment_login
# _attempts() that increments the value of login_attempts by 1. Write another
# method called reset_login_attempts() that resets the value of login_attempts
# to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was 
# incremented properly, and then call reset_login_attempts(). 
# Print login_attempts again to make sure it was reset to 0.

class User:
    '''models a user'''

    def __init__(self,first_name,last_name):
        '''assigns values to attributes when arguments upon creating objects'''
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        '''prints summary of user's information'''
        print(f"User's first name: {self.first_name}")
        print(f"User's last name: {self.last_name}")

    def greet_user(self):
        '''prints greeting to user'''
        print(f"Hello, {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        '''increments the value of login_attempts by 1'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        '''resets the value of login_attempts to 0'''
        self.login_attempts = 0

user1 = User("ABC", "XYZ")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"The user has tried to login {user1.login_attempts} times.")

user1.reset_login_attempts()
print(f"Reset the login attempts to {user1.login_attempts} times")