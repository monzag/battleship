# Write welcome screen
from data_reader import DataReader
import random
from player import Player
from ocean import Ocean
from output_manager import OutputManager
from ship import Ship


class GameController:

    def __init__(self):
        self.player = []

    def choose_option(self):
        '''
        Display options and choose game mode/level by user (number 1-3).

        Returns:
            mode, level - int
        '''

        option = '''
        Game modes:
        1) single player
        2) multiplayer
        3) simulation
        '''
        print(option)
        mode = DataReader.input_player_choice()

        level = '''
        Game level:
        1) easy
        2) medium
        3) hard
        '''
        print(level)
        level = DataReader.input_player_choice()

        return mode, level

    def choose_first_player(self, mode):
        '''
        Get user name and random choose first player

        Args:
            mode - int

        Returns:
            first_player, second_player - string
        '''
        print('First player')
        user_1 = DataReader.input_player_name()
        print('Second player')
        user_2 = DataReader.input_player_name()

        players = [user_1, user_2]
        first_player = random.choice(players)

        if first_player == user_1:
            second_player = user_2
        else:
            first_player = user_2
            second_player = user_1

        return first_player, second_player

    def set_mode(self, mode, first_player, second_player):
        '''
        Set proper mode: single players, multiplayers or simulation

        Args:
            ocean
            mode - int
            first_player - string
            second_player - string

        Returns:
            None
        '''

        # to do: single players

        # multiplayers
        if mode == 2:
            player_1 = Player(first_player, Ocean())
            print('{} set you ships'.format(player_1.name))
            player_1.get_ships_from_player()

            player_2 = Player(second_player, Ocean())
            print('{} set you ships'.format(player_2.name))
            player_2.get_ships_from_player()

            return player_1, player_2

    def play_game(self, player_1, player_2):
        present_player = player_1
        next_player = player_2

        game = present_player.is_game_win
        moves = 0
        while not game:
            moves += 1
            OutputManager.print_battlefield(present_player.ocean, next_player.ocean)
            print('Your turn, ' + present_player.name)
            hit_row, hit_column = DataReader.input_position()
            turn_result = next_player.check_user_hit(hit_row, hit_column)

            OutputManager.print_battlefield(present_player.ocean, next_player.ocean)
            input(turn_result)
            present_player, next_player = next_player, present_player

            game = present_player.is_game_win

        points = 1000 - int(moves/2)

        return next_player.name, points

    def end_game(self, winner, points):

        print('The winner is: {}, with {} points'.format(winner, points))
        with open('highscores.csv', 'a') as highscore:
            highscore.write('{}|{}\n'.format(points, winner))

    def run_up(self):
        mode, level = self.choose_option()
        first_player, second_player = self.choose_first_player(mode)
        print('first: ', first_player)
        print('second: ', second_player)
        ocean = Ocean()
        player_1, player_2 = self.set_mode(mode, first_player, second_player)
        winner, points = self.play_game(player_1, player_2)
        self.end_game(winner, points)






