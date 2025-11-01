# Date: 31-October-2025
# Name: S.Riyyan hassan

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Use a slice to
# print three items from the middle of the list.
# • Print the message The last three items in the list are:. Use a slice to print the
# last three items in the list.


numbers = [number for number in range(1,11)]

print(f"FIRST Three numbers in list are: {numbers[:3]}")
print(f"MIDDLE Three numbers in list are: {numbers[3:6]}")
print(f"LAST Three numbers in list are: {numbers[-3:]}")


