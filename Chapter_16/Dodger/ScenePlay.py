#  Play scene - the main game play scene
from pygame.locals import *
import pygwidgets
import pyghelpers
from Player import *
from Baddies import *
from Goodies import *

def showCustomYesNoDialog(theWindow, theText):
    oDialogBackground = pygwidgets.Image(theWindow, (40, 250),
                                            'images/dialog.png')
    oPromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 290),
                                            theText, width=WINDOW_WIDTH,
                                            justified='center', fontSize=36)

    oYesButton = pygwidgets.CustomButton(theWindow, (320, 370),
                                            'images/gotoHighScoresNormal.png',
                                            over='images/gotoHighScoresOver.png',
                                            down='images/gotoHighScoresDown.png',
                                            disabled='images/gotoHighScoresDisabled.png')

    oNoButton = pygwidgets.CustomButton(theWindow, (62, 370),
                                            'images/noThanksNormal.png',
                                            over='images/noThanksOver.png',
                                            down='images/noThanksDown.png',
                                            disabled='images/noThanksDisabled.png')

    choiceAsBoolean = pyghelpers.customYesNoDialog(theWindow,
                                            oDialogBackground, oPromptDisplayText,
                                            oYesButton, oNoButton)
    return choiceAsBoolean

BOTTOM_RECT = (0, GAME_HEIGHT + 1, WINDOW_WIDTH,
                                WINDOW_HEIGHT - GAME_HEIGHT)
STATE_WAITING = 'waiting'
STATE_PLAYING = 'playing'
STATE_GAME_OVER = 'game over'

