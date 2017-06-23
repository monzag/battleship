# Battleship in the OOP way

## The story

The object of Battleship is to try and sink all of the other player's before they sink all of your ships. All of the other player's ships are somewhere on his/her board.  You try and hit them by calling out the coordinates of one of the squares on the board.  The other player also tries to hit your ships by calling out coordinates. Neither you nor the other player can see the other's board so you must try to guess where they are.

## Specification

### 'main.py'

### 'square.py'

This is the file containing SQUARE item logic.

### Class Square

__Instance Attributes__
 
* 'row'
  - data: intiger
  - description: y position of square

* 'column'
  - data: intiger
  - description: x position of square

* 'is_hit'
  - data: bool
  - default: False
  - description: True if square is hit

* 'is_ship'
  - data: bool
  - default: False
  - description: True if square is ship

__Instance Method__

* #### '__init__(self, row, column)'

  Constructs an Square object
  
* 'hit(self)'
  
  Set object *is_hit* attribute to True

* 'set_as_ship(self)'

  Set object *is_ship* attribute to True

* 'get_square_string(self, is_player_own)'

  Returns a proper string, depending on *is_ship* attribute and *is_ship* attribute. 
  'x' when miss, otherwise proper ship.
  


### 'ship.py'

This is the file containing a Ship item logic.

### Class Ship

__Instance Attributes__

* 'is_sunk'
  - data: bool
  - default: False
  - description: True if ship is sunk

* 'is_vertical'
  - data: bool
  - description: True if is vertical

* 'size'
  - data: integer (1 - 5)
  - description: amount of Square objects in Ship 

* 'squares'
  - data: list 
  - description: list of Square objects


__Instance Method__

* #### '__init__(self, size, is_horizontal, row, column)'

  Constructs an Ship object

* 'insert_ship_to_ocean(self, ocean, start_row, start_column)'

  Set ship on valid position, can't touch another ships

* 'is_ship_sunk(self)'

  Returns False if any square object in ship is hit. Else return True.

* 'is_in_ocean(self, row, column)'

  Check proper row and column - range in board.


### 'ocean.py'

This is the file containing a Ocean item logic.

### Class Ocean

__Instance Attributes__

* 'board'
  data: list of lists
  description: contains strings representing positions or Square Object

__Instance Method__

* #### '__init__(self)'

  Constructs an Ocean object

* '__str__(self)'

  returns formatted string of Ocean object

* 'check_new_ship_position(self)'

  Check every position of new Ship and check if is valid (Ships objects can't touch one another).

### 'player.py'

This is the file containing a Player game logic.

### Class Player

__Instance Attributes__

* 'name'
  data: string
  description: name of player

* 'is_first'
  data: bool
  description: True if has first turn

__Instance Method__

* #### '__init__(self, name)'

  Constructs an Player object

* 'insert_ship(self)'
  
  Create Ship object from user default inputs (is vertical, ship's size, position x, y).
   

* 'get_position_from_player(self)'

  Get inputs from user: row and column.
  Repeat until input is valid. 


### 'main.py'

This is the file containing game logic.

__Functions__

* 'set_game'

  Creates Ocean objects for 2 players.
  Sets ships position.

* 'play_turn'

  Print board, choose position to hit and print result on board.

 

