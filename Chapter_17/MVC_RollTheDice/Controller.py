#  Controller - Roll The Dice

import pygame
from pygame.locals import *
import pygwidgets
import sys
from Constants import *
from View import *
from Model import *

BACKGROUND_COLOR = (0, 222, 222)

class Controller():
    def __init__(self, window, nRoundsToStart):
        self.window = window

        # Instantiate the Model and the View objects
        self.oModel = ModelDice(nRoundsToStart)
        self.oView = ViewDice(window, nRoundsToStart)

        self.oTitleDisplay = pygwidgets.DisplayText(window, (330, 30), 'Roll The Dice!',
                       fontName='monospaces', fontSize=34)
        self.oQuitButton = pygwidgets.TextButton(window, (20, 595), 'Quit', width=100, height=35)
        self.oRollButton = pygwidgets.TextButton(window, (690, 595), 'Roll Again', width=100, height=35)

        self.oRoundsDisplay = pygwidgets.DisplayText(window, (200, 600), 'Number of rolls:',
                          fontName='monospaces', fontSize=28, width=150, justified='right')

        self.oRoundsInput = pygwidgets.InputText(window, (355, 600), str(nRoundsToStart),
                            fontName='monospaces', fontSize=28, width=100,
                            initialFocus=True)
        self.oChangeButton = pygwidgets.TextButton(window, (465, 595), 'Change', width=100, height=35)

        self.oDiceImage = pygwidgets.Image(window, (650, 15), 'images/twoDice.png')
        self.viewArea = (45, 70, WINDOW_WIDTH - 90, WINDOW_HEIGHT - 140)

        # Generate the starting data, and tell the View about the results
        nRounds, theResultsDict = self.oModel.generateRolls()
        self.oView.update(nRounds, theResultsDict)

    def handleEvent(self, event):
        # Handle events

        if self.oQuitButton.handleEvent(event) or (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

        if self.oRollButton.handleEvent(event):
            nRounds, theResultsDict = self.oModel.generateRolls()
            self.oView.update(nRounds, theResultsDict)

        elif self.oChangeButton.handleEvent(event) or self.oRoundsInput.handleEvent(event):
            # Eventually Change this TextInput to InputNumber field
            nRounds = self.oRoundsInput.getValue()
            nRounds = int(nRounds)
            self.oView.setNumberOfRounds(nRounds)
            self.oModel.setNumberOfRounds(nRounds)
            nRounds, theResultsDict = self.oModel.generateRolls()
            self.oView.update(nRounds, theResultsDict)

        else:  # pass the event on to the View
            self.oView.handleEvent(event)

    def draw(self):
        # Draw everything
        self.window.fill(BACKGROUND_COLOR)

        pygame.draw.rect(self.window, BLACK, self.viewArea, 3)
        self.oView.draw()  # tell the view to draw itself
        self.oRollButton.draw()
        self.oTitleDisplay.draw()
        self.oDiceImage.draw()
        self.oRoundsDisplay.draw()
        self.oRoundsInput.draw()
        self.oChangeButton.draw()
        self.oQuitButton.draw()

