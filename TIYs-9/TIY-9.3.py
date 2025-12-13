# Date: 17 november 2025
# Name: Riyyan

# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically 
# stored in a user profile. Make a method called describe_user() that prints
# a summary of the user’s information. Make another method called greet_user() 
# that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

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

user1 = User("syed", "hassan")
user2 = User("noman", "hassan")
user3 = User("muhammad", "kamran")
user4 = User("awais", "maher")

user1.describe_user()
user1.greet_user()

print()

user2.describe_user()
user2.greet_user()

print()

user3.describe_user()
user3.greet_user()

print()

user4.describe_user()
user4.greet_user()