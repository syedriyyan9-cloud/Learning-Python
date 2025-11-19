'''A set of classes to represent Admin'''


from Users import User

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