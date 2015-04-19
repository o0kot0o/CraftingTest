import pygame
from random import randint

import gameobject
from gui import Label


class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1280, 768))
        pygame.display.set_caption('Crafting')
        self.clock = pygame.time.Clock()

        self.keys_pressed = None

        self.guilayer = pygame.sprite.Group()
        self.label = Label(300, 700)
        self.guilayer.add(self.label)

        self.player = gameobject.Player(0, 0)

        self.gameobjects = pygame.sprite.Group()
        self.gameobjects.add(self.player)
        for i in range(20):
            self.gameobjects.add(gameobject.Rock(randint(0, 1200), randint(0, 700)))
            self.gameobjects.add(gameobject.Stick(randint(0, 1200), randint(0, 700)))
            self.gameobjects.add(gameobject.PlantFiber(randint(0, 1200), randint(0, 700)))
        for i in range(2):
            self.gameobjects.add(gameobject.Axe(randint(0, 1200), randint(0, 700)))

    def input(self):
        self.keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    self.player.printInventory()
                elif event.key == pygame.K_c:
                    item = input("What item? ")
                    if item == 'axe':
                        self.player.craftItem(gameobject.Axe())
                    elif item == 'rope':
                        self.player.craftItem(gameobject.Rope())

        x, y = 0, 0
        if self.keys_pressed[pygame.K_w]: y = -1
        elif self.keys_pressed[pygame.K_s]: y = 1
        else: y = 0
        if self.keys_pressed[pygame.K_a]: x = -1
        elif self.keys_pressed[pygame.K_d]: x = 1
        else: x = 0

        self.player.move(x, y)

    def update(self):
        self.label.setText(self.player.inventory.checkItem(gameobject.Rock()))
        self.player.update(self.gameobjects)

    def render(self):
        self.window.fill((0, 0, 0))

        self.gameobjects.draw(self.window)
        self.guilayer.draw(self.window)

        pygame.display.update()

    def gameloop(self):
        while True:
            self.input()
            self.update()
            self.render()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.gameloop()