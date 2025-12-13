# Date: 3 november 2025
# Name: Riyyan

# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
# current_users containing the lowercase versions of all existing users.)

current_users = ['RIYYAN','HASSAN','SYED','KAMRAN','NOMAN']

copy_of_current_users = [user.lower() for user in current_users]

new_users = ['Ahmed','Khan','Riyyan','Noman','Awais']

for user in new_users:
    if user.lower() in copy_of_current_users:
        print(f"This username '{user}' is not available")
    else:
        print(f"This username '{user}' is available")