from ocean import Ocean
from ship import Ship
from data_reader import DataReader
from square import Square
from output_manager import OutputManager


class Player:

    def __init__(self, name, ocean):
        self.ships = []
        self.name = name
        self.ocean = ocean
        self.is_first = True

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
            for square in ship.squares:
                if not square.is_hit:
                    return False
        return True

    def get_ships_from_player(self):
        '''
        Sets 5 ships in proper size on position indicated by user.

        Return:
            None
        '''
        OutputManager.print_single_battlefield(self.ocean, True)
        for size in [2, 3, 3, 4, 5]:
            print('{} Insert ship of size: {}'.format(self.name, size))

            self.set_ship(size)
            OutputManager.print_single_battlefield(self.ocean, True)
        input('Press any key to continue')

    def check_user_hit(self, hit_row, hit_column):
        '''
        Check square on hit positions by user.

        Args:
            hit_row - int
            hit_column - int

        Returns:
            turn_result : str
        '''
        if not self.ocean.board[hit_row][hit_column].is_hit:
            self.ocean.board[hit_row][hit_column].hit()
            if self.ocean.board[hit_row][hit_column].is_ship:
                ship = self.find_ship_by_square(self.ocean.board[hit_row][hit_column])
                if ship.is_ship_sunk:
                    turn_result = '>>> Hit and sunk!! <<<'
                else:
                    turn_result = '>>> Hit!! <<<'
            else:
                turn_result = '>>> Miss! <<<'

        return turn_result

    def find_ship_by_square(self, square):
        '''
        Given square obj that is a part of ship returns Ship obj,
        that is owner of given square

        Parameters:
            square : square obj

        Returns:
            Ship obj
        '''
        for ship in self.ships:
            for sqr_obj in ship.squares:
                if sqr_obj == square:
                    return ship