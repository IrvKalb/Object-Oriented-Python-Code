#
# This the High Scores Scene
#

import pygame
import sys
from pygame.locals import *
import pygwidgets
import pyghelpers
from Constants import *
import json  # Write and read the data file in JSON format

def showCustomAnswerDialog(theWindow, theText):
    oDialogBackground = pygwidgets.Image(theWindow, (35, 450), 'images/dialog.png')
    oPromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 480), theText, \
                                width=WINDOW_WIDTH, justified='center', fontSize=36)
    oUserInputText = pygwidgets.InputText(theWindow, (200, 550), '',
                                            fontSize=36, initialFocus=True)
    oNoButton = pygwidgets.CustomButton(theWindow, (65, 595), \
                                        'images/noThanksNormal.png',\
                                        over='images/noThanksOver.png',\
                                        down='images/noThanksDown.png',\
                                        disabled='images/noThanksDisabled.png')
    oYesButton = pygwidgets.CustomButton(theWindow, (330, 595), \
                                        'images/addNormal.png',\
                                        over='images/addOver.png',\
                                        down='images/addDown.png',\
                                        disabled='images/addDisabled.png')
    choiceAsBoolean, userAnswer = pyghelpers.customAnswerDialog(theWindow, oDialogBackground, \
                                    oPromptDisplayText, oUserInputText, oYesButton, oNoButton)
    return choiceAsBoolean, userAnswer

def showCustomResetDialog(theWindow, theText):
    oDialogBackground = pygwidgets.Image(theWindow, (35, 450), 'images/dialog.png')
    oPromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 480), theText, \
                                width=WINDOW_WIDTH, justified='center', fontSize=36)
    oNoButton = pygwidgets.CustomButton(theWindow, (65, 595), \
                                        'images/cancelNormal.png',\
                                        over='images/cancelOver.png',\
                                        down='images/cancelDown.png',\
                                        disabled='images/cancelDisabled.png')
    oYesButton = pygwidgets.CustomButton(theWindow, (330, 595), \
                                        'images/okNormal.png',\
                                        over='images/okOver.png',\
                                        down='images/okDown.png',\
                                        disabled='images/okDisabled.png')
    choiceAsBoolean = pyghelpers.customYesNoDialog(theWindow, oDialogBackground, \
                                    oPromptDisplayText, oYesButton, oNoButton)
    return choiceAsBoolean


