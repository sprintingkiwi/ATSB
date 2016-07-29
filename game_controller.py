import pygame
import aree
import personaggi
import eventi
import math
import copy


class Status():

    def __init__(self, characters, maps, screen):
        #create player
        self.player = personaggi.Player(characters, 500, 0)

        self.all_characters = pygame.sprite.LayeredUpdates()

        self.change_area = True
        self.area_to_load = aree.Area1(characters, maps)

        self.screen = screen

    def load_area(self):
        #music
        self.music = pygame.mixer.music.load(self.area_to_load.music)
        pygame.mixer.music.play(-1)

        #ground
        self.ground = self.area_to_load.game_map.components[0]

        #overlay
        self.overlay = self.area_to_load.game_map.components[1]

        #self.ground_group.draw()
        #self.ground.disegna(self.screen)

        #characters
        #self.enemies_list = current_area.enemies_list
        #self.tutti = current_area.enemies_list
        #self.tutti.append(self.player)

        self.enemy_group = self.area_to_load.enemy_group

        for en in self.enemy_group:
            self.all_characters.add(en)
        self.all_characters.add(self.player)

        #for item in self.all_characters:
            #self.all_characters.remove(item)
        #for item in self.tutti:
            #self.all_characters.add(item)

        #se passo i rect all'update, al primo ciclo devo comunque
        #fare l'update di tutto lo schermo
        #pygame.display.update()

    def sort_characters(self):
        pass
        #ordino la lista di tutti i personaggi in base alla deep
        #self.tutti.sort(key=lambda sprite: sprite.deep)

    #calcolo delle collisioni basato sulle distanze reciproche tra i personaggi
    def calcola_collisioni(self):
        pass
        #for item in self.tutti:
            #altri = []
            #for sprite in self.tutti:
                #altri.append(sprite)
            #altri.remove(item)

            #item.lista_distanze = {}
            #for i in altri:
                #item.lista_distanze[i.name] = math.sqrt((i.base.centerx -
                                                         #item.base.centerx) ** 2 +
                                                        #(i.base.centery -
                                                         #item.base.centery) ** 2)

                #if item.lista_distanze[i.name] < 50:
                    ##item.collided = True
                    #print(item.name, "sta toccando", i.name)
                    #print(item.lista_distanze[i.name])

    def update_elements(self):
        #for item in self.tutti:
            #if item.dead:
                #self.tutti.remove(item)
                #self.all_characters.remove(item)

        self.all_characters.update()

        ##lista dei rettangoli dei personaggi
        #self.rettangoli = []
        #for item in self.tutti:
            #self.rettangoli.append(item.rect)
        ##lista delle basi dei personaggi
        #self.basi = []
        #for item in self.tutti:
            #self.basi.append(item.base)

    def draw_elements(self):
        #draw ground
        self.ground.draw(self.screen)

        #self.ground.disegna(self.screen)

        self.all_characters.draw(self.screen)
        #for item in self.tutti:
            #item.disegna(self.screen)
        #self.all_characters.draw(self.screen)

        # draw overlay
        self.overlay.draw(self.screen)

    #general UPDATE of the game status
    def update(self):
        if self.change_area is True:
            self.load_area()
            self.change_area = False

        self.sort_characters()

        eventi.manage_events(self.player)

        self.calcola_collisioni()

        self.update_elements()

        self.draw_elements()
