import os
from colors import Colors


class OutputMenager:
    
    @classmethod
    def print_battlefild(cls, own_ocean, enemy_ocean):
        '''
        Prints battlefild(ocean obj. of both players) next to each other,
        every next turn

        Parameters:
            own_battlefield   : ocean as string (current player that has turn)
            enemy_battlefiels : ocean as string (other player)
        
        Return
            None
        '''
        own_ocean = own_ocean.split('\n')
        enemy_ocean = enemy_ocean.split('\n')

        if len(own_ocean) != len(enemy_ocean):
            raise ValueError
        
        os.system('clear')
        battlefild = '\n'.join([' {}    {}'.format(own_ocean[i], enemy_ocean[i]) for i in range(len(own_ocean))])
        battlefild += '\n' + Colors.OKGREEN +'{: ^24}  '.format('YOUR MAP')
        battlefild += '{: ^24}\n'.format('ENEMY MAP') + Colors.ENDC
        print(battlefild)

        