import pygame
from Constants import *


class Square():

    def __init__(self, window, left, top):
        self.window = window
        self.loc = (left, top)
        self.rect = pygame.Rect(left, top, SQUARE_WIDTH, SQUARE_HEIGHT)

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setImage(self, image):
        self.image = image

    def getImage(self):
        return self.image

    def clickInside(self, mouseLoc):
        clickedInside = self.rect.collidepoint(mouseLoc)
        return clickedInside

    def draw(self):
        self.window.blit(self.image, self.loc)

