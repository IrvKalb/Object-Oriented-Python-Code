# Testing program for 6 dialog boxes

import sys
import os

# These lines are here just in case you are running from the command line
currentPath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(currentPath)

# 1 - Import packages
import pygame
from pygame.locals import *
import random
import pygwidgets
import pyghelpers

# 2 - Define constants
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (0, 138, 138)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30



def showCustomAlertDialog(theWindow, theText):
    oDialogBackground = pygwidgets.Image(theWindow, (60, 120), 'images/dialog.png')
    oPromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 170), theText, \
                                width=WINDOW_WIDTH, justified='center', fontSize=36)
    oOKButton = pygwidgets.CustomButton(theWindow, (355, 265), \
                                        'images/okNormal.png',\
                                        over='images/okOver.png',\
                                        down='images/okDown.png',\
                                        disabled='images/okDisabled.png')
    userAnswer = pyghelpers.customYesNoDialog(theWindow, oDialogBackground, \
                                    oPromptDisplayText, oOKButton, None)
    return userAnswer


def showCustomYesNoDialog(theWindow, theText):
    oDialogBackground = pygwidgets.Image(theWindow, (60, 120), 'images/dialog.png')
    oPromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 170), theText, \
                                width=WINDOW_WIDTH, justified='center', fontSize=36)
    oNoButton = pygwidgets.CustomButton(theWindow, (95, 265), \
                                        'images/noNormal.png',\
                                        over='images/noOver.png',\
                                        down='images/noDown.png',\
                                        disabled='images/noDisabled.png')
    oYesButton = pygwidgets.CustomButton(theWindow, (355, 265), \
                                        'images/yesNormal.png',\
                                        over='images/yesOver.png',\
                                        down='images/yesDown.png',\
                                        disabled='images/yesDisabled.png')
    userAnswer = pyghelpers.customYesNoDialog(theWindow, oDialogBackground, \
                                    oPromptDisplayText, oYesButton, oNoButton)
    return userAnswer

def showCustomAnswerDialog(theWindow, theText):
    oDialogBackground = pygwidgets.Image(theWindow, (60, 120), 'images/dialog.png')
    oPromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 170), theText, \
                                width=WINDOW_WIDTH, justified='center', fontSize=36)
    oUserInputText = pygwidgets.InputText(theWindow, (225, 220), '',
                                            fontSize=36, initialFocus=True)
    oNoButton = pygwidgets.CustomButton(theWindow, (105, 265), \
                                        'images/cancelNormal.png',\
                                        over='images/cancelOver.png',\
                                        down='images/cancelDown.png',\
                                        disabled='images/cancelDisabled.png')
    oYesButton = pygwidgets.CustomButton(theWindow, (375, 265), \
                                        'images/okNormal.png',\
                                        over='images/okOver.png',\
                                        down='images/okDown.png',\
                                        disabled='images/okDisabled.png')
    choiceAsBoolean, userAnswer = pyghelpers.customAnswerDialog(theWindow, oDialogBackground, \
                                    oPromptDisplayText, oUserInputText, oYesButton, oNoButton)
    return choiceAsBoolean, userAnswer


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  # set the speed (frames per second)

# 4 - Load assets: image(s), sounds,  etc.


# 5 - Initialize variables

textAlertButton = pygwidgets.TextButton(window, (75, 370), 'Text Alert')
customAlertButton = pygwidgets.TextButton(window, (75, 420), 'Custom Alert')
textYesNoButton = pygwidgets.TextButton(window, (280, 370), 'Text Yes/No')
customYesNoButton = pygwidgets.TextButton(window, (280, 420), 'Custom Yes/No')
textAnswerButton = pygwidgets.TextButton(window, (485, 370), 'Text Answer')
customAnswerButton = pygwidgets.TextButton(window, (485, 420), 'Custom Answer')

title = pygwidgets.DisplayText(window, (150, 50), 'Click all buttons to test dialogs', \
                                    fontSize=36, textColor=WHITE)


# 6 - Loop forever
while True:

    # 7 -  Check for and handle events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            sys.exit()

        if textAlertButton.handleEvent(event):
            ignore = pyghelpers.textYesNoDialog(window, (75, 100, 500, 150),
                                                  'This is an alert!', 'OK', '')
            print('User clicked the OK button')

        if customAlertButton.handleEvent(event):
            ignore = showCustomAlertDialog(window, 'This is an alert!')
            print('User clicked the OK button')

        if textYesNoButton.handleEvent(event):
            returnedValue = pyghelpers.textYesNoDialog(window, (75, 100, 500, 150),
                                                  'Do you want fries with that?', 'Yes', 'No')
            print('Returned value was:', returnedValue)
            if returnedValue:
                print('User clicked Yes')
            else:
                print('User clicked No')

        if customYesNoButton.handleEvent(event):
            returnedValue = showCustomYesNoDialog(window, 'Do you want fries with that?')
            print('Returned value was:', returnedValue)                                             
            if returnedValue:
                print('User clicked Yes')
            else:
                print('User clicked No')

        if textAnswerButton.handleEvent(event):
            returnedValue, userAnswer = pyghelpers.textAnswerDialog(window, (75, 100, 500, 200),
                                                  'What is your favorite flavor of ice cream?', 'OK', 'Cancel')
            print('Returned values were:', returnedValue, userAnswer)                                            
            if returnedValue:
                print('User clicked OK')
                print('Users answer was:', userAnswer)
            else:
                print('User clicked cancel')

        if customAnswerButton.handleEvent(event):
            returnedValue, userAnswer = showCustomAnswerDialog(window, \
                                                           'What is your favorite flavor of ice cream?')
            print('Returned values were:', returnedValue, userAnswer )                                                                                        
            if returnedValue:
                print('User clicked OK')
                print('Users answer was:', userAnswer)
            else:
                print('User clicked Cancel')


    # 8 - Do any "per frame" actions

    # 9 - Clear the screen before drawing it again
    window.fill(BACKGROUND_COLOR)
                          
    # 10 - Draw the screen elements
    title.draw()

    textAlertButton.draw()
    customAlertButton.draw()
    textYesNoButton.draw()
    customYesNoButton.draw()
    textAnswerButton.draw()
    customAnswerButton.draw()
    
    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount




