class Settings:
    '''a class to represent settings of Alien invasion'''

    def __init__(self):
        # initializes the settings for game
        self.width = 800
        self.height = 800
        self.bg_color = (255,255,255)
        # speed of the ship
        self.ship_speed = 3
        self.ship_limit = 3

        self.bullet_speed = 6
        self.bullet_width = 8
        self.bullet_height = 5
        self.bullet_color = (0,0,0)
        self.bullets_allowed = 3

        self.screen_width = 0
        self.screen_height = 0

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # how quickly game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_setting()

        self.score_scale = 1.5

    def initialize_dynamic_setting(self):
        '''initialize game attributes that will change'''
        self.ship_speed = 6
        self.alien_speed = 2
        self.bullet_speed = 10
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        '''increase speed every time player levels up'''
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


