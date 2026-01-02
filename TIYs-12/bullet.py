import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    '''a class to represent bullets'''
    
    def __init__(self, game):
        '''initilize the variables'''
        super().__init__()
        self.screen = game.screen
        self.setting = game.setting
        self.color = self.setting.bullet_color

        self.rect = pygame.Rect(0,0,self.setting.bullet_width,
                                self.setting.bullet_height)
        self.rect.midtop = game.character.rect.midtop
        self.x = float(self.rect.x)

    def update(self):
        '''update bullet motion'''
        self.x += self.setting.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        '''draw bullet onto screen'''
        pygame.draw.rect(self.screen,self.color,self.rect)
        
        