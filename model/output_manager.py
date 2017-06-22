import os
from colors import Colors
from ocean import Ocean


class OutputManager:

    _ROWS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    @classmethod
    def print_battlefield(cls, own_ocean, enemy_ocean):
        '''
        Prints battlefild(ocean obj. of both players) next to each other,
        every next turn

        Parameters:
            own_battlefield   : ocean obj (current player that has turn)
            enemy_battlefiels : ocean obj (other player)
        
        Return
            None
        '''
        own_ocean = own_ocean.get_ocean_string(True).split('\n')
        enemy_ocean = enemy_ocean.get_ocean_string(False).split('\n')

        battlefield = ['{}    {}'.format(own_ocean[i], enemy_ocean[i]) for i in range(len(own_ocean))]
        battlefield = '\n'.join(battlefield)

        os.system('clear')
        print(battlefield)
    
    @classmethod
    def print_single_battlefield(cls, ocean, is_player_own):
        '''
        Prints single ocean which is player owns

        Parameters:
            ocean : Ocean obj
        
        Return:
            None
        '''
        os.system('clear')
        battlefild = ocean.get_ocean_string(True)
        
        print(battlefild)