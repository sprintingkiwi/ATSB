import pygame
import graphics
import scenes
import characters
import events
import HUD
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
        self.party.add(characters.Monster(self, "dyno"),
                       characters.Monster(self, "spider"))

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

    def buttons_effect(self):
        for char in self.NPC:
            if self.buttonA and self.player.interaction_area.colliderect(char.base.rect):
                self.HUD.add(HUD.TextBox(self, char.talk))
            elif self.buttonA and not self.player.interaction_area.colliderect(char.base.rect):
                self.HUD.empty()

    def load_scene(self, scene):
        self.current_scene = scene
        # remove last area's trash
        for item in self.actors:
            self.actors.remove(item)
        for item in self.actors:
            self.actors.remove(item)

        # load and play music
        self.music = pygame.mixer.music.load(self.current_scene.music)
        pygame.mixer.music.play(-1)

        # load ground group
        self.bottom_layer = self.current_scene.bottom_layer
        self.original_bottom_image = self.current_scene.bottom_layer.sprites()[0].image.copy()

        # load passability group
        if not self.inbattle:
            self.passability = self.current_scene.passability

        # load overlay group
        self.overlay = self.current_scene.overlay

        # load area's characters
        self.NPC = self.current_scene.actors

        # add sprites to actors group
        for char in self.current_scene.actors:
            self.actors.add(char, layer=char.layer)
        if not self.inbattle:
            self.actors.add(self.player, layer=self.player.layer)

        self.current_scene.start(self)

    @out_of_battle
    def check_warps(self):
        for warp in self.current_scene.warps:
            if not warp.rect.colliderect(self.player.base.rect):
                self.change_scene = True

        for warp in self.current_scene.warps:
            if warp.rect.colliderect(self.player.base.rect) and self.change_scene:
                print "warp!"
                print(self.change_scene)
                print(warp.dest_map)
                self.load_scene(self.areas[warp.dest_map])
                self.player.x, self.player.y = warp.dest_coords
                self.change_scene = False

    def load_battle(self, ID):
        if not self.inbattle:
            print "loading battle..."
            self.inbattle = True
            self.load_scene(self.battles[ID])

    @out_of_battle
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

    @out_of_battle
    def scroll_map(self):
        map_rects = {"ground": self.bottom_layer.sprites()[0].rect,
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

        self.current_scene.update(self)

        self.scroll_map()

        self.actors.update()

        # order sprites in layers
        for sprite in self.actors:
            # print(sprite, ":", sprite.layer)
            self.actors.change_layer(sprite, sprite.layer)

        self.check_warps()

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

        self.buttons_effect()

        self.update_elements()

        self.draw_elements()
        # END

