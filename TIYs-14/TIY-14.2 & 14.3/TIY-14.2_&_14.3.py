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

# 14-3. Challenging Target Practice: Start with your work from Exercise 14-2
# (page 285). Make the target move faster as the game progresses, and restart
# the target at the original speed when the player clicks Play.

import sys

import pygame

from settings import Setting

from rectangle import Rectangle

from character import Character

from bullets import Bullet

from button import Button

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
        self.button = Button(self,'Play')
        self.game_active = False
        self.display_button = True
        self.missed_bullets = 0

    def update_screen(self):
        '''update screen for events'''
        # self.change_color()
        self.screen.fill(self.setting.bg_color_white)
        self.rectangle.draw()
        self.character.draw()
        for bullet in self.bullet.sprites():
            bullet.move_bullet()
            bullet.draw()
        self._delete_fired_bullets()
        if self.display_button:
            self.button.draw()
        pygame.display.flip()

    def check_events(self):
        '''check for events'''
        for event in pygame.event.get():
            self._check_up_events(event)
            self._check_down_events(event)
            self._check_mouse_down(event)
    
    def _check_down_events(self, event):
        '''check for key presses'''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.character.move_up = True
            if event.key == pygame.K_DOWN:
                self.character.move_down = True
            if event.key == pygame.K_LEFT:
                self.character.move_left = True
            if event.key == pygame.K_RIGHT:
                self.character.move_right = True
            if event.key == pygame.K_q:
                sys.exit()
            if self.game_active:
                if event.key == pygame.K_SPACE:
                    self._fire_bullet()

    def _check_mouse_down(self, event):
        '''check mouse presses'''
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self._check_mouse_pos(mouse_pos):
                self.game_active = True
                self.display_button = False
                self.character._center_character()
                self.setting.default_setting()
            
    def _check_mouse_pos(self, pos):
        '''check the position of mouse'''
        button_pos = self.button.rect.collidepoint(pos)
        if button_pos:
            return True

    def _fire_bullet(self):
        '''fire bullets'''
        bullet = Bullet(self)
        self.bullet.add(bullet)
    
    def _delete_fired_bullets(self):
        '''delete the bullet that have moved passed the screen'''
        for bullet in self.bullet.copy():
            if bullet.rect.right > self.screen_rect.right:
                self.bullet.remove(bullet)
                self.missed_bullets += 1
            self._check_collision()
            self._check_missed_bullets()


    def _check_collision(self):
        '''check for collisions'''
        collision = pygame.sprite.spritecollide(self.rectangle,self.bullet,0)
        bullet_hit = False
        if collision and self.missed_bullets > 0:
            self.missed_bullets -= 1
            self.increase_speed_when_hit(bullet_hit)

    def increase_speed_when_hit(self, bullet):
        '''increase game speed only when bullet hits the rectangle'''
        bullet = True
        if bullet:
            self.setting.increase_game_speed()
            bullet = False

    def _check_missed_bullets(self):
        '''check for missed bullets'''
        if self.missed_bullets >= 3:
            self.game_active = False
            self.display_button = True
            self.missed_bullets = 0
            self.character._center_character()
     
    def _check_up_events(self, event):
        '''check for key releases'''
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.character.move_up = False
            if event.key == pygame.K_DOWN:
                self.character.move_down = False
            if event.key == pygame.K_LEFT:
                self.character.move_left = False
            if event.key == pygame.K_RIGHT:
                self.character.move_right = False

    def hide_mouse(self):
        '''hide mouse'''
        pygame.mouse.set_visible(False)
    
    def show_mouse(self):
        '''show mouse'''
        pygame.mouse.set_visible(True)

    def run(self):
        '''keep the game window open indefinitly'''
        while True:
            if self.game_active:
                self.character.move_player()
                self.rectangle.move_rectangle()
                self.hide_mouse()
            else:
                self.show_mouse()
                
            self.update_screen()
            self.check_events()
            
if __name__ == "__main__":
    game = Game()
    game.run()