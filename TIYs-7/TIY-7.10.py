# Date: 11 november 2025
# Name: Riyyan

# 7-10. Dream Vacation: Write a program that polls users about their dream vaca-
# tion. Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.

prompt = 'If you could visit one place in the world, where would you go: '
poll = True
response = {}

while poll:
    key = input("What is your name? ")
    value = input(prompt)
    response[key] = value
    continuation = input('do you want to continue the poll? ')
    if continuation.lower() == 'no':
        poll = False

for key, value in response.items():
    print(f"{key} wants to visit {value}")

