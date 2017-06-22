from random import randint


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

    def flip_direction(self):
        ''' Flip current vector direction by 180 degree'''
        self.current_position = self.initial_position
        if self.direction[0] != 0:
            self.direction = (-self.direction[0], 0)
            self.direction_to_check.remove(self.direction)
        else:
            self.direction = (0, -self.direction[1])
            self.direction_to_check.remove(self.direction)

    def prepare_hit(self):
        ''' Return coordinates of next target field '''
        position = (self.current_position[0] + self.direction[0], self.current_position[1] + self.direction[1])
        if position[0] > 9 or position[0] < 0 or position[1] > 9 or position[1] < 0:
            self.flip_direction()
            position = (self.current_position[0] + self.direction[0], self.current_position[1] + self.direction[1])

        self.current_position = position
        return self.current_position[0], self.current_position[1]

