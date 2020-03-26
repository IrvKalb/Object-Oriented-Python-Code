#
# This the Splash Scene
#
# This is where the player sees the intro screen
#

import pygwidgets
import pyghelpers
import pygame
from pygame.locals import *
from Constants import *


class SceneSplash(pyghelpers.Scene):
    def __init__(self, window, sceneKey):
        # Save window and sceneKey in instance variables
        self.window = window
        self.sceneKey = sceneKey

        self.messageField = pygwidgets.DisplayText(window, (15, 25), 'Welcome to Rock, Paper, Scissors!', \
                                              fontSize=50, textColor=WHITE, width=610, justified='center')

        self.startButton = pygwidgets.CustomButton(self.window, (210, 300), \
                                                up='images/startButtonUp.png', \
                                                down='images/startButtonDown.png', \
                                                over='images/startButtonHighlight.png')

        self.rockImage = pygame.image.load("images/Rock.png")
        self.paperImage = pygame.image.load("images/Paper.png")
        self.scissorImage = pygame.image.load("images/Scissors.png")

    def enter(self, data):
        pass

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.startButton.handleEvent(event):
                self.goToScene(SCENE_PLAY)

    def update(self):
        pass

    def draw(self):
        self.window.fill(GRAY)
        self.messageField.draw()
        self.window.blit(self.rockImage, (25, 120))
        self.window.blit(self.paperImage, (225, 120))
        self.window.blit(self.scissorImage, (425, 120))
        self.startButton.draw()

    def leave(self):
        return None
