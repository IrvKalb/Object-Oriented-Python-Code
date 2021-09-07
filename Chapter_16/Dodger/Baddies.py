# Baddie and BaddieMgr classes

import pygame
import pygwidgets
import random
from Constants import *

# Baddie class
class Baddie():
    MIN_SIZE = 10
    MAX_SIZE = 40
    MIN_SPEED = 1
    MAX_SPEED = 8
    # Load the image only once
    BADDIE_IMAGE = pygame.image.load('images/baddie.png')

    def __init__(self, window):
        self.window = window
        # Create the image object
        size = random.randrange(Baddie.MIN_SIZE, Baddie.MAX_SIZE + 1)
        self.x = random.randrange(0, WINDOW_WIDTH - size)
        self.y = 0 - size # start above the window
        self.image = pygwidgets.Image(self.window, (self.x, self.y),
                                      Baddie.BADDIE_IMAGE)

        # Scale it
        percent = (size * 100) / Baddie.MAX_SIZE
        self.image.scale(percent, False)
        self.speed = random.randrange(Baddie.MIN_SPEED,
                                                      Baddie.MAX_SPEED + 1)

    def update(self):  # move the Baddie down
        self.y = self.y + self.speed
        self.image.setLoc((self.x, self.y))
        if self.y > GAME_HEIGHT:
            return True  # needs to be deleted
        else:
            return False  # stays in the window

    def draw(self):
        self.image.draw()

    def collide(self, playerRect):
        collidedWithPlayer = self.image.overlaps(playerRect)
        return collidedWithPlayer

# BaddieMgr class
class BaddieMgr():
    ADD_NEW_BADDIE_RATE = 8  # how often to add a new Baddie

    def __init__(self, window):
        self.window = window
        self.reset()

    def reset(self):  # called when starting a new game
        self.baddiesList = []
        self.nFramesTilNextBaddie = BaddieMgr.ADD_NEW_BADDIE_RATE

    def update(self):
        # Tell each Baddie to update itself
        # Count how many Baddies have fallen off the bottom.
        nBaddiesRemoved = 0
        baddiesListCopy = self.baddiesList.copy()
        for oBaddie in baddiesListCopy:
            deleteMe = oBaddie.update()
            if deleteMe:
                self.baddiesList.remove(oBaddie)
                nBaddiesRemoved = nBaddiesRemoved + 1

        # Check if it's time to add a new Baddie
        self.nFramesTilNextBaddie = self.nFramesTilNextBaddie - 1
        if self.nFramesTilNextBaddie == 0:
            oBaddie = Baddie(self.window)
            self.baddiesList.append(oBaddie)
            self.nFramesTilNextBaddie = BaddieMgr.ADD_NEW_BADDIE_RATE

        # Return that count of Baddies that were removed
        return nBaddiesRemoved

    def draw(self):
        for oBaddie in self.baddiesList:
            oBaddie.draw()

    def hasPlayerHitBaddie(self, playerRect):
        for oBaddie in self.baddiesList:
            if oBaddie.collide(playerRect):
                return True
        return False
