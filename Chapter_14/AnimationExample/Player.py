# Player class

# 1 - Import packages
import pygame
from pygame.locals import *
import pygwidgets


PIXELS_PER_MOVE = 5

SOUTH = 'south'
NORTH = 'north'
WEST = 'west'
EAST = 'east'


class Player():
    nPixelsPerMove = 5

    def __init__(self, window, loc):
        self.window = window
        self.loc = list(loc)
        walkSouthTuple = (('images/player/walkF0.png', .1), ('images/player/walkF1.png', .1),
                            ('images/player/walkF2.png', .1), ('images/player/walkF3.png', .1),
                            ('images/player/walkF4.png', .1), ('images/player/walkF5.png', .1),
                            ('images/player/walkF6.png', .1), ('images/player/walkF7.png', .1))
        walkNorthTuple = (('images/player/walkB0.png', .1), ('images/player/walkB1.png', .1),
                             ('images/player/walkB2.png', .1), ('images/player/walkB3.png', .1),
                             ('images/player/walkB4.png', .1), ('images/player/walkB5.png', .1),
                             ('images/player/walkB6.png', .1), ('images/player/walkB7.png', .1))
        walkWestTuple = (('images/player/walkL0.png', .1), ('images/player/walkL1.png', .1),
                         ('images/player/walkL2.png', .1), ('images/player/walkL3.png', .1),
                         ('images/player/walkL4.png', .1), ('images/player/walkL5.png', .1),
                         ('images/player/walkL6.png', .1), ('images/player/walkL7.png', .1))
        walkEastTuple = (('images/player/walkR0.png', .1), ('images/player/walkR1.png', .1),
                          ('images/player/walkR2.png', .1), ('images/player/walkR3.png', .1),
                          ('images/player/walkR4.png', .1), ('images/player/walkR5.png', .1),
                          ('images/player/walkR6.png', .1), ('images/player/walkR7.png', .1))

        self.oWalkAnimations = pygwidgets.AnimationCollection(window, self.loc,
                                              {SOUTH: walkSouthTuple,
                                               NORTH: walkNorthTuple,
                                               WEST: walkWestTuple,
                                               EAST: walkEastTuple},
                                               SOUTH, loop=True, autoStart=False)

        self.direction = SOUTH
        self.keysDownList = []
        self.isMoving = False
 
    def getRect(self):
        return self.oWalkAnimations.getRect()

    def getCenterLoc(self):
        theRect = self.getRect()
        theCenter = theRect.center
        return theCenter

    def getDirection(self):
        return self.direction

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.keysDownList.append(SOUTH)
                self.direction = SOUTH
                self.oWalkAnimations.replace(SOUTH)
                self.oWalkAnimations.start()
                self.isMoving = True
            elif event.key == pygame.K_UP:
                self.keysDownList.append(NORTH)
                self.direction = NORTH
                self.oWalkAnimations.replace(NORTH)
                self.oWalkAnimations.start()
                self.isMoving = True
            elif event.key == pygame.K_LEFT:
                self.keysDownList.append(WEST)
                self.direction = WEST
                self.oWalkAnimations.replace(WEST)
                self.oWalkAnimations.start()
                self.isMoving = True
            elif event.key == pygame.K_RIGHT:
                self.keysDownList.append(EAST)
                self.direction = EAST
                self.oWalkAnimations.replace(EAST)
                self.oWalkAnimations.start()
                self.isMoving = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.keysDownList.remove(SOUTH)
            elif event.key == pygame.K_UP:
                self.keysDownList.remove(NORTH)
            elif event.key == pygame.K_LEFT:
                self.keysDownList.remove(WEST)
            elif event.key == pygame.K_RIGHT:
                self.keysDownList.remove(EAST)

            if len(self.keysDownList) == 0:
                self.oWalkAnimations.stop()
                self.isMoving = False
            else:
                self.direction = self.keysDownList[0]  # just use first keydown in list
                self.oWalkAnimations.replace(self.direction)
                self.oWalkAnimations.start()
                self.isMoving = True


    def update(self):
        if self.isMoving:
            if self.direction == WEST:
                self.loc[0] = self.loc[0] - Player.nPixelsPerMove

            elif self.direction == EAST:
                self.loc[0] = self.loc[0] + Player.nPixelsPerMove

            elif self.direction == NORTH:
                self.loc[1] = self.loc[1] - Player.nPixelsPerMove

            elif self.direction == SOUTH:
                self.loc[1] = self.loc[1] + Player.nPixelsPerMove

            self.oWalkAnimations.update()
        return self.loc[0], self.loc[1]

    def draw(self):
        self.oWalkAnimations.draw()
