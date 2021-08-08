# Shows example of SimpleSpriteSheetAnimation object

# 1 - Import library
import pygame
from pygame.locals import *
import sys
import pygwidgets
from SimpleSpriteSheetAnimation import *

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

# 5 - Initialize variables
oWaterAnimation = SimpleSpriteSheetAnimation(window, (22, 140), 'images/water_003.png', 50, 192, 192, .05)
oPlayButton = pygwidgets.TextButton(window, (60, 320), "Play")

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if oPlayButton.handleEvent(event):
            oWaterAnimation.play()

    # 8 - Do any "per frame" actions
    oWaterAnimation.update()

    # 9 - Clear the window
    window.fill(BGCOLOR)

    # 10 - Draw all window elements
    oWaterAnimation.draw()
    oPlayButton.draw()

    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount
