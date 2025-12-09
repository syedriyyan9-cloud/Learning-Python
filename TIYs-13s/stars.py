from pygame.sprite import Sprite

import pygame

class stars(Sprite):
    '''a class to represent stars'''

    def __init__(self, game):
        '''set image to surface'''
        super().__init__()
        self.screen = game.screen
        # self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('images\star.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


