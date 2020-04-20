# pygame demo 8 Ball Text and Button

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Ball import *  # bring in the Ball class code
from SimpleText import *
from SimpleButton import *

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  # set the speed (frames per second)

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables
frameCounter = 0
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
frameCountDisplay = SimpleText(window, (100, 15), '', WHITE)
restartButton = SimpleButton(window, (290, 444), \
                             'images/restartUp.png', 'images/restartDown.png')

# 6 - Loop forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if restartButton.handleEvent(event):
            frameCounter = 0  # clicked button, reset counter

    # 8 - Do any "per frame" actions
    oBall.update()  # tell the ball to update itself
    messageText = 'Program has run through this many loops: ' + str(frameCounter)
    frameCountDisplay.setValue(messageText)
    frameCounter = frameCounter + 1  # increment each frame

   # 9 - Clear the screen before drawing it again
    window.fill(BLACK)
    frameCountDisplay.draw()
    
    # 10 - Draw the screen elements
    oBall.draw()   # tell the ball to draw itself
    frameCountDisplay.draw()
    restartButton.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount


