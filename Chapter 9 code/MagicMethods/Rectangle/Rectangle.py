# Rectangle class

import pygame
import random

# set up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Rectangle():

    def __init__(self, window):
        self.window = window
        self.width = random.choice((20, 30, 40))
        self.height = random.choice((20, 30, 40))
        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(0, 400)
        self.y = random.randrange(0, 400)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.area = self.width * self.height

    def clickedInside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked

    # Magic method called when you compare
    # two rectangle  objects with the == operator
    def __eq__(self, oOtherRectangle):
        if self.area == oOtherRectangle.area:
            return True
        else:
            return False

    # Magic method called when you compare
    # two rectangle  objects with the < operator
    def __lt__(self, oOtherRectangle):
        if self.area < oOtherRectangle.area:
            return True
        else:
            return False

    # Magic method called when you compare
    # two rectangle  objects with the > operator
    def __gt__(self, oOtherRectangle):
        if self.area > oOtherRectangle.area:
            return True
        else:
            return False

    def getArea(self):
        return self.area

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))

    # def __str__(self):
    #     print('width:', self.width)
    #     print('height', self.height)
    #     print('color', self.color)
    #     print('x', self.x)
    #     print('y', self.y)
    #     print('area', self.area)
    #     return 'string version of rect'
