# Circle class

import pygame
from Shape import *

class Circle(Shape):

    def __init__(self, window):
        super().__init__(window, 'Circle')
        self.radius = random.randrange(10, 50)
        self.centerX = self.x + self.radius
        self.centerY = self.y + self.radius
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        
    def clickedInside(self, mousePoint):
        theDistance = (((mousePoint[0] - self.centerX) ** 2) + ((mousePoint[1] - self.centerY)) ** 2) **.5
        if theDistance <= self.radius:
            return True
        else:
            return False

    def area(self):
        theArea = 3.14159 * (self.radius ** 2)  # pi times the radius squared
        return theArea

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.centerX, self.centerY), self.radius, 0)
