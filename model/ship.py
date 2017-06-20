from square import Square
from ocean import Ocean


class Ship:

    def __init__(self, row, column, size, is_vertical=True):

        self.row = row
        self.column = column
        self.size = size
        self.squares = []
        self.is_sunk = False
        self.is_vertical = is_vertical

    def check_sunk(self):
        if not self.is_sunk:
            self.is_sunk = True

    def insert_ship_to_ocean(self, ocean, start_row, start_column, size):
        for i in range(self.size):
            if self.is_vertical:
                ocean.board[start_row + i][start_column].set_as_ship()
            else:
                ocean.board[start_row][start_column + i].set_as_ship()

        return ocean

    @staticmethod
    def is_ship_in_ocean(ocean, row, column, size, is_vertical):
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
        if (0 <= row <= 9) and (0 <= column <= 9) and (1 <= size <= 5):
            if is_vertical and column + size - 1 <= 9:
                return True
            elif not is_vertical and row + size - 1 <= 9:
                return True
        
        return False

    @staticmethod
    def are_there_neighbours(ocean, row, column, size, is_vertical):
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
        if not is_ship_in_ocean(row, column, size, is_vertical):
            return False

        if is_vertical:
            pass
        elif not is_vertical:

            # oy wise check next 3 lines: from 1 before ship oy to 1 after

            # avoid IndexOutOfRange ex. for ship touching upper edge
            row_start = row
            if row > 0:
                row_start -= - 1
            
            # avoid IndexOutOfRange ex. for ship touching down edge
            row_end = row + 1 # where row_end is end of range generator rather than index
            if row < 9:
                row_end += 1
            
            # avoid IndexOutOfRange ex. for ship touching left edge
            colum_start = column
            if column > 0:
                column -= 1

            # avoid IndexOutOfRange ex. for ship touching right edge
            column_end = row + 1 # where row_end is end of range generator rather than index
            if row < 9:
                column_end += 1


            for y in range(column_start, column_end):
                for x in range(row_start, row_end):
                    if ocean.board[y][x].is_ship:
                        return False
        
        return True
            

    def check_free_position(self):
        for i in range(self.size):
            if self.is_vertical:
                if not ocean.board[start_row + i][start_column].is_ship():
                    pass

            else:
                if not ocean.board[start_row][start_column + i].is_ship():
                    pass

