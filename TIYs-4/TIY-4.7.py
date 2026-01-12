# Date: 31-October-2025
# Name: S.Riyyan hassan

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

numbers = [number for number in range(3,31) if number % 3 == 0]

for number in numbers:
    print(number,end="\t")

# print(numbers[::-1])