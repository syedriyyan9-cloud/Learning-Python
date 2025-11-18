# Date: 18 november 2025
# Name: Riyyan

# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

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

class Admin(User):
    '''child class that inherits from User class'''
    def __init__(self, first_name, last_name):
        super().__init__(first_name,last_name)
        self.privileges = [
                    "can add post", "can delete post", 
                    "can ban user", "can update post",
                    "can remove user",
                    ]
        
    def show_privileges(self):
        '''shows all the privileges that an admin can have'''
        print("Admins have the following privilegs")
        for privilege in self.privileges:
            print(privilege)

admin = Admin("riyyan", "Hassan")
admin.show_privileges()