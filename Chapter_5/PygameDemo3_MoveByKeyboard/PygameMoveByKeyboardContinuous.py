# pygame demo 3(b) - one image, continuous mode, move as long as a key is down

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from pathlib import Path

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 120
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3

# defining ball path
ROOT_DIR = Path(__file__).resolve().parent
PATH_TO_BALL = ROOT_DIR / 'images' / 'ball.png'
PATH_TO_TARGET = ROOT_DIR / 'images' / 'target.jpg'

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.
ballImage = pygame.image.load(PATH_TO_BALL)
targetImage = pygame.image.load(PATH_TO_TARGET)

# 5 - Initialize variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions
    # Check for user pressing keys
    keyPressedTuple = pygame.key.get_pressed()

    if keyPressedTuple[pygame.K_LEFT]:  # moving left
        ballX = ballX - N_PIXELS_TO_MOVE

    if keyPressedTuple[pygame.K_RIGHT]:  # moving right
        ballX = ballX + N_PIXELS_TO_MOVE

    if keyPressedTuple[pygame.K_UP]:  # moving up
        ballY = ballY - N_PIXELS_TO_MOVE

    if keyPressedTuple[pygame.K_DOWN]:  # moving down
        ballY = ballY + N_PIXELS_TO_MOVE

    # Check if the ball is colliding with the target
    ballRect = pygame.Rect(ballX, ballY,
                                       BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    if ballRect.colliderect(targetRect):
        print('Ball is touching the target')

    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    window.blit(targetImage, (TARGET_X, TARGET_Y))  # draw the target
    window.blit(ballImage, (ballX, ballY))    # draw the ball

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
