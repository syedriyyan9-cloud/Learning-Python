import pygame.font

class ScoreBoard:
    '''a class to represent score board '''

    def __init__(self, game):
        '''initialize variables'''
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.setting = game.setting
        self.stats = game.stats
        
        self.text_color = (30,30,30)
        self.bg_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()

    def prep_score(self):
        '''turn the score into an image'''
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,False,
                                      self.text_color,self.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        '''display the score on the screen'''
        self.screen.blit(self.score_image, self.score_rect)

    
