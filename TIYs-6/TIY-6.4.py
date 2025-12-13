# Date: 11 november 2025
# name: Riyyan

# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.

glossary = {
    'loops': 'To repeat',
    'boolean': 'Something that is either True or False',
    'Expression': 'A statement that computes to a value',
    'Statment': 'A line that gives information or defines some condition',
    'Condition': 'An expression that is True or False based on given inputs',
}

for key, value in glossary.items():
    print(f"{key}: \n\t{value}")

glossary['python'] = 'A general purpose language used to create different progs'
glossary['IDE'] = 'Integrated Development Environment'
glossary['Database'] = 'A collection of logiacally related data and its descrip'
glossary['DBMS'] = 'A software that allows users to use DDL and DML on database'
glossary['Verb'] = 'Any action'

for key, value in glossary.items():
    print(f"{key}: \n\t{value}")