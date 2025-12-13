# Date: 8 november 2025
# Name: Riyyan
# 
# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message say-
# ing they’ll have to wait for a table. Otherwise, report that their table is ready.

seating = input('How many seats would you like to arrange for dinner: ')
seating = int(seating)

if seating > 8:
    print('You will have to wait fo a table.')
else:
    print('Your table is ready.')