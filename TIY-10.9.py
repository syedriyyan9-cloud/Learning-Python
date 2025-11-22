# Date: 22 november 2025
# Name: Riyyan

# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.

filenames = ["cats.txt","dogs.txt"]
for filename in filenames:
    print("------------------------")
    try:
        with open(filename,"r") as file:
            contents = file.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)
