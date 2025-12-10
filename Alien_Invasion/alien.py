import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    '''a class to represent aliens'''
    def __init__(self, game):
        '''intilize setup attributes'''
        super().__init__()
        self.screen = game.screen
        self.setting = game.setting
        self.image_width = 100
        self.image_height = 100
        self.image = pygame.image.load('images\\alien_ship.bmp')
        self.resized_image = pygame.transform.scale(self.image,
                                                    (self.image_width,
                                                     self.image_height))
        self.rect = self.resized_image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        self.x = float(self.rect.x)

    def check_direction(self):
        '''check the direction of aliens'''
        self.screen_rect = self.screen.get_rect()
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        '''update alien position'''
        self.x += (self.setting.alien_speed * self.setting.fleet_direction)
        self.rect.x = self.x