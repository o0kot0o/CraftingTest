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

        for k in item.craftList:
            if not self.inventory.checkItem(k) > item.craftList[k]:
                canCraft = False
                print('Missing %d %s' % (item.craftList[k] - self.inventory.checkItem(k), k.name))

        if canCraft:
            for k in item.craftList:
                self.inventory.removeItem(k, item.craftList[k])
                print('Removed %d %ss' % (item.craftList[k], k.name))
            self.inventory.addItem(item)
            print('Created %s' % item.name)

    def canCraft(self, item):
        canCraft = True
        for k in item.craftList:
            if not self.inventory.checkItem(k) > item.craftList[k]:
                canCraft = False
        return canCraft


class Rock(GameObject):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.name = 'Rock'
        self.image = pygame.image.load('gfx/rock.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Stick(GameObject):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.name = 'Stick'
        self.image = pygame.image.load('gfx/stick.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class PlantFiber(GameObject):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.name = 'Plant Fiber'
        self.image = pygame.image.load('gfx/plantfiber.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Rope(GameObject):
    craftList = {
        PlantFiber(): 2
    }
    def __init__(self, x=0, y=0):
        super().__init__()
        self.name = 'Rope'
        self.image = pygame.image.load('gfx/rope.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Axe(GameObject):
    craftList = {
        Rope(): 1,
        Rock(): 1,
        Stick(): 1
    }
    def __init__(self, x=0, y=0):
        super().__init__()
        self.name = 'Axe'
        self.image = pygame.image.load('gfx/axe.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y