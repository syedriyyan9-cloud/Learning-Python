# Date: 14 november 2025
# Name: Riyyan

# 8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a
# profile of yourself by calling build_profile(), using your first and last names
# and three other key-value pairs that describe you.

def user_profile(first, last, **user_data):
    '''takes in user input for profile and returns it '''
    user_data['first_name'] = first
    user_data['last_name'] = last
    return user_data

profile1 = user_profile('Syed','hassan',
             occupation = 'student', height = 1.82, course = 'CS', semester = 5)

print(profile1)
