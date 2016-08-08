import pygame


class TextBox(pygame.sprite.Sprite):
    def __init__(self,
                 status,
                 text,
                 font_name="Liberation Serif",
                 font_size=64,
                 bold=False,
                 italic=False,
                 color=(0, 0, 0)):
        super(TextBox, self).__init__()
        self.image = pygame.Surface([1000, 200])
        self.rect = self.image.get_rect()
        self.rect.x = 140
        self.rect.y = 500

        # draw box background
        pygame.draw.rect(self.image, [255, 255, 255], [0, 0, 1000, 200])
        pygame.draw.rect(self.image, [0, 0, 0], [0, 0, 1000, 200], 20)
        font = pygame.font.SysFont(font_name, font_size, bold, italic)

        # create and distribute words
        x = 20
        y = 10
        words = text.split(" ")
        for word in words:
            word = word + " "
            img = font.render(word, True, color)
            self.image.blit(img, [x, y])
            wrect = img.get_rect()
            wrect.x, wrect.y = x, y
            limit = pygame.Rect([1140, 500, 100, 200])
            if wrect.colliderect(limit):
                y += 20
                x = 0
            else:
                x += wrect.width
