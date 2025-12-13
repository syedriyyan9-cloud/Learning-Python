from pygame.sprite import Sprite

import pygame

class Enemy(Sprite):
    '''a class to represent enemies'''

    def __init__(self, game):
        '''create attributes for enemy'''
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.setting = game.setting
        self.image = pygame.image.load('image\monster.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.rect.right = self.screen_rect.right
        self.rect.topright = self.screen_rect.topright

    def check_direction(self):
        '''check the direction of enemies'''
        if self.rect.bottom <= self.screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        '''move enemies'''
        self.x -= self.setting.enemy_speed
        self.rect.x = self.x
        self.y -= self.setting.enemy_speed * self.setting.enemy_direction
        self.rect.y = self.y
        if (self.rect.top == self.screen_rect.top or 
        self.rect.bottom == self.screen_rect.bottom):
            self.setting.enemy_direction *= -1
    
    # def built(self):
    #     '''draw enemies on the screen'''
    #     self.screen.blit(self.image,self.rect)