from random import randint

class Die:
    """A class to represent a die"""

    def __init__(self, n_sides = 6):
        """Initialize the variables"""
        self.n_sides = n_sides

    def roll(self):
        """Roll the die"""
        return randint(1,self.n_sides)