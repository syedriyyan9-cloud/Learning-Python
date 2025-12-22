import pygame.font

class Rectangle:
    '''a class to represent Rentangle'''

    def __init__(self,game):
        '''initilize variables'''
        pygame.font.init()
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.setting = game.setting
        self.color = (255,0,0)
        self.rect = pygame.Rect(0,0,
                                self.setting.rectangle_width,
                                self.setting.rectangle_height)
        self.rect.right = self.screen_rect.right
        self.font = pygame.font.SysFont(None, 48)
        self._render_font_as_image()
        self.y = float(self.rect.y)

    def _render_font_as_image(self):
        '''render font as an image'''
        self.image = self.font.render(None, True, self.color,self.color)
        self.image_rect = self.image.get_rect()
        self.image_rect.right = self.rect.right

    def move_rectangle(self):
        '''move the rectangle'''
        if self.rect.top >= 0:
            self.setting.direction *= -1
        if self.rect.bottom <= self.screen_rect.bottom:
            self.setting.direction *= -1

        self.y += self.setting.rectangle_speed * self.setting.direction
        self.image_rect.y = self.y
        self.rect.y = self.y
            
    def draw(self):
        '''draw the rectangle onto the screen'''
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.image,self.image_rect)