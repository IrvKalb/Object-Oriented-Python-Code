# Square class

import pygame
import random

# set up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Square():

    def __init__(self, window):
        self.window = window
        self.widthAndHeight = random.randrange(10, 100)
        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(0, 400)
        self.y = random.randrange(0, 400)
        self.rect = pygame.Rect(self.x, self.y, self.widthAndHeight, self.widthAndHeight)
        self.type = 'Square'
        
    def clickedInside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked

    def getType(self):
        return self.type
    
    def getArea(self):
        theArea = self.widthAndHeight * self.widthAndHeight
        return theArea

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.widthAndHeight, self.widthAndHeight))
