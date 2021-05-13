# Slider Puzzle Game with Count Up Timer

# 1 - Import packages
import pygame
from pygame.locals import *
import pygwidgets
import pyghelpers
import sys
from Game import *

# 2 - Define constants
WINDOW_WIDTH = 470
WINDOW_HEIGHT = 560
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
 
# 4 - Load assets: image(s), sounds,  etc.
restartButton = pygwidgets.CustomButton(window, (320, 455),
                                        up='images/restartButtonUp.jpg',
                                        down='images/restartButtonDown.jpg',
                                        over='images/restartButtonOver.jpg')

# 5 - Initialize variables
clock = pygame.time.Clock()

timerDisplay = pygwidgets.DisplayText(window, (50, 465), '',
                                    fontSize=36, textColor=WHITE)

messageDisplay = pygwidgets.DisplayText(window, (50, 510), 'Click on a tile to move it.',
                                    fontSize=36, textColor=WHITE)

oGame = Game(window)  # create the main game object

oCountUpTimer = pyghelpers.CountUpTimer()
oCountUpTimer.start()

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            sys.exit()
            
        if event.type == MOUSEBUTTONDOWN:
            messageDisplay.setText('')
            oGame.gotClick(event.pos)
            over = oGame.checkForWin()
            if over:
                messageDisplay.setText('Great job!!!')
                oCountUpTimer.stop()  

        if restartButton.handleEvent(event):
            oGame.startNewGame()
            oCountUpTimer.start()

    # 8 - Do any "per frame" actions
    timeToShow = oCountUpTimer.getTimeInHHMMSS()  # ask the Timer object for the elapsed time
    timerDisplay.setValue('Time: ' + timeToShow)  # put that into a text field

    # 9 - Clear the window before drawing it again
    window.fill(BLACK)

    # 10 - Draw the window elements
    oGame.draw()  # tell the game to draw itself
    restartButton.draw()

    timerDisplay.draw()  # draw the text field
    messageDisplay.draw()  # draw the message display

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
