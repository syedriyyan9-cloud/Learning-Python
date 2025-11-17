# Date: 17 november 2025
# Name: Riyyan

# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.

# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.

# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any num-
# ber you like that could represent how many customers were served in, say, a
# day of business.

class Restaurant:
    '''a class to represent a restaurant'''

    def __init__(self, restaurant_name, cuisine_type):
        '''method that assign values to parameters when creating an object'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_servered = 0

    def describe_restaurant(self):
        '''prints attributes'''
        print(f"{self.restaurant_name} and it serves {self.cuisine_type}")

    def open_restaurant(self):
        '''prints restaurant is open'''
        print("The restaurant is Open!")

    def set_number_served(self, number):
        '''sets the number servered to any value'''
        if number > 0 and number >= self.number_servered:
            self.number_servered = number
    
    def increment_number_served(self, inc):
        '''increments the number of customers servered in a day'''
        if inc > 0:
            self.number_servered += inc

my_restaurant = Restaurant('xyz','abc')
print(f"The restaurant has served: {my_restaurant.number_servered} customers")

my_restaurant.set_number_served(10)
print(f"The restaurant has served: {my_restaurant.number_servered} customers")

my_restaurant.increment_number_served(2)
my_restaurant.increment_number_served(2)
my_restaurant.increment_number_served(2)
print(f"The restaurant has served: {my_restaurant.number_servered} customers")

