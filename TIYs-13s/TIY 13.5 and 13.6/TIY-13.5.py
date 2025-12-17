# Date: 13 december 2025
# Name: Riyyan

# 13-5. Sideways Shooter Part 2: We’ve come a long way since Exercise 12-6,
# Sideways Shooter. For this exercise, try to develop Sideways Shooter to the
# same point we’ve brought Alien Invasion to. Add a fleet of aliens, and make
# them move sideways toward the ship. Or, write code that places aliens at ran-
# dom positions along the right side of the screen and then sends them toward
# the ship. Also, write code that makes the aliens disappear when they’re hit.

import pygame

import sys

from setting import Settings

from character import Character

from bullets import Bullet

from enemy import Enemy

from gamestats import GameStats

from time import sleep

class SidewaysShooter:
    '''a class to represent sideway shooter game'''

    def __init__(self):
        '''create attributes of game'''
        pygame.init()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.setting = Settings()
        self.character = Character(self)
        self.stats = GameStats(self)
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height
        self.bg_color = self.setting.bg_color_white
        self.bullet = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self._create_enemy_fleet()

    def _update_screen(self):
        '''a method to update screen'''
        self.character.built()
        self.enemy.draw(self.screen)
        self._delete_fired_bullet()
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
        self.screen.fill(self.bg_color)

    def check_events(self):
        '''method to check for events'''
        for event in pygame.event.get():
            self._check_down_events(event)
            self._check_up_events(event)
            if event.type == pygame.QUIT:
                sys.exit()

    def _check_down_events(self, event):
        '''method to check for key presses'''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.character.move_down = True
            if event.key == pygame.K_UP:
                self.character.move_up = True
            if event.key == pygame.K_LEFT:
                self.character.move_left = True
            if event.key == pygame.K_RIGHT:
                self.character.move_right = True
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_SPACE:
                self._fire_bullet()
            # if event.key == pygame.K_p:
            #     self.character.center_ship()
            #     self.stats.reset_game()
            #     self.stats.active = True


    def _check_up_events(self, event):
        '''method to check for key releases'''
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.character.move_down = False
            if event.key == pygame.K_UP:
                self.character.move_up = False
            if event.key == pygame.K_LEFT:
                self.character.move_left = False
            if event.key == pygame.K_RIGHT:
                self.character.move_right = False

    def _fire_bullet(self):
        '''method to fire bullets'''
        bullet = Bullet(self)
        self.bullet.add(bullet)
        # print(True)
    
    def _delete_fired_bullet(self):
        '''a method to delete fired bullets'''
        for bullet in self.bullet.copy():
            if bullet.rect.left >= self.screen_width:
                self.bullet.remove(bullet)
        self._collisions()

    def _collisions(self):
        '''method to check for collisions'''
        collision = pygame.sprite.groupcollide(self.bullet,self.enemy,True,True)
        if not self.enemy:
            self.bullet.empty()
            self._create_enemy_fleet()

    def _create_enemy_fleet(self):
        '''create enemy fleet'''
        enemy = Enemy(self)
        enemy_width = enemy.rect.width
        enemy_height = enemy.rect.height
        
        available_space_x = self.screen_width - (2 * enemy_width)
        available_space_y = self.screen_height - (2 * enemy_height)

        enemies_in_x = available_space_x // (3*enemy_width)
        enemies_in_y = available_space_y // (2*enemy_height)
        
        # print(enemies_in_x, enemies_in_y)
        for row in range(enemies_in_y):
            for column in range(enemies_in_x):
                self._create_enemies(row,column)
            
    def _create_enemies(self, row, column):
        '''create enemies for fleet'''
        enemy = Enemy(self)
        enemy_width = enemy.rect.width
        enemy_height = enemy.rect.height
        enemy.y = self.screen_height - (2*enemy_height * column) - enemy_height
        enemy.x = self.screen_width - 2 * enemy_width * row
        enemy.rect.x = enemy.x
        enemy.rect.y = enemy.y
        # print(row,column)
        self.enemy.add(enemy)

    def _update_enemies(self):
        '''update the position of enemies'''
        self.enemy.update()
        if pygame.sprite.spritecollideany(self.character,self.enemy,):
            self.setting.player_lives -= 1
            self._ship_hit()

    def _ship_hit(self):
        '''next step when ship is hit'''
        if self.stats.setting.player_lives > 0:
            self.character.center_ship()
            self.bullet.empty()
            self.enemy.empty()
            self._create_enemy_fleet()
            sleep(0.5)
        else:
            self.stats.active = False

    def run(self):
        '''method to keep the game running'''
        while True:
            self.check_events()
            if self.stats.active:
                self.bullet.update()
                self._update_enemies()
                self.character.move_position()
            self._update_screen()

if __name__ == "__main__":
    '''only run game when file is executed directly'''
    game = SidewaysShooter()
    game.run()

