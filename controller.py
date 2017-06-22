from hunting import Hunting
from destroying import Destroying


class AiController:

    def __init__(self):
        self.flag_hit = False
        self.flag_sunk = False
        self.ship_count = 5
        self.destroy_phase = False
        self.hunt = Hunting()
        self.destroy = None
        self.shots = []

    def ship_hunt(self):
        if self.pewpew(*self.hunt.shoot_random(self.shots)):
            self.destroy_phase = True
            destroy = Destroying(*self.shots[-1])

    def pewpew(self, row, col):
        self.shots.append((row, col))
        # ocean.board[row][col] -> depends on return

        if (row == 3 and col == 6):
            return True

    def ai_move(self):
        if self.destroy_phase and not self.destroy:
            self.destroy = Destroying(self.shots[-1])
            self.destroy = True
        elif self.destroy_phase and self.destroy:
            # self.destroy = Destroying(self.shots[-1])
            self.destroy.prepare_hit()
            self.hunt.shoot_random(self.shots)
        else:
            self.hunt.shoot_random(self.shots)



# def main():
#     ai = AiController()
#     for i in range(20):
#         ai.ship_hunt()
#         print(ai.destroy_phase)
#
# if __name__ == '__main__':
#     main()