import pygame


music = "music/Arpa.mp3"

game_map = "map1"

# ID delle aree confinanti
boundaries = {"S": None,
              "W": 1,
              "E": None,
              "N": None}

characters = [{  # first Ogre
             "kind": "Ogre",
             "position": (950, 200),
             "talk": "Go away!"},

            {  # second Ogre
             "kind": "Ogre",
             "position": (600, 100),
             "talk": "You fool!"}]

warps = [([0, 0, 32, 64], [1, [1280, 32]]),
         ([1240, 680, 32, 32],[1, [500, 500]])]
         
battleback = "battleback1"

troops = []


def start(status):
       pass
       
def update(status):
       pass
