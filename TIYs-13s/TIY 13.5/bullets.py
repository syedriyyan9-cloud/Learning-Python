from pygame.sprite import Sprite

import pygame

class Bullet(Sprite):
    '''a class to represent bullets'''

    def __init__(self, game):
        '''create bullet variables'''
        super().__init__()
        self.screen = game.screen
        self.setting = game.setting
        self.rect = pygame.Rect(0,0,self.setting.bullet_width,
                                  self.setting.bullet_height)
        self.rect.midright = game.character.rect.midright
        self.color = self.setting.bg_color_red

        self.x = float(self.rect.x)

    def update(self):
        '''method to update bullets position'''
        self.x += self.setting.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        '''method to draw bullets onto the screen'''
        pygame.draw.rect(self.screen,self.color,self.rect)
        # print(True)