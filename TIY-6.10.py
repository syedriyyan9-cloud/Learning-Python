# Date: 11 november 2025
# Name: Riyyan

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
# so each person can have more than one favorite number. Then print each per-
# son’s name along with their favorite numbers.

favorite_numbers = {
    'syed': [22,23,24,25,26],
    'riyyan': [33,34,35,36,37],
    'hassan': [44,45,46,47],
    'kamran': [55,51,52,53,54],
    'noman': [66,45,67,543,234],
}

for person,numbers in favorite_numbers.items():
    print(f"{person}'s favorite number are: ".title())
    for number in numbers:
        print(f"  {number}")
