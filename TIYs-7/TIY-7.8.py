# Date: 11 november 2025
# Name: Riyyan

# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of vari-
# ous sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.

sandwich_orders = ['club sandwich', 'grilled cheese','bit','cuban sandwich']
finished_sandwiches = []

while sandwich_orders:
    print(f'I made you {sandwich_orders[-1]}')
    finished_sandwiches.append(sandwich_orders.pop()) 

# print(sandwich_orders)
print('All sandwiches: ')

for sandwich in finished_sandwiches:
    print(f'{finished_sandwiches.index(sandwich) + 1}: {sandwich}')