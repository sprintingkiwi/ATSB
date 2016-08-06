import pygame


music = "music/Arpa.mp3"

game_map = "map2"

# ID delle aree confinanti
boundaries = {"S": None,
              "W": None,
              "E": 0,
              "N": None}

characters = [{  # first Ogre
             "kind": "Ogre",
             "position": (600, 0),
             "talk": "This is another map..."}]

warps = [([1280, 0, 32, 64], [0, [0, 32]])]

battleback = "battleback1"

troops = []


def start(status):
       pass
       
def update(status):
       collided = pygame.sprite.spritecollide(status.player, status.NPC, False)
       if len(collided) > 0:
              status.load_battle("area1")
       else:
              status.inbattle = False
