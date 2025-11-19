'''a set of classes to represent users, admins and privileges'''

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

class Privileges:
    '''class that represents the privileges an admin can have'''
    
    def __init__(self):
        '''initializes the privileges an admin can have'''
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

class Admin(User):
    '''child class that inherits from User class'''
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name,last_name)
        self.privileges = Privileges()