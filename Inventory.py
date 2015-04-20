from gameobject import *

class Inventory(object):
    def __init__(self):
        self.inventory = {'None': 0}

    def addItem(self, item):
        hasItem = False
        for k in self.inventory:
            if type(item) == type(k):
                hasItem = True
                self.inventory[k] += 1
        if not hasItem:
            self.inventory[item] = 1
        item.kill()

    def checkItem(self, item):
        for k in self.inventory:
            if type(item) == type(k):
                return self.inventory[k]
        return 0

    def removeItem(self, item, amount=1):
        hasItem = False
        for k in self.inventory:
            if type(item) == type(k):
                hasItem = True
                self.inventory[k] -= amount

    def printInventory(self):
        print("\n"*50)
        for item in self.inventory:
            if self.inventory[item] > 0:
                print('%s: %d' % (item.name, self.inventory[item]))

    def getCraftables(self, tool):
        if tool == 'Rock':
            for item in self.inventory:
                pass