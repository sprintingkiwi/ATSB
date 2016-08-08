import pygame
import characters
import imp


class Area():
    def __init__(self, status, ID):

        self.ID = ID

        # catching the area(ID).py file inside the scenes_data folder
        self.data = imp.load_source("area" + str(ID), "scenes_data/area" + str(ID) + ".py")

        self.music = self.data.music

        # Load MAP layers
        self.game_map = self.data.game_map
        self.bottom_layer = status.maps_dict[self.game_map][0]
        self.passability = status.maps_dict[self.game_map][1]
        self.overlay = status.maps_dict[self.game_map][2]

        # LOAD CHARACTERS
        self.actors = pygame.sprite.Group()
        for char in self.data.characters:
            print char
            sprite = getattr(characters, char["kind"])(status, char["position"])
            sprite.talk = char["talk"]
            self.actors.add(sprite)


        # LOADING WARPS
        self.warps = []
        for item in self.data.warps:
            self.warps.append(Warp(item[0], item[1]))

        # Start and Update functions
        self.start = self.data.start
        self.update = self.data.update


class Battle():
    def __init__(self, status, ID):

        self.ID = ID

        # catching the area(ID).py file inside the scenes_data folder
        self.data = imp.load_source("battle" + str(ID), "scenes_data/battle" + str(ID) + ".py")

        self.music = self.data.music

        # Load Battleback
        self.battleback = self.data.battleback
        self.bottom_layer = status.battlebacks_dict[self.battleback][0]
        self.overlay = status.battlebacks_dict[self.battleback][1]

        # Load Enemy Battlers
        left_places = [[200, 600], [400, 500], [250, 850], [450, 750]]
        i = 0
        self.actors = pygame.sprite.Group()
        for enemy in self.data.troops:
            print enemy
            sprite = characters.Monster(status, enemy)
            sprite.image = pygame.transform.flip(sprite.image, True, False)
            sprite.x, sprite.y = left_places[i]
            i += 1
            print sprite.x
            self.actors.add(sprite)
        right_places = [[1100, 500], [900, 600], [1150, 750], [950, 850]]
        i = 0
        for sprite in status.party:
            sprite.x, sprite.y = right_places[i]
            i += 1
            self.actors.add(sprite)

        # Start and Update functions
        self.start = self.data.start
        self.update = self.data.update


class Warp:
    def __init__(self, rect, dest):
        self.rect = pygame.Rect(rect)
        self.dest_map = dest[0]
        self.dest_coords = dest[1]
