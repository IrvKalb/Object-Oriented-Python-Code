# Testing program for 6 dialog boxes

import sys
import os

# These lines are here just in case you are running from the command line
currentPath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(currentPath)

# 1 - Import packages
import pygame
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
    oDialogBackground = pygwidgets.Image(theWindow, (60, 80),
                                            'images/dialog.png')
    oPromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 150),
                                            theText, width=WINDOW_WIDTH,
                                            justified='center', fontSize=36)
    oOKButton = pygwidgets.CustomButton(theWindow, (355, 235),
                                            'images/okNormal.png',
                                            over='images/okOver.png',
                                            down='images/okDown.png',
                                            disabled='images/okDisabled.png')
    response = pyghelpers.customYesNoDialog(theWindow,
                                            oDialogBackground,
                                            oPromptDisplayText,
                                            oOKButton, None)
    return response


def showCustomYesNoDialog(theWindow, theText):
    oDialogBackground = pygwidgets.Image(theWindow, (60, 80),
                                            'images/dialog.png')
    oPromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 150),
                                            theText, width=WINDOW_WIDTH,
                                            justified='center', fontSize=36)
    oNoButton = pygwidgets.CustomButton(theWindow, (95, 235),
                                            'images/noNormal.png',
                                            over='images/noOver.png',
                                            down='images/noDown.png',
                                            disabled='images/noDisabled.png')
    oYesButton = pygwidgets.CustomButton(theWindow, (355, 235),
                                            'images/yesNormal.png',
                                            over='images/yesOver.png',
                                            down='images/yesDown.png',
                                            disabled='images/yesDisabled.png')
    response = pyghelpers.customYesNoDialog(theWindow,
                                            oDialogBackground,
                                            oPromptDisplayText,
                                            oYesButton, oNoButton)
    return response

def showCustomAnswerDialog(theWindow, theText):
    oDialogBackground = pygwidgets.Image(theWindow, (60, 80),
                                            'images/dialog.png')
    oPromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 120),
                                            theText, width=WINDOW_WIDTH,
                                            justified='center', fontSize=36)
    oUserInputText = pygwidgets.InputText(theWindow, (225, 165), '',
                                            fontSize=36, initialFocus=True)
    oNoButton = pygwidgets.CustomButton(theWindow, (105, 235),
                                            'images/cancelNormal.png',
                                            over='images/cancelOver.png',
                                            down='images/cancelDown.png',
                                            disabled='images/cancelDisabled.png')
    oYesButton = pygwidgets.CustomButton(theWindow, (375, 235),
                                            'images/okNormal.png',
                                            over='images/okOver.png',
                                            down='images/okDown.png',
                                            disabled='images/okDisabled.png')
    response = pyghelpers.customAnswerDialog(theWindow,
                                            oDialogBackground, oPromptDisplayText,
                                            oUserInputText,
                                            oYesButton, oNoButton)
    return response


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  # set the speed (frames per second)

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
oTextAlertButton = pygwidgets.TextButton(window, (75, 320), 'Text Alert')
oCustomAlertButton = pygwidgets.TextButton(window, (75, 380), 'Custom Alert')
oTextYesNoButton = pygwidgets.TextButton(window, (280, 320), 'Text Yes/No')
oCustomYesNoButton = pygwidgets.TextButton(window, (280, 380), 'Custom Yes/No')
oTextAnswerButton = pygwidgets.TextButton(window, (485, 320), 'Text Answer')
oCustomAnswerButton = pygwidgets.TextButton(window, (485, 380), 'Custom Answer')

oTitle = pygwidgets.DisplayText(window, (150, 25), 'Click all buttons to test dialogs',
                                    fontSize=36, textColor=WHITE)
oResults = pygwidgets.DisplayText(window, (20, 450), '',
                                    fontSize=36, textColor=WHITE, width=600)

# 6 - Loop forever
while True:

    # 7 -  Check for and handle events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            sys.exit()

        if oTextAlertButton.handleEvent(event):
            ignore = pyghelpers.textYesNoDialog(window,
                                                  (75, 80, 500, 150),
                                                  'This is an alert!', 'OK', None)
            oResults.setValue('User clicked the OK button')

        if oCustomAlertButton.handleEvent(event):
            ignore = showCustomAlertDialog(window, 'This is an alert!')
            oResults.setValue('User clicked the OK button')

        if oTextYesNoButton.handleEvent(event):
            returnedValue = pyghelpers.textYesNoDialog(window, (75, 80, 500, 150),
                                                  'Do you want fries with that?')
            if returnedValue:
                oResults.setValue('User clicked the Yes button')
            else:
                oResults.setValue('User clicked the No button')

        if oCustomYesNoButton.handleEvent(event):
            returnedValue = showCustomYesNoDialog(window, 'Do you want fries with that?')
            if returnedValue:
                oResults.setValue('User clicked the Yes button')
            else:
                oResults.setValue('User clicked the No button')

        if oTextAnswerButton.handleEvent(event):
            userAnswer = pyghelpers.textAnswerDialog(window, (75, 80, 500, 200),
                                    'What is your favorite flavor of ice cream?', 'OK', 'Cancel')
            if userAnswer is not None:
                oResults.setValue('User clicked OK, text was: ' + userAnswer)
            else:
                oResults.setValue('User clicked Cancel')

        if oCustomAnswerButton.handleEvent(event):
            userAnswer = showCustomAnswerDialog(window,
                                    'What is your favorite flavor of ice cream?')
            if userAnswer is not None:
                oResults.setValue('User clicked OK, text was: ' + userAnswer)
            else:
                oResults.setValue('User clicked Cancel')

    # 8 - Do any "per frame" actions

    # 9 - Clear the screen before drawing it again
    window.fill(BACKGROUND_COLOR)
                          
    # 10 - Draw the screen elements
    oTitle.draw()
    oTextAlertButton.draw()
    oCustomAlertButton.draw()
    oTextYesNoButton.draw()
    oCustomYesNoButton.draw()
    oTextAnswerButton.draw()
    oCustomAnswerButton.draw()
    oResults.draw()
    
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
