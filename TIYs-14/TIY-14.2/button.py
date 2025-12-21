import pygame.font

class Button:
    '''a class to represent buttons'''

    def __init__(self,game,msg):
        '''initilize variables'''
        pygame.font.init()
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.setting = game.setting
        self.font = pygame.font.SysFont(None, 48)
        self.text_color = self.setting.button_color_black
        self.button_bg_color = self.setting.button_color_red
        self._create_button(msg)

    def _create_button(self,msg):
        '''create button from font'''
        self.image = self.font.render(msg,True,self.text_color,
                                      self.button_bg_color)
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
    
    def draw(self):
        '''create button on the screen'''
        self.screen.blit(self.image, self.rect)
