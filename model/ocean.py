from square import Square
from colors import Colors
from output_menager import OutputMenager


class Ocean:

    _ROWS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        return [[Square(row, column) for column in range(10)] for row in range(10)]

    def get_ocean_string(self, is_player_own):
        board_str = Colors.OKGREEN + '  ' + ' '.join(list(str(i) for i in range(len(self.board)))) + Colors.ENDC

        for i, row in enumerate(self.board):
            line = ' '.join(squere.get_squere_string(is_player_own) for squere in row)
            board_str += '\n' + Colors.OKGREEN + self._ROWS[i] + Colors.ENDC + ' ' + line

        return board_str