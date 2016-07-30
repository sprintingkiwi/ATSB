import pygame
import personaggi
import mappe


class Area():
    def __init__(self):
        pass

class Warp:
    def __init__(self, rect, dest):
        self.rect = pygame.Rect(rect)
        self.dest_map = dest[0]
        self.dest_coords = dest[1]


class Area1(Area):

    def __init__(self, characters, maps):

        self.ID = 1

        self.music = "music/Arpa.mp3"

        self.game_map = mappe.GameMap(maps, "map1")

        self.enemy1 = personaggi.Ogre(characters, 950, 200)
        self.enemy1.name = "Ogre1"
        self.enemy2 = personaggi.Ogre(characters, 500, 100)
        self.enemy2.name = "Ogre2"

        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(self.enemy1, self.enemy2)

        self.warps = [
                      Warp(rect=[0, 0, 32, 64], dest=[2, [1280, 32]]),
                      Warp(rect=[1240, 680, 32, 32], dest=[2, [500, 500]])
                     ]


class Area2(Area):

    def __init__(self, characters, maps):

        self.ID = 1

        self.music = "music/Arpa.mp3"

        self.game_map = mappe.GameMap(maps, "map2")

        self.enemy1 = personaggi.Ogre(characters, 600, 0)
        self.enemy1.name = "Ogre1"

        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(self.enemy1)

        self.warps = [
                      Warp(rect=[1280, 0, 32, 64], dest=[1, [0, 32]])
                     ]