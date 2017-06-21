from model.square import Square
from model.ocean import Ocean


class Ship:

    def __init__(self, size, is_vertical=True):

        self.size = size
        self.squares = []
        self.is_sunk = False
        self.is_vertical = is_vertical

    def check_sunk(self):
        if not self.is_sunk:
            self.is_sunk = True

    def insert_ship_to_ocean(self, ocean, start_row, start_column):
        for i in range(self.size):
            if self.is_vertical:
                ocean.board[start_row + i][start_column].set_as_ship()
                self.squares.append(ocean.board[start_row + i][start_column])
            else:
                ocean.board[start_row][start_column + i].set_as_ship()
                self.squares.append(ocean.board[start_row][start_column + i])

        return ocean

    @staticmethod
    def is_in_ocean(row, column, size, is_vertical):
        '''
        Checks if user passed attributes values for new Ship obj. fit
        in range of Oceans board.

        board is 10 element long squere 2d list:
            row, column are indexes from 0 to 9 (including)
        
        size is amount of squares in Ship object:
            size is a number from 1 to 5 (including)

        Parameters:
            row         : int (y index for board)
            column      : int (x index for board)
            size        : int
            is_vertical : bool
        
        Returns:
            True  : if new Ship obj. would fit in Ocean (index wise)
            False : otherwise
        '''
        # indexes and size of first square are in range of oceans board
        if (0 <= row <= 9) and (0 <= column <= 9) and (1 <= size <= 5):
            # would last squere be still in range of oceans board
            if is_vertical and row + size - 1 <= 9:
                return True
            elif not is_vertical and column + size - 1 <= 9:
                return True
        
        return False

    @staticmethod
    def can_be_set(ocean, row, column, size, is_vertical):
        '''
        Checks passed location of newly defined Ship obj. under fallowing
        curriculumstances:

            - ship is build of 1-5 Square obj.
            - ship has to fit in ocean board (both indexes of Squares 0-9)
            - ship cannot overwrite other ship object
            - ship cannot touch any existing ship (including corners)

            - ship is declared by first square index in ocean.board[y][z]
            - ship is build from left->right(horizontal) or from up->down(vertical)
        
        Parameters:
            ocean       : Ocean obj. where ship should fit
            row         : int (oy index for first new ship square)
            column      : int (ox index for first new ship square)
            size        : int (amount of squares in new ship)
            is_vertical : bool(if True new Ship obj. is set verticaly)
        
        Returns:
            True  : if new ship can be set in given location
            False : otherwise
        '''
        # disalow wrong indexes to be passed further in function
        if Ship.is_in_ocean(row, column, size, is_vertical):
            
            if is_vertical:

                # iterate through every single ocean.board.squere around new Ship
                for y in Ship.range_of_lenght(row, size):
                    for x in Ship.range_of_width(row):
                        # return False if any squere is a part of existing ship
                        if ocean.board[y][x].is_ship:
                            return False

            elif not is_vertical:

                # iterate through every single ocean.board.squere around new Ship
                for y in Ship.range_of_width(row):
                    for x in Ship.range_of_lenght(column, size):
                        # return False if any squere is a part of existing ship
                        if ocean.board[y][x].is_ship:
                            return False
            
            return True

        else:
            return False

    @staticmethod
    def range_of_width(index):
        '''
        Given a number representing index in ocean.board:
            row    : for horizontal ships
            column : for vertical
        
        finds 3 wide range between index-1 and index+1, with exepction
            of indexes out of oceans.board if on edges
        
        Parameters:
            index : int
        
        Returns:
            range generator range(start, end)
        '''

        start = index
        # avoid IndexOutOfRange ex. for ships touching first edge
        if index > 0: 
            start -= 1
        
        end = index + 1 # + 1 becaouse its rather range argument than index
        # avoid IndexOutOfRange ex. for ships touching last edge
        if index < 9:
            end += 1
        
        return range(start, end)
        
    @staticmethod
    def range_of_lenght(index, size):
        '''
        Given a number representing index in ocean.board:
            row    : for vertical ships
            column : for horizontal ships
        
        finds size+2 wide range between index and index+size-1, with exepction
            of indexes out of oceans.board if on edges
        
        Parameters:
            index : int
        
        Returns:
            range generator range(start, end)
        '''
        # avoid IndexOutOfRange ex. for ship touching last edge
        start = index
        if index > 0:
            start -= 1

        # find last index of ship (column + size - 1) and + 1 becaouse its rather range argument than index
        end = index + size
        # avoid IndexOutOfRange ex. for ship touching last edge
        if end < 10:
            end += 1
        
        return range(start, end)