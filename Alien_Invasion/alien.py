import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    '''a class to represent aliens'''
    def __init__(self, game):
        '''intilize setup attributes'''
        super().__init__()
        self.screen = game.screen
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
