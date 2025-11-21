# Date: 21 november 2025
# Name: Riyyan

# 10-4. Guest Book: Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry appears on a
# new line in the file.

guest_no = 0
while True:
    name = input("Enter your name(press 'q' to quit): ")
    if name.lower() == 'q':
        break
    print(f"Hello, {name.capitalize()}")
    guest_no += 1
    with open('guest_book.txt','a') as file:
        file.write(f"{guest_no}: {name}\n")
    
