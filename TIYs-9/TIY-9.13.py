# Date: 19 november 2025
# Name: Riyyan

# 9-13. Dice: Make a class Die with one attribute called sides, which has a 
# default value of 6. Write a method called roll_die() that prints a random 
# number between 1 and the number of sides the die has. Make a 6-sided die and 
# roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die:
    ''' a simple class to represent a dice '''
    
    def __init__(self, sides = 6):
        '''initializes parameter, if not intialized then have value of 6'''
        self.sides = sides

    def roll_die(self):
        '''print a random number between 1 and number of sides'''
        print(f"You Got: {randint(1, self.sides)}")


'''making a 6 sided dice and rolling it 10 times'''
dice = Die()
for roll in range(1,11):
    dice.roll_die()

print("--------------------------")

'''making a 10 sided dice and rolling it 10 times'''
dice = Die(10)
for roll in range(1,11):
    dice.roll_die()

print("--------------------------")

'''making a 20 sided dice and rolling it 10 times'''
dice = Die(20)
for roll in range(1,11):
    dice.roll_die()

