import pygame

class Ship:
    '''a class to manage ship'''

    def __init__(self, ai_game):
        '''initialize position and create image'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # load image and scaling it
        self.image_width = 100
        self.image_height = 150
        self.image = pygame.image.load('images\space_ship.bmp')
        self.scaled_image = pygame.transform.scale(
            self.image,(self.image_width,self.image_height))
        self.rect = self.scaled_image.get_rect()
        # load ship at bottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''Draw the ship at current position'''
        self.screen.blit(self.scaled_image, self.rect)