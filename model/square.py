from model.colors import Colors


class Square:

    def __init__(self, row, column, is_hit=False, is_ship=False):
        self.row = row
        self.column = column
        self.is_hit = is_hit
        self.is_ship = is_ship

    def __str__(self):
        sqr_str = Colors.OKBLUE + '️🌊' + Colors.ENDC
        if self.is_ship:
            sqr_str = Colors.WARNING + '⛴️' + Colors.ENDC
        elif not self.is_ship and self.is_hit:
            sqr_str = Colors.FAIL + '❌' + Colors.ENDC
        elif self.is_ship and self.is_hit:
            sqr_str = Colors.FAIL + '⛴️' + Colors.ENDC
        return sqr_str


    def set_as_ship(self):
        if not self.is_ship:
            self.is_ship = True
    
    def hit(self):
        if not self.is_hit:
            self.is_hit = True