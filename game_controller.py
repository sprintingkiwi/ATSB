import pygame
import aree
import personaggi
import eventi
import HUD
import math
import copy


class Status():

    def __init__(self, characters, maps, screen):
        # create areas
        self.areas = {}
        for area in range(len(aree.dictionaries)):
            self.areas[area] = aree.Area(characters, maps, area)

        # create player
        self.player = personaggi.Player(characters, 500, 0)

        # create player's party
        self.party = pygame.sprite.Group()

        # group for every character
        self.all_characters = pygame.sprite.LayeredUpdates()

        # determine if a new area is to load
        self.change_area = False
        self.current_area = self.areas[0]

        self.screen = screen

        self.buttonA = False
        self.buttonB = False

        self.HUD = pygame.sprite.Group()

        self.time = pygame.time.get_ticks()

    def buttons_effect(self):
        for en in self.enemies:
            if self.buttonA and self.player.interaction_area.colliderect(en.base.rect):
                self.HUD.add(HUD.TextBox(en.talk))
            elif self.buttonA and not self.player.interaction_area.colliderect(en.base.rect):
                self.HUD.empty()

    def load_area(self):
        # remove last area's trash
        if self.change_area:
            for item in self.all_characters:
                self.all_characters.remove(item)
            for item in self.enemies:
                self.enemies.remove(item)


        # load and play music
        self.music = pygame.mixer.music.load(self.current_area.music)
        pygame.mixer.music.play(-1)

        # load ground group
        self.ground = self.current_area.game_map.ground

        # load passability group
        self.passability = self.current_area.game_map.passability

        # load overlay group
        self.overlay = self.current_area.game_map.overlay

        # load enemies group
        self.enemies = self.current_area.enemies

        #load others group
        self.others = self.current_area.others

        # add sprites to all_characters group
        for en in self.enemies:
            self.all_characters.add(en, layer=en.layer)
        self.all_characters.add(self.player, layer=self.player.layer)

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

        self.all_characters.update()

        # order sprites in layers
        for sprite in self.all_characters:
            # print(sprite, ":", sprite.layer)
            self.all_characters.change_layer(sprite, sprite.layer)

        self.check_warps()

    def draw_elements(self):
        #draw ground
        self.ground.draw(self.screen)

        # draw characters
        self.all_characters.draw(self.screen)

        # draw overlay
        self.overlay.draw(self.screen)

        # draw HUD
        self.HUD.draw(self.screen)

    #general UPDATE of the game status
    def update(self):

        eventi.manage_events(self.player, self)

        self.buttons_effect()

        self.update_elements()

        self.draw_elements()
        # END

