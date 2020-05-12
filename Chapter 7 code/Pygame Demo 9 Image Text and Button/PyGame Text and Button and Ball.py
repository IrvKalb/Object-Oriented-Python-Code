# pygame demo text and buttons 

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
clock = pygame.time.Clock()  # set the speed (frames per second)

# 4 - Load assets: image(s), sounds,  etc.
#ball = pygame.image.load('images/ball.png')

# 5 - Initialize variables
#ballRect = ball.get_rect()

ball = pygwidgets.Image(window, (0, 0), 'images/ball.png')
ballLeft = 0
ballTop = 0

MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME



background = pygwidgets.Image(window, (0, 0), 'images/background1.jpg')

restartButton = pygwidgets.CustomButton(window, (500, 430), \
                                        up='images/RestartButtonUp.png', \
                                        down='images/RestartButtonDown.png', \
                                        over='images/RestartButtonOver.png', \
                                        disabled= 'images/RestartButtonDisabled.png')

hitMeButton = pygwidgets.TextButton(window, (500, 370), 'Hit Me')


messageTextA = pygwidgets.DisplayText(window, (20, 50), 'Here is some text', \
                                    fontSize=36, textColor=WHITE)

messageTextB = pygwidgets.DisplayText(window, (20, 150), 'Here is more text\nAnd more text\nAnd even more text', \
                                    fontSize=36, textColor=WHITE, justified='center')


userInputA = pygwidgets.InputText(window, (20, 350), '', \
                                  fontSize=24, textColor=BLACK, backgroundColor=WHITE)

userInputB= pygwidgets.InputText(window, (20, 430), '', width = 400, \
                                  fontSize=24, textColor=WHITE, backgroundColor=BLACK)

counter = 0

# 6 - Loop forever
while True:

    # 7 -  Check for and handle events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            sys.exit()

        if  restartButton.handleEvent(event):
                counter = 0

        if  hitMeButton.handleEvent(event):
                print('Do not hit me')

        if userInputA.handleEvent(event):
            userText = userInputA.getText()
            print('In the first field, the user entered:', userText)

        if userInputB.handleEvent(event):
            userText = userInputB.getText()
            print('The the second field, the user entered:', userText)


    # Main code
    counter = counter + 1
    messageTextA.setValue('Here is some text.  Loop counter:' + str(counter))

    ballLeft, ballRight = ball.getLoc()

    # 8 - Do any "per frame" actions
    if (ballLeft < 0) or (ballLeft + BALL_WIDTH_HEIGHT > WINDOW_WIDTH):
        xSpeed = -xSpeed  # reverse X direction

    if (ballTop < 0) or (ballTop + BALL_WIDTH_HEIGHT > WINDOW_HEIGHT):
        ySpeed = -ySpeed  # reverse Y direction

    # update the rectangle of the ball, based on the speed in two directions
    ballLeft = ballLeft + xSpeed
    ballTop = ballTop + ySpeed
    ball.setLoc( (ballLeft, ballTop ))


    # 9 - Clear the screen before drawing it again
    background.draw()  # draw a background image
                          
    # 10 - Draw the screen elements
    ball.draw()

    restartButton.draw()
    hitMeButton.draw()

    messageTextA.draw()
    messageTextB.draw()

    userInputA.draw()
    userInputB.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount




