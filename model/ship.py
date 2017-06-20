class Ship:

    def __init__(self, size, row, column, is_sunk=False, is_horizontal=False):
        self.is_sunk = is_sunk
        self.is_horizontal = is_horizontal
        self.size = size
        self.row = row
        self.column = column

