# Date: 18 november 2025
# Name: Riyyan

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class
# you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). 
# Either version of the class will work; just pick the one you like better. 
# Add an attribute called flavors that stores a list of ice cream flavors. 
# Write a method that displays these flavors. 
# Create an instance of IceCreamStand, and call this method.

class Restaurant:
    '''a class to represent a restaurant'''

    def __init__(self, restaurant_name, cuisine_type):
        '''method that assign values to parameters when creating an object'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''prints attributes'''
        print(f"{self.restaurant_name} and it serves {self.cuisine_type}")

    def open_restaurant(self):
        '''prints restaurant is open'''
        print("The restaurant is Open!")

class IceCreamStand(Restaurant):
    '''a child class that represent a restaurant that has icecream'''
    def __init__(self,restaurant_name, cuisine_type):
        '''creates object for icreamstand class'''
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Strawberry", "Mango", "Peach", "Kulfa"]

    def list_flavors(self):
        '''prints all the flavors available'''
        print("We have the following flavors available: ")
        for flavor in self.flavors:
            print(flavor)

icecream = IceCreamStand("Ice Cream Stand","Icecream")
icecream.list_flavors()