class SceneHighScores(pyghelpers.Scene):
    DATA_FILE_PATH = 'HighScores.txt'
    N_HIGH_SCORES = 10
    
    def __init__(self, window):
        self.window = window

        self.backgroundImage = pygwidgets.Image(self.window, (0, 0), "images/highScoresBackground.jpg")

        # The following will create a list of lists
        # Either by building a blank one from scratch, or by reading from a text file
        # The result will look like:
        # [[name, score], [name, score], [name, score] ...]
        # and will always be kept in order of the score (highest to lowest)
        if not pyghelpers.fileExists(SceneHighScores.DATA_FILE_PATH):
            self.setEmptyHighScores()

        else:
            data = pyghelpers.readFile(SceneHighScores.DATA_FILE_PATH)
            # read in all the data in json format, converts to a list of lists
            self.scoresList = json.loads(data)

        self.scoresField = pygwidgets.DisplayText(self.window, (25, 84), '', \
                                fontSize=48, textColor=BLACK, width=175, justified='right')
        self.namesField = pygwidgets.DisplayText(self.window, (260, 84), '', \
                                fontSize=48, textColor=BLACK, width=300, justified='left')

        self.quitButton = pygwidgets.CustomButton(self.window, (30, 650), \
                                                   up='images/quitNormal.png',\
                                                   down='images/quitDown.png',\
                                                   over='images/quitOver.png',\
                                                   disabled='images/quitDisabled.png')

        #self.resetScoresButton = pygwidgets.TextButton(self.window, (240, 650), 'Reset high scores')

        self.resetScoresButton = pygwidgets.CustomButton(self.window, (240, 650), \
                                                   up='images/resetNormal.png',\
                                                   down='images/resetDown.png',\
                                                   over='images/resetOver.png',\
                                                   disabled='images/resetDisabled.png')
        #self.startNewGameButton = pygwidgets.TextButton(self.window, (450, 650), 'Start new game')
        self.startNewGameButton = pygwidgets.CustomButton(self.window, (450, 650), \
                                                   up='images/startNewNormal.png',\
                                                   down='images/startNewDown.png',\
                                                   over='images/startNewOver.png',\
                                                   disabled='images/startNewDisabled.png')

        self.showHighScores()


    def setEmptyHighScores(self):
            self.scoresList = [] 
            for i in range(0, SceneHighScores.N_HIGH_SCORES):
                self.scoresList.append(['-----', 0])
            pyghelpers.writeFile(SceneHighScores.DATA_FILE_PATH, json.dumps(self.scoresList))

    def getSceneKey(self):
        return SCENE_HIGH_SCORES

    def enter(self, data):
        # This can be called two different ways:
        # 1. If there is no new high score, data will be None
        # 2. Otherwise, data will be the score of the current game
        if data is not None:
            self.draw()
            # We have a new high score sent in from the play scene
            newHighScoreValue = data  # this is the score

            dialogQuestion = 'To record your score of ' \
                                     + str(newHighScoreValue) + ',\n' + \
                                     'please enter your name:'

            answered, playerName = showCustomAnswerDialog(self.window, dialogQuestion)

            # Alternatively, could build a text-button based dialog like this
            #answered, playerName = pyghelpers.textDialogAsk(self.window, (35, 450, DIALOG_BOX_WIDTH, 200),\
            #   dialogQuestion, 'Add to high scores', 'No thanks')

            if answered:  # user said yes, add to high scores
                if playerName == '':
                    playerName = 'Anonymous'

                # Find the appropriate place to add the new high score
                for index, nameScoreList in enumerate(self.scoresList):
                    thisScore = nameScoreList[1]
                    if newHighScoreValue > thisScore:
                        self.scoresList.insert(index, [playerName, newHighScoreValue])
                        break
                # Remove the lowest score entry from the list (last element)
                self.scoresList.pop(SceneHighScores.N_HIGH_SCORES)
                # Show the new high scores table
                self.showHighScores()
                # Write out updated file of high scores
                pyghelpers.writeFile(SceneHighScores.DATA_FILE_PATH, json.dumps(self.scoresList))

    def showHighScores(self):
        # Build up strings and show them in text display fields
        scoresText = ''
        namesText = ''
        for nameScoreList in self.scoresList:
            # Each element is a list of [name, score]
            namesText = namesText + nameScoreList[0] + '\n'
            scoresText = scoresText + str(nameScoreList[1]) + '\n'

        self.scoresField.setValue(scoresText)
        self.namesField.setValue(namesText)

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.startNewGameButton.handleEvent(event):
                self.goToScene(SCENE_PLAY)

            elif self.quitButton.handleEvent(event):
                self.quit()

            elif self.resetScoresButton.handleEvent(event):
                #confirmed = pyghelpers.textYesNoDialog(self.window, (35, 450, DIALOG_BOX_WIDTH, 150), \
                #                              "Are you sure you want to RESET the high scores?")
                confirmed = showCustomResetDialog(self.window, \
                                                  "Are you sure you want to \nRESET the high scores?")
                if confirmed:
                    self.setEmptyHighScores()
                    self.showHighScores()


    def draw(self):
        self.backgroundImage.draw()
        self.scoresField.draw()
        self.namesField.draw()
        self.quitButton.draw()
        self.resetScoresButton.draw()
        self.startNewGameButton.draw()


    def respond(self, requestID):
        if requestID == HIGH_SCORES_DATA:
            # This is a request to get a dictionary made up of
            # the highest score so far, and the lowest high score of all scores in the list
            highestOnList = self.scoresList[0]
            lowestOnList = self.scoresList[-1]
            highestScore = highestOnList[1]
            lowestScore = lowestOnList[1]

            return {'highest':highestScore, 'lowest':lowestScore}
