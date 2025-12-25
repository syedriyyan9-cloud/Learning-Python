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
        self.prep_highscore()
        self.prep_level()

    def prep_score(self):
        '''turn the score into an image'''
        rounded_score = round(self.stats.score,-1)
        score_str = f"Score: {rounded_score:,}"
        self.score_image = self.font.render(score_str,False,
                                      self.text_color,self.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        '''display the score on the screen'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)

    def prep_highscore(self):
        '''turn high score into an image'''    
        rounded_high_score = round(self.stats.high_score,-1)
        high_score_str = f"High Score: {rounded_high_score:,}"
        self.high_score_image = self.font.render(high_score_str,False,
                                                 self.text_color,self.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        '''check for new high score'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_highscore()

    def prep_level(self):
        '''turn player level into an image'''
        lvl_str = "Player Level: " + str(self.stats.level)
        self.level_image = self.font.render(lvl_str,False,
                                        self.text_color, self.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.bottom = self.score_rect.bottom + 50