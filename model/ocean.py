from square import Square
from colors import Colors


class Ocean:

    _ROWS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        '''
        Creates 2 dimentional table (2d list) consisting of Square elements

        Returns
            2d list of squares
        '''
        return [[Square(row, column) for column in range(10)] for row in range(10)]

    def get_ocean_string(self, is_player_own):
        '''
        Creates formated string out of ocean object. String is set differently
        depending if printed field is player own (should see his own ships)
        or enemy's (should NOT see ships)

        Parameters:
            is_player_own : bool determines string method

        Returns:
            board_str : string of ocean obj.
        '''
        board_str = Colors.OKGREEN + '  ' + ' '.join(list(str(i) for i in range(len(self.board)))) + Colors.ENDC

        for i, row in enumerate(self.board):
            line = ' '.join(squere.get_squere_string(is_player_own) for squere in row)
            board_str += '\n' + Colors.OKGREEN + self._ROWS[i] + Colors.ENDC + ' ' + line

        return board_str