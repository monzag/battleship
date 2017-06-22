from random import randint


class Destroying:

    def __init__(self, row, col):
        self.initial_position = (row, col)
        self.direction_to_check = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.direction = self._choose_direction()
        self.current_position = self.initial_position

    def _choose_direction(self):
        ''' Pop random direction from direction list '''
        if len(self.direction_to_check) != 0:
            return self.direction_to_check.pop(randint(0, len(self.direction_to_check) - 1))
        else:
            return ()

    def flip_direction(self):
        ''' Flip current vector direction by 180 degree'''
        self.current_position = self.initial_position
        if self.direction[0] != 0 and self.direction_to_check:
            self.direction = (-self.direction[0], 0)
            self.direction_to_check.remove(self.direction)
        elif self.direction[1] != 0 and self.direction_to_check:
            self.direction = (0, -self.direction[1])
            self.direction_to_check.remove(self.direction)

    def prepare_hit(self, hit_flag, sunk_flag):
        ''' Return coordinates of next target field '''
        position = (self.current_position[0] + self.direction[0], self.current_position[1] + self.direction[1])
        if position[0] > 9 or position[0] < 0 or position[1] > 9 or position[1] < 0:
            self.direction = self._choose_direction()
            print('if_1', self.current_position)
            position = (self.current_position[0] + self.direction[0], self.current_position[1] + self.direction[1])
        if not sunk_flag and hit_flag:
            print('if_2', self.current_position)
            position = (self.current_position[0] + self.direction[0], self.current_position[1] + self.direction[1])
        if not hit_flag and not hit_flag:
            if len(self.direction_to_check) > 2:
                self.flip_direction()
            else:
                self.direction = self._choose_direction()
            print('if_3', self.current_position)
            print(self.direction)
            position = (self.current_position[0] + self.direction[0], self.current_position[1] + self.direction[1])

        self.current_position = position
        print((self.current_position[0], self.current_position[1]), self.direction)
        return self.current_position[0], self.current_position[1]



def main():
    for i in range(10):
        dest = Destroying(1, 8)
        print(dest.current_position)
        print(dest.direction_to_check)
        print(dest.prepare_hit())
        print(dest.prepare_hit())
        print(dest.prepare_hit())
        print(dest.prepare_hit())
        print(dest.prepare_hit())
        print(dest.direction_to_check)

if __name__ == '__main__':
    main()