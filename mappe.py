import pygame


class GameMap():

    def __init__(self, dictionary, mappa):
        # super(GameMap, self).__init__()
        self.components = dictionary[mappa]

    # def disegna(self, screen, area=None):
    #     screen.blit(self.ground, (self.rect.x, self.rect.y), area)
