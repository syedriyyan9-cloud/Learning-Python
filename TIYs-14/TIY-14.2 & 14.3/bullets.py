from pygame.sprite import Sprite

import pygame

class Bullet(Sprite):
    '''a class to represent bullets'''

    def __init__(self, game):
        '''initilize attributes'''
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.setting = game.setting
        self.rect = pygame.Rect(0,0,self.setting.bullet_width,
                                self.setting.bullet_height)
        self.character = game.character
        self.rect.midright = self.character.rect.midright
        self.x = float(self.rect.x)

    def move_bullet(self):
        '''move bullet position'''
        self.x += self.setting.bullet_speed
        self.rect.x = self.x

    def draw(self):
        '''draw bullets onto the screen'''
        pygame.draw.rect(self.screen, self.setting.bullet_color, self.rect)