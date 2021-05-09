# Timer using custom event

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import pygwidgets

# 2 - Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
FRAMES_PER_SECOND = 30
WHITE = (255, 255, 255)
#TIMER_EVENT_ID = pygame.USEREVENT + 1  # pygame 1.x approach
TIMER_EVENT_ID = pygame.event.custom_type()  # new in pygame 2.0
TIMER_LENGTH = 2.5 # seconds

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
headerMessage = pygwidgets.DisplayText(window, (0, 50), 'Click "Start" to start a ' +
                                    str(TIMER_LENGTH) + ' second timer:', 
                                    fontSize=36, justified='center', width=WINDOW_WIDTH)

startButton = pygwidgets.TextButton(window, (200, 100), 'Start')

clickMeButton = pygwidgets.TextButton(window, (320, 100), 'Click Me')

timerMessage = pygwidgets.DisplayText(window, (0, 160), 'Message showing during timer', 
                                    fontSize=36, justified='center', width=WINDOW_WIDTH)

timerMessage.hide()  # start off with this message hidden
 
# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # If the event was a click on the close box, quit pygame and the program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

        if startButton.handleEvent(event):
            pygame.time.set_timer(TIMER_EVENT_ID,
                                               int(TIMER_LENGTH * 1000), True)
            startButton.disable()
            timerMessage.show()
            print('Starting timer')

        if event.type == TIMER_EVENT_ID:
            startButton.enable()
            timerMessage.hide()
            print('Timer ended by event')

        if clickMeButton.handleEvent(event):
            print('Other button was clicked')

    # 8 - Do any "per frame" actions
    
    # 9 - Clear the screen
    window.fill(WHITE)
   
    # 10 - Draw all screen elements
    headerMessage.draw()
    startButton.draw()
    clickMeButton.draw()
    timerMessage.draw() 

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount




