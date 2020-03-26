#  Balloon Game main code

# 1 - Import packages
from pygame.locals import *
import pygwidgets
import sys
import pygame

# 2 - Define constants
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
PANEL_HEIGHT = 60
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND = 30


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()  # set the speed (frames per second)

# 4 - Load assets: image(s), sounds,  etc.
oScoreDisplay = pygwidgets.DisplayText(window, (10, USABLE_WINDOW_HEIGHT + 25), \
                                'Score: 0', textColor=BLACK, \
                                backgroundColor=None, width=140, fontSize=24)
oStatusDisplay = pygwidgets.DisplayText(window, (180, USABLE_WINDOW_HEIGHT + 25), '', \
                                 textColor=BLACK, backgroundColor=None, \
                                 width=300, fontSize=24)
oRestartButton = pygwidgets.TextButton(window, \
                                       (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10), \
                                       'Restart')
oRestartButton.disable()  # disable the button because the game starts running

# 5 - Initialize variables
from BalloonMgr import * # import BalloonMgr after pygame is initialized
from BalloonConstants import *
oBalloonMgr = BalloonMgr(window, WINDOW_WIDTH, USABLE_WINDOW_HEIGHT)

score = 0
playing = True  # start off playing

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    nPointsEarned = 0
    for event in pygame.event.get():
    
        # check if the event is the close button
        if event.type == pygame.QUIT:
            # if it is quit, the program
            pygame.quit()
            sys.exit()

        if playing:
            nPointsEarned = oBalloonMgr.handleEvent(event)
            if nPointsEarned > 0:
                score = score + nPointsEarned
                oScoreDisplay.setValue('Score: ' + str(score))

        else:
            if oRestartButton.handleEvent(event):
                oBalloonMgr.restart()
                score = 0
                oScoreDisplay.setValue('Score: ' + str(score))
                playing = True
                oRestartButton.disable()

    # 8  Do any "per frame" actions
    if playing:
        oBalloonMgr.update()
        nPopped = oBalloonMgr.getCountPopped()
        nMissed = oBalloonMgr.getCountMissed()
        oStatusDisplay.setValue('Popped: ' + str(nPopped) + \
                        '   Missed: ' + str(nMissed) + \
                        '   Out of: ' + str(N_BALLOONS))

        if (nPopped + nMissed) == N_BALLOONS:
            playing = False
            oRestartButton.enable()


    # 9 - Clear the screen
    window.fill(BACKGROUND_COLOR)

    # 10 - Draw all screen elements
    if playing:
        oBalloonMgr.draw()

    pygame.draw.rect(window, GRAY, pygame.Rect(0, USABLE_WINDOW_HEIGHT, \
                                        WINDOW_WIDTH, PANEL_HEIGHT))
    oScoreDisplay.draw()
    oStatusDisplay.draw()
    oRestartButton.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount
