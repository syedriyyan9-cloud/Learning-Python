import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
    '''a class to manage ship'''

    def __init__(self, ai_game):
        '''initialize position and create image'''
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.setting
        # load image and scaling it
        self.image_width = 100
        self.image_height = 150
        self.image = pygame.image.load('images\space_ship.bmp')
        self.scaled_image = pygame.transform.scale(
            self.image,(self.image_width,self.image_height))
        self.rect = self.scaled_image.get_rect()
        # load ship at bottom
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        # speed of the ship
        self.x = float(self.rect.x)

    def update_motion(self):
        '''update the position of the ship'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        '''Draw the ship at current position'''
        self.screen.blit(self.scaled_image, self.rect)

    def center_ship(self):
        '''recenter the ship'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)