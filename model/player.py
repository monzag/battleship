from ocean import Ocean


class Player:

    def __init__(self, name):
        self.name = name
        self.is_fisrt = True

    def get_positions_from_player(self):
        pos_x = input('Write position x (1-10): ')
        pos_y = input('Write position y (A-J): ')

        letter = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}

        column = int(ship_x) - 1
        row = int(''.join([value for key, value in letter.items() if key == pos_y]))

        if isinstance(index_x, int) or isinstance(index_y, int):
            raise TypeError('Incorrect type!')

        else:
            # insert ship to row and column?
            pass
