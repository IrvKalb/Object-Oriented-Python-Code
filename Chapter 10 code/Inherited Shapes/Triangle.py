# Triangle class

import pygame
from Shape import *

class Triangle(Shape):

    def __init__(self, window):
        super().__init__(window, 'Triangle')
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def clickedInside(self, mousePoint):
        inRect = self.rect.collidepoint(mousePoint)
        if not inRect:
            return False

        # Do some math to see if the point is inside the triangle
        xOffset = mousePoint[0] - self.x
        yOffset = self.y + self.height - mousePoint[1]
        if xOffset == 0:
            return True

        slope = yOffset / xOffset  # rise over run
        if slope > 1:
            return True
        else:
            return False

    def area(self):
        theArea = .5 * self.width * self.height
        return theArea

    def draw(self):
        pygame.draw.polygon(self.window, self.color, (\
            (self.x, self.y + self.height), \
            (self.x, self.y),\
            (self.x + self.width, self.y)))
