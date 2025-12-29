import sys

import pygame

import ship

from settings import Settings

import bullets

import alien

from time import sleep

from gamestats import GameStats

from button import Button

from scoreboard import ScoreBoard

from pygame import mixer #importing mixer to load and play sound effects

class Alien_Invasion:
    '''a class to represent game elements'''

    def __init__(self):
        '''constructor to initialize attributes and pygame'''
        pygame.init()
        self.setting = Settings()
        #create a game window
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.stats = GameStats(self)
        self.button = Button(self, "Play")
        self.sb = ScoreBoard(self)
        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = ship.Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.sound = mixer.Sound

    def run_game(self):
        '''method to keep the game running and update changes'''
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update_motion()
                self._check_fleet_direction()
                self._update_alien()
                self.bullets.update()
            self._delete_fired_bullets()
            self._update_screen()        

    def _delete_fired_bullets(self):
        '''a method to delete fired bullets'''
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        '''check collisions and delete sprites on collision'''
        collisions = pygame.sprite.groupcollide(self.bullets,
                                                self.aliens,True,True)
        if collisions:
            for alien in collisions.values():
                self.stats.score += self.setting.alien_points * len(alien)
            self._create_explosion_sound() #TIY 14.7
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            self.start_new_level()

    def _create_explosion_sound(self):
        '''creates an explosion sound effect ''' #TIY 14.7
        enemy_explosion = self.sound('sounds/explosion_sound.wav')
        enemy_explosion.play()

    def start_new_level(self):
        '''start new level'''
        self.bullets.empty()
        self._create_fleet()
        self.setting.increase_speed()
        self.stats.level += 1
        self.sb.prep_level()

    def _fire_bullets(self):
        '''a method to create and fire bullets'''
        if len(self.bullets) < self.setting.bullets_allowed:
            new_bullet = bullets.Bullets(self)
            self.bullets.add(new_bullet)

    # TIY 14.1 solution
    def _check_play_button(self, pos):
        '''Start a new game when the player clicks Play'''
        button_clicked = self.button.rect.collidepoint(pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()
            self.setting.initialize_dynamic_setting()

    def _start_game(self):
        '''start game by pressing button (P) '''
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ship()
        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()
        self.ship.center_ship()
        pygame.mouse.set_visible(False)

    def _check_events(self):
        '''a helper function to check for events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # TIY-14.5
                self._save_highscore()
                sys.exit() 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                            
            self._check_keydown_events(event)
            self._check_keyup_events(event)

    def _save_highscore(self):
        '''save high score to a txt file'''
        with open('highscore.txt','w') as file:
            file.write(str(self.stats.high_score))
    
    def _retrive_highscore(self):
        '''reetrive highscore from the file'''
        with open('highscore.txt','r') as file:
            line = file.readline()
            return int(line)

    def _check_keydown_events(self, event):
        '''a helper method to check for key presses'''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            if event.key == pygame.K_q:
                self._save_highscore()
                sys.exit()
            if event.key == pygame.K_SPACE:
                self._fire_bullets() 
                self._firing_sound()
            if event.key == pygame.K_p:
                self._start_game()

    def _firing_sound(self):
        '''creates a firing sound effect''' #TIY 14.7
        gun_sound = self.sound('sounds/shooting_sound.wav')
        gun_sound.play()

    def _check_keyup_events(self,event):
        '''a helper method to check for key releases'''
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False    
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _create_fleet(self):
        '''a method to create aliens'''
        Alien = alien.Alien(self)
        alien_width, alien_height = Alien.rect.size
        available_space = self.setting.screen_width - (2 * alien_width)
        number_of_aliens = available_space // (2 * alien_width)
        avaliable_space = (self.setting.screen_height + (3 * alien_height) - 
                           self.ship.image_height)
        number_of_rows = avaliable_space // (4 * alien_height)
        for alien_row in range(number_of_rows):
            for alien_number in range(number_of_aliens):
                self._create_alien(alien_number, alien_row)

    def _create_alien(self, alien_number,alien_row):
        '''a method to create aliens for the fleet'''
        Alien = alien.Alien(self)
        alien_width, alien_height = Alien.rect.size
        Alien.x = alien_width + 2.3 * alien_width * alien_number
        Alien.rect.y = self.ship.image_height + 2 * alien_row * alien_height
        Alien.rect.x = Alien.x
        self.aliens.add(Alien)
        
    def _update_screen(self):
        '''a helper function to display the most recent screen'''
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.ship.blitme()
        self.sb.show_score()
        if not self.stats.game_active:
            self.button.draw()
        pygame.display.flip()
        self.screen.fill(self.setting.bg_color) # fill screen with bg color
    
    def _update_alien(self):
        '''update all aliens position in the fleet'''
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _check_fleet_direction(self):
        '''check each alien direction'''
        for alien in self.aliens.sprites():
            if alien.check_direction():
                self._update_fleet_direction()
                break

    def _update_fleet_direction(self):
        '''update fleets direction in both x and y directions'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1

    def _ship_hit(self):
        '''respond to ship being hit'''
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ship()
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        
if __name__ == '__main__':
    ai = Alien_Invasion()
    ai.run_game()