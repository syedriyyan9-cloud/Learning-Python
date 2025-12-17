class GameStats:
    '''a class to represent game stats'''

    def __init__(self, game):
        '''create stats here'''
        self.screen = game.screen
        self.setting = game.setting
        # self.character = game.character
        self.active = True

    def reset_game(self):
        '''reset the game'''
        self.setting.player_lives = 3