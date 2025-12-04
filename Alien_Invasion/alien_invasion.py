import sys

import pygame

import ship

from settings import Settings

import bullets

class Alien_Invasion:
    '''a class to represent game elements'''

    def __init__(self):
        '''constructor to initialize attributes and pygame'''
        pygame.init()
        self.setting = Settings()
        #create a game window
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = ship.Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        '''method to keep the game running and update changes'''
        while True:
            self._check_events()
            self._update_screen()        
            self.ship.update_motion()
            self.bullets.update()
            self._delete_fired_bullets()

    def _delete_fired_bullets(self):
        '''a method to delete fired bullets'''
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    def _fire_bullets(self):
        '''a method to create and fire bullets'''
        new_bullet = bullets.Bullets(self)
        self.bullets.add(new_bullet)

    def _check_events(self):
        '''a helper function to check for events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
            
            self._check_keydown_events(event)
            self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        '''a helper method to check for key presses'''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_SPACE:
                self._fire_bullets() 

    def _check_keyup_events(self,event):
        '''a helper method to check for key releases'''
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False    
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _update_screen(self):
        '''a helper function to display the most recent screen'''
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
        self.screen.fill(self.setting.bg_color) # fill screen with bg color
        self.ship.blitme()


if __name__ == '__main__':
    ai = Alien_Invasion()
    ai.run_game()