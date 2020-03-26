#  Balloon class

import pygame
import random
from pygame.locals import *
import pygwidgets
from BalloonConstants import *

#
#  Balloon class
#

class Balloon():

    popSound = pygame.mixer.Sound('sounds/balloonPop.wav')
    smallBalloonImage = pygame.image.load('images/redBalloonSmall.png')
    mediumBalloonImage = pygame.image.load('images/redBalloonMedium.png')
    largeBalloonImage = pygame.image.load('images/redBalloonLarge.png')

    def __init__(self, window, maxWidth, maxHeight, ID):
        self.window = window
        self.ID = ID
        size = random.choice(('small', 'medium', 'large'))
        if size == 'small':
            self.balloonImage = pygwidgets.Image(window, (0, 0), Balloon.smallBalloonImage)
            self.nPoints = 30
            self.speedY = 3.1
        elif size == 'medium':
            self.balloonImage = pygwidgets.Image(window, (0, 0), Balloon.mediumBalloonImage)
            self.nPoints = 20
            self.speedY = 2.2
        else:  # large
            self.balloonImage = pygwidgets.Image(window, (0, 0), Balloon.largeBalloonImage)
            self.nPoints = 10
            self.speedY = 1.5


        balloonRect = self.balloonImage.getRect()
        self.width = balloonRect.width
        self.height = balloonRect.height
        # Position so that entire balloon is within the window
        self.x = random.randrange(maxWidth - self.width)
        self.y = maxHeight + random.randrange(75)
        self.balloonImage.setLoc((self.x, self.y))

    def clickedInside(self, mousePoint):
        myRect = pygame.Rect(self.x, self.y, self.width, self.height)
        if myRect.collidepoint(mousePoint):
            Balloon.popSound.play()
            return self.nPoints
        else:
            return 0

    def update(self):
        self.y = self.y - self.speedY   # update y position based on our speed
        self.balloonImage.setLoc((self.x, self.y))
        if self.y < -self.height:     # Off the top of the window
            return BALLOON_MISSED
        else:
            return BALLOON_MOVING

    def draw(self):
        self.balloonImage.draw()

    def __del__(self):
        print('Balloon', self.ID, 'is going away')


