from hunting import Hunting
from destroying import Destroying
from ocean import Ocean
from ship import Ship
from square import Square


class FSM:

    def __init__(self):
        self.hit_f = False
        self.sunk_f = False
        self.ship_counter = 1
        self.state = 1
        self.shots = []
        self.hunting = Hunting()
        self.destroy = None

    def controller(self, ocean):
        if self.state == 1:
            self.hit_on_board(*self.hunting.shoot_random(self.shots), ocean)
        elif self.state == 2 and not self.destroy:
            self.destroy = Destroying(*self.shots[-1])
            self.hit_f = self.hit_on_board(*self.destroy.prepare_hit(self.hit_f, self.sunk_f), ocean)
        elif self.state == 2 and self.destroy:
            self.hit_f = False
            self.hit_on_board(*self.destroy.prepare_hit(self.hit_f, self.sunk_f), ocean)
        elif self.state == 3:
            print("GAME OVER! KUCHWA!!!!1111oneONEone")

    def hit_on_board(self, row, col, ocean):
        square = ocean.board[row][col]
        print(square.is_ship)
        self.shots.append((row, col))
        if square.is_ship:
            self.hit_f = True
            self.state = 2
        if square.is_ship and square.check_ship_sunk():
            self.sunk_f = True
            self.hit_f = False
            self.state = 1
            self.ship_counter -= 1
            self.destroy = None
        if self.ship_counter == 0:
            self.state = 3
        return self.hit_f



