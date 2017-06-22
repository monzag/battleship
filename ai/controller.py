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

    def pewpew(self, row, col):
        if (row == 3 and col == 6):
            return True

