#  MVC Roll Them Dice - Irv Kalb

import pygame
import pygwidgets
import sys
from Constants import *
from Controller import *

FRAMES_PER_SECOND = 30
STARTING_ROUNDS = 2500

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Roll Them Dice')
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Instantiate the Controller object
oController = Controller(window, STARTING_ROUNDS)

while True:
    # Handle events - pass all to the Controller
    for event in pygame.event.get():
        oController.handleEvent(event)

    # Draw everything
    oController.draw()
    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
