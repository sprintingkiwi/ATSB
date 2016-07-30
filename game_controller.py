import pygame
import aree
import personaggi
import eventi
import math
import copy


class Status():

    def __init__(self, characters, maps, screen):
        # create areas
        self.areas = {}
        for ID in range(1, 1000):
            try:
                self.areas[ID] = getattr(aree, "Area" + str(ID))(characters, maps)
            except:
                print("areas loaded")
                break

        # create player
        self.player = personaggi.Player(characters, 500, 0)

        # group for every character
        self.all_characters = pygame.sprite.LayeredUpdates()

        # determine if a new area is to load
        self.change_area = False
        self.current_area = self.areas[1]

        self.screen = screen

    def load_area(self):
        # remove last area's trash
        if self.change_area:
            for item in self.all_characters:
                self.all_characters.remove(item)
            for item in self.enemy_group:
                self.enemy_group.remove(item)


        # music
        self.music = pygame.mixer.music.load(self.current_area.music)
        pygame.mixer.music.play(-1)

        #ground
        self.ground = self.current_area.game_map.components[0]

        #overlay
        self.overlay = self.current_area.game_map.components[1]

        self.enemy_group = self.current_area.enemy_group

        # add sprites to all_characters group
        for en in self.enemy_group:
            self.all_characters.add(en, layer=en.layer)
        self.all_characters.add(self.player, layer=self.player.layer)

    def check_warps(self):
        for warp in self.current_area.warps:
            if not warp.rect.colliderect(self.player.base):
                self.change_area = True

        for warp in self.current_area.warps:
            if warp.rect.colliderect(self.player.base) and self.change_area:
                print "warp!"
                print(self.areas)
                print(warp.dest_map)
                self.current_area = self.areas[warp.dest_map]
                self.load_area()
                self.player.x, self.player.y = warp.dest_coords
                self.change_area = False

    def calcola_collisioni(self):
        pass

    def update_elements(self):
        self.all_characters.update()

        # order sprites in layers
        for sprite in self.all_characters:
            # print(sprite, ":", sprite.layer)
            self.all_characters.change_layer(sprite, sprite.layer)

        self.calcola_collisioni()

        self.check_warps()

    def draw_elements(self):
        #draw ground
        self.ground.draw(self.screen)

        # draw characters
        self.all_characters.draw(self.screen)

        # draw overlay
        self.overlay.draw(self.screen)

    #general UPDATE of the game status
    def update(self):

        eventi.manage_events(self.player)

        self.update_elements()

        self.draw_elements()

