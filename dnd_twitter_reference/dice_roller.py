import random


class Dice:
    """A Class that rolls dice base on the number of sides given"""

    def __init__(self, sides):
        self.sides = sides

    def roll_the_die(self):
        """A single roll of the dice"""
        roll = random.randint(1, self.sides)
        return roll
