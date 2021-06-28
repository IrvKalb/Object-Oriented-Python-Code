# SimpleText class

import pygame
from pygame.locals import *

class SimpleText():
    
    def __init__(self, window, loc, value, textColor):
        pygame.font.init()
        self.window = window
        self.loc = loc
        self.font = pygame.font.SysFont(None, 30)
        self.textColor = textColor
        self.text = None # so that the call to setText below will force the creation of the text image
        self.setValue(value) # set the initial text for drawing

    def setValue(self, newText):  
        if self.text == newText:
            return  # nothing to change

        self.text = newText  # save the new text
        self.textSurface = self.font.render(self.text, True, self.textColor)

    def draw(self):
        self.window.blit(self.textSurface, self.loc)