class ScenePlay(pyghelpers.Scene):

    def __init__(self, window):
        self.window = window

        self.controlsBackground = pygwidgets.Image(self.window,
                                        (0, GAME_HEIGHT),
                                        'images/controlsBackground.jpg')

        self.quitButton = pygwidgets.CustomButton(self.window,
                                        (30, GAME_HEIGHT + 90),
                                        up='images/quitNormal.png',
                                        down='images/quitDown.png',
                                        over='images/quitOver.png',
                                        disabled='images/quitDisabled.png')

        self.highScoresButton = pygwidgets.CustomButton(self.window,
                                        (190, GAME_HEIGHT + 90),
                                        up='images/gotoHighScoresNormal.png',
                                        down='images/gotoHighScoresDown.png',
                                        over='images/gotoHighScoresOver.png',
                                        disabled='images/gotoHighScoresDisabled.png')

        self.newGameButton = pygwidgets.CustomButton(self.window,
                                        (450, GAME_HEIGHT + 90),
                                        up='images/startNewNormal.png',
                                        down='images/startNewDown.png',
                                        over='images/startNewOver.png',
                                        disabled='images/startNewDisabled.png',
                                        enterToActivate=True)

        self.soundCheckBox = pygwidgets.TextCheckBox(self.window,
                                        (430, GAME_HEIGHT + 17),
                                        'Background music',
                                        True, textColor=WHITE)

        self.gameOverImage = pygwidgets.Image(self.window, (140, 180),
                                        'images/gameOver.png')

        self.titleText = pygwidgets.DisplayText(self.window,
                                        (70, GAME_HEIGHT + 17),
                                        'Score:                                 High Score:',
                                        fontSize=24, textColor=WHITE)

        self.scoreText = pygwidgets.DisplayText(self.window,
                                        (80, GAME_HEIGHT + 47), '0',
                                        fontSize=36, textColor=WHITE,
                                        justified='right')

        self.highScoreText = pygwidgets.DisplayText(self.window,
                                        (270, GAME_HEIGHT + 47), '',
                                        fontSize=36, textColor=WHITE,
                                        justified='right')

        pygame.mixer.music.load('sounds/background.mid')
        self.dingSound = pygame.mixer.Sound('sounds/ding.wav')
        self.gameOverSound = pygame.mixer.Sound('sounds/gameover.wav')

        # Instantiate objects
        self.oPlayer = Player(self.window)
        self.oBaddieMgr = BaddieMgr(self.window)
        self.oGoodieMgr = GoodieMgr(self.window)

        self.highestHighScore = 0
        self.lowestHighScore = 0
        self.backgroundMusic = True
        self.score = 0
        self.playingState = STATE_WAITING

    def getSceneKey(self):
        return SCENE_PLAY

    def enter(self, data):
        self.getHiAndLowScores()

    def getHiAndLowScores(self):
        # Ask the High Scores scene for a dict of  scores
        # that looks like this:
        #  {'highest': highestScore, 'lowest': lowestScore}
        infoDict = self.request(SCENE_HIGH_SCORES, HIGH_SCORES_DATA)
        self.highestHighScore = infoDict['highest']
        self.highScoreText.setValue(self.highestHighScore)
        self.lowestHighScore = infoDict['lowest']

    def reset(self):   # start a new game
        self.score = 0
        self.scoreText.setValue(self.score)
        self.getHiAndLowScores()

        # Tell the managers to reset themselves
        self.oBaddieMgr.reset()
        self.oGoodieMgr.reset()

        if self.backgroundMusic:
            pygame.mixer.music.play(-1, 0.0)
        self.newGameButton.disable()
        self.highScoresButton.disable()
        self.soundCheckBox.disable()
        self.quitButton.disable()
        pygame.mouse.set_visible(False)

    def handleInputs(self, eventsList, keyPressedList):
        if self.playingState == STATE_PLAYING:
            return  # ignore button events while playing

        for event in eventsList:
            if self.newGameButton.handleEvent(event):
                self.reset()
                self.playingState = STATE_PLAYING

            if self.highScoresButton.handleEvent(event):
                self.goToScene(SCENE_HIGH_SCORES)

            if self.soundCheckBox.handleEvent(event):
                self.backgroundMusic = self.soundCheckBox.getValue()

            if self.quitButton.handleEvent(event):
                self.quit()

    def update(self):
        if self.playingState != STATE_PLAYING:
            return  # only update when playing

        # Move the Player to the mouse position, get back its rect
        mouseX, mouseY = pygame.mouse.get_pos()
        playerRect = self.oPlayer.update(mouseX, mouseY)

        # Tell the GoodieMgr to move all Goodies
        # Returns the number of Goodies that the Player contacted
        nGoodiesHit = self.oGoodieMgr.update(playerRect)
        if nGoodiesHit > 0:
            self.dingSound.play()
            self.score = self.score + (nGoodiesHit * POINTS_FOR_GOODIE)

        # Tell the BaddieMgr to move all the Baddies
        # Returns the number of Baddies that fell off the bottom
        nBaddiesEvaded  = self.oBaddieMgr.update()
        self.score = self.score + (nBaddiesEvaded * POINTS_FOR_BADDIE_EVADED)
        
        self.scoreText.setValue(self.score)

        # Check if the Player has hit any Baddie
        if self.oBaddieMgr.hasPlayerHitBaddie(playerRect):
            pygame.mouse.set_visible(True)
            pygame.mixer.music.stop()

            self.gameOverSound.play()
            self.playingState = STATE_GAME_OVER
            self.draw()  # force drawing of game over message

            if self.score > self.lowestHighScore:
                scoreString = 'Your score: ' + str(self.score) + '\n'
                if self.score > self.highestHighScore:
                    dialogText = (scoreString +
                                       'is a new high score, CONGRATULATIONS!')
                else:
                    dialogText = (scoreString +
                                      'gets you on the high scores list.')

                result = showCustomYesNoDialog(self.window, dialogText)
                if result: # navigate
                    self.goToScene(SCENE_HIGH_SCORES, self.score)  

            self.newGameButton.enable()
            self.highScoresButton.enable()
            self.soundCheckBox.enable()
            self.quitButton.enable()
    
    def draw(self):
        self.window.fill(BLACK)
    
        # Tell the managers to draw all the Baddies and Goodies
        self.oBaddieMgr.draw()
        self.oGoodieMgr.draw()
    
        # Tell the Player to draw itself
        self.oPlayer.draw()
    
        # Draw all the info at the bottom of the window
        self.controlsBackground.draw()
        self.titleText.draw()
        self.scoreText.draw()
        self.highScoreText.draw()
        self.soundCheckBox.draw()
        self.quitButton.draw()
        self.highScoresButton.draw()
        self.newGameButton.draw()

        if self.playingState == STATE_GAME_OVER:
            self.gameOverImage.draw()

    def leave(self):
        pygame.mixer.music.stop()
