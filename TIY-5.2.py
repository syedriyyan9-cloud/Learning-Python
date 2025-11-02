# Date: 2 november 2025
# Name: Riyyan

# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to ten. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

print('laser' == 'Laser')   # i predict false
print('apple' <= 'orange')  # i predict true

print('APPLE'.lower() == 'apple')   # i predict true
print('APPLE' != 'apple')   # i predict true

n1, n2 = 12,45
print(n1 != n2) # i predict true
print(n1 == n2) # i predict false
print(n1 >= n2) # i predict false
print(n1 <= n2) # i predict true

fruits = ['apple','coconut', 'pineapple']
print('apple' in fruits)    # i predict true
print('orange' in fruits)   # i predict false
print('apple' not in fruits)    # i predict false
print('orange' not in fruits)   # i predict true