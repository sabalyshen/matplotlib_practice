from random import randint

class Die():
    """表示一個骰子的class"""

    def __init__(self, num_sides=6):
        """骰子默認6面"""
        self.num_sides = num_sides

    def roll(self):
        """投骰子輸出數字"""
        return randint(1, self.num_sides)