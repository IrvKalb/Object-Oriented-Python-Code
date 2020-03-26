#  Balloon Manager

import pygame
import random
from pygame.locals import *
import pygwidgets
from BalloonConstants import *
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
        self.nPopped = 0
        self.nMissed = 0
        self.restart()

    def restart(self):
        self.balloonList = []
        self.nPopped = 0
        self.nMissed = 0

        for balloonNum in range(0, N_BALLOONS):
            oBalloon = Balloon(self.window, self.maxWidth, self.maxHeight, balloonNum)
            self.balloonList.append(oBalloon)



    def handleEvent(self, event):
        if event.type == MOUSEBUTTONDOWN:
            for oBalloon in self.balloonList:
                nPointsThisBalloon = oBalloon.clickedInside(event.pos)
                if nPointsThisBalloon > 0:
                    #print('clicked on a balloon')
                    self.balloonList.remove(oBalloon)  # remove this balloon
                    self.nPopped = self.nPopped + 1
                    return nPointsThisBalloon  # no need to check others
        # If falls through, no balloon was hit, return 0 points
        return 0

    def update(self):
        for oBalloon in self.balloonList:
            status = oBalloon.update()
            if status == BALLOON_MISSED:
                self.balloonList.remove(oBalloon)  # balloon went off the top end, remove it
                self.nMissed = self.nMissed + 1

    def getCountPopped(self):
        return self.nPopped

    def getCountMissed(self):
        return self.nMissed

    def draw(self):
        for oBalloon in self.balloonList:
            oBalloon.draw()
