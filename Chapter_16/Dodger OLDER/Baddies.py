### BADDIE
import pygame
import pygwidgets
import random
from Constants import *


class Baddie():
    MIN_SIZE = 10
    MAX_SIZE = 40
    MIN_SPEED = 1
    MAX_SPEED = 9  # max plus one
    BADDIE_IMAGE = pygame.image.load('images/baddie.png')   # Load the image only once

    def __init__(self, window):
        self.window = window

        # Create the image object
        size = random.randrange(Baddie.MIN_SIZE, Baddie.MAX_SIZE + 1)
        self.x = random.randrange(0, WINDOW_WIDTH - size)
        self.y = 0 - size # start above the window
        self.image = pygwidgets.Image(self.window, (self.x, self.y), Baddie.BADDIE_IMAGE)

        # Scale it
        percent = int((size * 100) / Baddie.MAX_SIZE)
        self.image.scale(percent, False)
        self.speed = random.randrange(Baddie.MIN_SPEED, Baddie.MAX_SPEED)

    def update(self):   # Move the baddie down
        self.y = self.y + self.speed
        self.image.setLoc((self.x, self.y))
        if self.y > GAME_HEIGHT:
            return True  # needs to be deleted
        else:
            return False  # stays on window

    def draw(self):
        self.image.draw()

    def collide(self, playerRect):
        collidedWithPlayer = self.image.overlaps(playerRect)
        return collidedWithPlayer


# BADDIEMGR
class BaddieMgr():
    ADD_NEW_BADDIE_RATE = 8  # add a new baddie every 8 frames

    def __init__(self, window):
        self.window = window
        self.reset()

    def reset(self):  # Called when starting a new game
        self.baddiesList = []
        self.frameCounter = 0  # add a new baddie every ADD_NEW_BADDIE_RATE frames

    def update(self):
        # If the correct amount of frames have passed,
        # add a new baddie
        self.frameCounter = self.frameCounter + 1
        if self.frameCounter == BaddieMgr.ADD_NEW_BADDIE_RATE:
            # Time to add a new baddie (and reset the counter)
            oBaddie = Baddie(self.window)
            self.baddiesList.append(oBaddie)
            self.frameCounter = 0

        # Tell each baddie to update itself
        # Count how many baddies have fallen off the bottom.
        # Return that count (so score can increase for each one that falls off).
        nBaddiesRemoved = 0
        for baddie in reversed(self.baddiesList):
            deleteMe = baddie.update()
            if deleteMe:
                self.baddiesList.remove(baddie)
                nBaddiesRemoved = nBaddiesRemoved + 1

        return nBaddiesRemoved

    def draw(self):
        for baddie in self.baddiesList:
            baddie.draw()

    def hasPlayerHitBaddie(self, playerRect):
        for baddie in self.baddiesList:
            if baddie.collide(playerRect):
                return True

        return False
