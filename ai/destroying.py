from random import random


class Destroying:

    def __init__(self):
        self.guess_hit = False
        self.first_guess = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def guess_pursue_direction(self, hit_row, hit_col):
        guess = self.first_guess.pop(random(len(self.first_guess)))
        return hit_row + guess[0], hit_col + guess[1]

    def pursue_direction(self, hit_row, hit_col):
        pass