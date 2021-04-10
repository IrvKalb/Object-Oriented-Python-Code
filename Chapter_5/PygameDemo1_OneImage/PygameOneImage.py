# pygame demo 1 - Draw one image

# 1 - Import packages
import pygame
from pygame.locals import *
import sys

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sounds,  etc.
ballImage = pygame.image.load('images/ball.png')

# 5 - Initialize variables
 
# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # If the event was a click on the close box, quit pygame and the program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

    # 8  Do any "per frame" actions
    
    # 9 - Clear the window
    window.fill(BLACK)
    
    # 10 - Draw all window elements
    # draw ball at position 100 across (X), and 200 down (Y)
    window.blit(ballImage, (100, 200))    

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
