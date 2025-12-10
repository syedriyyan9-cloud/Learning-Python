# Date: 9 december 2025
# Name: riyyan
# 13-1. Stars: Find an image of a star. Make a grid of stars appear on the screen.

import pygame

import sys

from stars import stars

import random

class Game:
    '''a class to represent game'''
    
    def __init__(self):
        '''intilize attributes'''
        pygame.init()
        self.screen = pygame.display.set_mode((1400,900))
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height
        self.stars = pygame.sprite.Group()

    def _calculate_stars(self):
        '''calculate number of stars in rows and columns'''
        star = stars(self)
        star_width = star.rect.width
        star_height = star.rect.height
        available_space_x = self.screen_width - (2 * star_width)
        number_of_stars_x = available_space_x // (2 * star_width)
        avaliable_space_y = self.screen_height - (2 * star_height)
        number_of_stars_y = avaliable_space_y // star_height

        random_number_x = random.randint(0, number_of_stars_x)
        random_number_y = random.randint(0, number_of_stars_y)

        random_row_of_stars = random.randint(-10,random_number_x)
        random_number_of_stars = random.randint(-10,random_number_y)
        
        for rows in range(random_row_of_stars):
            for number in range(random_number_of_stars):
                self._grid_of_stars(number, rows)

    def _grid_of_stars(self,number,rows):
        '''create grid of stars'''
        star = stars(self)
        star_width = star.rect.width
        star_height = star.rect.height
        star.y = 2 * star_height * rows
        star.x = star_width + 2 * star_width * number
        star.rect.x = star.x
        star.rect.y = star.y
        self.stars.add(star)        

    def _update_screen(self):
        '''update screen'''
        self._calculate_stars()
        self.stars.draw(self.screen)
        pygame.display.flip()

    def run(self):
        '''keep the game running'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._update_screen()

if __name__ == '__main__':
    game = Game()
    game.run()
