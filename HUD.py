import pygame


class TextBox(pygame.sprite.Sprite):
    def __init__(self,
                 status,
                 text,
                 font_name="Liberation Serif",
                 font_size=64,
                 bold=False,
                 italic=False,
                 color=(0, 0, 0),
                 duration=2000,
                 removable=True):
        super(TextBox, self).__init__()
        self.image = pygame.Surface([1000, 200])
        self.rect = self.image.get_rect()
        self.rect.x = 140
        self.rect.y = 500
        self.duration = duration
        self.start_time = pygame.time.get_ticks()

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

    def update(self, status):
        if pygame.time.get_ticks() - self.start_time >= self.duration:
            status.HUD.remove(self)
        # for char in status.NPC:
        #     if status.buttonA and not status.player.interaction_area.colliderect(char.base.rect):
        #         status.HUD.remove(self)
