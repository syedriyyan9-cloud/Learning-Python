import pygame

from pygame.sprite import Sprite

class Bullets(Sprite):
    '''a class to manage bullets'''

    def __init__(self, ai_game):
        '''Create a bullet object at the ship's current position'''
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.color = self.setting.bullet_color

        self.rect = pygame.Rect(0,0,self.setting.bullet_width,
                                self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        '''update bullets poisition'''
        self.y -= self.setting.bullet_speed

        self.rect.y = self.y

    def draw_bullet(self):
        '''method for drawing bullet onto the main screen'''
        pygame.draw.rect(self.screen,self.color,self.rect)


        