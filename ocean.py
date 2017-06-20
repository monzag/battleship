class Ocean:

    _letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


    def __init__(self):
        self.board = self.fill_board()


    def __str__(self):
        pass


    def fill_board(self):
        return [[Squere(row, column) for column in range(10)] for row in range(10)]

