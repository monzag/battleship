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

    def check_free_position(self):
        for i in range(self.size):
            if self.is_vertical:
                if not ocean.board[start_row + i][start_column].is_ship():
                    pass

            else:
                if not ocean.board[start_row][start_column + i].is_ship():
                    pass

