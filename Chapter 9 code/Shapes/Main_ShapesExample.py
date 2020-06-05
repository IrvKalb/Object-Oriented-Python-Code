import pygame
import sys
from pygame.locals import *
from Square import *
from Circle import *
from Triangle import *
import pygwidgets

# set up the constants
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_SHAPES = 10

# set up the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

shapesList = []
shapeTypesTuple = ('square', 'circle', 'triangle')
for i in range(0, N_SHAPES):
    thisType = random.choice(shapeTypesTuple)
    if thisType == 'square':
        oShape = Square(window)
    elif thisType == 'circle':
        oShape = Circle(window)
    else:  # must be triangle
        oShape = Triangle(window)
    shapesList.append(oShape)

statusLine = pygwidgets.DisplayText(window, (4,4), \
                    'Click on shapes', fontSize=28)

# main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            for oShape in shapesList:
                if oShape.clickedInside(event.pos):
                    thisArea = oShape.getArea()
                    thisType = oShape.getType()
                    newText = 'Clicked on a ' + thisType + ' whose area is ' + str(thisArea)
                    statusLine.setValue(newText)

    # Tell each shape to draw itself
    window.fill(WHITE)
    for oShape in shapesList:
        oShape.draw()
    statusLine.draw()

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
