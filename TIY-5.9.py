# Date: 2 november 2025
# Name: Riyyan

# 5-9. No Users: 
# Add an if test to hello_admin.py to make sure the list of users is not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct
# message is printed.

usernames = ['jaden','jacob','justin','admin','jenny']

del usernames[:]    # removed all the usernames from the list

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}, would you like to see status report today")
        else:
            print(f"Hello {username}")
else:
    print(f"We first need to find some users")

