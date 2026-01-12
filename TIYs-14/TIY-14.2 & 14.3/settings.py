class Setting:
    '''a class to represent game settings'''
    
    def __init__(self):
        '''create game settings'''
        self.color_change = (0,0,0)
        self.bg_color_white = (255,255,255)

        self.rectangle_speed = 1
        self.rectangle_width = 75
        self.rectangle_height = 100
        self.direction = -1

        self.character_speed = 3

        self.bullet_width = 6
        self.bullet_height = 6
        self.bullet_speed = 4
        self.bullet_color = (0,0,0)

        self.button_color_white = (255,255,255)
        self.button_color_black = (0,0,0)
        self.button_color_red = (255,0,0)
        self.button_color_green = (0,255,0)
        self.button_color_blue = (0,0,255)

        self.speedup_scale = 1.1

    def increase_game_speed(self):
        '''increase the game elements speed'''
        self.bullet_speed *= self.speedup_scale
        self.character_speed *= self.speedup_scale
        self.rectangle_speed *= self.speedup_scale
        self.direction *= -1
    
    def default_setting(self):
        '''restore game settings to default'''
        self.bullet_speed = 4
        self.character_speed = 3
        self.rectangle_speed = 1
        self.direction = -1