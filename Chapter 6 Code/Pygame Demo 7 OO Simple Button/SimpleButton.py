#
# SIMPLE BUTTON
#

import pygame
from pygame.locals import *

class SimpleButton():
        
    def __init__(self, window, loc, up, down):

        self.window = window
        self.loc = loc
        self.surfaceUp = pygame.image.load(up)
        self.surfaceDown = pygame.image.load(down)

        # figure out the rect of the button, (used to see if the mouse is within the button)
        self.rect = self.surfaceUp.get_rect()
        self.rect.left = self.loc[0]
        self.rect.top = self.loc[1]

        # used to track the state of the button
        self.buttonDown = False # is the button currently pushed down?
        self.mouseOverButton = False # is the mouse currently hovering over the button?
        self.lastMouseDownOverButton = False # was the last mouse down event over the button? (Tracks clicks.)
        self.mouseIsDown = False


    def handleEvent(self, eventObj):
        # This method will return True if user clicks the button.
        # Normally returns False.

        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN) :
            # The button only cares bout mouse-related events 
            return False

        clicked = False

        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)
        if (not self.mouseOverButton) and eventPointInButtonRect:
            # if mouse has entered the button:
            self.mouseOverButton = True

        elif self.mouseOverButton and (not eventPointInButtonRect):
            # if mouse has exited the button:
            self.mouseOverButton = False

        if eventPointInButtonRect:
            if eventObj.type == MOUSEBUTTONDOWN:
                self.buttonDown = True
                self.lastMouseDownOverButton = True
        else:
            if eventObj.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN):
                # if an up/down happens off the button, then the next up won't cause mouseClick()
                self.lastMouseDownOverButton = False

        if eventObj.type == MOUSEBUTTONDOWN:
            self.mouseIsDown = True
            
        # mouse up is handled whether or not it was over the button
        doMouseClick = False
        if eventObj.type == MOUSEBUTTONUP:
            self.mouseIsDown = False
            if self.lastMouseDownOverButton:
                doMouseClick = True
            self.lastMouseDownOverButton = False

            if self.buttonDown:
                self.buttonDown = False

            if doMouseClick:
                self.buttonDown = False
                clicked = True

        return clicked

    def draw(self):
        # Draw the button's current appearance to the window.
        if self.mouseIsDown:
            if self.mouseOverButton and self.lastMouseDownOverButton:
                self.window.blit(self.surfaceDown, self.loc)
            else:
                self.window.blit(self.surfaceUp, self.loc)
        else:  # mouse is up
            self.window.blit(self.surfaceUp, self.loc)




