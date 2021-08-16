# Pygame demo text and buttons 

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
import pygwidgets

# 2 - Define constants
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3
BALL_WIDTH_HEIGHT = 100

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
oBall = pygwidgets.Image(window, (0, 0), 'images/ball.png')
ballLeft = 0
ballTop = 0

MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

oBackground = pygwidgets.Image(window, (0, 0), 'images/background.jpg')

oRestartButton = pygwidgets.CustomButton(window, (500, 430), 
                                        up='images/restartUp.png', 
                                        down='images/restartDown.png', 
                                        over='images/restartOver.png', 
                                        disabled= 'images/restartDisabled.png')

oHitMeButton = pygwidgets.TextButton(window, (500, 370), 'Hit Me')

oMessageTextA = pygwidgets.DisplayText(window, (20, 50), 'Here is some text', 
                                    fontSize=36, textColor=WHITE)

oMessageTextB = pygwidgets.DisplayText(window, (20, 150),
                                       'Here is more text\nAnd more text\nAnd even more text', 
                                       fontSize=36, textColor=WHITE, justified='center')

oUserInputA = pygwidgets.InputText(window, (20, 350), '', 
                                  fontSize=24, textColor=BLACK, backgroundColor=WHITE)

oUserInputB= pygwidgets.InputText(window, (20, 430), '', width = 400, 
                                  fontSize=24, textColor=WHITE, backgroundColor=BLACK)

counter = 0

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if  oRestartButton.handleEvent(event):
                counter = 0

        if  oHitMeButton.handleEvent(event):
                print('Do not hit me')

        if oUserInputA.handleEvent(event):
            userText = oUserInputA.getText()
            print('In the first field, the user entered:', userText)

        if oUserInputB.handleEvent(event):
            userText = oUserInputB.getText()
            print('The the second field, the user entered:', userText)


    # 8 - Do any "per frame" actions
    counter = counter + 1
    oMessageTextA.setValue('Here is some text.  Loop counter:' + str(counter))

    ballLeft, ballRight = oBall.getLoc()

    if (ballLeft < 0) or (ballLeft + BALL_WIDTH_HEIGHT >= WINDOW_WIDTH):
        xSpeed = -xSpeed  # reverse X direction

    if (ballTop < 0) or (ballTop + BALL_WIDTH_HEIGHT >= WINDOW_HEIGHT):
        ySpeed = -ySpeed  # reverse Y direction

    # Update the rectangle of the ball, based on the speed in two directions
    ballLeft = ballLeft + xSpeed
    ballTop = ballTop + ySpeed
    oBall.setLoc( (ballLeft, ballTop ))


    # 9 - Clear the window before drawing it again
    oBackground.draw()  # draw a background image
                          
    # 10 - Draw the window elements
    oBall.draw()

    oRestartButton.draw()
    oHitMeButton.draw()

    oMessageTextA.draw()
    oMessageTextB.draw()

    oUserInputA.draw()
    oUserInputB.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait




