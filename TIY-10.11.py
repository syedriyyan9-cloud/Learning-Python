# Date: 23 november 2025
# Name: Riyyan

# 10-11. Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dump() to store this number in a file. Write a separate pro-
# gram that reads in this value and prints the message, “I know your favorite
# number! It’s _____.”

import json

filename = 'favorite_num.json'

favorite_num = int(input("Enter your favorite number: "))

with open(filename,'w') as file:
    json.dump(favorite_num, file)

with open(filename, 'r') as file:
    favorite_num = json.load(file)

print(f"I know your favorite number! It's {favorite_num}")