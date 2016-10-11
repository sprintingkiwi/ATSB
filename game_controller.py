import pygame
import graphics
import scenes
import characters
import monsters
import events
import os
import math
import copy


# decorator
def out_of_battle(func):
    def wrapper(self, *args):
        if not self.inbattle:
            return func(self, *args)
    return wrapper


class Status():

    def __init__(self):
        self.GAMEOVER = False
        self.game_speed = 60

        # Game Display
        self.resolution = [1280, 720]
        self.screen = pygame.display.set_mode(self.resolution)
        #self.screen = pygame.display.set_mode(self.resolution, pygame.FULLSCREEN)

        # Graphic Dictionaries
        self.char_dict = graphics.load_chars()
        self.maps_dict = graphics.load_maps()
        self.battlebacks_dict = graphics.load_battlebacks(self.resolution)
        self.battlers_dict = graphics.load_battlers()

        self.bottom_layer = None
        self.original_bottom_image = None
        self.passability = None
        self.overlay = None
        self.scroll = True
        self.music = None

        # create player
        self.player = characters.Player(self, [self.resolution[0]/2, self.resolution[1]/2])

        # create player's party
        self.party = pygame.sprite.Group()
        self.party.add(monsters.Monster(self, "dyno"),
                       monsters.Monster(self, "spider"))

        # group for NPC
        self.NPC = pygame.sprite.Group()

        # group for every sprite that will be drawn
        self.actors = pygame.sprite.LayeredUpdates()

        self.buttonA = False
        self.buttonB = False

        self.HUD = pygame.sprite.Group()

        self.time = pygame.time.get_ticks()

        self.inbattle = False

        # LOAD ALL SCENES
        # create areas
        self.areas = {}
        # for area in range(len(areas.dictionaries)):
        area_files = []
        for item in os.listdir("scenes_data/"):
            if item.startswith("area") and item.endswith("py"):
                area_files.append(item)
        for area in range(len(area_files)):
            self.areas[area] = scenes.Area(self, area)

        # create battle areas
        self.battles = {}
        # for area in range(len(areas.dictionaries)):
        battle_files = []
        for item in os.listdir("scenes_data/"):
            if item.startswith("battle") and item.endswith("py"):
                battle_files.append(item)
        for battle in range(len(battle_files)):
            self.battles[battle] = scenes.Battle(self, battle)

        # determine if a new scene is to load
        self.change_scene = False

        # LOAD FIRST SCENE
        self.load_scene(self.areas[0])

    # def buttons_effect(self):

    def load_scene(self, scene):
        self.current_scene = scene
        # remove last area's trash
        for item in self.actors:
            self.actors.remove(item)
        for item in self.actors:
            self.actors.remove(item)

        self.current_scene.load(self)

    def update_elements(self):
        self.current_scene.update(self)

        self.actors.update()

        self.HUD.update(self)

        # order sprites in layers
        for sprite in self.actors:
            # print(sprite, ":", sprite.layer)
            self.actors.change_layer(sprite, sprite.layer)

    def draw_elements(self):
        # restore original ground image
        self.bottom_layer.sprites()[0].image = self.original_bottom_image.copy()

        # draw characters on the ground
        self.actors.draw(self.bottom_layer.sprites()[0].image)

        # draw overlay
        self.overlay.draw(self.bottom_layer.sprites()[0].image)

        # draw ground with characters
        self.bottom_layer.draw(self.screen)

        # draw HUD
        self.HUD.draw(self.screen)

    # general UPDATE of the game status
    def update(self):
        events.manage_events(self)

        self.update_elements()

        self.draw_elements()
        # END

