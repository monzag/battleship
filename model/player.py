from ocean import Ocean
from ship import Ship
from data_reader import DataReader
from square import Square


class Player:

    def __init__(self, name, ocean):
        self.ships = []
        self.name = name
        self.ocean = ocean
        self.is_fisrt = True

    def set_ship(self, size):
        '''
        Uses DataReader module to get user defined data for new ship
        Checks if data and new Ship obj. are defined with game rules

        Will keep asking for data until new ship can be added to game

        Parameters:
            size : int(1-5) lenght of ship

        Returns:
            None
        '''

        row, column, is_vertical = DataReader.input_new_ship_data()
        ship = Ship(size, is_vertical)

        while not ship.can_be_set(self.ocean, row, column):
            print('\nThis ship could not be added! Try again.')
            row, column, is_vertical = DataReader.input_new_ship_data()
            ship = Ship(size, is_vertical)

        ship.insert_ship_to_ocean(self.ocean, row, column)
        self.ships.append(ship)

    @property
    def is_game_win(self):
        '''
        Check that all squares are hit. Returns True if yes.

        Returns:
            bool
        '''

        for ship in self.ships:
            ship.sunk()

        return True

    def get_ships_from_player(self):
        '''
        Sets 5 ships in proper size on position indicated by user.

        Return:
            None
        '''

        for size in [2, 3, 3, 4, 5]:
            print('Insert ship of size: ', size)

            self.set_ship(size)
            print(self.ocean.get_ocean_string(True))
            
    def check_user_hit(self, hit_row, hit_column):
        '''
        Check square on hit positions by user.

        Args:
            hit_row - int
            hit_column - int

        Returns:
            None
        '''
        hit_square = Square(hit_row, hit_column)
        if not self.check_free_field(hit_square):
            self.check_hit_square(hit_square)
            if self.is_game_win:
                # Wygrana, highscore, game again?
                pass

    def check_free_field(self, hit_square):
        if hit_square.is_hit:
            return False
        else:
            return True

    def check_hit_square(self, hit_square):
        if hit_square.is_ship:
            hit_square.hit()

            # jeśli tak to zatop, wydrukuj odpowiedni statek

