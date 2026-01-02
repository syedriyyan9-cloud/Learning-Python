import pygame

class Game_Character:
    '''a class to represent game character'''
    
    def __init__(self, game):
        '''initialize game character'''
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.setting = game.setting
        
        self.image = pygame.image.load('images\gun.bmp')
        self.character = pygame.transform.scale(self.image, (100,100))
        self.rect = self.character.get_rect()
        self.rect.centery = self.screen_rect.centery
        
        self.y = float(self.rect.y)
        self.move_up = False
        self.move_down = False

    def update_motion(self):
        '''update motion for the ship'''
        if self.move_up and self.rect.top > 0:
            self.y -= self.setting.character_speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.character_speed

        self.rect.y = self.y


    def built(self):
        '''built the character onto screen'''
        self.screen.blit(self.character, self.rect)