# Date: 11 november 2025
# Name: Riyyan

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

age = 1

# using a conditional test in the while statement
while age != 0:
    age = abs(int(input('Enter your age: ')))
    if age < 3:
        print('You can watch movie for free.')
    elif 3 <= age <= 12:
        print("Ticket fee is $10.")
    else:
        print('Ticket fee is $15.')


#using an active variable to control the loop
active = True
while active:
    age = int(input('Enter your age: '))
    if age == 0:
        active = False
    elif age < 3:
        print('You can watch movie for free.')
    elif 3 <= age <= 12:
        print("Ticket fee is $10.")
    else:
        print('Ticket fee is $15.')


# using a break statement to exit the loop
while age:
    age = abs(int(input('Enter your age: ')))
    if age == 0:
        break
    elif age < 3:
        print('You can watch movie for free.')
    elif 3 <= age <= 12:
        print("Ticket fee is $10.")
    else:
        print('Ticket fee is $15.')