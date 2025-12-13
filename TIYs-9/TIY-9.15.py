# Date: 19 november 2025
# Name: Riyyan

# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
# the kind of lottery you just modeled. Make a list or tuple called my_ticket.
# Write a loop that keeps pulling numbers until your ticket wins. Print a message
# reporting how many times the loop had to run to give you a winning ticket.

from random import choice

def lottery(lottery_values):
    ticket = str(choice(lottery_values))
    for value in range(1,4):
        ticket += str(choice(lottery_values))
    return ticket

lottery_values = [number for number in range(0,10)]
lottery_values.extend(letter for letter in "ABCDE")

my_ticket = []

ticket = lottery(lottery_values)

while True:
    my_ticket_num = lottery(lottery_values)
    my_ticket.append(my_ticket_num)
    if my_ticket_num == ticket:
        print("You won the lottery")
        print(f"Attempts: {len(my_ticket)}")
        break

