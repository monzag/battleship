class Squere:


    def __init__(self, column, row, is_hit, is_ship):
        self.column = column
        self.row = row
        self.is_hit = False
        self.is_ship = False
    

    def __str__(self):

        squere_str = ''

        if self.is_ship and self.is_hit:
            squere_str = 'X'
        elif not self.is_ship and self.is_hit:
            squere_str = 'o'
        else:
            squere_str = ' '
        
        return squere_str

    def hit(self):
        self.is_hit = True