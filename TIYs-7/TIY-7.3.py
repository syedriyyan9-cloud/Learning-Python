# Date: 8 november 2025
# Name: Riyyan
# 
# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = input('Enter a number and i will guess if it is a multiple of 10: ')
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is a multiple of 10.")
else:
    print(f"The number {number} is not a multiple of 10.")