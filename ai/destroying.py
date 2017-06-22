from random import random


class Destroying:

    def __init__(self, row, col):
        self.initial_position = (row, col)
        self.direction_to_check = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.direction = self._choose_direction()
        self.current_position = self.initial_position

    def guess_pursue_direction(self, hit_row, hit_col):
        guess = self.first_guess.pop(random(len(self.first_guess)))
        return hit_row + guess[0], hit_col + guess[1]

    def pursue_direction(self, hit_row, hit_col):
        pass