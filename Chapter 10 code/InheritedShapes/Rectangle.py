# Rectangle class

import pygame
from Shape import *


class Rectangle(Shape):

    def __init__(self, window):
        super().__init__(window, 'Rectangle')
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def clickedInside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked

    def area(self):
        theArea = self.width * self.height
        return theArea

# Uncomment to implement draw method for Rectangle
#    def draw(self):
#        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
