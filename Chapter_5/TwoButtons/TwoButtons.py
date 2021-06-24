#  pygame demo  2-Button Test 

# 1 - Import packages
import pygame
from pygame.locals import *
import pygwidgets
import sys

# Define constants
GRAY = (200, 200, 200)
WINDOW_WIDTH = 270
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30 

# 2 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 4 - Load assets: image(s), sound(s), etc.
barkSound = pygame.mixer.Sound('bark.wav')
meowSound = pygame.mixer.Sound('meow.wav')

# 5 - Initialize variables
# Create instances of a Simple button
buttonA = pygwidgets.TextButton(window, (20, 30), 'Bark')
buttonB = pygwidgets.TextButton(window, (150, 30), 'Meow')

counter = 0

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program  
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pass the event to the button, see if has been clicked on
        if  buttonA.handleEvent(event):
            print('User pressed the Bark button.  Program has run this many loops:', counter)
            barkSound.play()
        elif  buttonB.handleEvent(event):
            print('User pressed the Meow button.  Program has run this many loops:', counter)
            meowSound.play()

    # 8 - Do any "per frame" actions
    counter = counter + 1
    
    # 9 - Clear the screen
    window.fill(GRAY)
    
    # 10 - Draw all screen elements
    buttonA.draw()
    buttonB.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait the correct amount
