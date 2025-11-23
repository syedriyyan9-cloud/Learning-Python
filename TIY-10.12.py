# Date: 23 november 2025
# Name: Riyyan

# 10-12. Favorite Number Remembered: Combine the two programs from
# Exercise 10-11 into one file. If the number is already stored, report the 
# favorite number to the user. If not, prompt for the user’s favorite number 
# and store it in a file. Run the program twice to see that it works.

import json

filename = 'favorite_num.json'

try:
    with open(filename, 'r') as file:
        favorite_num = json.load(file)

except FileNotFoundError:
    favorite_num = int(input("Enter your favorite number: "))
    with open(filename,'w') as file:
        json.dump(favorite_num, file)
    print(f"We will remember your favorite number")

else:
    print(f"I know your favorite number! It's {favorite_num}")

