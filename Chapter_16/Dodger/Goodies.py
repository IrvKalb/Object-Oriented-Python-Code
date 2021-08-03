# Goodie and GoddieMgr classes
import pygame
import pygwidgets
import random
from Constants import *

class Goodie():
    MIN_SIZE = 10
    MAX_SIZE = 40
    MIN_SPEED = 1
    MAX_SPEED = 8
    # Load the image once
    GOODIE_IMAGE = pygame.image.load('images/goodie.png')
    RIGHT = 'right'
    LEFT = 'left'

    def __init__(self, window):
        self.window = window
        size = random.randrange(Goodie.MIN_SIZE, Goodie.MAX_SIZE + 1)
        self.y = random.randrange(0, GAME_HEIGHT - size)

        self.direction = random.choice([Goodie.LEFT, Goodie.RIGHT])
        if self.direction == Goodie.LEFT:  # start on right side of the window
            self.x = WINDOW_WIDTH
            self.speed = - random.randrange(Goodie.MIN_SPEED,
                                                            Goodie.MAX_SPEED + 1)
            self.minLeft = - size
        else:  # start on left side of the window
            self.x = 0 - size
            self.speed = random.randrange(Goodie.MIN_SPEED,
                                                          Goodie.MAX_SPEED + 1)

        self.image = pygwidgets.Image(self.window,
                                                     (self.x, self.y), Goodie.GOODIE_IMAGE)
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


class GoodieMgr():
    GOODIE_RATE_LO = 90
    GOODIE_RATE_HI = 111

    def __init__(self, window):
        self.window = window
        self.reset()

    def reset(self):  # Called when starting a new game
        self.goodiesList = []
        self.nFramesTilNextGoodie = GoodieMgr.GOODIE_RATE_HI

    def update(self, thePlayerRect):
        # Tell each Goodie to update itself.
        # If a Goodie goes off an edge, remove it
        # Count up all Goodies that contact the player and remove them.
        nGoodiesHit = 0
        goodiesListCopy = self.goodiesList.copy()
        for oGoodie in goodiesListCopy:
            deleteMe = oGoodie.update()
            if deleteMe:
                self.goodiesList.remove(oGoodie)  # remove this Goodie

            elif oGoodie.collide(thePlayerRect):
                self.goodiesList.remove(oGoodie)  # remove this Goodie
                nGoodiesHit = nGoodiesHit + 1
        
        # If the correct amount of frames have passed,
        # add a new Goodie (and reset the counter)
        self.nFramesTilNextGoodie = self.nFramesTilNextGoodie - 1
        if self.nFramesTilNextGoodie == 0:
            oGoodie = Goodie(self.window)
            self.goodiesList.append(oGoodie)
            self.nFramesTilNextGoodie = random.randrange(
                                                            GoodieMgr.GOODIE_RATE_LO,
                                                            GoodieMgr.GOODIE_RATE_HI)

        return nGoodiesHit  # return number of Goodies that contacted player

    def draw(self):
        for oGoodie in self.goodiesList:
            oGoodie.draw()
