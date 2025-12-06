import pygame

import settings

class Character:
    '''a class to represent character'''
    def __init__(self,game):
        '''consturctor'''
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.setting = game.setting

        self.image = pygame.image.load('images\\rocket.bmp')
        self.image_width = 100
        self.image_height = 100
        self.resize_image = pygame.transform.scale(self.image,(self.image_width,
                                                               self.image_height))
        self.rect = self.resize_image.get_rect()
        self.rect.center = self.screen_rect.center
        
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update_motion(self):
        '''check for motion'''
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.ship_speed
        if self.move_up and self.rect.top > 0:
            self.y -= self.setting.ship_speed
            
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        '''to put image to game screen'''
        self.screen.blit(self.resize_image, self.rect)