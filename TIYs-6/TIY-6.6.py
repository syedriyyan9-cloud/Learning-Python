# Date: 11 november 2025
# name: Riyyan

# 6-6. Polling: Use the code in favorite_languages.py (page 97).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

people_to_take_poll = ['jen','ali','sarah','edward','jacob','phil']

for name in people_to_take_poll:
    if name in favorite_languages:
        print(f"{name.title()} thanks for taking the poll.")
    else:
        print(f"{name.title()} Please take the poll.")