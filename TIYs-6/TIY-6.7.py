# Date: 11 november 2025
# Name: Riyyan

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

person1 = {
    'first_name': 'Syed',
    'last_name':'Hassan',
    'age': 22,
    'city': 'Lahore',
}

person2 = {
    'first_name': 'Muhammad',
    'last_name':'Kamran',
    'age': 20,
    'city': 'Lahore',
}

person3 = {
    'first_name': 'Muhammad',
    'last_name':'Noman',
    'age': 19,
    'city': 'Raiwand',
}

people = [person1, person2, person3]

for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print("--------------------")
