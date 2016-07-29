import pygame
import personaggi
import mappe


class Area():
    def warp_point(self):
        x = 0
        y = 0
        game_map = None


class Area1(Area):

    def __init__(self, characters, maps):

        self.music = "music/Arpa.mp3"

        self.game_map = mappe.GameMap(maps, "map1")

        self.enemy1 = personaggi.Ogre(characters, 950, 200)
        self.enemy1.name = "Ogre1"
        self.enemy2 = personaggi.Ogre(characters, 500, 100)
        self.enemy2.name = "Ogre2"

        #self.enemies_list = [self.enemy1, self.enemy2]
        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(self.enemy1, self.enemy2)

