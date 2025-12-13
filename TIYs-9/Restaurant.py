'''A class that represents Restaurant'''

class Restaurant:
    '''a class to represent a restaurant'''

    def __init__(self, restaurant_name, cuisine_type):
        '''method that assign values to parameters when creating an object'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''prints attributes'''
        print(f"Restaurant: {self.restaurant_name} "
              f"and it serves: {self.cuisine_type}")

    def open_restaurant(self):
        '''prints restaurant is open'''
        print("The restaurant is Open!")