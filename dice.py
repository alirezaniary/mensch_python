from random import choice
class Dice:
    def __init__(self):
        self.sides = [1, 2, 3, 4, 5, 6]
    
    def roll(self):
        return choice(self.sides)