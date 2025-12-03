# Date: 4 december 2025
# Name: Riyyan

# 12-4. Rocket: Make a game that begins with a rocket in the center of the
# screen. Allow the player to move the rocket up, down, left, or right using the
# four arrow keys. Make sure the rocket never moves beyond any edge of the
# screen.

import sys

import pygame

import settings

import game_character

class Rocket:
    '''a class to create rocket game'''

    def __init__(self):
        '''constructor to assign values'''
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.setting = settings.Settings()
        self.character = game_character.Character(self)

    def update(self):
        '''a method to refresh the screen'''
        pygame.display.flip()
        self.screen.fill(self.setting.bg_yellow)
        self.character.blitme()

    def run_game(self):
        '''a method to run the game'''
        while True:
            self.update()
            self._check_events()
            self.character.update_motion()

    def _check_events(self):
        '''a method to check for game events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self._check_keydown(event)
            self._check_keyup(event)

    def _check_keydown(self, event):
        '''a method to check keydown events'''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.character.move_right = True
            elif event.key == pygame.K_LEFT:
                self.character.move_left = True
            elif event.key == pygame.K_UP:
                self.character.move_up = True
            elif event.key == pygame.K_DOWN:
                self.character.move_down = True
            elif event.key == pygame.K_q:
                sys.exit()

    def _check_keyup(self, event):
        '''a method to check for key releases'''
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.character.move_right = False
            elif event.key == pygame.K_LEFT:
                self.character.move_left = False
            elif event.key == pygame.K_UP:
                self.character.move_up = False
            elif event.key == pygame.K_DOWN:
                self.character.move_down = False

if __name__ == '__main__':
    game = Rocket()
    game.run_game()