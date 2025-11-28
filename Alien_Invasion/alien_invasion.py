import sys

import pygame

import ship

from settings import Settings

class Alien_Invasion:
    '''a class to represent game elements'''

    def __init__(self):
        '''constructor to initialize attributes and pygame'''
        pygame.init()
        self.setting = Settings()
        #create a game window
        self.screen = pygame.display.set_mode((self.setting.width,
                                               self.setting.height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = ship.Ship(self)

    def run_game(self):
        '''method to keep the game running and update changes'''
        while True:
            # listen for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #display the most recent screen
            pygame.display.flip()
            self.screen.fill(self.setting.bg_color) # fill screen with bg color
            self.ship.blitme()

if __name__ == '__main__':
    ai = Alien_Invasion()
    ai.run_game()