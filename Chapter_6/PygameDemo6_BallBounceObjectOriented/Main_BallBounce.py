# pygame demo 6(a) - using the Ball class, bounce one ball

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Ball import *  # bring in the Ball class code

# 2 - Define constants
BLACK = (0, 0, 0)
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

# 6 - Loop forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()          

    # 8 - Do any "per frame" actions
    oBall.update()  # tell the Ball to update itself

   # 9 - Clear the window before drawing it again
    window.fill(BLACK)
    
    # 10 - Draw the window elements
    oBall.draw()   # tell the Ball to draw itself


    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait


