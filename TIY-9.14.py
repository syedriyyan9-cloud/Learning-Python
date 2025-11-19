# Date: 19 november 2025
# Name: Riyyan

# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and
# five letters. Randomly select four numbers or letters from the list and printa
# message saying that any ticket matching these four numbers or letters wins a
# prize.

from random import choice

lottery_values = [number for number in range(0,10)]
lottery_values.extend(letter for letter in "ABCDE")

ticket = str(choice(lottery_values))
for lotter_value in range(1,4):
    ticket += str(choice(lottery_values))
    
print(f"Ticket matching this number wins a prize: {ticket}")



