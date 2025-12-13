# Date: 14 november 2025
# Name: Riyyan

# 8-14. Cars: Write a function that stores information about a car in a diction-
# ary. The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. Call the func-
# tion with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:

# car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary that’s returned to make sure all the information was
# stored correctly.

def car_info(manufacturer, model, **specs):
    '''takes in manufacturer, model and other key value pairs'''
    specs['manufacturer'] = manufacturer
    specs['model'] = model
    return specs

print(car_info('nissan', 'armada', color = 'silver', no_of_doors = 4))
