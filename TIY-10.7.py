# Date: 22 november 2025
# Name: Riyyan

# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.

print("Enter two numbers to perform addition")
print("Press 'q' to quit")

while True:
    num1 = input("Enter first number: ")
    if num1 == 'q':
        break
    num2 = input("Enter second number: ")
    if num2 == 'q':
        break
    try:
        answer = int(num1) + int(num2)
    except ValueError:
        print("Enter a number not text")
    else:
        print(f"The sum of two numbers is: {answer}")
