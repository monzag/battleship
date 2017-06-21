from random import randint


class Hunting:

    def __init__(self):
        self.used = []

    def shoot_random(self):
        random_row = randint(0, 9)
        random_col = randint(0, 9)
        # prevent from shooting the same spot again
        while (random_row, random_col) in self.used:
            random_row = randint(0, 9)
            random_col = randint(0, 9)

        self.used.append((random_row, random_col))
        return random_row, random_col
