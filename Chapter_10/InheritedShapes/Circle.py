# Circle class

import pygame
from Shape import *
import math

class Circle(Shape):

    def __init__(self, window, maxWidth, maxHeight):
        super().__init__(window, 'Circle', maxWidth, maxHeight)
        self.radius = random.randrange(10, 50)
        self.centerX = self.x + self.radius
        self.centerY = self.y + self.radius
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        
    def clickedInside(self, mousePoint):
        theDistance = math.sqrt(((mousePoint[0] - self.centerX) ** 2) + 
                                             ((mousePoint[1] - self.centerY) ** 2))
        if theDistance <= self.radius:
            return True
        else:
            return False

    def getArea(self):
        theArea = math.pi * (self.radius ** 2)
        return theArea

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.centerX, self.centerY), self.radius, 0)
