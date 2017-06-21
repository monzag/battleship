from ai import Hunting
from ai import Destroying


class AiController:

    def __init__(self):
        self.hunt = Hunting()
        self.destroy = Destroying()
        self.hit_flag = False
        self.sunk_flag = False
        self.ships_left = 5

    def ai_move(self):
        # hit_flag False and sunk_flag False
        if not (self.hit_flag and self.sunk_flag):
            hit_row, hit_col = self.hunt.shoot_random()
        # hit_flag True and sunk_flag False and ship_hit True
        elif self.hit_flag and not self.sunk_flag and not self.destroy.guess_hit:
            hit_row, hit_col = self.destroy.guess_pursue_direction()
        return hit_row, hit_col

    def pewpew(self, ocean, row, col):
        square = ocean[row][col]
        square.hit()
        self.hit_flag = square.is_ship

