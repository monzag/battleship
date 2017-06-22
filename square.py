from colors import Colors


class Square:

    def __init__(self, row, column, is_hit=False, is_ship=None):
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

    def set_as_ship(self, ship):
        if not self.is_ship:
            self.is_ship = ship
    
    def hit(self):
        if not self.is_hit:
            self.is_hit = True
        
    def get_square_string(self, is_player_own):

        sqr_str = Colors.OKBLUE + '️🌊' + Colors.ENDC

        if self.is_ship and not self.is_hit and is_player_own:
            sqr_str = Colors.WARNING + '⛴️' + Colors.ENDC
        elif not self.is_ship and self.is_hit:
            sqr_str = Colors.FAIL + '❌' + Colors.ENDC
        elif self.is_ship and self.is_hit:
            sqr_str = Colors.FAIL + '⛴️' + Colors.ENDC

        return sqr_str

    def check_ship_sunk(self):
        return self.is_ship.check_sunk()
