#  Controller - Roll The Dice

import pygame
from pygame.locals import *
import pygwidgets
import sys
from Constants import *
from pyghelpers import *
from BarView import *
from PieView import *
from TextView import *
from Model import *
from InputNumber import *

BACKGROUND_COLOR = (0, 222, 222)
N_ROUNDS_AT_START = 2500
LIGHT_GRAY = (225, 225, 225)

class Controller():
    def __init__(self, window):
        self.window = window

        # Instantiate the Model
        self.oModel = Model()

        # Instantiate different View objects
        self.oBarView = BarView(self.window, self.oModel)
        self.oPieView = PieView(self.window, self.oModel)
        self.oTextView = TextView(self.window, self.oModel)

        # Default to bar view at start
        self.oView = self.oBarView  

        self.oTitleDisplay = pygwidgets.DisplayText(window, (330, 30), 'Roll The Dice!',
                          fontName='monospaces', fontSize=34)
        self.oQuitButton = pygwidgets.TextButton(window, (20, 595), 'Quit', width=100, height=35)

        self.oRoundsDisplay = pygwidgets.DisplayText(window, (260, 600), 'Number of rolls:',
                          fontName='monospaces', fontSize=28, width=150, justified='right')

        self.oRoundsInput = InputNumber(window, (430, 600), value=str(N_ROUNDS_AT_START),
                          fontName='monospaces', fontSize=28, width=100,
                          initialFocus=True, keepFocusOnSubmit=True,
                          allowFloatingNumber=False, allowNegativeNumber=False)

        self.oRollDiceButton = pygwidgets.TextButton(window, (690, 595), 'Roll Dice', width=100, height=35)

        self.oDiceImage = pygwidgets.Image(window, (650, 15), 'images/twoDice.png')
        # This area reserved for the different views
        self.viewArea = pygame.Rect(45, 70, WINDOW_WIDTH - 90, WINDOW_HEIGHT - 200)

        self.oBarButton = pygwidgets.TextRadioButton(window, (80, 540),
                                                     'View', 'Bar Chart', value=True, fontSize=36)
        self.oPieButton = pygwidgets.TextRadioButton(window, (350, 540),
                                                     'View', 'Pie Chart', fontSize=36)
        self.oTextButton = pygwidgets.TextRadioButton(window, (620, 540),
                                                      'View', 'Text', fontSize=36)

        # Generate the starting data, and tell the View about the results
        self.generateNewData()
        self.oView.update()

    def handleEvent(self, event):
        if self.oQuitButton.handleEvent(event):
            pygame.quit()
            sys.exit()

        if self.oRollDiceButton.handleEvent(event) or self.oRoundsInput.handleEvent(event):
            self.generateNewData()
            self.oView.update()

        if self.oBarButton.handleEvent(event):
            self.oView = self.oBarView
            self.oView.update()
        elif self.oPieButton.handleEvent(event):
            self.oView = self.oPieView
            self.oView.update()
        elif self.oTextButton.handleEvent(event):
            self.oView = self.oTextView
            self.oView.update()

    def generateNewData(self):
        """This method gets the number of rolls from the input field and
        after checking for errors, tells the model to generate new data based
        on the number of rolls the user asked for.
        """
        try:
            nRounds = self.oRoundsInput.getValue()
        except Exception as msg:
            pyghelpers.textYesNoDialog(self.window, pygame.Rect(170, 180, 430, 170),
                                       msg, 'OK', None, backgroundColor=LIGHT_GRAY)
            return
        if nRounds < 100:
            pyghelpers.textYesNoDialog(self.window, pygame.Rect(170, 180, 430, 170),
                                       'For meaningful results,\n enter 100 or more.', 'OK', None,
                                       backgroundColor=LIGHT_GRAY)
            return
        self.oModel.generateRolls(nRounds)

    def draw(self):
        # Draw everything the Controller is responsible for
        # (everything outside of the black rectangle)
        self.window.fill(BACKGROUND_COLOR)

        self.oBarButton.draw()
        self.oPieButton.draw()
        self.oTextButton.draw()
        self.oTitleDisplay.draw()
        self.oDiceImage.draw()
        self.oRoundsDisplay.draw()
        self.oRoundsInput.draw()
        self.oRollDiceButton.draw()
        self.oQuitButton.draw()

        # Each view is responsible for drawing the elements
        # inside the black rectangle
        pygame.draw.rect(self.window, BLACK, self.viewArea, 3)
        self.oView.draw()  # tell the current view to draw itself
