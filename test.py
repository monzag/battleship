from ocean import Ocean

from ship import Ship


def test():
    ocean = Ocean()
    ocean.board[0][0].set_as_ship()

    if Ship.can_be_set(ocean, 2, 1, 3, True):
        print('Ure ship was placed')
    else:
        print('U cannot place ship there!')

    print()
    print(ocean)


if __name__=='__main__':
    test()