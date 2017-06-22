from ocean import Ocean
from ship import Ship
from data_reader import DataReader
from output_manager import OutputManager


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
        '''    def is_game_win(self):
        Holds mechanick under player creating his ships

        Returns:
            None
        '''
        for size in range(1, 6):
            print('Insert ship of size: ', size)
            
            self.set_ship(size)
            OutputManager.print_single_battlefield(self.ocean)

    def find_ship_by_square(self, square):
        '''
        Given square obj that is a part of ship returns Ship obj,
        that is owner of given square

        Parameters:
            square : square obj
        
        Returns:
            Ship obj
        '''
        for ship in player.ships:
            for sqr_obj in ship.squares:
                if sqr_obj == square:
                    return ship
        raise ValueError
    
    def hit_ship_neighbour():

        
ocean = Ocean()
player = Player('Kogo', ocean)
ocean2 = Ocean()
player2 = Player('Soto', ocean2)

ship = Ship(1, True)
ship2 = Ship(3, False)

ship.insert_ship_to_ocean(player.ocean, 1, 1)
player.ships.append(ship)
ship2.insert_ship_to_ocean(player.ocean, 5, 5)
player.ships.append(ship2)

row = 1
column = 1
ocean.board[row][column].hit()

OutputManager.print_battlefield(player.ocean, player2.ocean)
if ocean.board[row][column].is_ship:
    ship = player.find_ship_by_square(ocean.board[row][column])
    if ship.is_ship_sunk:
        player.hit_ship_neighbour()




