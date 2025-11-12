# Date: 12 november 2025
# Name: Riyyan

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

def make_shirt(size, message):
    '''the function prints the size and message printed on it'''
    print(f"Shirt of {size} size, with '{message}' printed on it.")

make_shirt('large'.title(), 'working on it!@#'.title())
make_shirt(message = 'working on it!@#'.title(), size = 'large'.title())