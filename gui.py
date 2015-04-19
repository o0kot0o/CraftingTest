import pygame


class GuiElement(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([0, 0])
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()


class Label(GuiElement):
    def __init__(self, x, y):
        super().__init__()

        self.font = pygame.font.SysFont(None, 30)
        self.label = self.font.render('0', False, (255, 255, 255))

        self.image = pygame.Surface([self.label.get_width(), self.font.get_height()], pygame.SRCALPHA, 32)
        self.image.convert_alpha()
        self.image.set_colorkey((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.label.blit(self.image, (0, 0))

    def setText(self, text):
        self.image = pygame.Surface([self.label.get_width(), self.font.get_height()], pygame.SRCALPHA, 32)
        self.label = self.font.render(str(text), 1, (255, 255, 255))
        self.image.blit(self.label, (0, 0))