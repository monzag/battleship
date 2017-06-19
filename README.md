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

__Instance Method__

* #### '__init__(self, row, column)'

  Constructs an Square object
  
* 'hit(self)'
  
  Set object *is_hit* attribute to True

* '__str__(self)'

  Returns a string as a 'x' when Square is hit. 
  Otherwise returns position a string.


### 'ship.py'

This is the file containing a Ship item logic.

### Class Ship

__Instance Attributes__

* 'is_sunk'
  - data: bool
  - default: False
  - description: True if ship is sunk

* 'is_horizontal'
  - data: bool
  - description: True if is horizontal 

* 'size'
  - data: intiger (1 - 5)
  - description: amount of Square objects in Ship 

* 'squares'
  - data: list 
  - description: list of Square objects

* 'row'
  - data: intiger
  - description: y position of first Square object

* 'column'
  - data: intiger
  - description: x position of first Square object

__Instance Method__

* #### '__init__(self, size, is_horizontal, row, column)'

  Constructs an Ship object

* 'set_ship(self)'
  Set ship on valid position, can't touch another ships

* 'check_sunk(self)'
  Check every Square object in *squares*. 
  If every * is_hit* is True sets object's attribute *is_sunk* to True

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

 

