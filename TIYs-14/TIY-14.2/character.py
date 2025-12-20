import pygame

class Character:
    '''a class to represent the character'''

    def __init__(self, game):
        '''create character attributes'''
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.setting = game.setting
        self.image = pygame.image.load('image\\ranger.bmp')
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

    def move_player(self):
        '''move character position'''
        if self.move_up and self.rect.top >= self.screen_rect.top:
            self.y -= self.setting.character_speed
        if self.move_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.setting.character_speed
        if self.move_left and self.rect.left >= self.screen_rect.left:
            self.x -= self.setting.character_speed
        if self.move_right and self.rect.right <= self.screen_rect.right:
            self.x += self.setting.character_speed

        self.rect.x = self.x
        self.rect.y = self.y
    
    def draw(self):
        '''draw the player onto the screen'''
        self.screen.blit(self.image, self.rect)