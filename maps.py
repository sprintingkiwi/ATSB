import pygame


class GameMap():

    def __init__(self, dictionary, mappa):
        # super(GameMap, self).__init__()
        self.ground = dictionary[mappa][0]
        self.passability = dictionary[mappa][1]
        self.overlay = dictionary[mappa][2]

    # def disegna(self, screen, area=None):
    #     screen.blit(self.ground, (self.rect.x, self.rect.y), area)
