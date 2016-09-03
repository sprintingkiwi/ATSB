import pygame


music = "music/Arpa.mp3"

game_map = "map2"

# ID delle aree confinanti
boundaries = {"S": None,
              "W": None,
              "E": 0,
              "N": None}

characters = [{  # first Ogre
             "name": "Ogre3",
             "ID": 3,
             "position": [600, 0],
             "talk": "This is another map..."}]

warps = [{"entrance": pygame.Rect([1280, 0, 32, 64]),
         "dest_area": 0,
         "dest_rect": [0, 32]}]

battleback = "battleback1"

troops = []


def start(status):
       pass
       
def update(status):
       collided = pygame.sprite.spritecollide(status.player, status.NPC, False)
       if len(collided) > 0:
              status.load_scene(status.battles[0])
       else:
              status.inbattle = False
