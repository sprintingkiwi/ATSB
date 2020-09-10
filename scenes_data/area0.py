import pygame


music = "music/Call to Adventure.mp3"


game_map = "map1"


# ID delle aree confinanti
boundaries = {"S": None,
              "W": 1,
              "E": None,
              "N": None}
              
              
def ogre1act():
       print("ciao")


characters = [{  # first Ogre
             "name": "Ogre1",
             "ID": 3,
             "position": [950, 200],
             "talk": "Go away!",
             "action": ogre1act},

            {  # second Ogre
             "name": "Ogre2",
             "ID": 3,
             "position": (600, 100),
             "talk": "You fool!"}]


warps = [{"entrance": pygame.Rect([0, 0, 32, 64]),
         "dest_area": 1,
         "dest_rect": [1275, 128]},
         {"entrance": pygame.Rect([1240, 680, 32, 32]),
         "dest_area": 1,
         "dest_rect": [500, 500]}]
         
         
battleback = "battleback1"


troops = []


def start(status):
       print("OnStart area function working!")
       
       
def update(status):
       pass
