# Date: 11 november 2025
# Name: Riyyan

# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

age = 1
while age:
    age = abs(int(input('Enter your age: ')))
    if age < 3:
        print('You can watch movie for free.')
    elif 3 <= age <= 12:
        print("Ticket fee is $10.")
    else:
        print('Ticket fee is $15.')