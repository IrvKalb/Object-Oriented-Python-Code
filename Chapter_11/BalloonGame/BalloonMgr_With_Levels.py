#  Demo of deleting object

import pygame
import random
from pygame.locals import *
import pygwidgets
from Balloon import *

#
#  BalloonMgr manages a list of Balloon objects
#
class BalloonMgr():

    def __init__(self, window, maxWidth, maxHeight):
        self.window = window
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.balloonList = []

        self.levelDict = {
            1:{'nBalloons':10, 'speed':1},
            2:{'nBalloons':14, 'speed':2},
            3:{'nBalloons':16, 'speed':3},
            4:{'nBalloons':20, 'speed':3},
            5:{'nBalloons':22, 'speed':4}
            }
        self.level = 0
        self.nextLevel()

    def handleEvent(self, event):
        if event.type == MOUSEBUTTONDOWN:
            for oBalloon in self.balloonList:
                nPointsThisBalloon = oBalloon.clickedInside(event.pos)
                if nPointsThisBalloon > 0:
                    #print('clicked on a balloon')
                    self.balloonList.remove(oBalloon)  # remove this balloon
                    print('In handleEvent of bMgr, returning', nPointsThisBalloon)
                    return nPointsThisBalloon  # no need to check others
        # If falls through, no balloon was hit, return 0 points
        return 0

    def nextLevel(self):
        self.level = self.level + 1
        self.startLevel()

    def setLevel(self, newLevel):
        self.level = newLevel
        self.startLevel()

    def startLevel(self):
        levelDict = self.levelDict[self.level]
        nBalloons = levelDict['nBalloons']
        speed = levelDict['speed']

        self.balloonList = []
        for balloonNum in range(nBalloons):
            oBalloon = Balloon(self.window, self.maxWidth, self.maxHeight, balloonNum, speed)
            self.balloonList.append(oBalloon)

    def update(self):
        for oBalloon in self.balloonList:
            status = oBalloon.update()
            if status == 'Delete':
                self.balloonList.remove(oBalloon)  # balloon went off the top end, remove it

        return len(self.balloonList)

    def draw(self):
        for oBalloon in self.balloonList:
            oBalloon.draw()
