class Settings:
    '''a class to represent settings of Alien invasion'''

    def __init__(self):
        # initializes the settings for game
        self.width = 800
        self.height = 800
        self.bg_color = (255,255,255)
        # speed of the ship
        self.ship_speed = 3

        self.bullet_speed = 3
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = (0,0,0)
        self.bullets_allowed = 3

        self.screen_width = 0
        self.screen_height = 0