import pygame

class Enemy:
    '''a class to represent the enemy'''

    def __init__(self, game):
        '''create attributes for enemy'''
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.setting = game.setting
        self.rect = pygame.Rect(0,0,
                                self.setting.enemy_width,
                                self.setting.enemy_height)
        self.rect.left = self.screen_rect.left
    
    def draw(self):
        '''draw the rectangle onto the screen'''
        self.screen.blit()