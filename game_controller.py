import pygame
import graphics
import areas
import characters
import events
import HUD
import os
import battle
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
        self.battlebacks_dict = graphics.load_battlebacks(self.resolution)
        self.battlers_dict = graphics.load_battlers()

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
        self.player = characters.Player(self.char_dict,
                                        self.resolution[0]/2,
                                        self.resolution[1]/2)

        # create player's party
        self.party = pygame.sprite.Group()
        self.party.add(characters.Monster(self.battlers_dict, "dyno"),
                       characters.Monster(self.battlers_dict, "spider"))

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

        self.inbattle = False

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
        self.ground = self.current_area.ground
        self.original_ground_image = self.current_area.ground.sprites()[0].image.copy()

        # load passability group
        self.passability = self.current_area.passability

        # load overlay group
        self.overlay = self.current_area.overlay

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

    def load_battle(self, area):
        if not self.inbattle:
            print "loading battle..."
            self.inbattle = True
            self.battle = battle.Battle(area)

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

            self.scroll = False

        else:
            self.scroll = True

    def scroll_map(self):
        map_rects = {"ground": self.ground.sprites()[0].rect,
                     "passability": self.passability.sprites()[0].rect,
                     "overlay": self.overlay.sprites()[0].rect
        }

        scroll_down = map_rects["ground"].y >= (self.resolution[1] - map_rects["ground"].height)
        scroll_left = map_rects["ground"].x <= 0
        scroll_right = map_rects["ground"].x >= (self.resolution[0] - map_rects["ground"].width)
        scroll_up = map_rects["ground"].y <= 0

        if self.scroll:
            if self.player.walk_down and scroll_down and self.player.y >= self.resolution[1]/2:
                map_rects["ground"].y -= self.player.speed

            if self.player.walk_left and scroll_left and self.player.x <= map_rects["ground"].width - self.resolution[0]/2:
                map_rects["ground"].x += self.player.speed

            if self.player.walk_right and scroll_right and self.player.x >= self.resolution[0]/2:
                map_rects["ground"].x -= self.player.speed

            if self.player.walk_up and scroll_up and self.player.y <= map_rects["ground"].height - self.resolution[1]/2:
                map_rects["ground"].y += self.player.speed

    def update_elements(self):

        self.check_collisions()

        self.current_area.update(self)

        self.scroll_map()

        self.characters.update()

        # order sprites in layers
        for sprite in self.characters:
            # print(sprite, ":", sprite.layer)
            self.characters.change_layer(sprite, sprite.layer)

        self.check_warps()

    def draw_elements(self):
        #restore original ground image
        self.ground.sprites()[0].image = self.original_ground_image.copy()

        # draw characters on the ground
        self.characters.draw(self.ground.sprites()[0].image)

        # draw overlay
        self.overlay.draw(self.ground.sprites()[0].image)

        # draw ground with characters
        self.ground.draw(self.screen)

        # draw HUD
        self.HUD.draw(self.screen)

    #general UPDATE of the game status
    def update(self):

        events.manage_events(self.player, self)

        self.buttons_effect()

        self.update_elements()

        self.draw_elements()
        # END

