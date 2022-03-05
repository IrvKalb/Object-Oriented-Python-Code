#  Money example
#
#  Demonstrates overriding inherited DisplayText and InputText methods

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import pygwidgets
from DisplayMoney import *
from InputNumber import *

# 2 - Define constants
BLACK = (0, 0, 0)
BLACKISH = (10, 10, 10)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
title = pygwidgets.DisplayText(window, (0, 40),
                'Demo of InputNumber and DisplayMoney fields',
                fontSize=36, width=WINDOW_WIDTH, justified='center')

inputCaption = pygwidgets.DisplayText(window, (20, 150),
                'Input money amount:', fontSize=24,
                width=190, justified='right')
inputField = InputNumber(window, (230, 150), '', width=150, initialFocus=True)
okButton = pygwidgets.TextButton(window, (430, 150), 'OK')

outputCaption1 = pygwidgets.DisplayText(window, (20, 300),
                'Output dollars & cents:', fontSize=24,
                width=190, justified='right')
moneyField1 = DisplayMoney(window, (230, 300), '', textColor=BLACK,
                backgroundColor=WHITE, width=150)

outputCaption2 = pygwidgets.DisplayText(window, (20, 400),
                'Output dollars only:', fontSize=24,
                width=190, justified='right')
moneyField2 = DisplayMoney(window, (230, 400), '', textColor=BLACK,
                backgroundColor=WHITE, width=150,
                showCents=False)
# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # If the event was a click on the close box, quit pygame and the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pressing Return/Enter or clicking OK triggers action
        if inputField.handleEvent(event) or okButton.handleEvent(event):
            try:
                theValue = inputField.getValue()
            except ValueError:  # any remaining error
                inputField.setValue('(not a number)')
            else:  # input was OK
                theText = str(theValue)
                moneyField1.setValue(theText)
                moneyField2.setValue(theText)

    # 8  Do any "per frame" actions

    # 9 - Clear the window
    window.fill(BACKGROUND_COLOR)

    # 10 - Draw all window elements
    title.draw()
    inputCaption.draw()
    inputField.draw()
    okButton.draw()
    outputCaption1.draw()
    moneyField1.draw()
    outputCaption2.draw()
    moneyField2.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
