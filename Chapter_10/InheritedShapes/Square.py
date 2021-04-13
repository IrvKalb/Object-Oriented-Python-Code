# Square class

import pygame
from Shape import *

class Square(Shape):

    def __init__(self, window, maxWidth, maxHeight):
        super().__init__(window, 'Square', maxWidth, maxHeight)
        self.width = random.randrange(10, 100)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.width)

    def clickedInside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked
    
    def getArea(self):
        theArea = self.width * self.width
        return theArea

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.width))
