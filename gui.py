import pygame


class GuiElement(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([0, 0])
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()

        self.Visible = True

    def Show(self):
        self.Visible = True

    def Hide(self):
        self.Visible = False

    def click(self):
        print('CLICKED')


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
        self.image.convert_alpha()
        self.label = self.font.render(str(text), 1, (255, 255, 255))
        self.image.blit(self.label, (0, 0))


class Button(GuiElement):
    def __init__(self, x, y, w, h, image=None):
        super().__init__()

        self.image = pygame.Surface([w, h])
        self.image.set_colorkey((255, 0, 255))
        self.image.fill((130, 130, 130))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.button_image = image

        self.label = Label(0, 0)

        self.update(None)

    def setImage(self, image):
        self.image = image

    def setText(self, text):
        self.label.setText(text)

    def update(self, mousekeys):

        self.image = pygame.Surface([self.rect.w, self.rect.h])
        self.image.fill((130, 130, 130))

        self.image.blit(self.button_image, (self.image.get_rect().centerx - self.button_image.get_rect().centerx, self.image.get_rect().centery - self.button_image.get_rect().centery - 5))
        self.image.blit(self.label.image, (self.image.get_rect().centerx - self.label.image.get_rect().centerx, self.image.get_rect().centery - self.label.image.get_rect().centery + 15))


class Frame(GuiElement):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface([w, h], pygame.SRCALPHA, 32).convert_alpha()
        self.image.fill((40, 40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.clicked = False

        self.elements = []

    def addElement(self, element):
        self.elements.append(element)

    def update(self, mousekeys):
        self.image = pygame.Surface([self.rect.w, self.rect.h], pygame.SRCALPHA, 32).convert_alpha()
        if self.Visible:
            self.image.fill((40, 40, 40))
            for i, element in enumerate(self.elements):
                element.update(mousekeys)
                if element.Visible:
                    mouserect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1, 1)
                    if mouserect.colliderect((self.rect.x + element.rect.x, self.rect.y + element.rect.y, element.rect.width, element.rect.height)):
                        if mousekeys[0] == 1 and self.clicked == False:
                            self.clicked = True
                            element.click()
                        elif mousekeys[0] == 0:
                            self.clicked = False
                        else:
                            pass
                    self.image.blit(element.image, element.rect.topleft)

