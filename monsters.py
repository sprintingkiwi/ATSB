import pygame
import strategies
import HUD

class Monster(pygame.sprite.Sprite):
    def __init__(self, status, name):
        pygame.sprite.Sprite.__init__(self)

        self.x = 200
        self.y = 300
        self.image = status.battlers_dict[name]
        self.rect = self.image.get_rect()
        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)
        self.layer = 0
        self.formation = 0

    def parameters_initialization(self):
        # STAT
        self.HP = 100
        self.MP = 50
        self.TP = 0
        self.ATK = 20
        self.DEF = 10
        self.MATK = 5
        self.MDEF = 5
        self.DEX = 10
        self.LUK = 1

        # STATES
        self.dead = False
        self.burnt = 0
        self.poisoned = 0
        self.frozen = 0
        self.paralyzed = 0

    def update(self):
        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)
