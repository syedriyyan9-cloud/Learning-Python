# Date: 17 november 2025
# Name: Riyyan

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

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

mc_restaurant = Restaurant("Macdonalds","Fast Food")
subway = Restaurant("Subway", "Sandwiches")
kfc = Restaurant("KFC", "Fried Chicken")

mc_restaurant.describe_restaurant()
print()
subway.describe_restaurant()
print()
kfc.describe_restaurant()
