# Date: 4 november 2025
# Name: Riyyan

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

glossary = {
    'loops': 'To repeat',
    'boolean': 'Something that is either True or False',
    'Expression': 'A statement that computes to a value',
    'Statment': 'A line that gives information or defines some condition',
    'Condition': 'An expression that is True or False based on given inputs',
}

print(f"loops: \n\t{glossary['loops']}")
print(f"boolean: \n\t{glossary['boolean']}")
print(f"Expression: \n\t{glossary['Expression']}")
print(f"Statment: \n\t{glossary['Statment']}")
print(f"Condition: \n\t{glossary['Condition']}")