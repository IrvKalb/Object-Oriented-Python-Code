#  Money Input Number Example
#
#  demonstrates overriding inherited InputText methods
#

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import pygwidgets
from InputNumber import *

# 2 - Define constants
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  # set the speed (frames per second)
 
# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
title = pygwidgets.DisplayText(window, (0, 40), 'Demo of InputText and InputNumber fields',
                            fontSize=36, width=WINDOW_WIDTH, justified='center')

inputTextCaption = pygwidgets.DisplayText(window, (20, 150), 'Input any text:',
                            fontSize=24, width=190, justified='right')
oInputText = pygwidgets.InputText(window, (230, 150), '', width=150)
okButtonText = pygwidgets.TextButton(window, (430, 150), 'OK')

inputNumberCaption = pygwidgets.DisplayText(window, (20, 250), 'Input number only:',
                            fontSize=24, width=190, justified='right')
oInputNumber = InputNumber(window, (230, 250), '', width=150)
okButtonNumber = pygwidgets.TextButton(window, (430, 250), 'OK')


# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # If the event was a click on the close box, quit pygame and the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pressing Return/Enter or clicking OK triggers action
        if oInputText.handleEvent(event) or okButtonText.handleEvent(event):
            theText = oInputText.getValue()
            print('Input text field contains:', theText)

        if oInputNumber.handleEvent(event) or okButtonNumber.handleEvent(event):
            try:  # see if any error remains
                theText = oInputNumber.getValue()
            except ValueError:
                oInputNumber.setValue('(not a number)')
            else:  # input was OK
                print('Input number field contains:', theText)

    # 8  Do any "per frame" actions

    # 9 - Clear the screen
    window.fill(BACKGROUND_COLOR)

    # 10 - Draw all screen elements
    title.draw()
    inputTextCaption.draw()
    oInputText.draw()
    okButtonText.draw()
    inputNumberCaption.draw()
    oInputNumber.draw()
    okButtonNumber.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount
