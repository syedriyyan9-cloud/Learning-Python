class Settings:
    '''a class to represent settings for the game'''

    def __init__(self):
        '''create settings for the game'''
        self.bg_color_white = (255,255,255)
        self.bg_color_black = (0,0,0)
        self.bg_color_red = (255,0,0)
        self.bg_color_green = (0,255,0)
        self.bg_color_blue = (0,0,255)

        self.character_speed = 3

        self.bullet_width = 7
        self.bullet_height = 7
        self.bullet_speed = 5

        self.enemy_direction = 1
        self.enemy_speed = 0.3