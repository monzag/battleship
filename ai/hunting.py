from random import randint


class Hunting:

    def shoot_random(self, shots):
        random_row = randint(0, 9)
        random_col = randint(0, 9)
        # prevent from shooting the same spot again
        while (random_row, random_col) in shots:
            random_row = randint(0, 9)
            random_col = randint(0, 9)
        return random_row, random_col
