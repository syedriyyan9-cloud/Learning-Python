import pygame.font

class Button:
    '''a class to represent buttons'''

    def __init__(self, game, msg):
        '''initialize the attributes'''
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.width, self.height = 500, 250
        self.text_color = (255,255,255)
        self.bg_color = (0,255,0)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        '''render msg as an image'''
        self.msg_image = self.font.render(msg, True, 
                                          self.text_color,self.bg_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect = self.rect.center

    def draw(self):
        '''draw the button onto the screen'''
        self.screen.fill(self.text_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_rect)