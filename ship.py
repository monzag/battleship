class Ship:
    
    def __init__(self, column, row, size, is_horizontal):
        self.column = column
        self.row = row
        self.size = size
        self.is_horizontal = is_horizontal

        self.squares = []