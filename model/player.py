from ocean import Ocean
from ship import Ship
from data_reader import DataReader


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

        row, column, is_vertical  = DataReader.input_new_ship_data()
        ship = Ship(size, is_vertical)

        while not ship.can_be_set(self.ocean, row, column):
            print('\nThis ship could not be added! Try again.')
            row, column, is_vertical  = DataReader.input_new_ship_data()
            ship = Ship(size, is_vertical)

        ship.insert_ship_to_ocean(self.ocean, row, column)
        self.ships.append(ship)

    @property
    def is_game_win(self):
    '''
    Checks if any squere obj in ship.ships list is not hit 
    if there is at last one which wasn't hit means the game is still on

    Returns:
        bool : game end control
    '''
        for ship in self.ships:
            for square in ship:
                if not square.is_hit:
                    return False

        return True

    def get_ships_from_player(self):
    '''
    Holds mechanick under player creating his ships

    Returns:
        None
    '''
        for size in range(1, 6):
            print('Insert ship of size: ', size)
            
            self.set_ship(size)
            print(self.ocean.get_ocean_string(True))