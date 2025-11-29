# Date: 29 november 2025
# Name: Riyyan

# 12-2. Game Character: Find a bitmap image of a game character you like or
# convert an image to a bitmap. Make a class that draws the character at the
# center of the screen and match the background color of the image to the back-
# ground color of the screen, or vice versa.

import pygame

class Game_Character:
    '''a class to create a game character'''

    def __init__(self,game):
        '''set variables'''
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('images\image.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''print image onto the window'''
        self.screen.blit(self.image,self.rect)
