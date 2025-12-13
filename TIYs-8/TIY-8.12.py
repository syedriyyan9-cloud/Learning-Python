# Date: 14 november 2025
# Name: Riyyan

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sand-
# wich that’s being ordered. Call the function three times, using a different num-
# ber of arguments each time.

def items_in_sandwich(*items):
    '''collects the items a user wants in a sandwich and prints these items'''
    print(items)

items_in_sandwich('chicken')
items_in_sandwich('beef', 'cheese', 'egg')
items_in_sandwich('ketchup','mayo','cheese','tomatoes','chicken')