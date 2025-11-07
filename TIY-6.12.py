# Date: 11 november 2025
# Name: Riyyan

# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example pro-
# grams from this chapter, and extend it by adding new keys and values, chang-
# ing the context of the program or improving the formatting of the output.

# using exercise in TIY-6.10.py for this exercise
favorite_numbers = {
    'syed': [22,23,24,25,26],
    'riyyan': [33,34,35,36,37],
    'hassan': [44,45,46,47],
    'kamran': [55,51,52,53,54],
    'noman': [66,45,67,543,234],
}

for person,numbers in favorite_numbers.items():
    print(f"\n{person}'s favorite number are: ".title())
    for number in numbers:
        print(f"{number}", end='  ')
