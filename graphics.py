import pygame
import os


# load graphics
def load_maps():
    dictionary = {}
    maps = os.listdir("images/maps")
    for game_map in maps:
        name = str(game_map)

        ground = pygame.sprite.Group()
        img = pygame.image.load("images/maps/" + game_map + "/ground.png").convert()
        sprite = pygame.sprite.Sprite()
        sprite.image = img
        sprite.rect = img.get_rect()
        ground.add(sprite)

        passability = pygame.sprite.Group()
        img = pygame.image.load("images/maps/" + game_map + "/passability.png").convert_alpha()
        sprite = pygame.sprite.Sprite()
        sprite.image = img
        sprite.rect = img.get_rect()
        sprite.mask = pygame.mask.from_surface(img)
        passability.add(sprite)

        overlay = pygame.sprite.Group()
        img = pygame.image.load("images/maps/" + game_map + "/overlay.png").convert_alpha()
        sprite = pygame.sprite.Sprite()
        sprite.image = img
        sprite.rect = img.get_rect()
        overlay.add(sprite)

        dictionary[name] = [ground, passability, overlay]
    return dictionary


def load_chars():
    dictionary = {}
    chars = os.listdir("images/characters")
    for char in chars:
        if char.endswith(".png"):
            name = char[0:7]
            path = "images/characters/" + char
            image = pygame.image.load(path).convert_alpha()
            # scale original images
            rect = image.get_rect()
            w = rect.width
            h = rect.height
            image = pygame.transform.scale(image, [w * 2, h * 2])
            # add images to dictionary
            dictionary[name] = image
    return dictionary


def load_battlebacks(resolution):
    dictionary = {}
    battlebacks = os.listdir("images/battlebacks")
    for bb in battlebacks:
        name = str(bb)

        background = pygame.sprite.Group()
        img = pygame.image.load("images/battlebacks/" + bb + "/background.png").convert()
        img = pygame.transform.scale(img, resolution)
        sprite = pygame.sprite.Sprite()
        sprite.image = img
        sprite.rect = img.get_rect()
        background.add(sprite)
        
        overlay = pygame.sprite.Group()
        img = pygame.image.load("images/battlebacks/" + bb + "/overlay.png").convert_alpha()
        img = pygame.transform.scale(img, resolution)
        sprite = pygame.sprite.Sprite()
        sprite.image = img
        sprite.rect = img.get_rect()
        overlay.add(sprite)

        dictionary[name] = [background, overlay]
    return dictionary


def load_battlers():
    dictionary = {}
    battlers = os.listdir("images/battlers")
    for battler in battlers:
        if battler.endswith(".png"):
            name = str(battler.split(".")[0])
            path = "images/battlers/" + battler
            img = pygame.image.load(path).convert_alpha()
            # scale original images
            rect = img.get_rect()
            w = rect.width
            h = rect.height
            img = pygame.transform.scale(img, [w * 2, h * 2])
            # add images to dictionary
            dictionary[name] = img
    return dictionary
