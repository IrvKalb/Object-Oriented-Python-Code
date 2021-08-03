#  MVC Roll Them Dice - Irv Kalb

import pygame
import pygwidgets
import sys
from Constants import *
from DiceView import *
from DiceModel import *

FRAMES_PER_SECOND = 30
BACKGROUND_COLOR = (0, 222, 222)
STARTING_ROUNDS = 2500


pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Roll Them Dice')
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

oDiceModel = DiceModel(STARTING_ROUNDS)
oDiceView = DiceView(window, STARTING_ROUNDS)

oTitleDisplay = pygwidgets.DisplayText(window, (330, 30), 'Roll Them Dice!',
                       fontName='monospaces', fontSize=34)
oQuitButton = pygwidgets.TextButton(window, (20, 595), 'Quit', width=100, height=35)
oRollButton = pygwidgets.TextButton(window, (690, 595), 'Roll Again', width=100, height=35)

oRoundsDisplay = pygwidgets.DisplayText(window, (200, 600), 'Number of rolls:',
                          fontName='monospaces', fontSize=28, width=150, justified='right')

oRoundsInput = pygwidgets.InputText(window, (355, 600), str(STARTING_ROUNDS),
                            fontName='monospaces', fontSize=28, width=100,
                            initialFocus=True)
oChangeButton = pygwidgets.TextButton(window, (465, 595), 'Change', width=100, height=35)

oDiceImage = pygwidgets.Image(window, (28, 15), 'images/twoDice.png')

nRounds, theResultsDict = oDiceModel.generateRolls()
oDiceView.update(nRounds, theResultsDict)

while True:
    # Handle events
    for event in pygame.event.get():
        if oQuitButton.handleEvent(event) or (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

        if oRollButton.handleEvent(event):
            nRounds, theResultsDict = oDiceModel.generateRolls()
            oDiceView.update(nRounds, theResultsDict)

        elif oChangeButton.handleEvent(event) or oRoundsInput.handleEvent(event):
            # Eventually Change this TextInput to InputNumber field
            nRounds = oRoundsInput.getValue()
            nRounds = int(nRounds)
            oDiceView.setNumberOfRounds(nRounds)
            oDiceModel.setNumberOfRounds(nRounds)
            nRounds, theResultsDict = oDiceModel.generateRolls()
            oDiceView.update(nRounds, theResultsDict)

        else:  # pass the event onto the View
            oDiceView.handleEvent(event)

    # Draw everything
    window.fill(BACKGROUND_COLOR)

    oDiceView.draw()
    oRollButton.draw()
    oTitleDisplay.draw()
    oDiceImage.draw()
    oRoundsDisplay.draw()
    oRoundsInput.draw()
    oChangeButton.draw()
    oQuitButton.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
