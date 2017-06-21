from model import Ship, Colors
from model.ocean import Ocean
from model.square import Square

ocean = Ocean()
ocean.create_board()

ship3 = Ship(3)
ship3_2 = Ship(3, False)
ship5 = Ship(5, False)
ship3.insert_ship_to_ocean(ocean, 1, 1, 3)
ship3_2.insert_ship_to_ocean(ocean, 1, 3, 3)
ship5.insert_ship_to_ocean(ocean, 5, 5, 5)

print(ocean)
