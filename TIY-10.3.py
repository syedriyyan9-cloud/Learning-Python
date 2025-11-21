# Date: 21 november 2025
# Name: Riyyan

# 10-3. Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.

guest_name = input("Enter your name: ")
with open("guest.txt","w") as file:
    file.write(guest_name.capitalize())
