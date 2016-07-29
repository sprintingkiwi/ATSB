import pygame
import os


#load graphics
def load_maps():
    dictionary = {}
    maps = os.listdir("images/maps")
    for item in maps:
        name = str(item)

        ground_path = "images/maps/" + item + "/ground/"
        ground_maps = os.listdir(ground_path)
        ground = pygame.sprite.Group()
        for img_path in ground_maps:
            img = pygame.image.load(ground_path + img_path).convert()
            sprite = pygame.sprite.Sprite()
            sprite.image = img
            sprite.rect = img.get_rect()
            ground.add(sprite)

        overlay_path = "images/maps/" + item + "/overlay/"
        overlay_maps = os.listdir(overlay_path)
        overlay = pygame.sprite.Group()
        for img_path in overlay_maps:
            img = pygame.image.load(overlay_path + img_path).convert_alpha()
            sprite = pygame.sprite.Sprite()
            sprite.image = img
            sprite.rect = img.get_rect()
            overlay.add(sprite)

        dictionary[name] = [ground, overlay]
    return dictionary

def load_chars():
    dictionary = {}
    chars = os.listdir("images/characters")
    for item in chars:
        name = item[0:7]
        print(name)
        path = "images/characters/" + item
        image = pygame.image.load(path)
        image = image.convert_alpha()
        #scale original images
        rect = image.get_rect()
        w = rect.width
        h = rect.height
        image = pygame.transform.scale(image, [w * 2, h * 2])
        #add images to dictionary
        dictionary[name] = image
    return dictionary
