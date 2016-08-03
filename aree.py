import pygame
import personaggi
import mappe


class Area():
    def __init__(self, characters, maps, ID):

        self.ID = ID

        self.music = dictionaries[ID]["music"]

        self.game_map = mappe.GameMap(maps, dictionaries[ID]["game_map"])

        self.enemies = pygame.sprite.Group()
        for enemy in dictionaries[ID]["enemies"]:
            print enemy
            sprite = getattr(personaggi, enemy["kind"])(characters,
                                                        enemy["position"][0],
                                                        enemy["position"][1])
            sprite.talk = enemy["talk"]
            self.enemies.add(sprite)

        self.others = pygame.sprite.Group()
        for other in dictionaries[ID]["others"]:
            self.enemies.add(other)

        self.warps = dictionaries[ID]["warps"]

class Warp:
    def __init__(self, rect, dest):
        self.rect = pygame.Rect(rect)
        self.dest_map = dest[0]
        self.dest_coords = dest[1]


dictionaries = [
                   {  # AREA 0
                        "music": "music/Arpa.mp3",
                        "game_map": "map1",

                        "enemies": [{  # first Ogre
                                     "kind": "Ogre",
                                     "position": (950, 200),
                                     "talk": "Go away!"},

                                    {  # second Ogre
                                     "kind": "Ogre",
                                     "position": (500, 100),
                                     "talk": "You fool!"}],

                        "others": [],

                        "warps": [Warp(rect=[0, 0, 32, 64], dest=[1, [1280, 32]]),
                                  Warp(rect=[1240, 680, 32, 32], dest=[1, [500, 500]])]
                   },

                   {  # AREA 1
                        "music": "music/Arpa.mp3",
                        "game_map": "map2",

                        "enemies": [{  # first Ogre
                                     "kind": "Ogre",
                                     "position": (600, 0),
                                     "talk": "This is another map..."}],

                        "others": [],

                        "warps": [Warp(rect=[1280, 0, 32, 64], dest=[0, [0, 32]])]
                   }
               ]