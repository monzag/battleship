from square import Square


class Ocean:

    def __init__(self):

        self.board = self.create_board()

    def create_board(self):
        return [[Square(row, column) for column in range(10)] for row in range(10)]

    def __str__(self):
        pass





