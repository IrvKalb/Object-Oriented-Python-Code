# pygame demo 8  - SimpleText, SimpleButton, and Ball

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
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oFrameCountLabel = SimpleText(window, (60, 20), 
                             'Program has run through this many loops: ', WHITE)
oFrameCountDisplay = SimpleText(window, (500, 20), '', WHITE)
oRestartButton = SimpleButton(window, (280, 60), 
                      'images/restartUp.png', 'images/restartDown.png')
frameCounter = 0

# 6 - Loop forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if oRestartButton.handleEvent(event):
            frameCounter = 0  # clicked button, reset counter

    # 8 - Do any "per frame" actions
    oBall.update()  # tell the ball to update itself
    frameCounter = frameCounter + 1  # increment each frame
    oFrameCountDisplay.setValue(str(frameCounter))

   # 9 - Clear the window before drawing it again
    window.fill(BLACK)
    
    # 10 - Draw the window elements
    oBall.draw()   # tell the ball to draw itself
    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait 
