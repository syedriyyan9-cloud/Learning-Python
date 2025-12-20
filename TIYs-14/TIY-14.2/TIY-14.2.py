# Date: 20 december
# Name: Riyyan

# 14-2. Target Practice: Create a rectangle at the right edge of the screen that
# moves up and down at a steady rate. Then have a ship appear on the left side
# of the screen that the player can move up and down while firing bullets at the
# moving, rectangular target. 
# 
# Add a Play button that starts the game, and when
# the player misses the target three times, end the game and make the Play but-
# ton reappear. Let the player restart the game with this Play button.

import sys

import pygame

from settings import Setting

from rectangle import Rectangle

from character import Character

from bullets import Bullet

class Game:
    '''a class to represent the game'''

    def __init__(self):
        '''create game attributes'''
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.setting = Setting()
        self.rectangle = Rectangle(self)
        self.character = Character(self)
        self.bullet = pygame.sprite.Group()

    def update_screen(self):
        '''update screen for events'''
        self.screen.fill(self.setting.bg_color_white)
        self.rectangle.draw()
        self.character.draw()
        for bullet in self.bullet.sprites():
            bullet.move_bullet()
            bullet.draw()
        self._delete_fired_bullets()
        pygame.display.flip()

    def check_events(self):
        '''check for events'''
        for event in pygame.event.get():
            self._check_up_events(event)
            self._check_down_events(event)
    
    def _check_down_events(self, event):
        '''check for key presses'''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.character.move_up = True
            if event.key == pygame.K_s:
                self.character.move_down = True
            if event.key == pygame.K_a:
                self.character.move_left = True
            if event.key == pygame.K_d:
                self.character.move_right = True
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _fire_bullet(self):
        '''fire bullets'''
        bullet = Bullet(self)
        self.bullet.add(bullet)
    
    def _delete_fired_bullets(self):
        '''delete the bullet that have moved passed the screen'''
        for bullet in self.bullet.copy():
            if bullet.rect.right > self.screen_rect.right:
                self.bullet.remove(bullet)

    def _check_up_events(self, event):
        '''check for key releases'''
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.character.move_up = False
            if event.key == pygame.K_s:
                self.character.move_down = False
            if event.key == pygame.K_a:
                self.character.move_left = False
            if event.key == pygame.K_d:
                self.character.move_right = False

    def run(self):
        '''keep the game window open indefinitly'''
        while True:
            self.update_screen()
            self.check_events()
            self.character.move_player()
            self.rectangle.move_rectangle()
            
if __name__ == "__main__":
    game = Game()
    game.run()