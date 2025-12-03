import pygame

class Settings:
    '''a class to represent settings for the game'''
    
    def __init__(self):
        '''initialze attributes'''
        self.bg_white = (255,255,255)
        self.bg_black = (0,0,0)
        self.bg_blue = (0,0,255)
        self.bg_yellow = (255,225,53)

        self.ship_speed = 3