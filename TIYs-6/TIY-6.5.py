# Date: 11 november 2025
# name: Riyyan

# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers = {
    'nile':'egypt',
    'indus': 'pakistan',
    'kalapani':'nepal',
}

for key, value in rivers.items():
    print(f"{key.title()} runs through {value.title()}")

for key in rivers:
    print(f"{key.title()} river")

for value in rivers.values():
    print(f"{value.title()}")