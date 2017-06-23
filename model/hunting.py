from random import randint, choice


class Hunting:

    def __init__(self):
        self.shots = []
        self.rows = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}

    def shoot_random(self):
        random_row = randint(0, 9)
        random_col = randint(0, 9)
        # prevent from shooting the same spot again
        while (random_row, random_col) in self.shots:
            random_row = randint(0, 9)
            random_col = randint(0, 9)

        self.shots.append((random_row, random_col))
        print('Move: ', self.rows[random_row], random_col)

        return random_row, random_col

    def vertical_random(self):
        return choice([True, False])