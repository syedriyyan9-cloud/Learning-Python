# Date: 29 november 2025
# Name: Riyyan

# 12-1. Blue Sky: Make a Pygame window with a blue background.

import sys

import pygame

import settings

import game_character

class Blue_Background:
    '''a class to represent a window with blue background'''

    def __init__(self):
        '''define values for attributes'''
        pygame.init()
        self.settings = settings.Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_size))
        self.character = game_character.Game_Character(self)
        # to make the background blue use 0,0,255
        self.bg_color = (self.settings.black) 

    def run_window(self):
        '''method to keep the window open'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()
            self.screen.fill(self.bg_color)
            self.character.blitme()

if __name__ == '__main__':
    window = Blue_Background()
    window.run_window()