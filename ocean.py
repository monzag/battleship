from square import Square


class Ocean:

    _ROWS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    def __init__(self):

        self.board = self.create_board()

    def create_board(self):
        return [[Square(row, column) for column in range(10)] for row in range(10)]

    def get_ocean_string(self, is_player_own):
        board_str = '   ' + ' '.join(list(str(i) for i in range(len(self.board))))

        for i, row in enumerate(self.board):
            line = ' '.join(squere.get_squere_string(is_player_own) for squere in row)
            board_str += '\n{} {}'.format(self._ROWS[i], line)

        return board_str

    def __str__(self):
        return '\n'.join('  '.join([str(square) for square in row]) for row in self.board)
