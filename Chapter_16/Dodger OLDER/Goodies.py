### GOODIE
import pygame
import pygwidgets
import random
from Constants import *

class Goodie():
    MIN_SIZE = 10
    MAX_SIZE = 41  # max plus one
    MIN_SPEED = 1
    MAX_SPEED = 9  # max plus one
    GOODIE_IMAGE = pygame.image.load('images/goodie.png')  # load the image once
    RIGHT = 'right'
    LEFT = 'left'

    def __init__(self, window):
        self.window = window
        size = random.randrange(Goodie.MIN_SIZE, Goodie.MAX_SIZE)
        self.y = random.randrange(0, GAME_HEIGHT - size)

        self.direction = random.choice([Goodie.LEFT, Goodie.RIGHT])
        if self.direction == Goodie.LEFT:  # start on right side
            self.x = WINDOW_WIDTH   # start to the right of the window
            self.speed = - random.randrange(Goodie.MIN_SPEED, Goodie.MAX_SPEED)
            self.minLeft = - size
        else:  # start on left side
            self.x = 0 - size # start to the left of the window
            self.speed = random.randrange(Goodie.MIN_SPEED, Goodie.MAX_SPEED)


        self.image = pygwidgets.Image(self.window, (self.x, self.y), Goodie.GOODIE_IMAGE)
        percent = int((size * 100) / Goodie.MAX_SIZE)
        self.image.scale(percent, False)

    def update(self):
        self.x = self.x + self.speed
        self.image.setLoc((self.x, self.y))
        if self.direction == Goodie.LEFT:
            if self.x < self.minLeft:
                return True  # needs to be deleted
            else:
                return False  # stays in window
        else:
            if self.x > WINDOW_WIDTH:
                return True  # needs to be deleted
            else:
                return False  # stays in window


    def draw(self):
        self.image.draw()

    def collide(self, playerRect):
        collidedWithPlayer = self.image.overlaps(playerRect)
        return collidedWithPlayer


# GOODIEMGR
class GoodieMgr():
    GOODIE_RATE_LO = 90
    GOODIE_RATE_HI = 111

    def __init__(self, window):
        self.window = window
        self.reset()

    def reset(self):  # Called when starting a new game
        self.goodiesList = []
        self.frameCounter = 0
        self.createGoodieMax = GoodieMgr.GOODIE_RATE_HI

    def update(self):
        # If the correct amount of frames have passed,
        # add a new goodie at the left or right of the window

        self.frameCounter = self.frameCounter + 1
        if self.frameCounter == self.createGoodieMax:
            # Time to add a new goodie (and reset the counter)
            oGoodie = Goodie(self.window)
            self.goodiesList.append(oGoodie)
            self.frameCounter = 0
            # add a new goodie every createGoodieMax frames
            self.createGoodieMax = random.randrange(GoodieMgr.GOODIE_RATE_LO, GoodieMgr.GOODIE_RATE_HI)

        # Tell each goodie to update itself.
        # If a goodie goes off an edge, remove it
        for goodie in self.goodiesList:
            deleteMe = goodie.update()
            if deleteMe:
                self.goodiesList.remove(goodie)

    def draw(self):
        for goodie in self.goodiesList:
            goodie.draw()

    def hasPlayerHitGoodie(self, playerRect):
        for goodie in self.goodiesList:
            if goodie.collide(playerRect):
                self.goodiesList.remove(goodie)  # remove this goodie from the list
                return True

        return False
