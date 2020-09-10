import pygame
import characters
import monsters
import imp
import HUD


class Area():
    def __init__(self, status, ID):

        self.ID = ID

        # catching the area(ID).py file inside the scenes_data folder
        self.data = imp.load_source("area" + str(ID), "scenes_data/area" + str(ID) + ".py")

        self.music = self.data.music

        # Load MAP layers
        self.game_map = self.data.game_map
        self.ground = status.maps_dict[self.game_map][0]
        self.passability = status.maps_dict[self.game_map][1]
        self.overlay = status.maps_dict[self.game_map][2]

        # LOAD CHARACTERS
        self.actors = pygame.sprite.Group()
        for char in self.data.characters:
            print(char)
            print(char["ID"])
            sprite = characters.NPC(char["ID"], char["name"], status, char["position"])
            if "action" in char.keys():
                sprite.action = char["action"]
            sprite.talk = char["talk"]
            self.actors.add(sprite)

        # LOADING WARPS
        self.warps = self.data.warps

    def load(self, status):
        # call specific area's OnStart function
        self.data.start(status)

        # load and play music
        status.music = pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(-1)

        # load ground group
        status.bottom_layer = self.ground
        status.original_bottom_image = self.ground.sprites()[0].image.copy()

        # load passability group
        status.passability = self.passability

        # load overlay group
        status.overlay = self.overlay

        # load area's characters
        status.NPC = self.actors

        # add sprites to actors group
        for char in self.actors:
            status.actors.add(char, layer=char.layer)

        status.actors.add(status.player, layer=status.player.layer)

    def scroll_map(self, status):
        map_rects = {"ground": status.bottom_layer.sprites()[0].rect,
                     "passability": status.passability.sprites()[0].rect,
                     "overlay": status.overlay.sprites()[0].rect
                     }

        scroll_down = map_rects["ground"].y >= (status.resolution[1] - map_rects["ground"].height)
        scroll_left = map_rects["ground"].x <= 0
        scroll_right = map_rects["ground"].x >= (status.resolution[0] - map_rects["ground"].width)
        scroll_up = map_rects["ground"].y <= 0

        if status.scroll:
            if status.player.walk_down and scroll_down and status.player.y >= status.resolution[1] / 2:
                map_rects["ground"].y -= status.player.speed

            if status.player.walk_left and scroll_left and status.player.x <= map_rects["ground"].width - status.resolution[0] / 2:
                map_rects["ground"].x += status.player.speed

            if status.player.walk_right and scroll_right and status.player.x >= status.resolution[0] / 2:
                map_rects["ground"].x -= status.player.speed

            if status.player.walk_up and scroll_up and status.player.y <= map_rects["ground"].height - status.resolution[1] / 2:
                map_rects["ground"].y += status.player.speed

    def check_collisions(self, status):
        # passability
        if pygame.sprite.collide_mask(status.player.base, status.passability.sprites()[0]):
            if status.player.direction == "down":
                status.player.y -= status.player.speed
            if status.player.direction == "left":
                status.player.x += status.player.speed
            if status.player.direction == "right":
                status.player.x -= status.player.speed
            if status.player.direction == "up":
                status.player.y += status.player.speed

                status.scroll = False

        else:
            status.scroll = True

    def check_warps(self, status):
        for warp in self.warps:
            if not warp["entrance"].colliderect(status.player.base.rect):
                status.change_scene = True

        for warp in self.warps:
            if warp["entrance"].colliderect(status.player.base.rect) and status.change_scene:
                print("warp!")
                print(status.change_scene)
                print(warp["dest_area"])
                status.load_scene(status.areas[warp["dest_area"]])
                status.player.x, status.player.y = warp["dest_rect"]
                status.change_scene = False

    def update(self, status):
        self.check_warps(status)

        # call specific area's OnUpdate function
        self.data.update(status)

        self.scroll_map(status)

        self.check_collisions(status)

        # BUTTONS EFFECTS:
        for char in status.NPC:
            # call the action funcion defined for each NPC actor
            if status.buttonA and status.player.interaction_area.colliderect(char.base.rect):
                char.act(status)
                # status.HUD.add(HUD.TextBox(status, char.talk))


class Battle():
    def __init__(self, status, ID):

        self.ID = ID

        # catching the area(ID).py file inside the scenes_data folder
        self.data = imp.load_source("battle" + str(ID), "scenes_data/battle" + str(ID) + ".py")

        self.music = self.data.music

        # Load Battleback
        self.battleback = status.battlebacks_dict[self.data.battleback][0]
        self.overlay = status.battlebacks_dict[self.data.battleback][1]

        # Load Enemy Battlers
        left_places = [[200, 600], [400, 500], [250, 850], [450, 750]]
        i = 0
        self.actors = pygame.sprite.Group()
        for enemy in self.data.troops:
            print(enemy)
            sprite = monsters.Monster(status, enemy)
            sprite.image = pygame.transform.flip(sprite.image, True, False)
            sprite.x, sprite.y = left_places[i]
            i += 1
            print(sprite.x)
            self.actors.add(sprite)

        # Load party Battlers
        right_places = [[1100, 500], [900, 600], [1150, 750], [950, 850]]
        i = 0
        for sprite in status.party:
            sprite.x, sprite.y = right_places[i]
            i += 1
            self.actors.add(sprite)

        # Start and Update functions
        self.start = self.data.start
        self.update = self.data.update

    def load(self, status):
        print("loading battle...")
        status.inbattle = True

        # call OnStart function of the specific area
        self.start(status)

        # load and play music
        status.music = pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(-1)

        # load ground group
        status.bottom_layer = self.battleback
        status.original_bottom_image = self.battleback.sprites()[0].image.copy()

        # load overlay group
        status.overlay = self.overlay

        # load area's characters
        status.NPC = self.actors

        # add sprites to actors group
        for char in self.actors:
            status.actors.add(char, layer=char.layer)

    def update(self):
        pass


class Warp:
    def __init__(self, rect, dest):
        self.rect = pygame.Rect(rect)
        self.dest_map = dest[0]
        self.dest_coords = dest[1]
