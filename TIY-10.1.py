# Date: 20 november 2025
# Name: Riyyan

# 10-1. Learning Python: Open a blank file in your text editor and write a few
# lines summarizing what you’ve learned about Python so far. Start each line
# with the phrase In Python you can. . . . Save the file as learning_python.txt 
# in the same directory as your exercises from this chapter. Write a program 
# that reads the file and prints what you wrote three times. Print the contents 
# once by reading in the entire file, once by looping over the file object, and
# once by storing the lines in a list and then working with them outside the 
# with block.

with open('learning_python.txt') as file:
    contents = file.read()
    print(contents)

print("--------------------")

with open('learning_python.txt') as file:
    for line in file:
        print(line.strip())

print("--------------------")

with open('learning_python.txt') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())



