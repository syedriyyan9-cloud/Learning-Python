# Date: 17 november 2025
# Name: Riyyan

# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.

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

my_restaurant = Restaurant("Macdonalds","fast food")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()
