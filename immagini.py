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
    for game_map in chars:
        name = game_map[0:7]
        print(name)
        path = "images/characters/" + game_map
        image = pygame.image.load(path)
        image = image.convert_alpha()
        # scale original images
        rect = image.get_rect()
        w = rect.width
        h = rect.height
        image = pygame.transform.scale(image, [w * 2, h * 2])
        # add images to dictionary
        dictionary[name] = image
    return dictionary
