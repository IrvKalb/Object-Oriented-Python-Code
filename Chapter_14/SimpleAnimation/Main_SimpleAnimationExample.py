# Animation example
# Shows example of SimpleAnimation object

# 1 - Import library
import pygame
from pygame.locals import *
import sys
import pygwidgets
from SimpleAnimation import *

# 2 Define constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 30
BGCOLOR = (0, 128, 128)

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

# 4 - Load assets: images(s), sounds, etc.
dinosaurAnimTuple = ('images/Dinobike/f1.gif',
                      'images/Dinobike/f2.gif',
                      'images/Dinobike/f3.gif',
                      'images/Dinobike/f4.gif',
                      'images/Dinobike/f5.gif',
                      'images/Dinobike/f6.gif',
                      'images/Dinobike/f7.gif',
                      'images/Dinobike/f8.gif',
                      'images/Dinobike/f9.gif',
                      'images/Dinobike/f10.gif')

# 5 - Initialize variables
oDinosaurAnimation = SimpleAnimation(window, (22, 140),
                                     dinosaurAnimTuple, .1)
oPlayButton = pygwidgets.TextButton(window, (20, 240), "Play")

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        if oPlayButton.handleEvent(event):
            oDinosaurAnimation.play()

    # 8 - Do any "per frame" actions
    oDinosaurAnimation.update()

    # 9 - Clear the window
    window.fill(BGCOLOR)

    # 10 - Draw all window elements
    oDinosaurAnimation.draw()
    oPlayButton.draw()

    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
