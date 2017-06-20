def check_horiontal_ship(board, row, column, size):
    # if ship on edge start counting on its index
    # otherwise start one column/row before
    if row > 0:
        start_row = row - 1
    else:
        start_row = 0

    if column > 0:
        start_column = column - 1
    else:
        start_column = 0
    
    # check if ship will fit horizontaly so starting on column index
    # pass its size (-1 to take first index of consideration)
    end_column = column + size - 1
    # if last squere is on edge take end_column as proper, but add +1 for range
    if end_column == 9:
        end_column += 1
    # if not on edge check also 1 column behind it (+1 for column + 1 for range)
    elif end_column < 9:
        end_column += 2
    else:
        return False

    # + 1 for range
    end_row = row + 1
    # check veritcally next row after ship, but ignore it if on edge 
    if end_row + 1 < 10:
        end_row += 1


    for y in range(start_column, end_column):
        for x in range(start_row, end_row):
            if not board[x][y] == '~':
                return False

    return True


board = [['~' for i in range(10)] for j in range(10)]


board[8][9] = 'o'
if check_horiontal_ship(board, 7, 8, 2):
    print('yes')
else:
    print('no')


print('\n'.join(' '.join(row) for row in board))