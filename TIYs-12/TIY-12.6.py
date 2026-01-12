# Date: 5 december
# Name: Riyyan

# 12-6. Sideways Shooter: Write a game that places a ship on the left side of 
# the screen and allows the player to move the ship up and down. Make the ship 
# fire a bullet that travels right across the screen when the player presses 
# the spacebar. Make sure bullets are deleted once they disappear off the screen

import pygame

import sys

import setting

import game_character

import bullet

class Game:
    '''a class to represent game'''

    def __init__(self):
        '''initialize game attributes'''
        pygame.init()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.setting = setting.Setting()
        self.bg_color = self.setting.bg_color_white
        self.character = game_character.Game_Character(self)
        self.bullets = pygame.sprite.Group()

    def update_events(self):
        '''check for events in the game'''
        for event in pygame.event.get():            
            self._check_down_events(event)
            self._check_up_events(event)
            
    def _check_down_events(self,event):
        '''check for key presses'''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.character.move_up = True
            if event.key == pygame.K_DOWN:
                self.character.move_down = True
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_SPACE:
                self._fire_bullets()
        
    def _check_up_events(self, event):
        '''a method to check for key releases'''
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.character.move_up = False
            if event.key == pygame.K_DOWN:
                self.character.move_down = False

    def _update_screen(self):
        '''keep the screen updated'''
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
        self.screen.fill(self.bg_color)
        self.character.built()

    def _fire_bullets(self):
        '''method to fire bullets'''
        new_bullet = bullet.Bullet(self)
        self.bullets.add(new_bullet)

    def _delete_fired_bullets(self):
        '''a method to delete the bullets that went out of the screen'''
        for bullet in self.bullets.copy():
            if bullet.rect.right > self.screen_width:
                self.bullets.remove(bullet)

    def run_game(self):
        '''method to keep the game running'''
        while True:
            self.update_events()
            self.character.update_motion()
            self.bullets.update()
            self._delete_fired_bullets()
            self._update_screen()

if __name__ == '__main__':
    game = Game()
    game.run_game()