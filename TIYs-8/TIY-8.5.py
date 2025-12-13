# Date: 12 november 2025
# Name: Riyyan

# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not 
# in the default country.

def describe_city(city, country = 'Pakistan'):
    '''prints the name of city in country'''
    print(f"{city} is in {country}")

describe_city(city='Islamabad')
describe_city(city='Lahore')
describe_city(city='Kabul')
