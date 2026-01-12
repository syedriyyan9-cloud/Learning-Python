# Date: 4 december 2025
# Name: Riyyan

# 12-5. Keys: Make a Pygame file that creates an empty screen. In the event
# loop, print the event.key attribute whenever a pygame.KEYDOWN event is detected.
# Run the program and press various keys to see how Pygame responds.

import pygame

import sys

class Empty_Screen:
    '''class for creating empty screen'''

    def __init__(self):
        '''constructor'''
        self.screen = pygame.display.set_mode((800,800))

    def run(self):
        '''a method to run the game'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    print(f"{event.key}")

if __name__ == "__main__":
    empty_screen = Empty_Screen()
    empty_screen.run()