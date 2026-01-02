from pygame.sprite import Sprite

import pygame

class Drops(Sprite):
    '''a class to represent drops of rain'''

    def __init__(self,game):
        '''initialize drops'''
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = game.setting
        self.image = pygame.image.load('images\drop.bmp')
        self.rect = self.image.get_rect()
        self.y = float(self.rect.y)

    def check_edges(self):
        '''check the position of raindrops'''
        if self.rect.bottom >= self.screen_rect.bottom:
            return True

    # def update(self):
    #     '''update the position of rain drops'''
    #     self.y += self.setting.drop_speed
    #     self.rect.y = self.y