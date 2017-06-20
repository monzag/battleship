class Ship:

    def __init__(self, row, column, size, is_vertical=True):

        self.row = row
        self.column = column
        self.size = size
        self.squares = []
        self.is_sunk = False
        self.is_vertical = is_vertical

