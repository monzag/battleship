# Write welcome screen
from data_reader import DataReader
import random
from player import Player
from ocean import Ocean
from output_manager import OutputManager
from ship import Ship
from hunting import Hunting


class GameController:
    '''
    Logic game.
    '''

    def choose_option(self):
        '''
        Display options and choose game mode by user (number 1-3).

        Returns:
            mode : int
        '''

        option = '''
        Game modes:
        1) single player
        2) multiplayer
        3) simulation
        '''
        print(option)
        mode = DataReader.input_player_choice()

        return mode

    def choose_first_player(self, player_1, player_2):
        '''
        Random choose first player.

        Args:
            player_1, player_2 : Player object

        Returns:
            first_player, second_player : string
        '''

        players = [player_1.name, player_2.name]
        randomly = random.choice(players)

        if randomly == player_1.name:
            first_player = player_1
            second_player = player_2
        else:
            first_player = player_2
            second_player = player_1

        return first_player, second_player

    def set_mode(self, mode):
        '''
        Set proper mode: single players, multiplayers or simulation

        Args:
            mode : int

        Returns:
            None
        '''

        # to do: single players
        if mode == 1:
            player_1, player_2 = self.set_single_players()

        # multiplayers
        if mode == 2:
            player_1, player_2 = self.set_multiplayers()

        # simulation
        if mode == 3:
            player_1, player_2 = self.set_simulation()

        return player_1, player_2

    def set_single_players(self):
        '''
        Game player - computer. Set ships, 

        Returns:
            player_1, player_2 - Player object
        '''
        
        player_type = 'human'
        print('Setting First player')
        user_1 = DataReader.input_player_name()
        player_1 = Player(user_1, Ocean())
        print('{} set you ships'.format(player_1.name))
        player_1.get_ships_from_player(player_type)

        player_type = 'computer'
        print('Setting computer player')
        user_2 = 'computer'
        player_2 = Player(user_2, Ocean())
        player_2.generate_ships_for_computer(player_type)

        return player_1, player_2

    def set_multiplayers(self):
        '''
        Game player - player.

        Returns:
            player_1, player_2 - Player object
        '''

        player_type = 'human'
        print('Setting First player')
        user_1 = DataReader.input_player_name()
        player_1 = Player(user_1, Ocean())
        print('{} set you ships'.format(player_1.name))
        player_1.get_ships_from_player(player_type)

        print('Setting second player')
        user_2 = DataReader.input_player_name()
        player_2 = Player(user2, Ocean())
        print('{} set you ships'.format(player_2.name))
        player_2.get_ships_from_player(player_type)

        return player_1, player_2

    def set_simulation(self):
        '''
        Game computer - computer

        Returns:
            player_1, player_2 - Player object
        '''

        player_type = 'computer'

        print('Setting computer player')
        user_1 = 'computer'
        player_1 = Player(user_1, Ocean())
        player_1.generate_ships_for_computer(player_type)

        print('Setting second computer player')
        user_2 = 'computer_2'
        player_2 = Player(user_2, Ocean())
        player_2.generate_ships_for_computer(player_type)

        return player_1, player_2

    def play_game(self, present_player, next_player):
        '''
        Set present player and next player.
        Set player turns: display 2 board (user and enemy), get hit position, check result.
        If player not win, switch players.

        Args:
            player_1 - Player object
            player_2 - Player object

        Returns:
            name player : name Player object
            points: int
        '''

        game = present_player.is_game_win
        moves = 0
        while not game:
            moves += 1
            OutputManager.print_battlefield(present_player.ocean, next_player.ocean)
            print('Your turn, ' + present_player.name)

            if present_player.name == 'computer':
                hunting = Hunting()
                hit_row, hit_column = hunting.shoot_random()
                input('enter')

            elif present_player.name == 'computer_2':
                hunting = Hunting()
                hit_row, hit_column = hunting.shoot_random()
                input('enter')

            else:
                hit_row, hit_column = DataReader.input_position()

            turn_result = next_player.check_user_hit(hit_row, hit_column)
            OutputManager.print_battlefield(present_player.ocean, next_player.ocean)
            input(turn_result)
            present_player, next_player = next_player, present_player

            game = present_player.is_game_win

        points = 1000 - int(moves/2)

        return next_player.name, points

    def end_game(self, winner, points):
        '''
        Display information about winner and write result to file. 

        Args:
            winner : string
            points : int

        Returns:
            None
        '''

        print('The winner is: {}, with {} points'.format(winner, points))
        with open('highscores.csv', 'a') as highscore:
            highscore.write('{}|{}\n'.format(points, winner))

    def run_up(self):
        '''
        Starting Game.

        Returns:
            None
        '''

        mode = self.choose_option()
        ocean = Ocean()
        player_1, player_2 = self.set_mode(mode)
        present_player, next_player = self.choose_first_player(player_1, player_2)
        winner, points = self.play_game(present_player, next_player)
        self.end_game(winner, points)






