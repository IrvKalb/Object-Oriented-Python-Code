# CountUpTimer Example

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import pygwidgets
import pyghelpers

# 2 - Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
FRAMES_PER_SECOND = 30
WHITE = (255, 255, 255)

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
oHeaderMessage = pygwidgets.DisplayText(window, (0, 50), 'Click Start to start a timer:',
                                       fontSize=36, justified='center', width=WINDOW_WIDTH)

oStartButton = pygwidgets.TextButton(window, (180, 100), 'Start')

oStopButton = pygwidgets.TextButton(window, (320, 100), 'Stop')

oTimerMessage = pygwidgets.DisplayText(window, (66, 160), 'getTimeInSeconds      getTimeInHHMMSS',
                                      fontSize=36, width=WINDOW_WIDTH)

oTimerDisplaySeconds = pygwidgets.DisplayText(window, (220, 190), '',
                                      fontSize=36, justified='right')
oTimerDisplayHHMMSS = pygwidgets.DisplayText(window, (356, 190), '',
                                      fontSize=36, justified='right')

oTimerMessage.hide()  # start off with the message hidden
oTimer = pyghelpers.CountUpTimer()  # create a timer object


# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # If the event was a click on the close box, quit pygame and the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oStartButton.handleEvent(event):
            oTimer.start()  # start the timer
            oStartButton.disable()
            oTimerMessage.show()
            print('Starting timer')

        if oStopButton.handleEvent(event):
            print('Stop button was clicked')
            oTimerMessage.hide()
            oTimer.stop()
            oStartButton.enable()

    # 8 - Do any "per frame" actions
    timeInSeconds = oTimer.getTimeInSeconds()
    timeInHHMMSS = oTimer.getTimeInHHMMSS(2)
    oTimerDisplaySeconds.setValue(str(timeInSeconds))
    oTimerDisplayHHMMSS.setValue(timeInHHMMSS)

    # 9 - Clear the window
    window.fill(WHITE)

    # 10 - Draw all window elements
    oHeaderMessage.draw()
    oStartButton.draw()
    oStopButton.draw()
    oTimerMessage.draw()
    oTimerDisplaySeconds.draw()
    oTimerDisplayHHMMSS.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
