#  Pygame demo 7a 3-Button Test with callbacks

# 1 - Import packages
import pygame
from pygame.locals import *
from SimpleButton import *
import sys

# Define constants
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

# Define a function to be used as a "callback"
def myCallBackFunction():
    print('Called myFunction')

# Define a class with a method to be used as a "callback"
class CallBackTest():
    def __init__(self):
        pass

    def myMethod(self):
        print('Called myMethod of the CallBackTest object')


# 2 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables

oCallBackTest = CallBackTest()
# Create instances of SimpleButton
oButtonA = SimpleButton(window, (25, 30), \
                        'images/buttonAUp.png', \
                        'images/buttonADown.png')
oButtonB = SimpleButton(window, (150, 30), \
                        'images/buttonBUp.png', \
                        'images/buttonBDown.png', myCallBackFunction)  # specifying a function to call back
oButtonC = SimpleButton(window, (275, 30), \
                        'images/buttonCUp.png', \
                        'images/buttonCDown.png', oCallBackTest.myMethod)  # method to callback
counter = 0


# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            sys.exit()

        # Pass the event to the button, see if has been clicked on
        if oButtonA.handleEvent(event):
            print('User pressed button A.  Detected in the main loop')

        # buttonB and buttonC have callbacks, no need to check result of these calls.
        oButtonB.handleEvent(event)

        oButtonC.handleEvent(event)

    # 8 - Do any "per frame" actions
    counter = counter + 1
    
    # 9 - Clear the screen
    window.fill(GRAY)
    
    # 10 - Draw all screen elements
    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount
