from FSMcontroller import FSM
from ocean import Ocean
from ship import Ship


def main():
    ocean = Ocean()
    ocean.create_board()
    ship3 = Ship(3)
    ship3.insert_ship_to_ocean(ocean, 3, 3)

    fsm = FSM()
    while fsm.ship_counter > 0:
        fsm.controller(ocean)
        print(ocean)

if __name__ == '__main__':
    main()
