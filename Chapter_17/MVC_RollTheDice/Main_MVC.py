#  Main MVC Roll The Dice - Irv Kalb

# 1 - Import packages
# import pygame
import pygwidgets
import sys
from Constants import *
from Controller import *

# 2 - Define constants
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Roll Them Dice')
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
# Instantiate the Controller object
oController = Controller(window)

# 6 - Loop forever
while True:
    # 7 -  Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Pass all events to the Controller
        oController.handleEvent(event)

    # 8 - Do any "per frame" actions

    # 9 - Clear the window  (let the Controller do it)
    # 10 - Draw the window elements
    oController.draw()

    # 11 - Update the widow
    pygame.display.update()

    # 12 - Slow things down
    clock.tick(FRAMES_PER_SECOND) # make pygame wait
