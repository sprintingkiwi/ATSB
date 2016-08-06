import pygame
import characters
import imp


class Area():
    def __init__(self, char_dict, maps_dict, ID):

        self.ID = ID

        self.data = imp.load_source("area" + str(ID), "areas_data/area" + str(ID) + ".py")

        self.music = self.data.music

        #Load MAP layers
        self.game_map = self.data.game_map
        self.ground = maps_dict[self.game_map][0]
        self.passability = maps_dict[self.game_map][1]
        self.overlay = maps_dict[self.game_map][2]

        self.characters = pygame.sprite.Group()
        for enemy in self.data.characters:
            print enemy
            sprite = getattr(characters, enemy["kind"])(char_dict,
                                                        enemy["position"][0],
                                                        enemy["position"][1])
            sprite.talk = enemy["talk"]
            self.characters.add(sprite)

        self.warps = []
        for item in self.data.warps:
            self.warps.append(Warp(item[0], item[1]))

        self.start = self.data.start
        self.update = self.data.update


class Warp:
    def __init__(self, rect, dest):
        self.rect = pygame.Rect(rect)
        self.dest_map = dest[0]
        self.dest_coords = dest[1]


class Event():
    def __init__(self, status):
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = None
        self.sprite.rect = None
        self.sprite.mask = None
        self.group = pygame.sprite.Group()
        self.group.add(self.sprite)

    def update(self):
        pass


# dictionaries = [
#                    {  # AREA 0
#                         "music": "music/Arpa.mp3",
#                         "game_map": "map1",
#
#                         "enemies": [{  # first Ogre
#                                      "kind": "Ogre",
#                                      "position": (950, 200),
#                                      "talk": "Go away!"},
#
#                                     {  # second Ogre
#                                      "kind": "Ogre",
#                                      "position": (500, 100),
#                                      "talk": "You fool!"}],
#
#                         "others": [],
#
#                         "warps": [Warp(rect=[0, 0, 32, 64], dest=[1, [1280, 32]]),
#                                   Warp(rect=[1240, 680, 32, 32], dest=[1, [500, 500]])]
#                    },
#
#                    {  # AREA 1
#                         "music": "music/Arpa.mp3",
#                         "game_map": "map2",
#
#                         "enemies": [{  # first Ogre
#                                      "kind": "Ogre",
#                                      "position": (600, 0),
#                                      "talk": "This is another map..."}],
#
#                         "others": [],
#
#                         "warps": [Warp(rect=[1280, 0, 32, 64], dest=[0, [0, 32]])]
#                    }
#                ]
