# Date: 11 november 2025
# Name: Riyyan

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwich_orders = ['club sandwich', 'grilled cheese','bit','cuban sandwich']

sandwich_orders.insert(2,'pastrami')
sandwich_orders.insert(0,'pastrami')
sandwich_orders.insert(-1,'pastrami')

print(f"Deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = sandwich_orders[:] 
