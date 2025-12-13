# Date: 12 november 2025
# Name: Riyyan

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size = 'Large', message = 'I love Python'):
    print(f"Shirt of {size} size with, '{message}' printed on it")

make_shirt()
make_shirt(size = 'Medium')
make_shirt(size = 'Small', message = 'I am learning python')