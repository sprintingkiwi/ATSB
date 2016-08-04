import pygame
import graphics
import areas
import characters
import events
import HUD
import os
import math
import copy


class Status():

    def __init__(self):

        # Game Display
        self.resolution = [1280, 720]
        self.screen = pygame.display.set_mode(self.resolution)

        # Graphic Dictionaries
        self.char_dict = graphics.load_chars()
        self.maps_dict = graphics.load_maps()

        # create areas
        self.areas = {}
        # for area in range(len(areas.dictionaries)):
        area_files = []
        for item in os.listdir("areas_data/"):
            if item.startswith("area") and item.endswith("py"):
                area_files.append(item)
        for area in range(len(area_files)):
            self.areas[area] = areas.Area(self.char_dict, self.maps_dict, area)

        # create player
        self.player = characters.Player(self.char_dict, 500, 0)

        # create player's party
        self.party = pygame.sprite.Group()

        # group for NPC
        self.NPC = pygame.sprite.Group()

        # group for every character that will be drawn
        self.characters = pygame.sprite.LayeredUpdates()

        # determine if a new area is to load
        self.change_area = False
        self.current_area = self.areas[0]

        self.buttonA = False
        self.buttonB = False

        self.HUD = pygame.sprite.Group()

        self.time = pygame.time.get_ticks()

    def buttons_effect(self):
        for char in self.NPC:
            if self.buttonA and self.player.interaction_area.colliderect(char.base.rect):
                self.HUD.add(HUD.TextBox(char.talk))
            elif self.buttonA and not self.player.interaction_area.colliderect(char.base.rect):
                self.HUD.empty()

    def load_area(self):
        # remove last area's trash
        if self.change_area:
            for item in self.characters:
                self.characters.remove(item)
            for item in self.characters:
                self.characters.remove(item)


        # load and play music
        self.music = pygame.mixer.music.load(self.current_area.music)
        pygame.mixer.music.play(-1)

        # load ground group
        self.ground = self.current_area.game_map.ground

        # load passability group
        self.passability = self.current_area.game_map.passability

        # load overlay group
        self.overlay = self.current_area.game_map.overlay

        # load area's characters
        self.NPC = self.current_area.characters

        # add sprites to characters group
        for char in self.current_area.characters:
            self.characters.add(char, layer=char.layer)
        self.characters.add(self.player, layer=self.player.layer)

        self.current_area.start(self)

    def check_warps(self):
        for warp in self.current_area.warps:
            if not warp.rect.colliderect(self.player.base.rect):
                self.change_area = True

        for warp in self.current_area.warps:
            if warp.rect.colliderect(self.player.base.rect) and self.change_area:
                print "warp!"
                print(self.change_area)
                print(warp.dest_map)
                self.current_area = self.areas[warp.dest_map]
                self.load_area()
                self.player.x, self.player.y = warp.dest_coords
                self.change_area = False

    def check_collisions(self):
        # passability
        if pygame.sprite.collide_mask(self.player.base, self.passability.sprites()[0]):
            if self.player.direction == "down":
                self.player.y -= self.player.speed
            if self.player.direction == "left":
                self.player.x += self.player.speed
            if self.player.direction == "right":
                self.player.x -= self.player.speed
            if self.player.direction == "up":
                self.player.y += self.player.speed

    def update_elements(self):

        self.check_collisions()

        self.current_area.update(self)

        self.characters.update()

        # order sprites in layers
        for sprite in self.characters:
            # print(sprite, ":", sprite.layer)
            self.characters.change_layer(sprite, sprite.layer)

        self.check_warps()

    def draw_elements(self):
        #draw ground
        self.ground.draw(self.screen)

        # draw characters
        self.characters.draw(self.screen)

        # draw overlay
        self.overlay.draw(self.screen)

        # draw HUD
        self.HUD.draw(self.screen)

    #general UPDATE of the game status
    def update(self):

        events.manage_events(self.player, self)

        self.buttons_effect()

        self.update_elements()

        self.draw_elements()
        # END

