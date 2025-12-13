# Date: 11 november 2025
# Name: Riyyan

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

toppings = ''

while toppings != 'quit':
    toppings = input('Enter toppings you want on pizza: ')
    if toppings != 'quit':
        print(f"{toppings} have been added to your pizza.")

