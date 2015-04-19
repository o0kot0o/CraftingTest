import pygame

from Inventory import *


class GameObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([0, 0])
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()


class Player(GameObject):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([32, 32])
        self.image.fill((255, 128, 128))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.movex = 0
        self.movey = 0

        self.inventory = Inventory()

    def move(self, x, y):
        self.movex = x * 5
        self.movey = y * 5

    def update(self, gameobjects):
        self.rect.x += self.movex
        self.rect.y += self.movey

        collide, collider = self.checkCollision(gameobjects)
        if collide:
            self.inventory.addItem(collider)

    def checkCollision(self, gameobjects):
        for gameobject in gameobjects:
            if gameobject is not self:
                if self.rect.colliderect(gameobject.rect):
                    return True, gameobject
        return False, None

    def printInventory(self):
        self.inventory.printInventory()

    def craftItem(self, item):
        canCraft = True

        print(item.name)
        print('--------------------')
        for k in item.craftList:
            print('%s: %d' % (k.name, item.craftList[k]))
        print('--------------------')

        for k in item.craftList:
            if not self.inventory.checkItem(k) > 0:
                canCraft = False

        if canCraft:
            for k in item.craftList:
                self.inventory.removeItem(k)
            self.inventory.addItem(item)

        # for k in self.inventory.inventory:
        #     if type(item) == type(k):
        #         if not self.inventory.inventory[k] > k.craftList[k]:
        #             canCraft = False
        # if canCraft:
        #     self.inventory.addItem(item)



class Rock(GameObject):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.name = 'Rock'
        self.image = pygame.Surface([8, 8])
        self.image.fill((75, 75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Stick(GameObject):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.name = 'Stick'
        self.image = pygame.Surface([20, 4])
        self.image.fill((130, 82, 1))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class PlantFiber(GameObject):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.name = 'Plant Fiber'
        self.image = pygame.Surface([8, 8])
        self.image.fill((24, 130, 24))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Axe(GameObject):
    craftList = {
        PlantFiber(): 1,
        Rock(): 1,
        Stick(): 1
    }
    def __init__(self, x=0, y=0):
        super().__init__()
        self.name = 'Axe'
        self.image = pygame.Surface([15, 15])
        self.image.fill((130, 82, 1), (0, 0, 5, 15))
        self.image.fill((75, 75, 75), (5, 0, 5, 7))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
