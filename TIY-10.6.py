# Date: 22 november 2025
# Name: Riyyan

# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a ValueError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the ValueError if
# either input value is not a number, and print a friendly error message. Test 
# your program by entering two numbers and then by entering some text instead of
# a number.

print("Enter two numbers to perform addition")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
try:
    answer = int(num1) + int(num2)
except ValueError:
    print("Enter a number not text")
else:
    print(f"The sum of two numbers is: {answer}")



