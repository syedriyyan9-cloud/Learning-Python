import pygame

import sys

import raindrops

import pygame.sprite

from settings import Setting

class Rain:
    '''a class to represent rain'''

    def __init__(self):
        '''initilize attributes'''
        pygame.init()
        self.screen = pygame.display.set_mode((1000,800))
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height
        self.raindrops = pygame.sprite.Group()
        self.setting = Setting()
        self.bg_color = self.setting.bg_color_white
        self._drops_of_rain()

    def check_event(self):
        '''check if user wants to exit'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _drops_of_rain(self):
        '''calculate drops space for drops'''
        drop = raindrops.Drops(self)
        available_space_x = self.screen_width - (2 * drop.rect.width)
        number_of_drops = available_space_x // drop.rect.width
        available_space_y = self.screen_height - (2 * drop.rect.height)
        rows_of_drops = available_space_y // (2 * drop.rect.height)
        for row in range(rows_of_drops):
            for number in range(number_of_drops):
                self._add_drops(number,row)
                
    def _add_drops(self, number, row):
        '''add drops in group'''
        drop = raindrops.Drops(self)
        self.number = number
        self.x = drop.rect.width + 2 * drop.rect.width * number
        drop.rect.x = self.x
        self.y = drop.rect.height * 3 * (row / 3)
        drop.rect.y = self.y
        self.raindrops.add(drop)

    # def _create_only_a_row(self, number):
    #     '''add row of raindrops'''
    #     drop = raindrops.Drops(self)
    #     # drop.y = 0
    #     for number in range(self.number+1):
    #         self.x = drop.rect.width + 2 * drop.rect.width * number
    #         drop.rect.x = self.x
    #         self.raindrops.add(drop)

    def _grid_formation(self):
        '''change sprites into grid'''
        for rain in self.raindrops.sprites():
            rain.rect.y += self.setting.drop_speed

    def _create_new_row(self):
        '''create new rows when previous row reaches bottom'''
        for rain in self.raindrops.sprites():
            if rain.check_edges():
                # self._create_only_a_row(self.number)
                self._drops_of_rain()
                self._delete_raindrops()
                break

    def _delete_raindrops(self):
        '''delete raindrops'''
        for rain in self.raindrops.copy():
            if rain.rect.bottom >= self.screen_rect.bottom:
                self.raindrops.remove(rain)
        # print(self.raindrops)

    def _update_screen(self):
        '''update screen with raindrops'''
        self.raindrops.draw(self.screen)
        pygame.display.flip()
        self.screen.fill(self.bg_color)

    def run(self):
        '''keep the simulation running'''
        while True:
            self.check_event()
            self._create_new_row()
            self._update_screen()
            self._grid_formation()
            # self.raindrops.update()
    
if __name__ == "__main__":
    simulation = Rain()
    simulation.run()