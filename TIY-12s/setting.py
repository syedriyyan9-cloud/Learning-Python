class Setting:
    '''a class to represent the setting for game'''

    def __init__(self):
        '''initilize setting values'''
        self.bg_color_white = (255,255,255)
        self.bg_color_black = (0,0,0)
        self.bg_color_red = (255,0,0)
        self.bg_color_green = (0,255,0)
        self.bg_color_blue = (0,0,255)

        self.character_speed = 5

        self.bullet_color = (0,0,0)
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_speed = 7

        self.enemy_width = 50
        self.enemy_height = 50