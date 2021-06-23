#
# This is the Splash Scene
#
# This is where the player sees the intro screen
#

import pygwidgets
import pyghelpers
import pygame
from pygame.locals import *
from Constants import *


class SceneSplash(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window

        self.messageField = pygwidgets.DisplayText(window, (15, 25), 'Welcome to Rock, Paper, Scissors!', \
                                              fontSize=50, textColor=WHITE, width=610, justified='center')

        self.startButton = pygwidgets.CustomButton(self.window, (210, 300), \
                                                up='images/startButtonUp.png', \
                                                down='images/startButtonDown.png', \
                                                over='images/startButtonHighlight.png')

        self.rockImage = pygwidgets.Image(window, (25, 120), 'images/Rock.png')
        self.paperImage = pygwidgets.Image(window, (225, 120), 'images/Paper.png')
        self.scissorsImage = pygwidgets.Image(window, (425, 120), 'images/Scissors.png')

    def getSceneKey(self):
        return SCENE_SPLASH

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
        self.rockImage.draw()
        self.paperImage.draw()
        self.scissorsImage.draw()
        self.startButton.draw()

    def leave(self):
        return None
