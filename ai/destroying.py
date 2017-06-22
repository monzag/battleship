from random import random


class Destroying:

    def __init__(self, row, col):
        self.initial_position = (row, col)
        self.direction_to_check = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.direction = self._choose_direction()
        self.current_position = self.initial_position

    def _choose_direction(self):
        ''' Pop random direction from direction list '''
        direction = self.direction_to_check.pop(randint(0, len(self.direction_to_check) - 1))
        return direction

    def pursue_direction(self, hit_row, hit_col):
        pass