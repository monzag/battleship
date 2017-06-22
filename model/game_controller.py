# Write welcome screen
from data_reader import DataReader
import random
from player import Player


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
        mode = DataReader.input_player_choice(option)

        level = '''
        Game level:
        1) easy
        2) medium
        3) hard
        '''
        print(level)
        level = DataReader.input_player_choice(level)

        return mode, level

    def choose_first_player(self, mode):
        '''
        Get user name and random choose first player

        Args:
            mode - int

        Returns:
            first_player, second_player - string
        '''

        user_1 = DataReader.input_player_name()
        user_2 = DataReader.input_player_name()

        players = [user_1, user_2]
        first_player = random.choice(players)

        if first_player == user_1:
            second_player = user_2
        else:
            first_player = user_2
            second_player = user_1

        return first_player, second_player

    def set_mode(self, ocean, mode, first_player, second_player):
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
        if mode == '2':
            player_1 = Player(first_player, ocean)
            print(ocean.get_ocean_string(True))

            player_2 = Player(second_player, ocean)
            print(ocean.get_ocean_string(True))

            return player_1, player_2

    def player_turn(self, player_1, player_2):
        # to do: show 2 board

        present_player = player_1
        next_player = player_2
        while True:
            print('Your turn, ' + present_player.name)

            hit_pos = DataReader.input_position()
            present_player.check_user_hit(hit_pos)

            present_player, next_player = next_player, present_player
        pass

    def run_up(self):
        mode, level = self.choose_option
        first_player, second_player = self.choose_first_player
        ocean = Ocean()
        player_1, player_2 = self.set_mode(ocean, mode, first_player, second_player)
        self.player_turn(player_1, player_2)





