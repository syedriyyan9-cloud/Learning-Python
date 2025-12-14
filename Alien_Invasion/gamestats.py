class GameStats:
    '''a class to represent statistics for the game'''
    
    def __init__(self, game):
        '''create stats for the game here!!'''
        self.screen = game.screen
        self.setting = game.setting
        self.reset_stats()

    def reset_stats(self):
        '''reset to default values'''
        self.ships_left = self.setting.ship_limit