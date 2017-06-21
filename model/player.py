from ocean import Ocean
from ship import Ship


class Player:

    def __init__(self, name, ocean):
        self.ships = []
        self.name = name
        self.ocean = ocean
        self.is_fisrt = True

    def set_ship(self, row, column, is_vertical, size):
        ship = Ship(size, is_vertical)
        if ship.can_be_set(self.ocean, row, column):
            ship.insert_ship_to_ocean(self.ocean, row, column)
            self.ships.append(ship)

    def is_input_valid(self, pos_x, pos_y, letter, is_vertical):
        if pos_x.isdigit() and pos_y in list(letter) and is_vertical in ['Y', 'N']:

            if 0 < int(pos_x) < 10:
                return True

        return False

    def get_positions_from_player(self, size):
        letter = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        pos_x = ''
        pos_y = ''
        is_vertical = ''

        while not self.is_input_valid(pos_x, pos_y, letter, is_vertical):
            pos_y = input('Write position y (A-J): ').upper()
            pos_x = input('Write position x (1-10): ')
            is_vertical = input('Should your ship be vertical? (y/n): ').upper()

        if is_vertical.upper() == 'Y':
            is_vertical = True
        else:
            is_vertical = False

        column = int(pos_x) - 1
        row = letter[pos_y]

        self.set_ship(row, column, is_vertical, size)

    def is_game_win(self):
        for ship in self.ships:
            for square in ship:
                if not square.is_hit:
                    return False

        return True

    def get_ships_from_player(self):
        for size in range(1, 6):
            self.get_positions_from_player(size)

ocean = Ocean()
player = Player('Arek', ocean)
print(ocean.get_ocean_string(True))

player.get_ships_from_player()
print(ocean.get_ocean_string(True))





