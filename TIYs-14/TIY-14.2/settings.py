class Setting:
    '''a class to represent game settings'''
    
    def __init__(self):
        '''create game settings'''
        self.bg_color_white = (255,255,255)

        self.rectangle_speed = 5
        self.rectangle_width = 75
        self.rectangle_height = 100
        self.direction = -1

        self.character_speed = 3

        self.bullet_width = 6
        self.bullet_height = 6
        self.bullet_speed = 4
        self.bullet_color = (0,0,0)