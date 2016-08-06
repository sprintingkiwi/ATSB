import pygame
import imp


class Battle():
    def __init__(self, area):
        self.data = imp.load_source(area, "areas_data/" + area + ".py")
        self.battleback = self.data.battleback
        self.troops = self.data.troops