# Splash scene - first scene the user sees
import pygwidgets
import pyghelpers
from Constants import *

class SceneSplash(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window

        self.backgroundImage = pygwidgets.Image(self.window,
                                                (0, 0), 'images/splashBackground.jpg')
        self.dodgerImage = pygwidgets.Image(self.window,
                                                (150, 30), 'images/dodger.png')
        
        self.startButton = pygwidgets.CustomButton(self.window, (250, 500),
                                                up='images/startNormal.png',
                                                down='images/startDown.png',
                                                over='images/startOver.png',
                                                disabled='images/startDisabled.png',
                                                enterToActivate=True)

        self.quitButton = pygwidgets.CustomButton(self.window, (30, 650),
                                                up='images/quitNormal.png',
                                                down='images/quitDown.png',
                                                over='images/quitOver.png',
                                                disabled='images/quitDisabled.png')

        self.highScoresButton = pygwidgets.CustomButton(self.window, (360, 650),
                                                up='images/gotoHighScoresNormal.png',
                                                down='images/gotoHighScoresDown.png',
                                                over='images/gotoHighScoresOver.png',
                                                disabled='images/gotoHighScoresDisabled.png')

    def getSceneKey(self):
        return SCENE_SPLASH

    def handleInputs(self, events, keyPressedList):
        for event in events:
            if self.startButton.handleEvent(event):
                self.goToScene(SCENE_PLAY)
            elif self.quitButton.handleEvent(event):
                self.quit()
            elif self.highScoresButton.handleEvent(event):
                self.goToScene(SCENE_HIGH_SCORES)

    def draw(self):
        self.backgroundImage.draw()
        self.dodgerImage.draw()
        self.startButton.draw()
        self.quitButton.draw()
        self.highScoresButton.draw()
