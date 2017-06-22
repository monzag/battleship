from ai import Hunting
from ai import Destroying


class AiController:

    def __init__(self):
        self.flag_hit = False
        self.flag_sunk = False
        self.ship_count = 5
        self.destroy_phase = False
        self.hunt = Hunting()

    def ship_hunt(self):
        if self.pewpew(*self.hunt.shoot_random()):
            self.destroy_phase = True
            destroy = Destroying(*self.hunt.used[-1])

    def pewpew(self, ocean, row, col):
        square = ocean[row][col]
        square.hit()
        self.hit_flag = square.is_ship

