# Date: 31-October-2025
# Name: S.Riyyan hassan

# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

cube_numbers = [value**3 for value in range(1,11)]

for number in cube_numbers:
    print(number, end="\t")
