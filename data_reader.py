import re

class DataReader:

    _ROWS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    
    def input_position(self):
        '''
        Repeat asking user for position in Ocean object (ex. A3) 
        until provided data is a valid position

        Returns:
            (row, column) : tuple of ints in range of 0->9
        '''
        pattern = r'(?P<row>[a-j]|[A-J])(?P<column>[0-9])$'

        user_input = input('\nInput posision(ex. A3): ')
        while not re.match(pattern, user_input):
            user_input = input('\nInvalid posision, try again(ex. A3): ')

        match = re.match(pattern, user_input)
        if match:
            row = self._ROWS.index(match.group('row').upper())
            column = int(match.group('column'))

        return row, column
    
    def input_orientation(self):
        '''
        Repeats asking user for orientation (vertical-horizontal)
        until provided data is correct

        Returns:
            True  if vertical
            False if horizontal
        '''
        pattern = r'(?P<is_vertical>(Y|YES)|(N|NO))'

        user_input = input('\nShould ship be vertical(yes/no): ').upper()
        while not re.match(pattern, user_input):
            user_input = input('\nInvalid answer, try again(yes/no): ').upper()
        
        match = re.match(pattern, user_input)
        if match:
            if 'Y' not in match.group('is_vertical'):
                return False
        
        return True
    
    def input_player_name(self, player_number):
        if player_number == 1:
            player_number = 'first'
        else:
            player_number = 'second'
    
        name = input('\nWhat is the name of {} player: '.format(player_number))
        while not (3 < len(name) < 13):
            name = input('\nName should be between 4-12 characters long: ')
        
        return name.capitalize()


data_reader = DataReader()
name = data_reader.input_player_name(1)
print(name)